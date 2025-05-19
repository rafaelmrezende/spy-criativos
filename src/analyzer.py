"""
Módulo de análise de criativos com IA.
Identifica o ângulo principal e gera variações otimizadas.
"""

import re
import json
import os

class CreativeAnalyzer:
    """Classe para análise de criativos e identificação de ângulos de persuasão."""
    
    def __init__(self):
        # Padrões linguísticos para identificação de ângulos
        self.patterns = {
            'emocional': [
                r'sinta', r'imagine', r'ame', r'feliz', r'felicidade', r'sonho', r'desejo',
                r'emocion[a-z]+', r'paixão', r'amor', r'alegria', r'satisfação', r'prazer',
                r'surpreend[a-z]+', r'incrível', r'maravilhos[a-z]+', r'emoção', r'sentimento'
            ],
            'escassez': [
                r'último[s]?', r'limitad[a-z]+', r'acaba[r]?', r'restam apenas', r'poucas unidades',
                r'por tempo limitado', r'enquanto durar[em]?', r'esgotad[a-z]+', r'exclusiv[a-z]+',
                r'não perca', r'oferta especial', r'promoção', r'desconto', r'hoje', r'agora',
                r'rápido', r'corra', r'urgente', r'imediato', r'última chance'
            ],
            'autoridade': [
                r'especialista[s]?', r'profissional', r'cientista[s]?', r'estudo[s]?', r'comprovad[a-z]+',
                r'certificad[a-z]+', r'expert[s]?', r'líder', r'reconhecid[a-z]+', r'premiado',
                r'garantid[a-z]+', r'conforme', r'segundo', r'de acordo', r'pesquisa[s]?',
                r'teste[s]?', r'aprovad[a-z]+', r'recomendad[a-z]+'
            ],
            'solucao_problema': [
                r'resolv[a-z]+', r'soluciona', r'acaba[r]? com', r'elimina', r'combate',
                r'problema[s]?', r'dificuldade[s]?', r'desafio[s]?', r'obstáculo[s]?',
                r'dor', r'sofrimento', r'frustração', r'irritação', r'preocupação',
                r'melhora', r'aprimora', r'otimiza', r'facilita', r'simplifica'
            ],
            'beneficio': [
                r'benefício[s]?', r'vantage[m|ns]', r'ganho[s]?', r'lucro[s]?', r'economia',
                r'economiz[a-z]+', r'poupa', r'gratuito', r'grátis', r'bônus', r'brinde',
                r'presente', r'recompensa', r'prêmio', r'valor', r'qualidade', r'durabilidade'
            ]
        }
    
    def analyze_creative(self, ad_data):
        """Analisa o criativo e identifica o ângulo principal."""
        if not ad_data or not isinstance(ad_data, dict):
            return {
                'success': False,
                'error': 'Dados do anúncio inválidos ou ausentes'
            }
        
        # Combina headline e descrição para análise
        text_content = f"{ad_data.get('headline', '')} {ad_data.get('description', '')}"
        text_content = text_content.lower()
        
        # Conta ocorrências de cada padrão
        angle_scores = {}
        for angle, patterns in self.patterns.items():
            score = 0
            for pattern in patterns:
                matches = re.findall(pattern, text_content)
                score += len(matches)
            angle_scores[angle] = score
        
        # Identifica o ângulo predominante
        primary_angle = max(angle_scores, key=angle_scores.get)
        
        # Se o score máximo for 0, define como "beneficio" por padrão
        if angle_scores[primary_angle] == 0:
            primary_angle = 'beneficio'
        
        # Ordena os ângulos por pontuação (do maior para o menor)
        sorted_angles = sorted(angle_scores.items(), key=lambda x: x[1], reverse=True)
        
        return {
            'success': True,
            'primary_angle': primary_angle,
            'angle_scores': angle_scores,
            'sorted_angles': sorted_angles,
            'original_content': {
                'headline': ad_data.get('headline', ''),
                'description': ad_data.get('description', ''),
                'cta': ad_data.get('cta', '')
            }
        }
    
    def generate_variations(self, analysis_result):
        """Gera variações do criativo com base na análise."""
        if not analysis_result or not analysis_result.get('success', False):
            return {
                'success': False,
                'error': 'Resultado de análise inválido ou ausente'
            }
        
        original_headline = analysis_result['original_content']['headline']
        original_description = analysis_result['original_content']['description']
        original_cta = analysis_result['original_content']['cta']
        
        # Garante valores padrão se estiverem vazios
        if not original_headline:
            original_headline = "Produto/Serviço Incrível"
        if not original_description:
            original_description = "Descrição do produto ou serviço com seus benefícios principais."
        if not original_cta:
            original_cta = "Saiba mais"
        
        # Gera variações com base em templates para cada ângulo
        variations = {
            'emocional': self._generate_emotional_variation(original_headline, original_description, original_cta),
            'escassez': self._generate_scarcity_variation(original_headline, original_description, original_cta),
            'autoridade': self._generate_authority_variation(original_headline, original_description, original_cta)
        }
        
        # Gera uma variação de landing page
        landing_page_variation = self._generate_landing_page_variation(
            original_headline, 
            original_description,
            analysis_result['primary_angle']
        )
        
        return {
            'success': True,
            'variations': variations,
            'landing_page': landing_page_variation,
            'original': {
                'headline': original_headline,
                'description': original_description,
                'cta': original_cta,
                'primary_angle': analysis_result['primary_angle']
            }
        }
    
    def _generate_emotional_variation(self, headline, description, cta):
        """Gera uma variação com foco emocional."""
        # Intensificadores emocionais
        emotional_intensifiers = [
            "Surpreendente", "Incrível", "Emocionante", "Fascinante", "Extraordinário",
            "Maravilhoso", "Impressionante", "Sensacional", "Fantástico", "Espetacular"
        ]
        
        # Verbos emocionais
        emotional_verbs = [
            "Descubra", "Sinta", "Experimente", "Imagine", "Transforme", 
            "Encante-se", "Apaixone-se", "Surpreenda-se", "Emocione-se", "Viva"
        ]
        
        # Frases emocionais para descrição
        emotional_phrases = [
            "Você vai se apaixonar por",
            "Imagine como seria incrível",
            "Sinta a diferença que",
            "Transforme sua experiência com",
            "Desperte sensações únicas com"
        ]
        
        # Modificadores de CTA emocionais
        emotional_cta_modifiers = [
            "Descubra agora", "Sinta a diferença", "Experimente já",
            "Transforme sua vida", "Viva essa experiência"
        ]
        
        # Gera headline emocional
        import random
        emotional_headline = f"{random.choice(emotional_intensifiers)}! {random.choice(emotional_verbs)} {headline.split('!', 1)[-1].strip()}"
        
        # Gera descrição emocional
        emotional_description = f"{random.choice(emotional_phrases)} {description.split('.', 1)[0].strip()}. Você merece essa experiência única!"
        
        # Gera CTA emocional
        emotional_cta = random.choice(emotional_cta_modifiers)
        
        return {
            'headline': emotional_headline,
            'description': emotional_description,
            'cta': emotional_cta,
            'angle': 'emocional'
        }
    
    def _generate_scarcity_variation(self, headline, description, cta):
        """Gera uma variação com foco em escassez e urgência."""
        # Intensificadores de escassez
        scarcity_intensifiers = [
            "ÚLTIMAS UNIDADES", "OFERTA LIMITADA", "POR TEMPO LIMITADO", 
            "ACABANDO", "PROMOÇÃO RELÂMPAGO", "ESTOQUE LIMITADO",
            "ÚLTIMAS HORAS", "OFERTA EXCLUSIVA", "VAGAS LIMITADAS"
        ]
        
        # Frases de urgência
        urgency_phrases = [
            "Corra! Restam apenas poucas unidades",
            "Não perca! Esta oferta termina hoje",
            "Atenção! Promoção por tempo limitado",
            "Últimas unidades disponíveis",
            "Aproveite enquanto durar"
        ]
        
        # Modificadores de CTA urgentes
        urgent_cta_modifiers = [
            "Garanta já", "Aproveite agora", "Compre antes que acabe",
            "Reserve imediatamente", "Não perca essa chance"
        ]
        
        # Gera headline com escassez
        import random
        scarcity_headline = f"{random.choice(scarcity_intensifiers)}: {headline.split(':', 1)[-1].strip()}"
        
        # Gera descrição com urgência
        scarcity_description = f"{random.choice(urgency_phrases)}! {description.split('!', 1)[-1].strip()}. Oferta válida enquanto durar o estoque!"
        
        # Gera CTA urgente
        scarcity_cta = random.choice(urgent_cta_modifiers)
        
        return {
            'headline': scarcity_headline,
            'description': scarcity_description,
            'cta': scarcity_cta,
            'angle': 'escassez'
        }
    
    def _generate_authority_variation(self, headline, description, cta):
        """Gera uma variação com foco em autoridade e prova social."""
        # Intensificadores de autoridade
        authority_intensifiers = [
            "COMPROVADO", "CERTIFICADO", "RECOMENDADO POR ESPECIALISTAS",
            "TESTADO E APROVADO", "CIENTIFICAMENTE COMPROVADO",
            "LÍDER DE MERCADO", "PREMIADO", "RECONHECIDO INTERNACIONALMENTE"
        ]
        
        # Frases de autoridade
        authority_phrases = [
            "Recomendado por 9 entre 10 especialistas",
            "Comprovado por estudos científicos",
            "Testado e aprovado por profissionais",
            "Reconhecido como líder no segmento",
            "Utilizado por milhares de clientes satisfeitos"
        ]
        
        # Modificadores de CTA com autoridade
        authority_cta_modifiers = [
            "Confira os resultados", "Veja as avaliações", "Conheça a qualidade",
            "Descubra por que somos líderes", "Comprove a eficácia"
        ]
        
        # Gera headline com autoridade
        import random
        authority_headline = f"{random.choice(authority_intensifiers)}: {headline.split(':', 1)[-1].strip()}"
        
        # Gera descrição com autoridade
        authority_description = f"{random.choice(authority_phrases)}. {description.split('.', 1)[-1].strip()}. Junte-se aos milhares de clientes satisfeitos!"
        
        # Gera CTA com autoridade
        authority_cta = random.choice(authority_cta_modifiers)
        
        return {
            'headline': authority_headline,
            'description': authority_description,
            'cta': authority_cta,
            'angle': 'autoridade'
        }
    
    def _generate_landing_page_variation(self, headline, description, primary_angle):
        """Gera uma variação de landing page com base no ângulo principal."""
        # Estrutura básica de landing page
        landing_page = {
            'headline': headline,
            'subheadline': '',
            'bullets': [],
            'cta': '',
            'testimonial': ''
        }
        
        # Ajusta com base no ângulo principal
        if primary_angle == 'emocional':
            landing_page['subheadline'] = f"Descubra como transformar sua experiência com {headline.split(' ')[-2:][0]}"
            landing_page['bullets'] = [
                "✓ Sinta a diferença desde o primeiro momento",
                "✓ Experimente uma sensação única e incomparável",
                "✓ Transforme sua rotina com mais prazer e satisfação",
                "✓ Desfrute de momentos inesquecíveis"
            ]
            landing_page['cta'] = "QUERO TRANSFORMAR MINHA EXPERIÊNCIA AGORA"
            landing_page['testimonial'] = "\"Nunca imaginei que poderia me sentir tão bem! Simplesmente incrível!\" - Maria S."
            
        elif primary_angle == 'escassez':
            landing_page['subheadline'] = f"Aproveite esta oportunidade única antes que acabe"
            landing_page['bullets'] = [
                "✓ Oferta por tempo limitado - Apenas hoje!",
                "✓ Últimas unidades disponíveis no estoque",
                "✓ Condições especiais que não se repetirão",
                "✓ Bônus exclusivos apenas para os primeiros compradores"
            ]
            landing_page['cta'] = "GARANTIR MINHA OFERTA EXCLUSIVA"
            landing_page['testimonial'] = "\"Quase perdi essa oportunidade incrível. Ainda bem que comprei a tempo!\" - João P."
            
        elif primary_angle == 'autoridade':
            landing_page['subheadline'] = f"A escolha número 1 dos especialistas em {headline.split(' ')[-2:][0]}"
            landing_page['bullets'] = [
                "✓ Recomendado por 9 entre 10 profissionais da área",
                "✓ Certificado pelos principais órgãos reguladores",
                "✓ Desenvolvido com tecnologia de ponta e pesquisa avançada",
                "✓ Utilizado por mais de 10.000 clientes satisfeitos"
            ]
            landing_page['cta'] = "CONHECER A SOLUÇÃO RECOMENDADA PELOS ESPECIALISTAS"
            landing_page['testimonial'] = "\"Como especialista há 15 anos, posso afirmar: este é o melhor produto do mercado.\" - Dr. Carlos M."
            
        else:  # benefício ou solução de problema como fallback
            landing_page['subheadline'] = f"A solução definitiva para {description.split(' ')[:5][0]}"
            landing_page['bullets'] = [
                "✓ Resolva seu problema de forma rápida e eficiente",
                "✓ Economize tempo e dinheiro com nossa solução completa",
                "✓ Resultados visíveis desde o primeiro uso",
                "✓ Satisfação garantida ou seu dinheiro de volta"
            ]
            landing_page['cta'] = "QUERO RESOLVER MEU PROBLEMA AGORA"
            landing_page['testimonial'] = "\"Finalmente encontrei algo que realmente funciona! Recomendo a todos.\" - Ana R."
        
        return landing_page


# Função para uso direto
def analyze_ad_creative(ad_data):
    """Função auxiliar para analisar um criativo de anúncio."""
    analyzer = CreativeAnalyzer()
    analysis = analyzer.analyze_creative(ad_data)
    if analysis['success']:
        return analyzer.generate_variations(analysis)
    return analysis
