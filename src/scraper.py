"""
Módulo de scraping para extração de criativos de anúncios.
Suporta Meta Ads Library, Taboola, Outbrain e páginas comuns de dropshipping.
"""

import requests
from bs4 import BeautifulSoup
import re
import json
import os
from urllib.parse import urlparse, urljoin

class AdScraper:
    """Classe para extração de criativos de anúncios de diferentes plataformas."""
    
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
    
    def identify_platform(self, url):
        """Identifica a plataforma com base na URL."""
        domain = urlparse(url).netloc.lower()
        
        if 'facebook.com' in domain or 'fb.com' in domain or 'meta.com' in domain:
            return 'meta'
        elif 'taboola.com' in domain:
            return 'taboola'
        elif 'outbrain.com' in domain:
            return 'outbrain'
        else:
            return 'generic'
    
    def scrape_ad(self, url):
        """Extrai informações de um anúncio com base na URL fornecida."""
        platform = self.identify_platform(url)
        
        try:
            response = self.session.get(url, timeout=15)
            response.raise_for_status()
            
            if platform == 'meta':
                return self._scrape_meta_ad(response.text, url)
            elif platform == 'taboola':
                return self._scrape_taboola_ad(response.text, url)
            elif platform == 'outbrain':
                return self._scrape_outbrain_ad(response.text, url)
            else:
                return self._scrape_generic_page(response.text, url)
                
        except requests.RequestException as e:
            return {
                'success': False,
                'error': f"Erro ao acessar a URL: {str(e)}",
                'platform': platform
            }
    
    def _scrape_meta_ad(self, html_content, url):
        """Extrai informações de anúncios do Meta Ads Library."""
        soup = BeautifulSoup(html_content, 'html.parser')
        result = {
            'success': True,
            'platform': 'meta',
            'url': url,
            'headline': '',
            'description': '',
            'images': [],
            'cta': '',
            'landing_page': '',
            'raw_html': html_content[:5000]  # Armazena parte do HTML para análise
        }
        
        # Tenta extrair o título/headline
        headline_candidates = soup.select('div[role="heading"], h1, h2, .x1lliihq')
        if headline_candidates:
            result['headline'] = headline_candidates[0].get_text(strip=True)
        
        # Tenta extrair a descrição
        description_candidates = soup.select('div[data-ad-preview="message"], .xdj266r, .x11i5rnm')
        if description_candidates:
            result['description'] = description_candidates[0].get_text(strip=True)
        
        # Tenta extrair imagens
        images = soup.select('img[src*="scontent"], img[data-visualcompletion="media-vc-image"]')
        for img in images:
            if img.get('src') and 'data:image' not in img.get('src'):
                result['images'].append(img.get('src'))
        
        # Tenta extrair CTA
        cta_candidates = soup.select('div[aria-label*="Learn More"], div[aria-label*="Shop Now"], div[aria-label*="Saiba mais"], div[aria-label*="Comprar"]')
        if cta_candidates:
            result['cta'] = cta_candidates[0].get_text(strip=True)
        
        # Tenta extrair landing page
        landing_links = soup.select('a[href*="l.facebook.com"], a[href*="lm.facebook.com"]')
        if landing_links:
            result['landing_page'] = landing_links[0].get('href')
        
        return result
    
    def _scrape_taboola_ad(self, html_content, url):
        """Extrai informações de anúncios do Taboola."""
        soup = BeautifulSoup(html_content, 'html.parser')
        result = {
            'success': True,
            'platform': 'taboola',
            'url': url,
            'headline': '',
            'description': '',
            'images': [],
            'cta': 'Saiba mais',  # CTA padrão do Taboola
            'landing_page': '',
            'raw_html': html_content[:5000]
        }
        
        # Tenta extrair o título/headline
        headline_candidates = soup.select('.video-title, .videoCube_title, h2')
        if headline_candidates:
            result['headline'] = headline_candidates[0].get_text(strip=True)
        
        # Tenta extrair imagens
        images = soup.select('img.thumbnail, img[data-src], img.trc_rbox_border_elm')
        for img in images:
            src = img.get('src') or img.get('data-src')
            if src and 'data:image' not in src:
                result['images'].append(src)
        
        # Tenta extrair landing page
        landing_links = soup.select('a.videoCube_thumbnail_link, a.trc_rbox_div')
        if landing_links:
            result['landing_page'] = landing_links[0].get('href')
        
        return result
    
    def _scrape_outbrain_ad(self, html_content, url):
        """Extrai informações de anúncios do Outbrain."""
        soup = BeautifulSoup(html_content, 'html.parser')
        result = {
            'success': True,
            'platform': 'outbrain',
            'url': url,
            'headline': '',
            'description': '',
            'images': [],
            'cta': 'Leia mais',  # CTA padrão do Outbrain
            'landing_page': '',
            'raw_html': html_content[:5000]
        }
        
        # Tenta extrair o título/headline
        headline_candidates = soup.select('.ob-rec-text, .ob-headline, .ob-unit-title')
        if headline_candidates:
            result['headline'] = headline_candidates[0].get_text(strip=True)
        
        # Tenta extrair imagens
        images = soup.select('img.ob-rec-image, img.ob_what')
        for img in images:
            src = img.get('src') or img.get('data-src')
            if src and 'data:image' not in src:
                result['images'].append(src)
        
        # Tenta extrair landing page
        landing_links = soup.select('a.ob-rec-link, a.ob-click')
        if landing_links:
            result['landing_page'] = landing_links[0].get('href')
        
        return result
    
    def _scrape_generic_page(self, html_content, url):
        """Extrai informações de páginas genéricas (dropshipping, landing pages)."""
        soup = BeautifulSoup(html_content, 'html.parser')
        result = {
            'success': True,
            'platform': 'generic',
            'url': url,
            'headline': '',
            'description': '',
            'images': [],
            'cta': '',
            'landing_page': url,
            'raw_html': html_content[:5000]
        }
        
        # Tenta extrair o título/headline
        headline_candidates = soup.select('h1, .headline, .title, .product-title')
        if headline_candidates:
            result['headline'] = headline_candidates[0].get_text(strip=True)
        else:
            # Fallback para o título da página
            title = soup.find('title')
            if title:
                result['headline'] = title.get_text(strip=True)
        
        # Tenta extrair a descrição
        description_candidates = soup.select('.description, .product-description, p.lead, .subtitle, meta[name="description"]')
        if description_candidates:
            if description_candidates[0].name == 'meta':
                result['description'] = description_candidates[0].get('content', '')
            else:
                result['description'] = description_candidates[0].get_text(strip=True)
        
        # Tenta extrair imagens principais
        images = soup.select('img.product-image, img.hero-image, img.banner, img[src*="product"], img[src*="hero"]')
        if not images:
            # Fallback para imagens maiores que 100x100 pixels
            all_images = soup.find_all('img')
            for img in all_images:
                width = img.get('width')
                height = img.get('height')
                if width and height and int(width) > 100 and int(height) > 100:
                    src = img.get('src')
                    if src and 'data:image' not in src:
                        # Converte URL relativa para absoluta
                        if not src.startswith(('http://', 'https://')):
                            src = urljoin(url, src)
                        result['images'].append(src)
        else:
            for img in images:
                src = img.get('src')
                if src and 'data:image' not in src:
                    # Converte URL relativa para absoluta
                    if not src.startswith(('http://', 'https://')):
                        src = urljoin(url, src)
                    result['images'].append(src)
        
        # Tenta extrair CTA
        cta_candidates = soup.select('button.cta, a.cta, .btn-primary, button.buy-now, a.buy-now')
        if cta_candidates:
            result['cta'] = cta_candidates[0].get_text(strip=True)
        
        return result
    
    def download_image(self, image_url, save_path):
        """Baixa uma imagem da URL fornecida e salva no caminho especificado."""
        try:
            response = self.session.get(image_url, stream=True)
            response.raise_for_status()
            
            with open(save_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            return True
        except Exception as e:
            print(f"Erro ao baixar imagem: {str(e)}")
            return False
    
    def extract_with_fallback(self, url):
        """Extrai informações com fallback para entrada manual se o scraping falhar."""
        result = self.scrape_ad(url)
        
        if not result['success'] or not result['headline']:
            # Implementar fallback para entrada manual
            result['needs_manual_input'] = True
        
        return result


# Função para uso direto
def scrape_ad_from_url(url):
    """Função auxiliar para extrair informações de um anúncio a partir de uma URL."""
    scraper = AdScraper()
    return scraper.scrape_ad(url)
