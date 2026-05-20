# Previmed Pages Audit — repetição de problemas estruturais — 2026-05-20

## Purpose

Verificar se os problemas estruturais identificados em `/saude-no-trabalho/` (title duplicado, hierarquia H1→H3 sem H2, schema genérico, zero links externos institucionais) se **repetem** noutras páginas core do site Previmed.

Se sim → quick fixes em batch, não pontuais.
Se não → fix isolado da `/saude-no-trabalho/`.

Origem: `reports/2026-05-20__competitor-deep-dive.md` §T1.

## Scope

URLs a auditar (todas existentes confirmadas via sitemap/navegação):

1. https://previmed.pt/ (home)
2. https://previmed.pt/saude-no-trabalho/ (já auditada em deep-dive — baseline)
3. https://previmed.pt/?page_id= ou páginas equivalentes de Segurança no Trabalho, HACCP, Formação se existirem
4. Discovery via navegação a partir do menu

**Não coberto:** posts de blog/notícias, páginas legais (política, cookies), submenu de portal trabalhador.

## Data Sources Used

| Fonte | Estado |
|---|---|
| Playwright MCP (navegação + JS evaluation) | em uso |
| `setup/BASELINE_AUDIT.md` (auditoria Fase 2.1) | reviewed |
| `reports/2026-05-20__competitor-deep-dive.md` (baseline `/saude-no-trabalho/`) | reviewed |

## Confidence Level

- **Medium.**
- Limitações: site Previmed em produção pode mudar entre captura e leitura deste relatório; URLs detectadas via menu podem não cobrir todas as páginas de serviço; algumas páginas pillar podem estar em CPTs internos não-públicos.

## Executive Summary

**Sim, os problemas estruturais de `/saude-no-trabalho/` repetem-se em todas as páginas core auditadas.** É template-level, não pontual.

5 URLs auditadas (Home + 4 páginas de serviço core). Padrão observado em **100% das páginas de serviço**:

- ❌ **Title duplicado**: `"<página> - Previmed - PrevimedPrevimed"` em 4/4 páginas de serviço.
- ❌ **Hierarquia H1 → H3** (sem H2) em 4/4.
- ❌ **Schema genérico** (Organization, WebSite, WebPage, BreadcrumbList, SearchAction) em 4/4. **Zero** Service / Article / FAQPage / HowTo.
- ❌ **0 links externos institucionais** em 4/4 (apenas links internos do grupo: careview, myprevimed, academia).
- ❌ **Word count extremamente baixo**: média 359w (range 165–732w) — competidores citados por AIO têm 1000–1400w.

**Achado crítico adicional** (compliance):
- `/consultoria-formacao/` cita **"35 horas" 3 vezes** e **"40 horas" 0 vezes**. Conteúdo desatualizado face à Lei 93/2019. Risco editorial.

**Achado adicional sobre home**:
- `/` (home) tem **H1 "Notícias Previmed"** — a home está como blog feed, não como homepage SEO-otimizada. Achado já flagged em `setup/BASELINE_AUDIT.md`, confirmado aqui.

**Conclusão:** os fixes têm de ser feitos **em batch ao template WordPress**, não página a página. Provavelmente um único template `page-servico.php` (ou equivalente) gera as 4 páginas de serviço com o mesmo defeito (title + estrutura).

## Findings

### Tabela comparativa Previmed

| Página | Title duplicado | H1 | H2 | H3 | Schema custom | Ext links institucionais | WC | Lists | FAQs |
|---|---|---|---|---|---|---|---|---|---|
| `/` (home) | ❌ "Previmed" (singular OK) | "Notícias Previmed" ⚠️ | 5 | n/d | nenhum | 0 | 318 | n/d | n/d |
| `/saude-no-trabalho/` | ✅ duplicado | 1 | **0** | 3 | nenhum | **0** | 732 | 2 | 3 |
| `/seguranca-no-trabalho/` | ✅ duplicado | 1 | **0** | 1 | nenhum | **0** | **219** | 3 | 3 |
| `/seguranca-higiene-alimentar/` | ✅ duplicado | 1 | **0** | 1 | nenhum | **0** | 331 | 4 | 3 |
| `/consultoria-formacao/` | ✅ duplicado | 1 | **0** | 1 | nenhum | **0** | **165** | 2 | 3 |

> **Schema comum em todas as páginas de serviço**: Organization, WebSite, WebPage, BreadcrumbList, SearchAction. **Nenhuma Service, Article, FAQPage, HowTo.**

### Detalhes por página

#### `/seguranca-no-trabalho/`
- Title: `"Segurança no Trabalho - Previmed - PrevimedPrevimed"`
- H1 "Segurança no Trabalho" → salta para H3 "Seguranca No Trabalho" (sem til!).
- 219w — abaixo do limiar mínimo defensável (~600w).
- Mesma stack `previmed.careview` + 0 ext institucionais.

#### `/seguranca-higiene-alimentar/`
- Title: `"Serviços de Segurança e Higiene Alimentar - Previmed - PrevimedPrevimed"`
- H1 "Serviços de Segurança e Higiene Alimentar" → H3 "Seguranca Higiene Alimentar" (sem til!).
- 331w. Cluster HACCP onde ASAE/DGAV citações eram obrigatórias — zero presentes.

