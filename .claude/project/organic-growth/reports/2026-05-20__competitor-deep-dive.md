# Competitor Deep-Dive — top AIO citations — 2026-05-20

## Purpose

Auditar tecnicamente e editorialmente as páginas dos 3 concorrentes HSST PT que dominam citações AIO segundo o relatório [`2026-05-20__aio-expansion.md`](./2026-05-20__aio-expansion.md):

- **Forprev** (top citado em Q5 "como escolher empresa medicina do trabalho").
- **SEPRI** (3 citações em Q1 "medicina do trabalho" — pillar + spin-offs).
- **Centralmed** (citado em Q1, Q3, Q5 — cross-cluster authority).

Identificar **porquê** estas páginas são premiadas pela AIO e que padrões Previmed deve replicar (ou superar) nos 5 briefs P1.

## Scope

URLs auditadas (sessão 2026-05-20):

1. https://forprev.pt/medicina-do-trabalho/ (cluster MT)
2. https://sepri.pt/noticia/medicina-do-trabalho-o-que-e-obrigacoes-como-funciona/ (cluster MT — pillar SEPRI)
3. https://sepri.pt/noticia/medicina-do-trabalho-lisboa-obrigacoes-legislacao/ (cluster MT — spin-off geográfico)
4. https://sepri.pt/noticia/ficha-de-aptidao-para-o-trabalho-tudo-o-que-deve-saber/ (cluster MT — spin-off tópico)
5. https://centralmed.pt/blog/como-funciona-a-medicina-do-trabalho-relevancia/ (cluster MT)
6. https://centralmed.pt/blog/haccp-nas-empresas-principais-vantagens/ (cluster HACCP)
7. https://centralmed.pt/blog/prestadoras-de-seguranca-higiene-e-saude-no-trabalho/ (cluster "como escolher")
8. https://previmed.pt/saude-no-trabalho/ (baseline próprio para comparação)

Por página, capturar:
- Estrutura H1–H4 (hierarquia editorial).
- Comprimento aproximado (contagem palavras).
- Schema markup detectado (JSON-LD).
- Links externos a fontes institucionais (ACT, ASAE, DGS, Diário República, pgdlisboa, OA, etc.).
- Links internos para outros artigos do mesmo domínio.
- Presença de tabelas, FAQs, vídeos embebidos, imagens, CTA.
- Frequência da keyword principal no H1/H2 e no body.
- Meta description e title da página.

**Não coberto:** análise de backlinks externos (requer Ahrefs/SEMrush — bloqueado pela decisão keyword data tool); análise de Core Web Vitals (PSI ainda não ligado).

## Data Sources Used

| Fonte | Estado |
|---|---|
| Playwright MCP (navegação + JS evaluation) | em uso |
| `reports/2026-05-20__aio-expansion.md` (origem da lista) | reviewed |
| Google Search Console / GA4 | not connected |
| DataForSEO / SEMrush / Ahrefs (backlinks, DR) | not connected |
| PSI / Lighthouse | not run nesta sessão |

## Confidence Level

- **Medium.**
- **Limitações:**
  - Snapshot único por página — não capta variações A/B test ou versões mobile.
  - Sem dados de backlinks/autoridade externa: o "porquê" da citação AIO pode ser autoridade off-site, não só on-page.
  - Schema é extraído por leitura do JSON-LD presente — schemas dinâmicos injetados por JS pós-load podem ser invisíveis.

## Executive Summary

Auditadas 8 URLs (7 concorrentes + 1 Previmed). Padrão claro emerge:

**1. Centralmed é o "padrão ouro" de citação institucional.** Em cada uma das 3 páginas auditadas (MT, HACCP, "como escolher"), Centralmed linka explicitamente para ACT (2–3 URLs específicas), DGS, DGERT, pgdlisboa (Lei 102/2009), e — onde aplicável — FAO/Codex Alimentarius, EUR-Lex, WHO, CDC, APSEI. **8–12 links externos institucionais por artigo.** Curiosamente, Centralmed **não tem schema JSON-LD detectável** nas páginas — o que sugere que a citação AIO está a ser premiada pela **densidade de citações outbound a fontes institucionais**, não por schema.

**2. SEPRI tem a estratégia de "árvore" mais agressiva.** 3 URLs distintas no AIO Q1 (pillar 1393w + spin-off geográfico Lisboa 1273w + spin-off tópico Ficha Aptidão 1186w). Cada uma é um Article com schema completo (7 tipos: Article, WebPage, ImageObject, BreadcrumbList, WebSite, Organization, Person). Padrão replicável: 1 pillar + N spin-offs cruzados.

