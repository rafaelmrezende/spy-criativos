"""
Módulo de exportação para gerar resultados em PDF, HTML e Markdown.
"""

import os
import json
import markdown
from weasyprint import HTML, CSS
from fpdf2 import FPDF
import base64
import re
from datetime import datetime

class ResultExporter:
    """Classe para exportação dos resultados em diferentes formatos."""
    
    def __init__(self, output_dir='/home/ubuntu/spy-criativos/output'):
        """Inicializa o exportador com o diretório de saída."""
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    def export_all(self, ad_data, analysis_result):
        """Exporta os resultados em todos os formatos disponíveis."""
        if not ad_data or not analysis_result:
            return {
                'success': False,
                'error': 'Dados do anúncio ou resultado da análise ausentes'
            }
        
        results = {}
        
        # Exporta para HTML
        html_result = self.export_to_html(ad_data, analysis_result)
        results['html'] = html_result
        
        # Exporta para Markdown
        md_result = self.export_to_markdown(ad_data, analysis_result)
        results['markdown'] = md_result
        
        # Exporta para PDF
        pdf_result = self.export_to_pdf(ad_data, analysis_result)
        results['pdf'] = pdf_result
        
        # Exporta landing page
        landing_result = self.export_landing_page(ad_data, analysis_result)
        results['landing_page'] = landing_result
        
        return {
            'success': all([r.get('success', False) for r in results.values()]),
            'results': results
        }
    
    def export_to_html(self, ad_data, analysis_result):
        """Exporta os resultados para formato HTML."""
        try:
            # Prepara os dados
            original = analysis_result.get('original', {})
            variations = analysis_result.get('variations', {})
            
            # Cria o caminho do arquivo
            file_path = os.path.join(self.output_dir, 'variacoes.html')
            
            # Gera o HTML
            html_content = self._generate_html_content(ad_data, original, variations)
            
            # Salva o arquivo
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            return {
                'success': True,
                'file_path': file_path
            }
        
        except Exception as e:
            return {
                'success': False,
                'error': f"Erro ao exportar para HTML: {str(e)}"
            }
    
    def export_to_markdown(self, ad_data, analysis_result):
        """Exporta os resultados para formato Markdown."""
        try:
            # Prepara os dados
            original = analysis_result.get('original', {})
            variations = analysis_result.get('variations', {})
            
            # Cria o caminho do arquivo
            file_path = os.path.join(self.output_dir, 'variacoes.md')
            
            # Gera o Markdown
            md_content = self._generate_markdown_content(ad_data, original, variations)
            
            # Salva o arquivo
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(md_content)
            
            return {
                'success': True,
                'file_path': file_path
            }
        
        except Exception as e:
            return {
                'success': False,
                'error': f"Erro ao exportar para Markdown: {str(e)}"
            }
    
    def export_to_pdf(self, ad_data, analysis_result):
        """Exporta os resultados para formato PDF usando WeasyPrint."""
        try:
            # Prepara os dados
            original = analysis_result.get('original', {})
            variations = analysis_result.get('variations', {})
            
            # Cria o caminho do arquivo
            file_path = os.path.join(self.output_dir, 'variacoes.pdf')
            
            # Gera o HTML para conversão em PDF
            html_content = self._generate_html_content(ad_data, original, variations, for_pdf=True)
            
            # Define o CSS para o PDF
            css_content = """
            @page {
                margin: 1cm;
                @top-center {
                    content: "Spy Criativos - Variações de Anúncios";
                    font-size: 9pt;
                    color: #666;
                }
                @bottom-right {
                    content: "Página " counter(page) " de " counter(pages);
                    font-size: 9pt;
                    color: #666;
                }
            }
            body {
                font-family: "Noto Sans CJK SC", "WenQuanYi Zen Hei", sans-serif;
                line-height: 1.5;
                color: #333;
            }
            h1 {
                color: #2c3e50;
                border-bottom: 1px solid #eee;
                padding-bottom: 10px;
            }
            h2 {
                color: #3498db;
                margin-top: 20px;
            }
            h3 {
                color: #e74c3c;
            }
            .variation {
                margin: 20px 0;
                padding: 15px;
                border: 1px solid #ddd;
                border-radius: 5px;
                background-color: #f9f9f9;
            }
            .original {
                background-color: #e8f4f8;
                border-color: #bde0ec;
            }
            .emocional {
                background-color: #f8e8e8;
                border-color: #ecbdbd;
            }
            .escassez {
                background-color: #f8f4e8;
                border-color: #ece5bd;
            }
            .autoridade {
                background-color: #e8f8ea;
                border-color: #bdecbf;
            }
            .headline {
                font-size: 18px;
                font-weight: bold;
                margin-bottom: 10px;
            }
            .description {
                margin-bottom: 10px;
            }
            .cta {
                font-weight: bold;
                color: #2980b9;
            }
            .image-container {
                margin: 15px 0;
                text-align: center;
            }
            .image-container img {
                max-width: 100%;
                max-height: 300px;
                border: 1px solid #ddd;
            }
            .metadata {
                font-size: 12px;
                color: #777;
                margin-top: 20px;
                border-top: 1px solid #eee;
                padding-top: 10px;
            }
            """
            
            # Cria o PDF com WeasyPrint
            html = HTML(string=html_content)
            css = CSS(string=css_content)
            html.write_pdf(file_path, stylesheets=[css])
            
            return {
                'success': True,
                'file_path': file_path
            }
        
        except Exception as e:
            return {
                'success': False,
                'error': f"Erro ao exportar para PDF: {str(e)}"
            }
    
    def export_landing_page(self, ad_data, analysis_result):
        """Exporta a variação de landing page em HTML."""
        try:
            # Obtém os dados da landing page
            landing_page = analysis_result.get('landing_page', {})
            
            if not landing_page:
                return {
                    'success': False,
                    'error': 'Dados da landing page ausentes'
                }
            
            # Cria o caminho do arquivo
            file_path = os.path.join(self.output_dir, 'landing_page_variacao.html')
            
            # Gera o HTML da landing page
            html_content = self._generate_landing_page_html(ad_data, landing_page)
            
            # Salva o arquivo
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            return {
                'success': True,
                'file_path': file_path
            }
        
        except Exception as e:
            return {
                'success': False,
                'error': f"Erro ao exportar landing page: {str(e)}"
            }
    
    def _generate_html_content(self, ad_data, original, variations, for_pdf=False):
        """Gera o conteúdo HTML para as variações."""
        # Cabeçalho HTML
        html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Spy Criativos - Variações de Anúncios</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 1px solid #eee;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #3498db;
            margin-top: 20px;
        }}
        h3 {{
            color: #e74c3c;
        }}
        .variation {{
            margin: 20px 0;
            padding: 15px;
            border: 1px solid #ddd;
            border-radius: 5px;
            background-color: #f9f9f9;
        }}
        .original {{
            background-color: #e8f4f8;
            border-color: #bde0ec;
        }}
        .emocional {{
            background-color: #f8e8e8;
            border-color: #ecbdbd;
        }}
        .escassez {{
            background-color: #f8f4e8;
            border-color: #ece5bd;
        }}
        .autoridade {{
            background-color: #e8f8ea;
            border-color: #bdecbf;
        }}
        .headline {{
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 10px;
        }}
        .description {{
            margin-bottom: 10px;
        }}
        .cta {{
            font-weight: bold;
            color: #2980b9;
        }}
        .image-container {{
            margin: 15px 0;
            text-align: center;
        }}
        .image-container img {{
            max-width: 100%;
            max-height: 300px;
            border: 1px solid #ddd;
        }}
        .metadata {{
            font-size: 12px;
            color: #777;
            margin-top: 20px;
            border-top: 1px solid #eee;
            padding-top: 10px;
        }}
        @media print {{
            .variation {{
                page-break-inside: avoid;
            }}
        }}
    </style>
