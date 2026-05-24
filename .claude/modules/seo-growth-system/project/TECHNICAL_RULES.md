# Technical SEO Rules

## Objetivo
Definir as regras técnicas de SEO e o que nunca alterar sem plano.

## Quando usar
Crawl/index, canonical, redirects, sitemap, robots, status codes, schema técnico, paginação, CWV, render, WordPress técnico, mudanças de URL.

## Regras principais

### Áreas críticas (risco médio/alto)
robots.txt, sitemap.xml, noindex, canonical, redirects, slugs, status codes, schema, paginação, hreflang (se existir), archives WordPress, media attachment pages, Core Web Vitals, JS renderizado, links internos.

### Nunca alterar sem plano
slugs, redirects, canonical, robots, sitemap, noindex/nofollow, schema global, plugin SEO, URLs indexadas, páginas com tráfego orgânico.
**Plano mínimo:** problema · evidência · URLs afetadas · alteração proposta · risco · rollback · validação.

### Core Web Vitals
Alvos: LCP ≤ 2.5s · INP < 200ms · CLS baixo/estável. Ver em mobile e com experiência real. Não adicionar JS pesado global, animações sem fallback, imagens não otimizadas, fontes excessivas, dependências sem necessidade.

### Structured data
JSON-LD; representar conteúdo visível; sem schema enganador/reviews falsas; sem duplicação por plugin/tema; propriedades obrigatórias; preferir completo e correto a excessivo; validar com Rich Results quando possível. (Detalhe em [`SCHEMA_ENTITY_MODEL.md`](SCHEMA_ENTITY_MODEL.md).)

### WordPress SEO técnico
Verificar: archives desnecessários, tags/categories sem estratégia, author/date archives, media attachment pages, canonical do plugin, schema duplicado, breadcrumbs, enqueues, cache, lazy loading, templates globais, redirects, permalinks.

## Processo

### Auditoria técnica (framework)
- **Crawl/Index:** robots, sitemap, status codes, index/noindex, canonical, redirects, broken links, orphan pages, duplicate titles/descriptions, thin content, paginação, faceted URLs.
- **WordPress:** plugin SEO, schema duplicado, archives indexáveis, author/date, category/tag, attachment pages, templates, enqueues, caching.
- **Renderização:** conteúdo principal no HTML/renderizado, JS não bloqueia indexação, links em `<a href>`, lazy load não esconde conteúdo crítico.
- **Performance:** LCP/INP/CLS, imagens, fontes, JS/CSS, cache, mobile.
- **Structured data:** JSON-LD, Organization/LocalBusiness, BreadcrumbList, WebPage, Service, FAQ quando adequado, validação.

### URL changes (sempre sensível)
1. confirmar motivo; 2. verificar tráfego/indexação; 3. mapear redirect 301; 4. verificar internal links; 5. atualizar sitemap; 6. testar status/canonical; 7. validar no Search Console; 8. manter rollback.

## Inputs
URLs/área, acesso a GSC/URL Inspection/crawl (se autorizado), contexto WordPress.

## Outputs
Problemas (tabela), impacto, evidência, recomendação, risco, validação, necessidade de autorização.

## Agentes relacionados
[`technical-seo`](../agents/technical-seo.md), [`cwv-performance-seo`](../agents/cwv-performance-seo.md), [`wordpress-seo-implementation`](../agents/wordpress-seo-implementation.md), [`seo-qa`](../agents/seo-qa.md).

## Skills relacionadas
[`technical-seo-crawl-audit`](../skills/technical-seo-crawl-audit/SKILL.md), [`cwv-performance-seo-review`](../skills/cwv-performance-seo-review/SKILL.md).

## Ferramentas/MCPs possíveis
Search Console, URL Inspection, Lighthouse/PageSpeed, Playwright, Rich Results Test, sitemap/crawl. Ver [`TOOLING_MODEL.md`](TOOLING_MODEL.md).

## Critérios de qualidade
URLs estáveis preservadas; mudanças sensíveis com plano+rollback+validação; sem schema sem conteúdo visível; validação declarada honestamente.

## Notas de consolidação
Fusão das regras técnicas SEO do conteúdo ativo com o framework de auditoria da versão anterior do pacote SEO + checklist do agente técnico.