**3. Forprev é o caso mais curto (656w) que aparece em AIO.** Conta com Service schema com offers, breadcrumb, e 28 FAQ-like accordions (mas SEM FAQPage schema explícito). Apenas 2 links externos. Sugere que **um Service schema bem feito + FAQ estruturada** pode compensar baixo word count.

**4. Previmed `/saude-no-trabalho/` tem problemas estruturais graves comparativamente:**
- **Title duplicado**: "Medicina No Trabalho - Previmed - PrevimedPrevimed" (confirma achado do `setup/BASELINE_AUDIT.md`).
- **Hierarquia editorial quebrada**: H1 → salta para H3 (sem H2 visíveis).
- **0 hits da query "medicina do trabalho"** no body: a página usa "Medicina **No** Trabalho" (com N maiúsculo, sem preposição "do") — divergência ortográfica relevante face à query AIO real.
- **0 links externos institucionais**: nem ACT, nem Lei 102/2009 (mencionada em meta description mas não linkada), nem DGS, nem ASAE. Citação Previmed em AIO Q5 acontece **apesar** disto, não por mérito on-page — provavelmente por autoridade de marca residual.
- **Sem Service schema** (Forprev tem), **sem Article schema** (SEPRI tem), **sem FAQPage** (apesar dos 3 FAQ-like elements). Apenas Organization + WebSite + WebPage + BreadcrumbList + SearchAction (todos genéricos de tema WordPress, não SEO-específicos).
- **732w**, **2 listas**, **3 FAQs** — muito abaixo do padrão Centralmed/SEPRI.

**Conclusão estratégica:** o caminho mais barato e mais alto-impacto para Previmed entrar em AIO de forma consistente nas 5 queries P1 é **replicar o padrão Centralmed de citação institucional outbound** (4–10 links externos a ACT/DGS/Lei 102/Lei 93/ASAE/Codex por pillar) + **adoptar padrão SEPRI de árvore** (pillar + 2–3 spin-offs) + **adicionar schema completo** (Article, FAQPage, HowTo, Service). A página `/saude-no-trabalho/` precisa de fix urgente independentemente de tudo o resto (title duplicado, H2 ausentes).

## Priority Findings

### Critical

- **C1. Previmed `/saude-no-trabalho/` tem title duplicado** — "Medicina No Trabalho - Previmed - PrevimedPrevimed". Já tinha sido flagged em `setup/BASELINE_AUDIT.md`. Esta página **é citada em AIO Q5** — o title impacta CTR e snippet. Fix imediato (baixo esforço, alto impacto).
- **C2. Previmed `/saude-no-trabalho/` usa "Medicina No Trabalho"** (N maiúsculo, sem "do") em vez da forma idiomática "medicina do trabalho". 0 ocorrências da query AIO real no body. **Decisão necessária**: corrigir on-page e/ou criar nova página com slug correto + redirect.
- **C3. Zero links externos institucionais nas páginas Previmed.** Centralmed linka 8–12 fontes (ACT, DGS, DGERT, pgdlisboa, FAO, APSEI). Padrão a replicar em todos os 5 briefs P1.

### High

- **H1. SEPRI usa estratégia "árvore" (pillar + spin-offs cruzados)** confirmada: 3 URLs do mesmo domínio dominam AIO Q1 com geo (Lisboa) + tópico (Ficha Aptidão) como variações. Replicar para Previmed com `/servicos/medicina-trabalho/` + spin-offs (`/recursos/guias/ficha-aptidao/`, `/recursos/medicina-trabalho-porto/` ou `/medicina-trabalho-norte/`).
- **H2. Schema do Previmed é "tema WordPress genérico"**, não SEO-específico. Não tem Service, Article, FAQPage, HowTo. Schema é gratuito de adicionar e pesa em AIO.
- **H3. Hierarquia editorial Previmed quebrada**: H1 → H3 (sem H2). Quebra outline acessibilidade + sinal SEO.
- **H4. Centralmed não tem schema JSON-LD detectável mas é fortemente citada por AIO.** Sinal de que **densidade de citação outbound institucional** pode pesar mais que schema na hierarquia AIO atual. Tornar isto **regra obrigatória** dos briefs.

### Medium