</head>
<body>
    <h1>Spy Criativos - Variações de Anúncios</h1>
    
    <div class="metadata">
        <p>URL original: {ad_data.get('url', 'N/A')}</p>
        <p>Plataforma: {ad_data.get('platform', 'N/A').capitalize()}</p>
        <p>Data de geração: {datetime.now().strftime('%d/%m/%Y %H:%M')}</p>
    </div>
    
    <h2>Criativo Original</h2>
    <div class="variation original">
        <h3>Ângulo Principal: {original.get('primary_angle', 'N/A').capitalize()}</h3>
        <div class="headline">{original.get('headline', 'Sem título')}</div>
        <div class="description">{original.get('description', 'Sem descrição')}</div>
        <div class="cta">CTA: {original.get('cta', 'Sem CTA')}</div>
"""

        # Adiciona imagens se disponíveis
        if ad_data.get('images') and len(ad_data['images']) > 0:
            html += '    <div class="image-container">\n'
            for img_url in ad_data['images'][:1]:  # Limita a uma imagem para não sobrecarregar
                html += f'        <img src="{img_url}" alt="Imagem do anúncio">\n'
            html += '    </div>\n'

        html += '</div>\n\n'

        # Adiciona as variações
        html += '<h2>Variações Geradas</h2>\n'
        
        # Variação Emocional
        emocional = variations.get('emocional', {})
        html += f"""
    <div class="variation emocional">
        <h3>Variação A: Foco Emocional</h3>
        <div class="headline">{emocional.get('headline', 'Sem título')}</div>
        <div class="description">{emocional.get('description', 'Sem descrição')}</div>
        <div class="cta">CTA: {emocional.get('cta', 'Sem CTA')}</div>
    </div>
