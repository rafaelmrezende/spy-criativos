# README - Spy Criativos

## Sobre o Projeto

O Spy Criativos é um micro SaaS que permite extrair criativos de anúncios (Meta Ads, Taboola, Outbrain, etc.) e gerar automaticamente 3 novas versões otimizadas com diferentes ângulos de persuasão (emocional, escassez e autoridade).

## Funcionalidades

- **Extração de Criativos**: Cole a URL de um anúncio para extrair texto, imagem e página de destino
- **Análise com IA**: Identifica automaticamente o ângulo principal do anúncio original
- **Geração de Variações**: Cria 3 novas versões otimizadas com diferentes abordagens:
  - Variação A: Foco emocional
  - Variação B: Foco em escassez e urgência
  - Variação C: Foco em autoridade / prova social
- **Geração de Landing Page**: Cria uma variação de landing page otimizada para conversão
- **Exportação Múltipla**: Exporte os resultados em PDF, HTML e Markdown

## Instruções de Deploy (Sem Programação)

### Opção 1: Deploy via Vercel (Recomendado)

1. **Crie uma conta na Vercel**
   - Acesse [vercel.com](https://vercel.com)
   - Clique em "Sign Up" e crie uma conta (pode usar GitHub, GitLab ou email)

2. **Crie um repositório no GitHub**
   - Acesse [github.com](https://github.com)
   - Clique em "New repository"
   - Dê um nome ao repositório (ex: "spy-criativos")
   - Deixe como público e clique em "Create repository"

3. **Faça upload dos arquivos**
   - Na página do repositório, clique em "uploading an existing file"
   - Arraste todos os arquivos da pasta `spy-criativos-interface` para o navegador
   - Clique em "Commit changes"

4. **Conecte o Vercel ao GitHub**
   - Volte para o Vercel e faça login
   - Clique em "New Project"
   - Selecione o repositório que você acabou de criar
   - Mantenha as configurações padrão e clique em "Deploy"

5. **Acesse seu site**
   - Após o deploy (cerca de 1-2 minutos), o Vercel fornecerá uma URL
   - Seu Spy Criativos estará disponível nessa URL!

### Opção 2: Deploy Local (Para Testes)

1. **Instale o Node.js**
   - Baixe e instale o Node.js em [nodejs.org](https://nodejs.org)

2. **Abra o terminal/prompt de comando**
   - No Windows: Pressione Win+R, digite "cmd" e pressione Enter
   - No Mac: Abra o aplicativo Terminal

3. **Navegue até a pasta do projeto**
   ```
   cd caminho/para/spy-criativos-interface
   ```

4. **Instale as dependências**
   ```
   npm install
   ```

5. **Inicie o servidor local**
   ```
   npm start
   ```

6. **Acesse o aplicativo**
   - Abra seu navegador e acesse: http://localhost:3000

## Estrutura do Projeto

```
spy-criativos/
├── src/                    # Código-fonte Python
│   ├── scraper.py          # Módulo de extração de anúncios
│   ├── analyzer.py         # Módulo de análise e geração de variações
│   └── exporter.py         # Módulo de exportação (PDF, HTML, Markdown)
│
├── output/                 # Arquivos gerados
│   ├── variacoes.html      # Variações em formato HTML
│   ├── variacoes.pdf       # Variações em formato PDF
│   ├── variacoes.md        # Variações em formato Markdown
│   └── landing_page_variacao.html  # Landing page otimizada
│
├── spy-criativos-interface/  # Interface de usuário React
│   ├── src/                # Código-fonte da interface
│   ├── public/             # Arquivos públicos
│   └── package.json        # Dependências e scripts
│
└── README.md               # Este arquivo
```

## Uso do Aplicativo

1. Acesse a URL do seu aplicativo (fornecida pelo Vercel ou localhost)
2. Cole a URL de um anúncio no campo de entrada
3. Clique em "Analisar"
4. Navegue entre as abas para ver as diferentes variações
5. Use os botões de download para exportar os resultados

## Suporte

Se precisar de ajuda, entre em contato através do email: suporte@spycriativos.com

---

Desenvolvido com ❤️ pelo Spy Criativos