- **M1. Forprev compensa baixo word count (656w) com Service schema + offers + FAQ extensa.** Para páginas de serviço comerciais (não pillars informacionais), Forprev é o modelo replicável.
- **M2. SEPRI tem schema Article com Person** (autor identificado). Centralmed e Forprev não. AIO pode estar a usar Person como sinal de autoridade editorial. Hipótese — adicionar autor em briefs futuros.
- **M3. Previmed tem apenas 4 external links — 3 internos do grupo + cookieadmin.** Nenhum a fontes institucionais ou de autoridade temática.

### Low

- **L1. Nenhuma das páginas auditadas tem vídeo embebido**, mesmo as que YouTube aparece em AIO. Reforça hipótese L1 de `2026-05-20__aio-expansion.md`: vídeo é fonte AIO **paralela**, não embebida em pillar.
- **L2. Forprev tem schema com `dateModified` 2026-01-09** — datado recente. SEPRI também usa `datePublished` + `dateModified`. Previmed não tem nenhum. Frescura editorial pode ser sinal AIO.

## Current SEO State (Previmed comparativo)

### Strengths

- Página `/saude-no-trabalho/` consegue citação AIO Q5 apesar das fraquezas técnicas — sinal de autoridade de marca residual e/ou backlink profile aproveitável.
- Domínio claro do tema (HSST B2B nacional).
- Estrutura de subdomínios/serviços do grupo (careview, academia) — base para schema Organization rica.

### Weaknesses

- Title duplicado.
- Variação ortográfica não-canónica ("Medicina No Trabalho" em vez de "medicina do trabalho").
- Sem links externos institucionais.
- Schema genérico (sem Service / Article / FAQPage / HowTo).
- Hierarquia H1→H3 quebrada (sem H2).
- Word count baixo (732) mas sem compensação em schema, listas ou FAQs estruturadas.
- Sem `datePublished` / `dateModified` visível no schema.

### Opportunities

- Quick fix título + canónico (baixo esforço, alto impacto).
- Refazer `/saude-no-trabalho/` com padrão **Centralmed** (citações institucionais) + **SEPRI** (árvore pillar+spin-offs) + **Forprev** (Service schema + FAQ).
- Criar 4 pillars novos para queries Q1–Q4 onde Previmed está fora de AIO.
- Posicionamento "Solução Integrada MT + HST + Formação" já é critério AIO Q5 — Previmed pode reivindicar como vantagem comparativa explícita.

### Risks

- Concorrentes (Centralmed, SEPRI, Forprev) consolidam autoridade enquanto Previmed corrige problemas estruturais.
- Refactor do site pode acidentalmente quebrar o foothold AIO da `/saude-no-trabalho/` se URL/slug for alterada sem 301.
- "Medicina No Trabalho" pode ser brand voice deliberada — qualquer alteração tem de ser validada com stakeholder antes de mexer.

## Detailed Analysis

### Tabela comparativa

| Métrica | Forprev | SEPRI Q1 | SEPRI Lisboa | SEPRI Ficha | Centralmed MT | Centralmed HACCP | Centralmed Q5 | **Previmed** |
|---|---|---|---|---|---|---|---|---|
| Word count | 656 | 1393 | 1273 | 1186 | 1374 | 1017 | 1270 | **732** |
| Schemas | 5 (Org, WebSite, Breadcrumb, WebPage, **Service**) | 7 (Article, WebPage, Image, Breadcrumb, WebSite, Org, **Person**) | 7 idem | 7 idem | **0 detectado** | 0 detectado | 0 detectado | 5 (Org, WebSite, WebPage, Breadcrumb, SearchAction) — **sem Article/Service/FAQ** |
| Ext links instit. | 1 (DR-Lei) | 0 | n/d | n/d | **8** (ACT×2, pgdlisboa×2, WHO, CDC, DGS, DGERT) | **6** (FAO×2, EUR-Lex, ACT, DGS, DGERT) | **6** (pgdlisboa, ACT×3, APSEI, DGS, DGERT) | **0** |
| FAQ/accordion | 28 | 33 | n/d | n/d | n/d | n/d | n/d | **3** |
| Listas | 12 | 51 | n/d | n/d | n/d | n/d | n/d | **2** |
| Imagens | 9 | 20 | n/d | n/d | n/d | n/d | n/d | 15 |
| Internal links | 29 | 32 | n/d | n/d | n/d | n/d | n/d | **12** |

### Forprev — `forprev.pt/medicina-do-trabalho/`

