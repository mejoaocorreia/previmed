---
name: technical-seo-crawl-audit
description: Procedimento passo a passo para auditar o estado técnico de um site — crawl, indexação, renderização, WordPress técnico e schema estrutural. Usado principalmente pelo agente technical-seo.
---

# Skill: Technical SEO Crawl Audit

Procedimento operacional para auditar o estado técnico de um site ou secção.

Esta skill é usada principalmente pelo [`technical-seo`](../../agents/technical-seo.md) para conduzir auditorias técnicas estruturadas — crawl, indexação, renderização, WordPress técnico e schema estrutural.

Esta skill não é um agente.  
Esta skill não coordena subagentes.  
Esta skill não executa alterações.  
Esta skill não aprova produção, redirects, canonical ou robots sem autorização.  
Esta skill define o procedimento para auditar o estado técnico de forma consistente.

---

## Objetivo

Auditar o estado técnico de um site identificando o que bloqueia ou prejudica rastreamento, indexação, renderização e performance técnica — com evidência, impacto, prioridade e plano de handoff.

---

## Quando usar

Usar nos modos:

- `/seo audit` — como parte da auditoria SEO completa;
- `/seo technical` — auditoria técnica específica;
- `/seo go-live` — checklist antes de publicar;
- análise pontual de problema técnico específico.

Usar quando o pedido envolver:

- o site não está a indexar;
- páginas não aparecem no Google;
- robots.txt, sitemap, canonical ou noindex incorretos;
- redirects quebrados ou em cadeia;
- archives WordPress desnecessários indexados;
- schema duplicado;
- conteúdo não renderizado pelo Google;
- orphan pages;
- go-live técnico.

---

## Quando não usar

Não usar esta skill para:

- escrever ou otimizar conteúdo — usar `onpage-optimization-pass`;
- fazer keyword research — usar `keyword-cluster-map`;
- análise semântica de schema — usar `schema-entity-review`;
- análise aprofundada de Core Web Vitals — usar `cwv-performance-seo-review`;
- implementar alterações em WordPress — usar `technical-seo` → handoff para `wordpress-seo-implementation`;
- decidir produção, deploy ou rollback — escalar para Supervisor/System Safety.

---

## Quem pode usar

Principal:

- [`technical-seo`](../../agents/technical-seo.md)

Também pode usar:

- [`seo-lead`](../../agents/seo-lead.md) em coordenação de auditoria completa;
- [`seo-qa`](../../agents/seo-qa.md) para validação técnica antes de go-live.

---

## Fontes de verdade

Consultar por esta ordem:

1. [`../../project/TECHNICAL_RULES.md`](../../project/TECHNICAL_RULES.md) — regras técnicas, áreas críticas, URL changes, WordPress.
2. [`../../project/SCHEMA_ENTITY_MODEL.md`](../../project/SCHEMA_ENTITY_MODEL.md) — tipos de schema, propriedades, validação.
3. [`../../project/QUALITY_GATE.md`](../../project/QUALITY_GATE.md) — critérios de aprovação.
4. [`../../project/TOOLING_MODEL.md`](../../project/TOOLING_MODEL.md) — ferramentas disponíveis e limites.

---

## Inputs necessários

Para executar a auditoria:

- URLs ou área a auditar (secção, domínio, template);
- acesso autorizado a GSC / URL Inspection (se disponível);
- acesso a Playwright ou sitemap para crawl leve (se disponível);
- contexto WordPress: plugin SEO activo, tema, plugins relevantes;
- alterações recentes no site (deploys, redirects, conteúdo novo);
- fase do projecto: novo site, migração, refresh ou manutenção;
- ambiente: local, staging, preview, produção ou desconhecido;
- objetivo: auditoria completa, problema específico ou go-live.

Se inputs estiverem incompletos:

- trabalhar com o disponível;
- marcar hipóteses como hipóteses;
- não inventar estado técnico;
- declarar o que ficou por validar.

---

## Procedimento

### Passo 1 — Confirmar escopo e ambiente

Antes de auditar, confirmar:

- que site/secção/páginas estão em análise;
- qual é o ambiente (staging vs produção);
- que ferramentas estão disponíveis e autorizadas;
- que alterações recentes possam ter causado problemas;
- se há URLs críticas a priorizar.

