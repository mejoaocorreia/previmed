# Technical SEO Rules

## Áreas críticas

Tratar como risco médio/alto:

- robots.txt;
- sitemap.xml;
- noindex;
- canonical;
- redirects;
- slugs;
- status codes;
- schema;
- pagination;
- hreflang, se existir;
- archives WordPress;
- media attachment pages;
- Core Web Vitals;
- JS renderizado;
- links internos.

---

## Nunca alterar sem plano

- slugs;
- redirects;
- canonical;
- robots;
- sitemap;
- noindex/nofollow;
- schema global;
- plugin SEO;
- URLs indexadas;
- páginas com tráfego orgânico.

Plano mínimo:
- problema;
- evidência;
- URLs afetadas;
- alteração proposta;
- risco;
- rollback;
- validação.

---

## Core Web Vitals

Alvos recomendados:

- LCP: até 2.5s;
- INP: inferior a 200ms;
- CLS: baixo/estável.

Performance deve ser vista em mobile e com experiência real.

Não adicionar:
- JS pesado global;
- animações sem fallback;
- imagens não otimizadas;
- fontes excessivas;
- dependências sem necessidade.

---

## Structured Data

Usar JSON-LD quando possível.

Regras:

- schema deve representar conteúdo visível;
- não usar schema enganador;
- não criar reviews falsas;
- não duplicar schema por plugin/tema;
- incluir propriedades obrigatórias;
- preferir completo e correto a excessivo;
- validar com Rich Results Test quando possível.

Tipos prováveis:

- Organization;
- LocalBusiness, se aplicável;
- WebSite;
- WebPage;
- BreadcrumbList;
- Service;
- FAQPage apenas com FAQ visível e útil.

---

## WordPress SEO técnico

Verificar:

- páginas de arquivo desnecessárias;
- tags/categories sem estratégia;
- author/date archives;
- media attachment pages;
- canonical gerado por plugin;
- schema duplicado;
- breadcrumbs;
- enqueues;
- cache;
- lazy loading;
- templates globais;
- redirects;
- permalinks.

---

## URL changes

Mudança de URL é sempre sensível.

Antes de mudar slug/URL:

1. confirmar motivo;
2. verificar tráfego/indexação;
3. mapear redirect 301;
4. verificar internal links;
5. atualizar sitemap;
6. testar status/canonical;
7. validar no Search Console;
8. manter rollback.

---

## Validação

Usar quando autorizado:

- Search Console;
- URL Inspection Tool/API;
- Lighthouse/PageSpeed;
- Playwright render check;
- Rich Results Test;
- sitemap check;
- crawl leve.

Se não foi validado, dizer claramente.


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
