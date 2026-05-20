# Growth Quality Gate

Este gate deve ser usado antes de aprovar recomendações ou implementação SEO/Growth.

## Perguntas obrigatórias

### Utilizador

- A alteração ajuda uma pessoa real?
- Responde melhor à intenção?
- Melhora clareza?
- Melhora confiança?

### Negócio

- Serve um objetivo comercial?
- Ajuda conversão?
- Está alinhado com serviços reais?
- Não promete demais?

### SEO

- Mantém indexabilidade?
- Não quebra URLs?
- Não cria duplicação?
- Não usa schema enganador?
- Não depende de keyword stuffing?
- Não cria conteúdo em escala sem valor?
- Não entra em conflito com Search Essentials/spam policies?

### Técnica

- Não prejudica performance?
- Não prejudica mobile?
- Não prejudica acessibilidade?
- É seguro em WordPress?
- Tem rollback quando necessário?

### Conteúdo

- É específico?
- É original?
- Tem prova?
- Evita genérico?
- Está revisto?
- Não inventa claims?

### AI Search

- Segue fundamentos SEO?
- Não usa truques de manipulação?
- Não cria conteúdo em escala sem valor?
- Mantém informação textual visível?
- Reforça entidade/marca de forma legítima?

### Governance

- Está dentro do escopo?
- Precisa de autorização?
- Precisa de dados reais?
- Precisa de ficheiro persistente?
- Precisa de validação humana?
- Precisa de handoff para WordPress/Visual/Safety?

---

## Resultado do gate

Classificar:

- **Aprovado** — pode avançar.
- **Aprovado com notas** — pode avançar com correções.
- **Bloqueado** — não avançar.
- **Precisa de dados** — falta Search Console, GA4, SERP, etc.
- **Precisa de autorização** — risco técnico/produção/dados.

## Formato

```md
## Growth Quality Gate

Resultado: [Aprovado / Aprovado com notas / Bloqueado / Precisa de dados / Precisa de autorização]

### Razão
...

### Riscos
...

### Correções obrigatórias
...

### Próximo passo
...
```


## Referências externas base

- Google Search Essentials: https://developers.google.com/search/docs/essentials
- Google SEO Starter Guide: https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- Helpful, reliable, people-first content: https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- AI features and your website: https://developers.google.com/search/docs/appearance/ai-features
- Structured data general guidelines: https://developers.google.com/search/docs/appearance/structured-data/sd-policies
- Structured data introduction: https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- Core Web Vitals and Google Search: https://developers.google.com/search/docs/appearance/core-web-vitals
- URL Inspection API: https://developers.google.com/search/blog/2022/01/url-inspection-api
- URL Inspection Tool: https://support.google.com/webmasters/answer/9012289
- Search spam policies: https://developers.google.com/search/docs/essentials/spam-policies
- Google Business Profile local ranking: https://support.google.com/business/answer/7091