Se o ambiente for desconhecido, não assumir produção. Pedir confirmação.

---

### Passo 2 — Crawl e indexação

**robots.txt:**
- Verificar se existe e está acessível em `/robots.txt`.
- Verificar se User-agent: Googlebot tem regras de Disallow indevidas.
- Testar URLs críticas contra as regras (tool GSC Robot Testing ou manualmente).
- Verificar se sitemap está referenciado.

**sitemap.xml:**
- Verificar se existe e está acessível.
- Verificar se inclui as páginas certas (sem noindex, sem páginas 404/301).
- Verificar se foi submetido ao GSC.
- Verificar data de última modificação.

**Status codes:**
- Verificar páginas principais: 200 ou redirecionadas adequadamente?
- Verificar redirects: 301 (permanente) vs 302 (temporário) — 302 onde deve ser 301?
- Verificar cadeias de redirect (A→B→C): devem ser resolvidas para redirect direto.
- Verificar loops de redirect.
- Verificar 404 em páginas que deveriam existir.
- Verificar broken links internos.

**noindex / nofollow:**
- Verificar se páginas importantes têm `noindex` indevido (via meta robots ou X-Robots-Tag).
- Verificar se pages de arquivo WordPress (author, date, tags sem estratégia) estão indexadas quando não deveriam.
- Verificar se páginas de staging ou ambiente de teste têm noindex activo.

**canonical:**
- Verificar se canonical está a auto-referenciar a URL correcta.
- Verificar se canonical não aponta para página errada.
- Verificar se há canonical conflict (dois canonicals na mesma página).
- Verificar se versões http/https e www/non-www têm canonical consistente.
- Verificar paginação: rel="next"/"prev" ou canonical adequado.

**Cobertura GSC** (se autorizado):
- Verificar páginas com erros de indexação (redirect error, server error, not found).
- Verificar páginas excluídas por canonical, noindex ou crawl anomaly.
- Verificar páginas descobertas mas não indexadas.
- Verificar páginas válidas com ou sem rich results.

---

### Passo 3 — Renderização

**Conteúdo visível:**
- Confirmar que conteúdo principal (H1, texto crítico, FAQs) está no HTML renderizado.
- Verificar se há conteúdo importante carregado apenas via JavaScript que pode não ser indexado.

**JavaScript:**
- Verificar se JS render-blocking bloqueia indexação de conteúdo crítico.
- Verificar se conteúdo em SPA, tabs escondidas, accordions ou modal é acessível no DOM.

**Lazy load:**
- Verificar que imagens com lazy load não escondem conteúdo textual crítico.
- Verificar que imagens Hero/LCP não têm lazy load (deve ser `loading="eager"`).

**Links internos:**
- Confirmar que links internos estão em `<a href="...">` rastreáveis (não apenas em JS event handlers).
- Verificar que menu, breadcrumbs e footer estão rastreáveis.

**Mobile rendering:**
- Se Playwright disponível, verificar rendering em viewport mobile.
- Verificar que conteúdo mobile = conteúdo desktop (indexação mobile-first).

---

### Passo 4 — Estrutura de URLs

**Slugs e estrutura:**
- Verificar se URLs são limpas, descritivas e sem parâmetros desnecessários.
- Verificar se há parâmetros de sessão, tracking ou UTM indexados.
- Verificar se faceted navigation está a gerar URLs indexáveis desnecessárias.
- Verificar se há paginação mal configurada.

**Orphan pages:**
- Identificar páginas importantes sem nenhum link interno.
- Verificar se páginas de serviço, guias e landing pages críticas têm links internos.

---

### Passo 5 — WordPress técnico

**Plugin SEO:**
- Identificar plugin SEO activo (Yoast SEO, Rank Math, All in One SEO, AIOSEO, etc.).
- Verificar configuração básica: title/meta activos, sitemap gerado, breadcrumbs.
- Verificar se plugin SEO e tema não estão a duplicar metadados ou schema.

