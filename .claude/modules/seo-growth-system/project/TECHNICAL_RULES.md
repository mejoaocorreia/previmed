# Technical SEO Rules

Fonte de verdade técnica do **SEO Growth System**.

Este ficheiro define as regras técnicas de SEO — o que nunca alterar sem plano, como auditar, como proteger URLs e indexação, como gerir WordPress SEO técnico e quando escalar para autorização ou handoff.

Este ficheiro não é um agente.  
Este ficheiro não executa alterações.  
Este ficheiro não substitui o `technical-seo`, o `seo-qa`, a skill `technical-seo-crawl-audit` nem o Supervisor/System Safety.

---

## Objetivo

Garantir que qualquer decisão ou alteração técnica SEO — crawl, indexação, redirects, canonical, robots, schema, WordPress técnico, Core Web Vitals — é feita com plano, evidência e rollback, e nunca compromete URLs indexadas, tráfego orgânico ou experiência do utilizador.

---

## Âmbito

Este documento cobre as regras para:

- crawl e indexação: robots.txt, sitemap.xml, noindex/nofollow, canonical, status codes;
- redirects: 301, 302, cadeias, loops, plano de redirect em mudanças de URL;
- renderização: conteúdo visível, JavaScript, lazy load, mobile-first;
- WordPress SEO técnico: plugin SEO, archives, media attachment pages, schema duplicado, breadcrumbs, permalinks, templates;
- structured data: JSON-LD, tipos, propriedades, validação, duplicação;
- Core Web Vitals: alvos LCP, INP, CLS, causas técnicas;
- URL changes: processo obrigatório antes de alterar slugs ou estrutura;
- go-live safety: checklist técnica antes de publicar.

---

## Fora de âmbito

Este documento não cobre:

- estratégia de conteúdo editorial — ver `CONTENT_RULES.md`;
- estratégia de intenção e keywords — ver `STRATEGY_RULES.md`;
- schema semântico completo (modelação de entidades) — ver `SCHEMA_ENTITY_MODEL.md`;
- local SEO e GBP — ver `LOCAL_SEO_PLAYBOOK.md`;
- ferramentas e MCP stack — ver `TOOLING_MODEL.md`;
- métricas e KPIs — ver `KPI_MODEL.md`.

---

## Responsabilidades por componente

| Componente | Responsabilidade |
|---|---|
| `TECHNICAL_RULES.md` (este ficheiro) | Standard e regras técnicas |
| [`technical-seo`](../agents/technical-seo.md) | Diagnóstico e recomendações técnicas |
| [`technical-seo-crawl-audit`](../skills/technical-seo-crawl-audit/SKILL.md) | Procedimento passo a passo de auditoria |
| [`wordpress-seo-implementation`](../agents/wordpress-seo-implementation.md) | Implementação controlada em WordPress |
| [`cwv-performance-seo`](../agents/cwv-performance-seo.md) | Diagnóstico aprofundado de Core Web Vitals |
| [`seo-qa`](../agents/seo-qa.md) | Validação final antes de entrega ou go-live |
| Supervisor/System Safety | Autorização de produção, rollback e risco crítico |

---

## Standards e regras

### Áreas críticas — risco médio/alto

Tratar com cuidado reforçado:

- robots.txt;
- sitemap.xml;
- noindex/nofollow;
- canonical;
- redirects e cadeias de redirect;
- slugs e estrutura de URLs;
- status codes (especialmente 301, 302, 404, 500);
- schema (duplicação, dados enganadores);
- paginação (rel next/prev, canonical);
- hreflang (se existir);
- archives WordPress (author, date, category, tag, attachment);
- Core Web Vitals (LCP, INP, CLS);
- JavaScript renderizado;
- links internos (rastreabilidade, orphan pages).

---

### Nunca alterar sem plano documentado

As seguintes áreas nunca devem ser alteradas sem plano documentado e autorização:

- slugs de páginas indexadas com tráfego;
- redirects de URLs com tráfego orgânico;
- canonical em páginas críticas;
- robots.txt com impacto em indexação;
- sitemap.xml global;
- noindex/nofollow em páginas indexadas;
- schema global ou configuração de plugin SEO;
- plugins activos no WordPress;
- permalinks (mudança de estrutura = mudança de todos os slugs);
- URLs indexadas com backlinks externos.