#### `/consultoria-formacao/`
- Title: `"Formação profissional - Previmed - PrevimedPrevimed"`
- H1 "Formação profissional" → H3 "Consultoria Formacao" (sem til!).
- **165w — a página mais curta auditada.**
- **3 ocorrências de "35 horas"** vs **0 ocorrências de "40 horas"**. Conteúdo desatualizado.

### Padrões observados

1. **Title duplicado segue padrão `"<H1 da página> - Previmed - PrevimedPrevimed"`.** Provavelmente erro de template — duplica "Previmed" no `<title>` (uma vez pelo SEO plugin, outra pelo blogname WP).
2. **H3 secundário usa slug normalizado sem til** ("Seguranca", "Saude"). Sugere que o H3 é gerado pelo `post_name` em vez do `post_title`.
3. **Schema é puramente de tema WordPress** (provavelmente Yoast ou plugin SEO default). Sem customização por tipo de página.
4. **Stack de subdomínios `previmed.careview` é o único bloco de links** — toda a página é "ofertas internas", sem citação editorial.

## Recommended Action Plan

> **Importante:** todos estes fixes são **alterações ao site/templates WordPress**. **Não fazer agora** — apenas planear. Decisão de quando aplicar fica para o utilizador.

### Phase 1 — Template-level fixes (1 sessão de dev WP)

- [ ] **F1.** Corrigir bug do title duplicado no template global (`header.php` ou plugin SEO). Remover o duplo "Previmed".
- [ ] **F2.** Substituir o H3 secundário (slug normalizado) por H2 com o título correto (ou eliminar). Resolve a hierarquia H1→H3 em batch.
- [ ] **F3.** Adicionar campo "intro long" (rich text) ao CPT/template das páginas de serviço para suportar conteúdo de 800–1500w.

### Phase 2 — Schema markup (1 sessão dev WP)

- [ ] **S1.** Adicionar schema `Service` (com `offers` + `provider`) às 4 páginas de serviço core via custom JSON-LD por template.
- [ ] **S2.** Adicionar schema `FAQPage` à secção FAQ de cada página (preciso de criar FAQ se não existir).
- [ ] **S3.** Adicionar `datePublished` + `dateModified` ao schema (frescura editorial).
- [ ] **S4.** Considerar `Article` schema na pillar `/recursos/guias/*` quando esse hub for criado.

### Phase 3 — Editorial refresh (5 pillars × ~2h cada)

Aplicar a cada página de serviço o **template editorial Previmed** (a derivar dos relatórios `aio-expansion` + `competitor-deep-dive`):
- 1100–1500w por pillar.
- ≥4 links externos institucionais (ACT, pgdlisboa Lei 102/2009, + cluster-specific: DGS, ASAE/DGAV, Diário República).
- H1 → 6–8 H2 → H3 onde aplicável.
- 8–15 FAQs estruturadas.

### Phase 4 — Compliance fix urgente

- [ ] **C1.** `/consultoria-formacao/` — atualizar todas as ocorrências de "35 horas" para "40 horas (anteriormente 35h, alteração pela Lei 93/2019)". Aplicar política do cluster Formação registada em `strategy/KEYWORDS.md` §9.

### Phase 5 — Home

- [ ] **H1.** `/` — substituir H1 "Notícias Previmed" por H1 SEO-otimizado ("Serviços de Segurança e Saúde no Trabalho em Portugal — Previmed" ou similar). Atualmente a home está como feed de blog.

## Backlog Items To Add

A copiar para `../_living/BACKLOG.md`:

- `[Quick win] P1` Fix title duplicado a nível de template (afeta todas as páginas core). Origem: `reports/2026-05-20__previmed-pages-audit.md` §F1.
- `[Quick win] P1` `/consultoria-formacao/`: atualizar "35h" → "40h (Lei 93/2019)" — compliance editorial. Origem: §C1.
- `[Quick win] P2` Home `/`: substituir H1 "Notícias Previmed" por H1 SEO. Origem: §H1.
- `[Technical blocker] P1` Refatorar template páginas de serviço — H1→H2 (não H3). Origem: §F2.
- `[Schema/entity improvements] P1` Schema Service + FAQPage por template — afeta 4 páginas em batch. Origem: §S1+§S2.
- `[Content opportunity] P1` Editorial refresh por pillar (5 pillars × ~2h, aplica padrão Centralmed+SEPRI+Forprev). Origem: §Phase 3.

## Decisions Needed

1. **Quando aplicar os fixes ao site?** Greenfield SEO-first significa que o ideal é fazer tudo em batch antes de re-promover o site. Mas o foothold AIO Q5 atual da `/saude-no-trabalho/` está dependente do estado atual — refactor pode quebrar temporariamente. **Recomendação**: fazer os fixes em batch num staging environment, validar AIO em recapture pós-deploy.

2. **Ordem de produção dos pillars editorial-refresh** (Phase 3): igual à do brief plan?

## Last Updated

2026-05-20 por Claude (SEO Lead).
