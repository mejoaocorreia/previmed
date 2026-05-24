# Skill: Technical SEO Crawl Audit

## Objetivo
Auditar o estado técnico de um site: crawl/index, render, WordPress técnico e structured data.

## Quando usar
Auditoria técnica, diagnóstico de indexação, antes de go-live, ou como parte de `/seo audit`/`/seo technical`.

## Quem pode usar
[`technical-seo`](../../agents/technical-seo.md) (principal); SEO Lead em coordenação.

## Inputs necessários
URLs/área, acesso (se autorizado) a GSC/URL Inspection/crawl leve, contexto WordPress (plugin SEO, tema).

## Procedimento
1. **Crawl/Index:** robots, sitemap, status codes, index/noindex, canonical, redirects, broken links, orphan/thin, paginação, faceted URLs.
2. **WordPress:** plugin SEO, schema duplicado, archives/author-date/category-tag/attachment pages, templates, enqueues, caching.
3. **Renderização:** conteúdo no HTML/renderizado, JS não bloqueia, links em `<a href>`, lazy load não esconde conteúdo crítico.
4. **Performance:** LCP/INP/CLS, imagens, fontes, JS/CSS, cache, mobile (handoff a `cwv-performance-seo` se profundo).
5. **Structured data:** JSON-LD, tipos esperados, validação.
6. Registar evidência e classificar impacto.

## Output esperado
Technical SEO Review: escopo · problemas (tabela) · impacto · evidência · recomendação · risco · validação · necessidade de autorização.

## Critérios de qualidade
Cada problema com evidência e impacto; URLs estáveis preservadas; valida só o que foi testado.

## Erros comuns
Assumir Lighthouse = SEO completo; confiar cegamente no plugin SEO; recomendar alterar canonical/redirect sem plano; concluir sem indicar validação.

## Agentes relacionados
[`technical-seo`](../../agents/technical-seo.md), [`cwv-performance-seo`](../../agents/cwv-performance-seo.md), [`seo-qa`](../../agents/seo-qa.md).

## Project docs relacionados
[`TECHNICAL_RULES`](../../project/TECHNICAL_RULES.md).

## Ferramentas/MCPs possíveis
Search Console, URL Inspection, Lighthouse/PageSpeed, Playwright, Rich Results, sitemap/crawl leve. Read-only.

## Notas de consolidação
Consolidado da versão anterior do pacote SEO (skill de crawl audit + framework de auditoria técnica).