**Plano mínimo obrigatório antes de qualquer alteração:**

1. Problema: o que está errado e porquê.
2. Evidência: dados, URLs, GSC, ferramenta.
3. URLs afetadas: lista completa.
4. Alteração proposta: o que vai mudar exactamente.
5. Risco: o que pode correr mal.
6. Rollback: como reverter se necessário.
7. Validação: como confirmar que resultou.

---

### Core Web Vitals

**Alvos de referência:**

- LCP ≤ 2.5s (mobile e desktop);
- INP < 200ms;
- CLS ≤ 0.1 (baixo e estável).

**Regras:**

- Medir sempre em mobile (Google usa mobile-first indexing).
- Distinguir lab data (Lighthouse/PageSpeed) de field data (CrUX).
- Não usar apenas lab data como estado definitivo — confirmar com field data quando disponível.
- Performance mobile é prioritária face a desktop.

**Causas técnicas mais comuns:**

| Métrica | Causa provável |
|---|---|
| LCP lento | Imagem Hero pesada sem preload; TTFB alto; render-blocking JS/CSS; servidor lento |
| INP alto | JS bloqueante em interacção; event handlers pesados; third-party scripts; long tasks |
| CLS elevado | Imagens sem dimensões definidas; fontes com FOUT; ads sem espaço reservado; injeção de conteúdo |

**Não fazer:**

- Não adicionar JS pesado global sem performance review.
- Não adicionar animações sem fallback para `prefers-reduced-motion`.
- Não servir imagens não optimizadas.
- Não usar fontes excessivas ou sem font-display swap.
- Não adicionar dependências sem necessidade.

---

### Structured data / Schema técnico

**Regras gerais:**

- Usar JSON-LD sempre que possível (preferido pelo Google).
- Schema deve representar **conteúdo visível** na página — nunca marcar conteúdo inexistente.
- Não criar schema enganador: reviews, ratings, preços ou dados falsos.
- Não duplicar schema já gerado por plugin ou tema.
- Incluir propriedades obrigatórias antes das recomendadas.
- Preferir schema completo e correto a excessivo e inválido.
- Validar com Rich Results Test (quando URL acessível) ou Schema.org validator.

**Tipos mais comuns em sites WordPress:**

- Organization (homepage): name, url, logo, sameAs, contactPoint.
- LocalBusiness (se local): name, address, telephone, openingHours.
- WebSite: name, url, potentialAction (SearchAction).
- WebPage: name, url, breadcrumb.
- BreadcrumbList: itemListElement com item/name/position.
- Service: name, description, provider.
- FAQPage: apenas com FAQ visível no HTML.
- Article/BlogPosting: se houver blog com artigos reais.

Para detalhe completo de modelação semântica, ver [`SCHEMA_ENTITY_MODEL.md`](SCHEMA_ENTITY_MODEL.md).

---

### WordPress SEO técnico

**Checklist de áreas a verificar:**

- Plugin SEO activo (Yoast, Rank Math, etc.): configuração base, sitemap, breadcrumbs, metadados.
- Archives desnecessários indexados: author, date, category sem estratégia, tag sem estratégia.
- Media attachment pages: estão indexadas sem conteúdo útil?
- Schema duplicado: plugin + tema + manual a gerar o mesmo tipo de schema?
- Breadcrumbs: activos, corretos, com schema?
- Enqueues: scripts e estilos desnecessários a carregar globalmente?
- Caching: plugin de cache a interferir com rendering?
- Lazy loading: imagem LCP com `loading="lazy"` indevidamente?
- Templates globais: algum template com noindex acidental?
- Redirects de plugin: conflitos com rewrite rules?
- Permalinks: estrutura limpa? Alteração recente sem plano de redirects?

**Regra WordPress:**

Nunca alterar plugin SEO, tema activo, breadcrumbs globais, sitemap ou schema global sem:

1. ambiente de staging/preview validado;
2. plano de rollback definido;
3. autorização do Supervisor.

---

## Processo

### Framework de auditoria técnica