**Estrutura editorial:** H1 + 6 H2 (incluindo "Como funciona o serviço", "A quem se destina", "Exames Médicos", "Exames Complementares de Diagnóstico", "Medicina do Trabalho"). H3 dedicados a Exames Admissão / Periódicos / Ocasionais + "Perguntas frequentes" + "Links úteis" + "Contactos" + "Horário".

**Schema:** @graph com Organization, WebSite, BreadcrumbList, WebPage (com `datePublished` 2025-01-07 + `dateModified` 2026-01-09), e **Service com offers**. **SEM FAQPage** apesar das 28 accordions.

**External:** apenas Diário República (Lei 102/2009 consolidada) + livroreclamacoes. Pouca densidade institucional.

**Por que é o top AIO Q5:** combinação de (a) Service schema explícito, (b) breadcrumb claro, (c) H3 "Perguntas frequentes" extensiva, (d) sub-headings que correspondem 1:1 ao framework AIO ("Como funciona / A quem se destina / Exames Médicos"). Não é o caso por densidade de conteúdo, é pelo **mapping estrutural** com a expectativa AIO.

### SEPRI — Pillar + spin-offs (3 URLs em Q1)

**Pillar `/noticia/medicina-do-trabalho-o-que-e-obrigacoes-como-funciona/`** (1393w)
- H2s do artigo principal (filtrados dos relacionados): "Ficha de Aptidão para o Trabalho" (link para spin-off) + outros artigos do blog em sidebar.
- Schema completo: Article, WebPage, ImageObject, BreadcrumbList, WebSite, Organization, **Person** (autor identificado).
- 51 listas, 33 accordions, 20 imagens.

**Spin-off geográfico `/noticia/medicina-do-trabalho-lisboa-obrigacoes-legislacao/`** (1273w)
- H2s: "O que é a Medicina do Trabalho", "Importância e impacto nas empresas", "Periodicidade dos exames", "Perguntas mais frequentes", "Legislação Medicina do Trabalho".
- Mesmo schema set.

**Spin-off tópico `/noticia/ficha-de-aptidao-para-o-trabalho-tudo-o-que-deve-saber/`** (1186w)
- H2s: "Ficha de Aptidão: o que é?", "para que serve?", "Que classificações podem constar?", "A empresa fica a saber o diagnóstico?".

**Padrão SEPRI:** 1 pillar abrangente + spin-offs especializados (geo: Lisboa/Porto; tópico: Ficha Aptidão, Exames). Cada um com schema Article completo, autor (Person), e cross-links entre eles. **3 URLs distintas a competir simultaneamente em AIO Q1.**

### Centralmed — Cross-cluster authority (3 URLs em Q1+Q3+Q5)

**Centralmed MT `/blog/como-funciona-a-medicina-do-trabalho-relevancia/`** (1374w)
- H2s: "O que é a Medicina do Trabalho", "O que estipula a legislação", "Fichas clínicas e de aptidão", "Acesso e comparência às consultas é obrigatório", "Importância para empresas e colaboradores".
- **8 links externos institucionais**: WHO (workplace framework), ACT (médicos do trabalho), pgdlisboa (Lei 102/2009, 2 URLs), CDC (workplace health), whistleblower, ACT, DGS, DGERT.
- **Sem schema JSON-LD detectável.**

**Centralmed HACCP `/blog/haccp-nas-empresas-principais-vantagens/`** (1017w)
- H2s: "HACCP e a importância vital do controlo da qualidade alimentar", "HACCP nas empresas: muito mais do que uma obrigação legal".
- **6 institucionais**: FAO/Codex Alimentarius (2 URLs incluindo CXC_001), EUR-Lex (Reg 852/2004), ACT, DGS, DGERT.

**Centralmed Q5 `/blog/prestadoras-de-seguranca-higiene-e-saude-no-trabalho/`** (1270w)
- H2s: "O que diz a legislação?", "A importância dos serviços", "Que critérios se deve ter em conta?".
- **6 institucionais**: pgdlisboa, ACT (3 URLs específicas — promoção SST, serviços internos, serviços externos), APSEI (guia organizacional), DGS, DGERT.

**Padrão Centralmed:** **densidade de citação outbound institucional é a regra**. Cada artigo cita 6–8 fontes (UE/internacional + autoridade nacional + lei). Word count consistente (~1000–1400w). Schema JSON-LD não é a alavanca — provavelmente o **link graph outbound** está a ser usado pela AIO como sinal de E-E-A-T.

