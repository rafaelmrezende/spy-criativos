document.addEventListener('DOMContentLoaded', function() {
    // Elementos do DOM
    const urlForm = document.getElementById('urlForm');
    const urlInput = document.getElementById('urlInput');
    const analyzeBtn = document.getElementById('analyzeBtn');
    const errorMessage = document.getElementById('errorMessage');
    const loadingContainer = document.getElementById('loadingContainer');
    const resultsSection = document.getElementById('resultsSection');
    const downloadSection = document.getElementById('downloadSection');
    
    // Elementos de tabs
    const tabButtons = document.querySelectorAll('.tab-btn');
    const tabPanes = document.querySelectorAll('.tab-pane');
    
    // Botões de download
    const pdfBtn = document.getElementById('pdfBtn');
    const htmlBtn = document.getElementById('htmlBtn');
    const markdownBtn = document.getElementById('markdownBtn');
    const landingBtn = document.getElementById('landingBtn');
    
    // Dados de exemplo para demonstração
    const mockData = {
        adData: {
            success: true,
            platform: 'meta',
            url: '',
            headline: 'Descubra o Segredo para Pele Jovem aos 50+',
            description: 'Este produto revolucionário está ajudando milhares de mulheres a recuperar a juventude da pele. Resultados visíveis em apenas 14 dias!',
            images: ['https://via.placeholder.com/400x300'],
            cta: 'Saiba Mais',
            landing_page: 'https://exemplo.com/produto'
        },
        analysisResult: {
            success: true,
            variations: {
                emocional: {
                    headline: 'Surpreendente! Sinta a Transformação da Sua Pele aos 50+',
                    description: 'Imagine como seria incrível Este produto revolucionário está ajudando milhares de mulheres. Você merece essa experiência única!',
                    cta: 'Sinta a diferença',
                    angle: 'emocional'
                },
                escassez: {
                    headline: 'ÚLTIMAS UNIDADES: Descubra o Segredo para Pele Jovem aos 50+',
                    description: 'Corra! Restam apenas poucas unidades! Este produto revolucionário está ajudando milhares de mulheres. Oferta válida enquanto durar o estoque!',
                    cta: 'Garanta já',
                    angle: 'escassez'
                },
                autoridade: {
                    headline: 'CIENTIFICAMENTE COMPROVADO: Descubra o Segredo para Pele Jovem aos 50+',
                    description: 'Recomendado por 9 entre 10 especialistas. Este produto revolucionário está ajudando milhares de mulheres. Junte-se aos milhares de clientes satisfeitos!',
                    cta: 'Veja as avaliações',
                    angle: 'autoridade'
                }
            },
            landing_page: {
                headline: 'Descubra o Segredo para Pele Jovem aos 50+',
                subheadline: 'A solução definitiva para recuperar a juventude da sua pele',
                bullets: [
                    '✓ Resultados visíveis em apenas 14 dias',
                    '✓ Fórmula exclusiva com ingredientes naturais',
                    '✓ Testado e aprovado por dermatologistas',
                    '✓ Satisfação garantida ou seu dinheiro de volta'
                ],
                cta: 'QUERO TRANSFORMAR MINHA PELE AGORA',
                testimonial: '"Nunca imaginei que poderia me sentir tão bem com minha pele novamente!" - Maria S.'
            },
            original: {
                headline: 'Descubra o Segredo para Pele Jovem aos 50+',
                description: 'Este produto revolucionário está ajudando milhares de mulheres a recuperar a juventude da pele. Resultados visíveis em apenas 14 dias!',
                cta: 'Saiba Mais',
                primary_angle: 'beneficio'
            }
        }
    };
    
    // Manipulação de eventos
    urlForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const url = urlInput.value.trim();
        
        if (!url) {
            showError('Por favor, insira uma URL válida');
            return;
        }
        
        // Limpa mensagens de erro
        clearError();
        
        // Mostra o loading
        showLoading();
        
        // Simula uma chamada de API (em um ambiente real, isso seria uma chamada fetch)
        setTimeout(() => {
            // Atualiza os dados mockados com a URL inserida
            mockData.adData.url = url;
            
            // Preenche os resultados com os dados mockados
            fillResults(mockData.adData, mockData.analysisResult);
            
            // Esconde o loading e mostra os resultados
            hideLoading();
            showResults();
        }, 2000);
    });
    
    // Navegação por tabs
    tabButtons.forEach(button => {
        button.addEventListener('click', function() {
            const tabId = this.getAttribute('data-tab');
            
            // Remove a classe active de todos os botões e painéis
            tabButtons.forEach(btn => btn.classList.remove('active'));
            tabPanes.forEach(pane => pane.classList.remove('active'));
            
            // Adiciona a classe active ao botão e painel clicados
            this.classList.add('active');
            document.getElementById(tabId).classList.add('active');
        });
    });
    
    // Eventos de download
    pdfBtn.addEventListener('click', () => simulateDownload('PDF'));
    htmlBtn.addEventListener('click', () => simulateDownload('HTML'));
    markdownBtn.addEventListener('click', () => simulateDownload('Markdown'));
    landingBtn.addEventListener('click', () => simulateDownload('Landing Page'));
    
    // Funções auxiliares
    function showError(message) {
        errorMessage.textContent = message;
        errorMessage.style.display = 'block';
    }
    
    function clearError() {
        errorMessage.textContent = '';
        errorMessage.style.display = 'none';
    }
    
    function showLoading() {
        loadingContainer.style.display = 'flex';
        resultsSection.style.display = 'none';
        downloadSection.style.display = 'none';
    }
    
    function hideLoading() {
        loadingContainer.style.display = 'none';
    }
    
    function showResults() {
        resultsSection.style.display = 'block';
        downloadSection.style.display = 'block';
    }
    
    function fillResults(adData, analysisResult) {
        // Preenche os dados do original
        document.getElementById('originalHeadline').textContent = analysisResult.original.headline;
        document.getElementById('originalDescription').textContent = analysisResult.original.description;
        document.getElementById('originalCta').textContent = `CTA: ${analysisResult.original.cta}`;
        document.getElementById('originalAngle').textContent = analysisResult.original.primary_angle;
        
        // Preenche os dados da variação emocional
        document.getElementById('emocionalHeadline').textContent = analysisResult.variations.emocional.headline;
        document.getElementById('emocionalDescription').textContent = analysisResult.variations.emocional.description;
        document.getElementById('emocionalCta').textContent = `CTA: ${analysisResult.variations.emocional.cta}`;
        
        // Preenche os dados da variação escassez
        document.getElementById('escassezHeadline').textContent = analysisResult.variations.escassez.headline;
        document.getElementById('escassezDescription').textContent = analysisResult.variations.escassez.description;
        document.getElementById('escassezCta').textContent = `CTA: ${analysisResult.variations.escassez.cta}`;
        
        // Preenche os dados da variação autoridade
        document.getElementById('autoridadeHeadline').textContent = analysisResult.variations.autoridade.headline;
        document.getElementById('autoridadeDescription').textContent = analysisResult.variations.autoridade.description;
        document.getElementById('autoridadeCta').textContent = `CTA: ${analysisResult.variations.autoridade.cta}`;
        
        // Preenche os dados da landing page
        document.getElementById('landingHeadline').textContent = analysisResult.landing_page.headline;
        document.getElementById('landingSubheadline').textContent = analysisResult.landing_page.subheadline;
        document.getElementById('landingCta').textContent = analysisResult.landing_page.cta;
        document.getElementById('landingTestimonial').textContent = analysisResult.landing_page.testimonial;
        
        // Preenche as bullets da landing page
        const bulletsContainer = document.getElementById('landingBullets');
        bulletsContainer.innerHTML = '';
        analysisResult.landing_page.bullets.forEach(bullet => {
            const bulletItem = document.createElement('div');
            bulletItem.className = 'bullet-item';
            bulletItem.textContent = bullet;
            bulletsContainer.appendChild(bulletItem);
        });
        
        // Atualiza as imagens se disponíveis
        if (adData.images && adData.images.length > 0) {
            const imageUrl = adData.images[0];
            document.getElementById('adImage').src = imageUrl;
            document.getElementById('adImageEmocional').src = imageUrl;
            document.getElementById('adImageEscassez').src = imageUrl;
            document.getElementById('adImageAutoridade').src = imageUrl;
        }
    }
    
    function simulateDownload(format) {
        alert(`Download do arquivo em formato ${format} iniciado!\n\nEm um ambiente de produção, isso baixaria o arquivo real.`);
    }
});