Seguir este framework para cada área (detalhe na skill [`technical-seo-crawl-audit`](../skills/technical-seo-crawl-audit/SKILL.md)):

**Crawl / Indexação:**
robots.txt · sitemap.xml · status codes · noindex/nofollow · canonical · cobertura GSC · redirects · broken links · orphan pages · thin/duplicate content · paginação · faceted URLs.

**WordPress técnico:**
plugin SEO · schema duplicado · archives indexáveis · author/date/category/tag · attachment pages · templates · enqueues · caching · lazy loading.

**Renderização:**
conteúdo principal no HTML renderizado · JS não bloqueia indexação · links em `<a href>` · lazy load não esconde conteúdo crítico · mobile rendering.

**Performance técnica:**
LCP · INP · CLS · imagens · fontes · JS/CSS render-blocking · cache · mobile-first.

**Structured data:**
JSON-LD · tipos corretos · propriedades obrigatórias · sem duplicação · sameAs · validação.

---

### URL changes — processo obrigatório

Mudança de URL/slug é sempre sensível e irreversível sem redirect.

**Antes de qualquer alteração de slug ou URL:**

1. Confirmar motivo da mudança (porquê agora? É necessário?).
2. Verificar tráfego orgânico e indexação da URL actual.
3. Mapear redirect 301 de URL antiga para URL nova.
4. Verificar e actualizar links internos.
5. Actualizar sitemap.
6. Testar status code e canonical após mudança.
7. Validar no Search Console (URL Inspection).
8. Manter rollback disponível (redirect reverse se necessário).

**Nunca alterar URL de página com tráfego orgânico sem redirect 301 mapeado.**

---

## Gates

**Bloquear ou pedir autorização obrigatoriamente** quando envolver:

- alteração de robots.txt com impacto em indexação;
- alteração de noindex/nofollow em páginas indexadas;
- alteração de canonical em páginas críticas;
- alteração de slugs ou estrutura de URLs indexadas;
- configuração de plugin SEO global;
- alteração de tema activo;
- alteração de sitemap.xml global;
- deploys ou go-live;
- rollback;
- Google Business Profile;
- credenciais, tokens, API keys;
- dados pessoais;
- ferramentas pagas.

**O resultado deve ser Bloqueado ou Precisa de autorização quando qualquer item acima estiver presente sem autorização explícita.**

---

## Relação com agentes, skills e comandos

- [`technical-seo`](../agents/technical-seo.md) — usa este documento como referência de regras e áreas críticas.
- [`technical-seo-crawl-audit`](../skills/technical-seo-crawl-audit/SKILL.md) — procedimento de auditoria que aplica estas regras.
- [`wordpress-seo-implementation`](../agents/wordpress-seo-implementation.md) — executa alterações dentro dos limites definidos aqui.
- [`cwv-performance-seo`](../agents/cwv-performance-seo.md) — aprofunda Core Web Vitals dentro dos alvos definidos aqui.
- [`seo-qa`](../agents/seo-qa.md) — aplica estes critérios na validação final.
- [`SCHEMA_ENTITY_MODEL.md`](SCHEMA_ENTITY_MODEL.md) — detalhe de schema semântico.
- [`/seo technical`](../commands/seo.md) — modo do comando SEO para trabalho técnico.
- [`/seo go-live`](../commands/seo.md) — modo do comando para go-live safety.

---

## Records / Persistência

Recomendar record quando houver:

- auditoria técnica completa;
- decisão de mudança de URL ou slug;
- plano de redirects com múltiplas URLs;
- go-live técnico de site ou secção;
- resolução de problema técnico crítico (noindex indevido, canonical errado, etc.).

Records reais vivem no projeto-alvo em `.claude/records/`.  
Usar templates em [`../records-templates/`](../records-templates/README.md).

Não guardar dados pessoais, credenciais ou informação confidencial em records.

---

## Regra final

SEO técnico protege a fundação do site.

Crawl, indexação, canonical, robots e redirects errados anulam qualquer trabalho de conteúdo ou keywords.

Antes de qualquer alteração técnica sensível: plano documentado, evidência, rollback, autorização.  
O que não foi validado não pode ser declarado como correto.  
O que pode partir a indexação não deve avançar sem revisão por `seo-qa` e Supervisor.