### Previmed — Baseline `/saude-no-trabalho/`

**Title:** "Medicina No Trabalho - Previmed - PrevimedPrevimed" — **duplicado**.

**Meta description:** menciona "Lei nº 102/2009" mas **não há link para ela na página**.

**Headings:**
- H1: "Medicina No Trabalho"
- H3 (sem H2!): "Saude No Trabalho", "Saúde no Trabalho", "Medicina no Trabalho"
- H4: Atividade Clínica, Exames Médicos, Exames Complementares, Riscos Psicossociais, Consulta do Viajante

**Hierarquia editorial quebrada:** H1 → H3 (sem H2). Repetição confusa: "Saude No Trabalho" (sem til) + "Saúde no Trabalho" (com til) + "Medicina no Trabalho" como H3 distintos.

**Schema:** Organization, WebSite, WebPage, BreadcrumbList, SearchAction — todos genéricos de tema WordPress. **Sem Service, sem Article, sem FAQPage, sem HowTo.**

**External links: 4** — `previmed.careview.pt`, `myprevimed.careview.pt`, `previmed-academia.careview.pt` (todos próprios), cookieadmin. **Zero externos institucionais.**

**Body:** 0 ocorrências de "medicina do trabalho" (a página usa "Medicina No Trabalho" — sem "do" e com N maiúsculo, variante não-canónica).

**Listas: 2. FAQs/accordions: 3. Tabelas: 0. Vídeos: 0.**

**Internal links: 12** (menos de metade dos competidores).

### Padrões cross-concorrente

1. **Citação outbound institucional é o sinal AIO-friendly mais forte** (observado em Centralmed, replicado parcialmente em Forprev/SEPRI). Mínimo recomendado: 4 links externos por pillar (ACT + Lei 102/2009 + 2 outros).
2. **Word count médio**: 1100–1400w (Centralmed, SEPRI). Forprev compensa com schema. Previmed precisa subir de 732 para ≥1100w.
3. **Schema completo é vantagem**: Article (SEPRI) ou Service (Forprev) > genérico (Previmed atual).
4. **Person/autor identificado** (SEPRI) é diferenciador. Hipótese — adicionar autoria em briefs futuros.
5. **FAQ/accordion: 28–33** nos top — não é só "ter uma secção FAQ" no fim, é ter 8–15 perguntas estruturadas.
6. **Hierarquia H1 → H2 → H3 limpa**: Previmed quebra ao saltar para H3.
7. **Estratégia árvore (pillar + spin-offs cruzados)** apenas SEPRI usa de forma consistente.

## Recommended Action Plan

### Phase 1 — Foundation (quick fixes)

- [ ] **F1.** Corrigir title duplicado de `/saude-no-trabalho/` ("Previmed - PrevimedPrevimed" → "Medicina do Trabalho — Previmed"). **Sem alterar URL/slug.** Página já tem foothold AIO Q5.
- [ ] **F2.** Decidir: manter "Medicina No Trabalho" como brand voice OU canonicalizar para "Medicina do Trabalho" (forma idiomática). Decisão de stakeholder antes de mexer. Registar no `_living/DECISION_LOG.md`.
- [ ] **F3.** Atualizar hierarquia editorial `/saude-no-trabalho/`: introduzir H2 antes dos blocos H3 atuais.

### Phase 2 — Content & Structure (briefs P1)

Aplicar a todos os 5 briefs originados em `2026-05-20__aio-expansion.md`:

- [ ] **C0.** **Regra obrigatória dos briefs:** mínimo 4 links externos institucionais por pillar (ACT + pgdlisboa Lei 102/2009 + 2 outros conforme tema: DGS, DGERT, ASAE, DGAV, FAO/Codex, EUR-Lex, APSEI, OA).
- [ ] **C1.** Word count alvo por pillar: 1100–1500w (modelo Centralmed/SEPRI).
- [ ] **C2.** FAQ estruturada com 8–15 perguntas, com schema `FAQPage`.
- [ ] **C3.** Schema obrigatório: `Article` + `FAQPage` (+ `HowTo` em "como escolher" e HACCP 7 princípios + `Service` na página de serviço comercial).
- [ ] **C4.** Hierarquia H1 → H2 → H3 limpa; usar 6–8 H2 por pillar.
- [ ] **C5.** Adicionar `author` (Person) com identificação real ao schema Article. Decidir quem assina (ver Decisions Needed #1).

### Phase 3 — Technical SEO

- [ ] **T1.** Auditoria rápida de OUTRAS páginas Previmed core (`/seguranca-trabalho/`, `/higiene-seguranca-alimentar/`, `/formacao/` ou equivalentes) para verificar se padrões de problema (`title duplicado`, `H2 ausentes`, `schema genérico`, `0 ext links`) se repetem. Se sim → fix em batch.
- [ ] **T2.** Adicionar `datePublished` + `dateModified` ao schema de todas as páginas pillar (frescura editorial).

### Phase 4 — Authority & Internal Linking

- [ ] **A1.** Estratégia "árvore" SEPRI: cada pillar P1 deve ter 2–3 spin-offs planeados desde início (geo / tópico). Ex.: pillar MT → spin-off Porto + spin-off Ficha Aptidão.
- [ ] **A2.** Cada pillar deve linkar internamente para ≥4 outras páginas Previmed.
- [ ] **A3.** Linkar todos os pillars para a página de serviço comercial correspondente (CTA contextual).

### Phase 5 — Measurement & Iteration

- [ ] **M1.** Após pillars publicados (t+30d, t+90d, t+180d): recaptura AIO + verificar se Previmed entra nas fontes citadas (relatórios datados em `reports/`).
- [ ] **M2.** Trackear GSC (quando ligado) impressões/ranking para queries Q1–Q5.

## Backlog Items To Add

A copiar para `../_living/BACKLOG.md`:

- `[Quick win] P1` Corrigir title duplicado `/saude-no-trabalho/` ("Previmed - PrevimedPrevimed"). Origem: `reports/2026-05-20__competitor-deep-dive.md` §F1.
- `[Quick win] P2` Adicionar H2 à página `/saude-no-trabalho/` (atualmente salta H1→H3). Origem: §F3.
- `[Technical blocker] P2` Auditoria rápida das páginas core Previmed (`/seguranca-trabalho/`, HACCP, formação) para repetição dos problemas estruturais. Origem: §T1.
- `[Schema/entity improvements] P1` Regra "4+ links externos institucionais por pillar" (ACT + Lei 102/2009 + 2 outros). Origem: §C0.
- `[Schema/entity improvements] P1` Schema obrigatório por tipo: Article + FAQPage + HowTo + Service. Origem: §C3.
- `[Content opportunity] P2` Spin-offs planeados desde início de cada pillar (geo + tópico). Origem: §A1.

## Decisions Needed

1. **Brand voice: "Medicina No Trabalho" ou "Medicina do Trabalho"?** Página atual usa a primeira (sem preposição "do", com N maiúsculo). Query AIO real é a segunda. Impacto SEO: alto. Impacto branding: por confirmar. Recomendação: canonicalizar para "Medicina do Trabalho" no body, manter "Medicina No Trabalho" apenas se for brand registado.

2. **Quem assina os pillars como autor (schema Person)?** Opções: pessoa real (médico do trabalho do quadro), pessoa fictícia editorial ("Equipa Previmed" — fraco), nenhum. SEPRI usa Person — sinal de autoridade editorial. Recomendação: nome de médico + cargo + foto + LinkedIn.

3. **Atacar primeiro os quick fixes da `/saude-no-trabalho/` ou produzir briefs novos?** Recomendação: paralelo — fix títulos/H2 (1 dia) + arrancar brief Q5 (foothold) já com novo padrão.

## Open Questions

- Centralmed não tem JSON-LD detectável mas domina AIO. Será que está injetado via JS pós-load (não detectado pelo evaluate inicial) ou realmente não usa? Confirmar com View-Source manual.
- Person/autor é mesmo um sinal AIO ou apenas correlação? Hipótese a validar em t+90d.
- Spin-offs SEPRI funcionam porque há link interno cross-pillar ou porque cada um é otimizado independentemente? Investigar topologia interna.

## Next Steps

1. Atualizar `_living/CURRENT_STATUS.md`, `_living/BACKLOG.md`, `_living/OPPORTUNITIES.md` com findings deste relatório.
2. Registar decisão "brand voice MT" no `_living/DECISION_LOG.md` quando o utilizador resolver.
3. Decidir com utilizador qual quick fix arrancar primeiro.
4. Aplicar as regras de Phase 2 (C0–C5) como **template fixo** dos briefs futuros — promover a documento próprio se necessário.

## Last Updated

2026-05-20 por Claude (SEO Lead).