"""

        # Variação Escassez
        escassez = variations.get('escassez', {})
        html += f"""
    <div class="variation escassez">
        <h3>Variação B: Foco em Escassez e Urgência</h3>
        <div class="headline">{escassez.get('headline', 'Sem título')}</div>
        <div class="description">{escassez.get('description', 'Sem descrição')}</div>
        <div class="cta">CTA: {escassez.get('cta', 'Sem CTA')}</div>
    </div>
"""

        # Variação Autoridade
        autoridade = variations.get('autoridade', {})
        html += f"""
    <div class="variation autoridade">
        <h3>Variação C: Foco em Autoridade / Prova Social</h3>
        <div class="headline">{autoridade.get('headline', 'Sem título')}</div>
        <div class="description">{autoridade.get('description', 'Sem descrição')}</div>
        <div class="cta">CTA: {autoridade.get('cta', 'Sem CTA')}</div>
    </div>
"""

        # Rodapé
        html += """
    <div class="metadata">
        <p>Gerado automaticamente pelo Spy Criativos</p>
        <p>Todas as variações são otimizadas para maior conversão com base em análise de IA</p>
    </div>
</body>
</html>
"""
        
        return html
    
    def _generate_markdown_content(self, ad_data, original, variations):
        """Gera o conteúdo Markdown para as variações."""
        md = f"""# Spy Criativos - Variações de Anúncios

**URL original:** {ad_data.get('url', 'N/A')}  
**Plataforma:** {ad_data.get('platform', 'N/A').capitalize()}  
**Data de geração:** {datetime.now().strftime('%d/%m/%Y %H:%M')}

## Criativo Original

**Ângulo Principal:** {original.get('primary_angle', 'N/A').capitalize()}

**Headline:**  
{original.get('headline', 'Sem título')}

**Descrição:**  
{original.get('description', 'Sem descrição')}

**CTA:**  
{original.get('cta', 'Sem CTA')}

"""

        # Adiciona informações sobre imagens
        if ad_data.get('images') and len(ad_data['images']) > 0:
            md += f"**Imagens:** {len(ad_data['images'])} imagem(ns) disponível(is)\n\n"
        
        # Adiciona as variações
        md += "## Variações Geradas\n\n"
        
        # Variação Emocional
        emocional = variations.get('emocional', {})
        md += f"""### Variação A: Foco Emocional

**Headline:**  
{emocional.get('headline', 'Sem título')}

**Descrição:**  
{emocional.get('description', 'Sem descrição')}

**CTA:**  
{emocional.get('cta', 'Sem CTA')}

"""

        # Variação Escassez
        escassez = variations.get('escassez', {})
        md += f"""### Variação B: Foco em Escassez e Urgência

**Headline:**  
{escassez.get('headline', 'Sem título')}

**Descrição:**  
{escassez.get('description', 'Sem descrição')}

**CTA:**  
{escassez.get('cta', 'Sem CTA')}

"""

        # Variação Autoridade
        autoridade = variations.get('autoridade', {})
        md += f"""### Variação C: Foco em Autoridade / Prova Social

**Headline:**  
{autoridade.get('headline', 'Sem título')}

**Descrição:**  
{autoridade.get('description', 'Sem descrição')}

**CTA:**  
{autoridade.get('cta', 'Sem CTA')}

"""

        # Rodapé
        md += """---