**Archives desnecessários:**
- Author pages: estão indexadas? Têm conteúdo útil?
- Date archives: estão indexadas sem estratégia?
- Category pages: têm conteúdo útil ou são thin content?
- Tag pages: têm conteúdo útil ou são doorway pages de tags?
- Acção recomendada padrão: noindex em archives sem valor; não remover sem plano.

**Media attachment pages:**
- WordPress cria páginas para cada ficheiro de media. Estão indexadas?
- Se sim, verificar se têm conteúdo útil ou são thin content.
- Acção recomendada: redirecionar para imagem ou página pai, ou noindex.

**Schema duplicado:**
- Verificar se plugin SEO, tema e markup manual estão a gerar o mesmo schema.
- Identificar origem de cada bloco JSON-LD na página.
- Schema duplicado pode causar erros no Rich Results Test.

**Breadcrumbs:**
- Verificar se breadcrumbs estão activos e corretos.
- Verificar schema BreadcrumbList associado.

**Caching:**
- Verificar se plugin de cache está activo.
- Verificar se cache está a servir versões incorretas de páginas.
- Verificar se cache interfere com rendering do Googlebot.

**Lazy loading de imagens:**
- Verificar que imagem LCP (Hero) não tem `loading="lazy"`.
- Verificar que lazy load de imagens está correto para as restantes.

**Permalinks:**
- Verificar estrutura de permalinks: `/slug/` ou `/%postname%/` é preferível.
- Verificar se estrutura foi alterada recentemente sem plano de redirects.

---

### Passo 6 — Schema técnico

**Inventário:**
- Identificar todos os tipos de schema activos no site.
- Registar origem: plugin SEO, tema, código manual, Gutenberg block.

**Correspondência:**
- Verificar que cada schema representa conteúdo visível na página.
- Não deve existir schema para conteúdo escondido ou inexistente.

**Propriedades obrigatórias:**
- Organization: name, url. Recomendado: logo, contactPoint, sameAs.
- LocalBusiness: name, address, telephone. Recomendado: openingHours, geo.
- WebPage: name, url. Recomendado: description, breadcrumb.
- BreadcrumbList: itemListElement com item/name/position.
- FAQPage: apenas com FAQ visível no HTML.
- Service: name, description, provider.

**sameAs:**
- Apenas perfis oficiais reais: LinkedIn, Facebook, Instagram, Twitter/X, Google Business Profile.
- Não inventar perfis.
- Verificar se URLs estão correctas e acessíveis.

**Duplicação:**
- Verificar se plugin SEO e tema geram o mesmo tipo de schema.
- Identificar o que deve ser desactivado para evitar conflito.

**Validação:**
- Rich Results Test (quando URL acessível).
- Schema.org validator (quando apenas código disponível).

---

### Passo 7 — Core Web Vitals (resumo técnico)

**Dados a recolher:**
- LCP, INP, CLS de páginas principais via PageSpeed Insights (lab data).
- Field data CrUX quando disponível.
- Identificar se dados são lab, field ou hipótese.

**Causas técnicas prováveis:**
- LCP lento: imagem LCP pesada, sem preload, lazy load indevido, TTFB alto.
- INP alto: JS bloqueante, event handlers pesados, third-party scripts.
- CLS elevado: imagens sem dimensões, fontes com FOUT, ads sem espaço reservado.

**Decisão:**
- Se diagnóstico for superficial (apenas identificar causa provável), reportar aqui.
- Se for necessário análise profunda: handoff para `seo-growth-system:cwv-performance-seo`.

---

### Passo 8 — Classificar e priorizar

Para cada problema encontrado, registar:

| Área | Problema | Evidência | Impacto | Prioridade | Correção proposta | Precisa de autorização? |
|---|---|---|---|---|---|---|

Impacto: Crítico / Alto / Médio / Baixo / Informativo.  
Prioridade: 1 (bloqueio) / 2 (urgente) / 3 (importante) / 4 (melhoria) / 5 (nota).

---

### Passo 9 — Declarar validação e lacunas

Declarar explicitamente:

- "Validado com [ferramenta/evidência]": o que foi confirmado.
- "Hipótese": o que foi inferido sem validação completa.
- "Não validado / a confirmar": o que ficou por verificar.

Nunca dizer "está tudo limpo" sem crawl real ou GSC.

