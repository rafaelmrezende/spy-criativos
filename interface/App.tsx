import React, { useState } from 'react';
import './App.css';

interface Variation {
  headline: string;
  description: string;
  cta: string;
  angle: string;
}

interface LandingPage {
  headline: string;
  subheadline: string;
  bullets: string[];
  cta: string;
  testimonial: string;
}

interface AnalysisResult {
  success: boolean;
  variations: {
    emocional: Variation;
    escassez: Variation;
    autoridade: Variation;
  };
  landing_page: LandingPage;
  original: {
    headline: string;
    description: string;
    cta: string;
    primary_angle: string;
  };
}

interface AdData {
  success: boolean;
  platform: string;
  url: string;
  headline: string;
  description: string;
  images: string[];
  cta: string;
  landing_page: string;
}

function App() {
  const [url, setUrl] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);
  const [adData, setAdData] = useState<AdData | null>(null);
  const [analysisResult, setAnalysisResult] = useState<AnalysisResult | null>(null);
  const [activeTab, setActiveTab] = useState<string>('original');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!url) {
      setError('Por favor, insira uma URL válida');
      return;
    }
    
    setLoading(true);
    setError(null);
    
    try {
      // Simulação de chamada de API para o backend
      // Em um ambiente real, isso seria substituído por chamadas fetch para o backend
      setTimeout(() => {
        // Dados simulados para demonstração
        const mockAdData: AdData = {
          success: true,
          platform: 'meta',
          url: url,
          headline: 'Descubra o Segredo para Pele Jovem aos 50+',
          description: 'Este produto revolucionário está ajudando milhares de mulheres a recuperar a juventude da pele. Resultados visíveis em apenas 14 dias!',
          images: ['https://via.placeholder.com/400x300'],
          cta: 'Saiba Mais',
          landing_page: 'https://exemplo.com/produto'
        };
        
        const mockAnalysisResult: AnalysisResult = {
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
        };
        
        setAdData(mockAdData);
        setAnalysisResult(mockAnalysisResult);
        setLoading(false);
      }, 2000);
      
    } catch (err) {
      setError('Ocorreu um erro ao processar a URL. Por favor, tente novamente.');
      setLoading(false);
    }
  };

  const handleDownload = (format: string) => {
    // Em um ambiente real, isso seria substituído por chamadas para download dos arquivos
    alert(`Download do arquivo em formato ${format} iniciado!`);
  };

  return (
    <div className="app-container">
      <header className="app-header">
        <h1>🕵️‍♂️ Spy Criativos</h1>
        <p>Extraia e otimize criativos de anúncios com IA</p>
      </header>

      <main className="app-main">
        <section className="url-input-section">
          <form onSubmit={handleSubmit}>
            <div className="input-group">
              <input
                type="url"
                value={url}
                onChange={(e) => setUrl(e.target.value)}
                placeholder="Cole a URL do anúncio (Meta Ads, Taboola, Outbrain, etc.)"
                required
              />
              <button type="submit" disabled={loading}>
                {loading ? 'Processando...' : 'Analisar'}
              </button>
            </div>
            {error && <div className="error-message">{error}</div>}
          </form>
        </section>

        {loading && (
          <div className="loading-container">
            <div className="loading-spinner"></div>
            <p>Analisando o anúncio e gerando variações...</p>
          </div>
        )}

        {adData && analysisResult && !loading && (
          <>
            <section className="results-section">
              <div className="tabs">
                <button
                  className={activeTab === 'original' ? 'active' : ''}
                  onClick={() => setActiveTab('original')}
                >
                  Original
                </button>
                <button
                  className={activeTab === 'emocional' ? 'active' : ''}
                  onClick={() => setActiveTab('emocional')}
                >
                  Emocional
                </button>
                <button
                  className={activeTab === 'escassez' ? 'active' : ''}
                  onClick={() => setActiveTab('escassez')}
                >
                  Escassez
                </button>
                <button
                  className={activeTab === 'autoridade' ? 'active' : ''}
                  onClick={() => setActiveTab('autoridade')}
                >
                  Autoridade
                </button>
                <button
                  className={activeTab === 'landing' ? 'active' : ''}
                  onClick={() => setActiveTab('landing')}
                >
                  Landing Page
                </button>
              </div>

              <div className="tab-content">
                {activeTab === 'original' && (
                  <div className="variation-card original">
                    <div className="card-header">
                      <h3>Criativo Original</h3>
                      <span className="angle-badge">
                        {analysisResult.original.primary_angle}
                      </span>
                    </div>
                    <div className="card-body">
                      <div className="headline">{analysisResult.original.headline}</div>
                      <div className="description">{analysisResult.original.description}</div>
                      <div className="cta">CTA: {analysisResult.original.cta}</div>
                      {adData.images && adData.images.length > 0 && (
                        <div className="image-container">
                          <img src={adData.images[0]} alt="Imagem do anúncio" />
                        </div>
                      )}
                    </div>
                  </div>
                )}

                {activeTab === 'emocional' && (
                  <div className="variation-card emocional">
                    <div className="card-header">
                      <h3>Variação Emocional</h3>
                      <span className="angle-badge">emocional</span>
                    </div>
                    <div className="card-body">
                      <div className="headline">{analysisResult.variations.emocional.headline}</div>
                      <div className="description">{analysisResult.variations.emocional.description}</div>
                      <div className="cta">CTA: {analysisResult.variations.emocional.cta}</div>
                      {adData.images && adData.images.length > 0 && (
                        <div className="image-container">
                          <img src={adData.images[0]} alt="Imagem do anúncio" />
                        </div>
                      )}
                    </div>
                  </div>
                )}

                {activeTab === 'escassez' && (
                  <div className="variation-card escassez">
                    <div className="card-header">
                      <h3>Variação Escassez</h3>
                      <span className="angle-badge">escassez</span>
                    </div>
                    <div className="card-body">
                      <div className="headline">{analysisResult.variations.escassez.headline}</div>
                      <div className="description">{analysisResult.variations.escassez.description}</div>
                      <div className="cta">CTA: {analysisResult.variations.escassez.cta}</div>
                      {adData.images && adData.images.length > 0 && (
                        <div className="image-container">
                          <img src={adData.images[0]} alt="Imagem do anúncio" />
                        </div>
                      )}
                    </div>
                  </div>
                )}

                {activeTab === 'autoridade' && (
                  <div className="variation-card autoridade">
                    <div className="card-header">
                      <h3>Variação Autoridade</h3>
                      <span className="angle-badge">autoridade</span>
                    </div>
                    <div className="card-body">
                      <div className="headline">{analysisResult.variations.autoridade.headline}</div>
                      <div className="description">{analysisResult.variations.autoridade.description}</div>
                      <div className="cta">CTA: {analysisResult.variations.autoridade.cta}</div>
                      {adData.images && adData.images.length > 0 && (
                        <div className="image-container">
                          <img src={adData.images[0]} alt="Imagem do anúncio" />
                        </div>
                      )}
                    </div>
                  </div>
                )}

                {activeTab === 'landing' && (
                  <div className="variation-card landing">
                    <div className="card-header">
                      <h3>Variação Landing Page</h3>
                    </div>
                    <div className="card-body landing-preview">
                      <h2 className="landing-headline">{analysisResult.landing_page.headline}</h2>
                      <h3 className="landing-subheadline">{analysisResult.landing_page.subheadline}</h3>
                      <div className="landing-bullets">
                        {analysisResult.landing_page.bullets.map((bullet, index) => (
                          <div key={index} className="bullet-item">{bullet}</div>
                        ))}
                      </div>
                      <div className="landing-cta">{analysisResult.landing_page.cta}</div>
                      <div className="landing-testimonial">{analysisResult.landing_page.testimonial}</div>
                    </div>
                  </div>
                )}
              </div>
            </section>

            <section className="download-section">
              <h3>Exportar Resultados</h3>
              <div className="download-buttons">
                <button onClick={() => handleDownload('pdf')} className="download-btn pdf">
                  Baixar PDF
                </button>
                <button onClick={() => handleDownload('html')} className="download-btn html">
                  Baixar HTML
                </button>
                <button onClick={() => handleDownload('markdown')} className="download-btn markdown">
                  Baixar Markdown
                </button>
                <button onClick={() => handleDownload('landing')} className="download-btn landing">
                  Baixar Landing Page
                </button>
              </div>
            </section>
          </>
        )}
      </main>

      <footer className="app-footer">
        <p>Spy Criativos - Otimize seus anúncios com IA</p>
      </footer>
    </div>
  );
}

export default App;