*Gerado automaticamente pelo Spy Criativos*  
*Todas as variações são otimizadas para maior conversão com base em análise de IA*
"""
        
        return md
    
    def _generate_landing_page_html(self, ad_data, landing_page):
        """Gera o HTML para a landing page."""
        # Extrai dados da landing page
        headline = landing_page.get('headline', 'Produto/Serviço Incrível')
        subheadline = landing_page.get('subheadline', 'Descubra como transformar sua experiência')
        bullets = landing_page.get('bullets', ['Benefício 1', 'Benefício 2', 'Benefício 3', 'Benefício 4'])
        cta = landing_page.get('cta', 'QUERO SABER MAIS')
        testimonial = landing_page.get('testimonial', '"Este produto mudou minha vida!" - Cliente Satisfeito')
        
        # Imagem do produto (usa a primeira imagem do anúncio, se disponível)
        image_url = '#'
        if ad_data.get('images') and len(ad_data['images']) > 0:
            image_url = ad_data['images'][0]
        
        # Gera o HTML da landing page
        html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{headline}</title>
    <style>
        :root {{
            --primary-color: #3498db;
            --secondary-color: #2ecc71;
            --accent-color: #e74c3c;
            --text-color: #333;
            --light-bg: #f9f9f9;
        }}
        
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            background-color: #fff;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }}
        
        header {{
            background-color: var(--primary-color);
            color: white;
            padding: 20px 0;
            text-align: center;
        }}
        
        .hero {{
            padding: 60px 0;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            text-align: center;
        }}
        
        .hero h1 {{
            font-size: 2.5rem;
            margin-bottom: 20px;
            color: var(--primary-color);
        }}
        
        .hero h2 {{
            font-size: 1.5rem;
            margin-bottom: 30px;
            color: var(--text-color);
            font-weight: normal;
        }}
        
        .product-image {{
            max-width: 100%;
            height: auto;
            margin: 30px 0;
            border-radius: 8px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }}
        
        .benefits {{
            padding: 60px 0;
            background-color: var(--light-bg);
        }}
        
        .benefits-list {{
            max-width: 800px;
            margin: 0 auto;
        }}
        
        .benefits-list li {{
            font-size: 1.2rem;
            margin-bottom: 15px;
            list-style-type: none;
            position: relative;
            padding-left: 30px;
        }}
        
        .benefits-list li:before {{
            content: "✓";
            color: var(--secondary-color);
            font-weight: bold;
            position: absolute;
            left: 0;
        }}
        
        .cta-section {{
            padding: 60px 0;
            text-align: center;
            background-color: white;
        }}
        
        .cta-button {{
            display: inline-block;
            padding: 15px 40px;
            background-color: var(--accent-color);
            color: white;
            text-decoration: none;
            font-size: 1.2rem;
            font-weight: bold;
            border-radius: 5px;
            transition: all 0.3s ease;
            margin-top: 20px;
        }}
        
        .cta-button:hover {{
            background-color: #c0392b;
            transform: translateY(-3px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }}
        
        .testimonial {{
            font-style: italic;
            font-size: 1.2rem;
            max-width: 800px;
            margin: 40px auto 0;
            color: #555;
        }}
        
        footer {{
            background-color: #333;
            color: white;
            text-align: center;
            padding: 20px 0;
            font-size: 0.9rem;
        }}
        
        @media (max-width: 768px) {{
            .hero h1 {{
                font-size: 2rem;
            }}
            
            .hero h2 {{
                font-size: 1.2rem;
            }}
            
            .benefits-list li {{
                font-size: 1rem;
            }}
        }}
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h3>Apresentamos</h3>
        </div>
    </header>
    
    <section class="hero">
        <div class="container">
            <h1>{headline}</h1>
            <h2>{subheadline}</h2>
            <img src="{image_url}" alt="Imagem do Produto" class="product-image">
        </div>
    </section>
    
    <section class="benefits">
        <div class="container">
            <div class="benefits-list">
                <ul>
                    <li>{bullets[0]}</li>
                    <li>{bullets[1]}</li>
                    <li>{bullets[2]}</li>
                    <li>{bullets[3]}</li>
                </ul>
            </div>
        </div>
    </section>
    
    <section class="cta-section">
        <div class="container">
            <a href="#" class="cta-button">{cta}</a>
            <p class="testimonial">{testimonial}</p>
        </div>
    </section>
    
    <footer>
        <div class="container">
            <p>© {datetime.now().year} Todos os direitos reservados. Gerado pelo Spy Criativos.</p>
        </div>
    </footer>
</body>
</html>
"""
        
        return html


# Função para uso direto
def export_results(ad_data, analysis_result, output_dir=None):
    """Função auxiliar para exportar resultados em todos os formatos."""
    exporter = ResultExporter(output_dir=output_dir)
    return exporter.export_all(ad_data, analysis_result)
