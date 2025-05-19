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

2. **Faça upload dos arquivos**
   - Na página inicial da Vercel, clique em "Add New..." e depois em "Project"
   - Escolha "Upload" na seção "Import Git Repository"
   - Arraste todos os arquivos descompactados da pasta para o navegador
   - Clique em "Deploy"

3. **Acesse seu site**
   - Após o deploy (cerca de 1-2 minutos), o Vercel fornecerá uma URL
   - Seu Spy Criativos estará disponível nessa URL!

### Opção 2: Deploy via GitHub + Vercel

1. **Crie uma conta no GitHub**
   - Acesse [github.com](https://github.com)
   - Clique em "Sign Up" e crie uma conta

2. **Crie um repositório no GitHub**
   - Na página inicial do GitHub, clique em "New repository"
   - Dê um nome ao repositório (ex: "spy-criativos")
   - Deixe como público e clique em "Create repository"

3. **Faça upload dos arquivos**
   - Na página do repositório, clique em "uploading an existing file"
   - Arraste todos os arquivos descompactados para o navegador
   - Clique em "Commit changes"

4. **Conecte o Vercel ao GitHub**
   - Acesse [vercel.com](https://vercel.com) e faça login
   - Clique em "Add New..." e depois em "Project"
   - Selecione o repositório que você acabou de criar
   - Mantenha as configurações padrão e clique em "Deploy"

5. **Acesse seu site**
   - Após o deploy (cerca de 1-2 minutos), o Vercel fornecerá uma URL
   - Seu Spy Criativos estará disponível nessa URL!

### Opção 3: Deploy Local (Para Testes)

1. **Instale um servidor local simples**
   - Se você tem Python instalado, abra o terminal/prompt de comando
   - Navegue até a pasta com os arquivos descompactados
   - Execute: `python -m http.server 8000`
   - Abra seu navegador e acesse: http://localhost:8000

## Estrutura do Projeto

```
spy-criativos-vercel/
├── index.html          # Página principal da aplicação
├── styles.css          # Estilos CSS da aplicação
├── script.js           # Código JavaScript para funcionalidades
└── vercel.json         # Configuração para deploy no Vercel
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