---

## Output esperado

```md
## Technical SEO Crawl Audit — [Escopo] — YYYY-MM-DD

### Resumo executivo
[1-3 problemas mais críticos + estado geral]

### Problemas encontrados
| Área | Problema | Evidência | Impacto | Prioridade | Correção proposta | Autorização? |
|---|---|---|---|---|---|---|

### Diagnóstico detalhado por área
[crawl/indexação, renderização, redirects/URLs, WordPress técnico, schema, CWV resumo, internal links/orphan]

### Evidência usada
[ferramentas usadas, URLs testadas, dados disponíveis]

### Não validado / a confirmar
[lista explícita do que ficou por verificar]

### Riscos
[produção, URLs indexadas, redirects, WordPress, schema]

### Plano de handoff
[o que deve executar: wordpress-seo-implementation, seo-qa, Supervisor, WordPress Engineering]

### Record recomendado?
[sim — auditoria técnica datada]

### Próximo passo
[ação imediata]
```

---

## Gates de segurança

Read-only por defeito.

Esta skill deve bloquear ou pedir autorização quando envolver:

- produção;
- robots.txt com impacto em indexação;
- noindex/nofollow em páginas indexadas;
- canonical em páginas críticas;
- redirects de URLs com tráfego;
- slugs de páginas indexadas;
- plugin SEO configuração global;
- tema activo;
- deploy ou go-live;
- credenciais, tokens, API keys;
- dados pessoais ou sensíveis.

Esta skill não concede autorização.  
Identifica risco e encaminha para o agente/área correta.

---

## Relação com agentes e docs

- [`technical-seo`](../../agents/technical-seo.md) — agente principal que usa este procedimento.
- [`wordpress-seo-implementation`](../../agents/wordpress-seo-implementation.md) — executa as correções identificadas.
- [`seo-qa`](../../agents/seo-qa.md) — valida a auditoria antes de entrega ou go-live.
- [`cwv-performance-seo-review`](../cwv-performance-seo-review/SKILL.md) — aprofunda CWV se necessário.
- [`schema-entity-review`](../schema-entity-review/SKILL.md) — aprofunda schema semântico se necessário.
- [`TECHNICAL_RULES.md`](../../project/TECHNICAL_RULES.md) — regras e standards técnicos.
- [`QUALITY_GATE.md`](../../project/QUALITY_GATE.md) — critérios de aprovação.

---

## Exemplos de pedidos que aceita

- "Aplica o procedimento de auditoria técnica a este site."
- "Segue o processo de crawl audit para esta secção."
- "Usa este procedimento para preparar a checklist de go-live."
- "Audita tecnicamente o site antes da migração."
- "Diagnostica os problemas técnicos que podem estar a bloquear indexação."

---

## Exemplos de pedidos que deve encaminhar

Encaminhar para `technical-seo` (agente principal):

- "Faz uma auditoria técnica completa" — o agente decide o escopo e usa esta skill.

Encaminhar para `wordpress-seo-implementation` + Supervisor:

- "Implementa os redirects."
- "Altera o robots.txt."
- "Corrige os canonicals em produção."

Encaminhar para `cwv-performance-seo-review`:

- "Analisa em detalhe o LCP e CLS desta página."

Encaminhar para Supervisor/System Safety:

- "Acede ao GSC com estas credenciais."
- "Faz deploy após a auditoria."

---

## Erros comuns a evitar

- Assumir que Lighthouse = auditoria técnica completa.
- Confiar cegamente que o plugin SEO resolve tudo.
- Recomendar alterar canonical ou redirect sem plano documentado.
- Concluir sem declarar o que não foi validado.
- Ignorar archives WordPress desnecessários indexados.
- Dizer "schema está correto" sem validação com ferramenta.
- Tratar hipótese como evidência.

---

## Regra final

Esta skill existe para tornar auditorias técnicas SEO consistentes e profissionais.

Cada problema deve ter evidência.  
Cada recomendação deve ter impacto e risco.  
Cada decisão sensível deve ter plano e autorização.  
O que não foi validado deve ser declarado como tal.

SEO técnico sem evidência não é diagnóstico — é especulação.
