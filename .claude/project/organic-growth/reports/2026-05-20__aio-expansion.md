# AIO Expansion — 5 P1 queries — 2026-05-20

## Purpose

Capturar e analisar a resposta do **Google Modo IA (AI Overview)** em 5 queries P1 do cluster HSST/Formação para perceber:
- que conteúdo a IA gera para cada query;
- que fontes a IA cita;
- onde Previmed está / não está;
- que lacunas e oportunidades emergem para a estratégia de conteúdo.

Snapshot fechado no tempo. Quando o Google atualizar a AIO destas queries, criar **novo relatório datado** (`YYYY-MM-DD__aio-expansion.md`) em vez de editar este.

## Scope

- **5 queries** capturadas em `udm=50` (Modo IA), `hl=pt-PT`, `gl=PT`, navegador sem login, sem cookies aceites (rejected all).
- Sessão de captura: 2026-05-20.
- Snapshots brutos em [`../clusters/q<N>-*/aio-capture.yml`](../clusters/) (1 por cluster).
- **Não coberto:** análise de SERP tradicional (10 blue links) — já feita parcialmente em Lote 1.4 (`strategy/COMPETITORS.md`). Não coberto também: variações de query, queries long-tail, queries comerciais puras (`preço`, `proposta`, `orçamento`).

## Data Sources Used

| Fonte | Estado |
|---|---|
| Playwright MCP (`mcp__playwright`) — Modo IA Google.pt | completed |
| `strategy/KEYWORDS.md` (clusters P1 origem) | reviewed |
| `setup/BASELINE_AUDIT.md` (estado site) | reviewed |
| `strategy/COMPETITORS.md` (Lote 1.4) | reviewed |
| Google Search Console / GA4 | not connected |
| DataForSEO / SEMrush / Ahrefs (volumes, dificuldade) | not connected |
| PageSpeed / Lighthouse | not run nesta sessão |

## Confidence Level

- **Medium.**
- **Limitações:**
  - AIO é não-determinística: a mesma query a uma hora diferente pode devolver fontes e texto diferentes. Capturas únicas, sem repetição cross-time.
  - Sem dados quantitativos: volumes, CTR, CPC, dificuldade SEO — ainda bloqueados pela decisão de keyword data tool (`setup/KEYWORD_DATA_DECISION.md`).
  - Sem GSC: não sabemos se Previmed já tem ranking marginal para estas queries que poderíamos amplificar.
  - Q1–Q4 são head terms — AIO está estável o suficiente para serem indicativas; Q5 é mais nicho e pode flutuar mais.
  - AIO PT mistura fontes BR — análise tem de filtrar.

## Executive Summary

5 queries P1 capturadas em Modo IA do Google.pt. Resultado a 3 níveis:

**1. AIO está presente e expandida em todas as 5 queries.** Não é apenas "link Modo IA" como observado em Lote 1.4 — a resposta completa carrega, com 11–18 fontes citadas por query. O Modo IA é hoje a primeira camada de resposta visível para um decisor B2B que faz a pesquisa em PT.

**2. Previmed só aparece em 1/5 queries** (Q5, "como escolher empresa medicina do trabalho"). Nas outras 4 queries — todas head terms dos 3 serviços core — Previmed está **fora** das fontes citadas. Concorrentes diretos PT que dominam: **Centralmed, SEPRI, Forprev, Medilav, Ecosáude, Preveris**. Conteúdo institucional (ACT, ASAE, DGS, Ordem dos Advogados) tem peso massivo.

**3. Achado crítico em Q4 (formação 35h):** AIO afirma que **"a lei mudou: 35 → 40 horas"** (Lei 93/2019). Maioria do conteúdo PT existente (e provavelmente do Previmed quando voltar a ter formação online) ainda fala em 35h. Conteúdo atualizado para 40h é defensável legalmente e diferenciador editorialmente. Implica revisão imediata de `strategy/KEYWORDS.md` (cluster "Formação 35h") e do plano de conteúdo informacional.

**Decisão pendente que bloqueia depth:** sem keyword data tool ligado (`setup/KEYWORD_DATA_DECISION.md`) não temos volumes nem dificuldade reais. As 5 queries são P1 por intuição estratégica (head terms dos clusters core) — confirmação quantitativa fica para depois da decisão A–F.

**Direção recomendada:** preparar 5 briefs de conteúdo (1 por query) com estrutura "AIO-friendly" — secções claras, schema FAQPage/HowTo/Article, citações de fontes institucionais (Lei 102/2009, ACT, ASAE) — visando entrada nas fontes AIO num horizonte de 4–8 meses pós-publicação.

## Priority Findings

### Critical

- **C1. Lei mudou: 35h → 40h de formação anual obrigatória.** Lei 93/2019 alterou Art.º 131.º do Código do Trabalho. AIO já reflete esta correção. `strategy/KEYWORDS.md` cluster "Formação 35h" tem de ser revisto (volumes "35h" vs "40h" — qual maior hoje?). Conteúdo Previmed sobre formação tem de ser explicitamente "40 horas" + nota explicativa sobre transição 35→40. Risco: produzir conteúdo desatualizado que perde credibilidade junto a RH/jurídico.

- **C2. Previmed fora de AIO em 4/5 head terms P1.** Para queries de altíssimo valor estratégico (medicina do trabalho, segurança no trabalho, HACCP, formação obrigatória), Previmed não está nas fontes que a IA usa para responder a um decisor B2B. Concorrentes diretos PT (Centralmed, SEPRI, Forprev, Medilav, Ecosáude) ocupam o espaço.

### High

- **H1. Página `/saude-no-trabalho/` já é citada por AIO em Q5.** É a única citação Previmed observada. Confirmar e otimizar — não mexer em URL/slug sem plano de redirect.

- **H2. SEPRI é citado 3 vezes em Q1.** SEPRI domina autoridade temática para "medicina do trabalho" via 3 artigos: definição/obrigações, página Lisboa, Ficha Aptidão. Padrão a estudar para replicação (sem copiar).

- **H3. AIO PT mistura fontes BR.** Q1 (onsafety.com.br, LinkedIn BR), Q3 (kaizen.com BR), Q5 (clinimedjoinville, metamed, soc, ABQV). Significa que fontes BR estão a competir por mindshare em queries PT. Conteúdo PT bem otimizado pode deslocá-las com relativa facilidade.

- **H4. Conteúdo institucional/regulatório domina.** Lei 102/2009 (pgdlisboa, Diário República), Portal ACT, ASAE, DGS, DGAV, OCC, Ordem dos Advogados. Conteúdo Previmed que **cite explicitamente** estas fontes (com hyperlink e schema citation) tem maior probabilidade de ser citado pela AIO.

### Medium

- **M1. Q5 ("como escolher") tem estrutura AIO em 5 passos.** Padrão claro: Legitimidade DGS/ACT → Infraestrutura → Abrangência (MT+HST) → Tecnologia (portal/Relatório Único) → Reputação/faturação. Brief Previmed deve seguir esta estrutura (ou superá-la com 6º critério defensável).

- **M2. Q3 (HACCP) cita ASAE 3 vezes.** ASAE é a fonte oficial de facto. Conteúdo Previmed sobre HACCP tem de citar ASAE (linkar páginas específicas) e seguir o "Codex Alimentarius + 7 princípios" como spinal cord.

- **M3. AIO em todas as queries termina com perguntas follow-up estruturadas.** Q1: "coimas / exames específicos / inaptidão"; Q2: "setor industrial / plano prevenção / exames"; Q4: "trabalhador ou empresa / crédito horas / efetivo ou termo"; Q5: "localidade / setor / nº trabalhadores". Estas follow-ups revelam **intenções secundárias** que valem briefs próprios.

### Low

- **L1. Vídeo é fonte AIO recorrente** — YouTube aparece em Q1, Q3, Q4, Q5. Hipótese: vídeo curto (1–5 min) explicativo embebido numa página textual pode reforçar citações. Por validar — exige investimento em produção.

- **L2. Forprev (Q5) é o "top citado" entre concorrentes PT.** Vale auditoria competitiva específica à página `forprev.pt/medicina-do-trabalho/`.

## Current SEO State

### Strengths

- Página `/saude-no-trabalho/` já tem reconhecimento AIO (Q5).
- Marca Previmed reconhecível ("Medicina No Trabalho - Previmed" surge naturalmente como title).
- Posicionamento integrado MT + HST é validado pela AIO Q5 ("Solução Integrada" como critério #3).

### Weaknesses

- Sem páginas citadas para 4 dos 5 head terms P1.
- Conteúdo atual provavelmente não cita Lei 102/2009, ACT, ASAE com a frequência/estrutura que a AIO premeia.
- Hub editorial inexistente (já flagged em `setup/BASELINE_AUDIT.md`).
- Risco de conteúdo desatualizado em formação (35h obsoleto).

### Opportunities

- Pillar "Como escolher empresa de medicina do trabalho" — Q5 tem AIO mas só 3 fontes PT robustas (Forprev, Centralmed, Medilav). Gap claro.
- Pillar "Formação obrigatória 40h" — Q4 com correção legal explícita. Conteúdo "40h" defensável vs "35h" comum.
- Hub HACCP com referência ASAE.
- Hub "Lei 102/2009 explicada" (head institucional).
- Hub "Diferença Segurança / Higiene / Saúde no Trabalho" (Q2 estrutura).

### Risks

- Concorrentes (Centralmed, SEPRI, Forprev) consolidam citações AIO se Previmed atrasar conteúdo.
- AIO está instável — janela de oportunidade pode fechar quando Google amadurecer modelo de citações.
- Conteúdo 35h desatualizado se publicado sem revisão para 40h.

## Detailed Analysis

### Query 1 — "medicina do trabalho"

**AIO resposta (resumo):**
> "A Medicina do Trabalho (ou saúde ocupacional) é uma especialidade médica obrigatória por lei em Portugal que visa a prevenção de riscos profissionais... Regulada pela Lei n.º 102/2009..."
>
> Estrutura: Definição → Lei 102/2009 → Principais Tipos de Exames (Admissão/Periódico/Ocasional) → Ficha de Aptidão (Apto/Apto Condicionado/Inapto Temporário/Inapto Definitivo) → Obrigações (Empresas: organização obrigatória + coimas ACT; Trabalhadores: direito + obrigação de comparência).
>
> Follow-ups sugeridos pelo AIO: coimas aplicadas, exames de profissão de risco, inaptidão médica.

**18 fontes citadas (top 18 do painel):**

| # | Fonte | URL | Tipo |
|---|---|---|---|
| 1 | SPMT | `spmtrabalho.org` | Sociedade científica |
| 2 | SEPRI | `sepri.pt/noticia/medicina-do-trabalho-o-que-e-obrigacoes-como-funciona/` | **Concorrente HSST** |
| 3 | FactorialHR | `factorialhr.pt/blog/medicina-do-trabalho/` | HR SaaS / blog |
| 4 | Santander | `santander.pt/salto/...` | Banco / hub editorial |
| 5 | pgdlisboa | `pgdlisboa.pt/leis/...` (Lei 102/2009) | Institucional jurídico |
| 6 | stop-sindicato | `stop-sindicato.pt/...` | Sindicato educação |
| 7 | Ecosáude | `ecosaude.pt/medicina-do-trabalho/` | **Concorrente HSST** |
| 8 | pgdlisboa | `pgdlisboa.pt/...artigo aptidão` | Institucional jurídico |
| 9 | YouTube / HealthworkTV | `youtube.com/shorts/...` | Vídeo (BR) |
| 10 | SEPRI Lisboa | `sepri.pt/noticia/medicina-do-trabalho-lisboa-...` | **Concorrente HSST** |
| 11 | Centralmed | `centralmed.pt/blog/...` | **Concorrente HSST** |
| 12 | InvoiceXpress | `invoicexpress.com/blog/...` | SaaS faturação |
| 13 | SEPRI Ficha Aptidão | `sepri.pt/noticia/ficha-de-aptidao-...` | **Concorrente HSST** |
| 14 | Slideshare / ACT Guia | `slideshare.net/.../act-guia-micro-pequenas-medias-empresas` | Doc ACT |
| 15 | onsafety.com.br | `onsafety.com.br/...` | BR |
| 16 | Doutor Finanças | `doutorfinancas.pt/...` | Hub editorial financeiro |
| 17 | Ordem dos Advogados | `portal.oa.pt/...` | Institucional |
| 18 | LinkedIn | `pt.linkedin.com/pulse/...` | Post BR |

**Previmed:** ❌ não citado.

**Padrão a explorar:** SEPRI tem 3 entradas distintas (top-level "o que é", "Lisboa", "Ficha Aptidão"). Aponta para estratégia de **conteúdo em árvore** — pillar + subtópicos com URLs próprias.

---

### Query 2 — "segurança no trabalho"

**AIO resposta (resumo):**
> "A Segurança no Trabalho consiste num conjunto de metodologias... para prevenir acidentes laborais e proteger a integridade física e mental dos trabalhadores. Regulamentado pela Lei 102/2009..."
>
> Estrutura: Definição → Diferenças SST (Segurança / Higiene / Saúde) → Obrigações Empresas (Avaliar riscos, EPIs, Formação, Sinalização) → Tipos de Organização (Internos / Externos / Comuns / Trabalhador Designado) → Deveres dos Trabalhadores.
>
> Tabela: 4 modalidades de serviço com descrição curta.

**11 fontes citadas:**

| # | Fonte | URL | Tipo |
|---|---|---|---|
| 1 | Portal ACT | `portal.act.gov.pt/Pages/Seguranca_Saude_no_Trabalho.aspx` | **Institucional** |
| 2 | Santander | `santander.pt/salto/higiene-e-seguranca-no-trabalho` | Hub editorial |
| 3 | DGEEC | `dgeec.medu.pt/api/ficheiros/...` (PDF) | Institucional |
| 4 | Doutor Finanças | `doutorfinancas.pt/...` | Hub editorial |
| 5 | Traininghouse | `traininghouse.pt/modalidades-de-servico-de-seguranca-no-trabalho/` | **Concorrente HSST** |
| 6 | Fidelidade | `fidelidade.pt/PT/empresas/...` | Seguradora |
| 7 | Blog Tecniquitel | `blogtecniquitel.com/...` | Hub editorial |
| 8 | ABQV (BR) | `abqv.org.br/...` | BR |
| 9 | YouTube / Pense Prevenção (BR) | `youtube.com/shorts/...` | Vídeo BR |
| 10 | WageIndicator | `wageindicator.org/pt-pt/...` | Hub jurídico |
| 11 | LP Segurança (BR) | `lpsegurancaesaudetrabalho.com.br/` | BR |

**Previmed:** ❌ não citado.

**Padrão a explorar:** Tabela de 4 modalidades de serviço é repetida em vários artigos PT — formato AIO-friendly. Conteúdo Previmed deve ter esta tabela com schema apropriado.

---

### Query 3 — "HACCP"

**AIO resposta (resumo):**
> "O HACCP (Análise de Perigos e Controlo de Pontos Críticos) é um sistema de gestão preventiva internacionalmente reconhecido para garantir a segurança alimentar..."
>
> Estrutura: Definição → 7 Princípios (Análise perigos / PCC / Limites críticos / Monitorização / Ações corretivas / Verificação / Registo) → Pré-requisitos (Higiene pessoal / Higienização / Pragas / Formação / Água+resíduos) → Legislação (Reg CE 852/2004, ASAE).
>
> Follow-ups: registos diários, limites críticos de temperatura.

**15 fontes citadas:**

| # | Fonte | URL | Tipo |
|---|---|---|---|
| 1 | ASAE | `asae.gov.pt/seguranca-alimentar/haccp.aspx` | **Institucional** |
| 2 | ASAE FAQ | `asae.gov.pt/perguntas-frequentes1/.../haccp-o-que-e-.aspx` | **Institucional** |
| 3 | DGAV | `dgav.pt/alimentos/conteudo/...` | **Institucional** |
| 4 | SGS Portugal | `sgs.com/pt-pt/servicos/haccp` | Certificadora |
| 5 | Preveris | `preveris.pt/haccp-sistema-seguranca-alimentar/` | **Concorrente HSST** |
| 6 | ASAE Esclarecimento | `asae.gov.pt/perguntas-frequentes1/.../haccp-esclarecimento--simplificacao.aspx` | **Institucional** |
| 7 | Kaizen | `kaizen.com/pt/insights-pt/haccp-sistema-seguranca-alimentar/` | Consultoria |
| 8 | Centralmed | `centralmed.pt/blog/haccp-nas-empresas-...` | **Concorrente HSST** |
| 9 | YouTube / Hospitality Broadcast | `youtube.com/watch?v=c8BozVEWteo` | Vídeo (EN) |
| 10 | YouTube / ZONAVERDE | `youtube.com/watch?v=LFnNB9TJHr8` | Vídeo PT (concorrente formação) |
| 11 | Superprof | `superprof.pt/blog/...` | Plataforma formação |
| 12 | LTM Consultoria | `ltm.pt/haccp/` | **Concorrente formação** |
| 13 | Duoligiene | `duoligiene.pt/haccp-o-que-e-e-para-que-serve/` | **Concorrente HSST** |
| 14 | AHRESP | `ahresp.com/2026/02/haccp-digital-ahresp/` | Associação setorial |
| 15 | RCR Contabilidade | `rcrcontabilidade.pt/...` | Hub contabilidade |

**Previmed:** ❌ não citado.

**Padrão a explorar:** ASAE domina (3 entradas). Conteúdo Previmed sobre HACCP tem de **citar ASAE com hyperlinks específicos** (não apenas mencionar) — `asae.gov.pt/seguranca-alimentar/haccp.aspx` e `asae.gov.pt/perguntas-frequentes1/...`.

---

### Query 4 — "formação 35 horas obrigatória" ⚠️ CRITICAL

**AIO resposta (resumo):**
> ⚠️ **"A lei mudou e o número mínimo de formação contínua obrigatória passou de 35 para 40 horas anuais por trabalhador."**
>
> Lei 93/2019 alterou Art.º 131.º do Código do Trabalho. Referencial atualizado: **40h/ano**.
>
> Estrutura:
> - Principais Regras: Direito/dever (10% colaboradores anualmente) → Proporcionalidade (contratos ≥3 meses) → Acumulação (3 anos) → Escolha de temas (atividade / TIC / SST / línguas).
> - Consequências de incumprimento: Crédito de horas (trabalhador pode usar com aviso prévio) → Cessação contrato (empresa paga horas devidas) → Coimas ACT (contraordenação grave).
>
> Follow-ups: trabalhador vs empresa; crédito horas; efetivo vs termo.

**11 fontes citadas:**

| # | Fonte | URL | Tipo |
|---|---|---|---|
| 1 | CGTP-IN | `cgtp.pt/sitio-dos-direitos/guias-de-direitos/8911-formacao-profissional-o-que-diz-a-lei` | Sindical |
| 2 | Doutor Finanças | `doutorfinancas.pt/...` | Hub editorial |
| 3 | Portal ACT Nota Técnica 9 | `portal.act.gov.pt/AnexosPDF/...PDF` | **Institucional** |
| 4 | Alento | `alento.pt/noticias/35h-de-Formacao-Obrigatoria:...` | Consultoria RH |
| 5 | Diário República | `diariodarepublica.pt/dr/lexionario/termo/dever-formacao-continua-direito-trabalho` | **Institucional** |
| 6 | OCC | `occ.pt/sites/default/files/...PDF` | Ordem Contabilistas |
| 7 | AEDL | `aedl.pt/formacao-obrigatoria-na-empresa-...-40horas-anuais-obrigatorias/` | Concorrente formação |
| 8 | YouTube / CERTFORM | `youtube.com/watch?v=...` | Vídeo (concorrente formação) |
| 9 | Facebook ACT | `facebook.com/act.gov.pt/...` | **Institucional** social |

**Previmed:** ❌ não citado.

**Achado crítico:** Mesmo a query usar "35 horas", a AIO **corrige** para 40h. Qualquer brief Previmed para este cluster tem de:
1. Manter "35 horas" no slug/título visível por volume de pesquisa,
2. Explicar a alteração 35→40 logo no H2 inicial,
3. Citar Lei 93/2019 e Nota Técnica 9 da ACT.

Revisão imediata necessária: `strategy/KEYWORDS.md` linhas 213–216 (cluster Formação 35h).

---

### Query 5 — "como escolher empresa medicina do trabalho" ✅ Previmed citado

**AIO resposta (resumo):**
> "Para escolher a melhor empresa de Medicina do Trabalho... deve priorizar a autorização legal da DGS/ACT, a proximidade geográfica das clínicas e a capacidade de integração com a plataforma do eSocial ou Relatório Único."
>
> Estrutura em 5 passos:
> 1. **Legitimidade e Certificações** — autorização DGS/ACT, médicos especialistas, técnicos certificados.
> 2. **Infraestrutura e Logística** — rede de clínicas, unidades móveis.
> 3. **Abrangência dos Serviços (SST)** — solução integrada MT + HST, gestão completa de exames.
> 4. **Tecnologia e Apoio Digital** — portal online, Relatório Único Anexo D / eSocial.
> 5. **Reputação e Modelo de Faturação** — referências do setor, avença mensal vs ato isolado.
>
> Follow-ups: localidade / setor / nº trabalhadores.

**11 fontes citadas:**

| # | Fonte | URL | Tipo |
|---|---|---|---|
| 1 | **Forprev** | `forprev.pt/medicina-do-trabalho/` | **Concorrente HSST (top citado)** |
| 2 | Centralmed | `centralmed.pt/blog/prestadoras-de-seguranca-...` | **Concorrente HSST** |
| 3 | Clinimed Joinville (BR) | `clinimedjoinville.com.br/...` | BR |
| 4 | Metamed (BR) | `metamed.com.br/blog/...` | BR |
| 5 | **PREVIMED** ✅ | `previmed.pt/saude-no-trabalho/` | **Próprio** |
| 6 | RCR Contabilidade | `rcrcontabilidade.pt/...` | Hub contabilidade |
| 7 | Medilav | `medilav.pt/servicos/saude-ocupacional/medicina-do-trabalho/` | **Concorrente HSST** |
| 8 | YouTube / Sistema ESO | `youtube.com/watch?v=Bc7JmysccGo` | Vídeo BR |
| 9 | Facebook | `facebook.com/.../posts/escolher-a-empresa-certa-...` | Social BR |
| 10 | Doutor Finanças | `doutorfinancas.pt/seguros/...` | Hub editorial |
| 11 | SOC (BR) | `soc.com.br/blog-de-sst/...` | BR |

**Previmed:** ✅ **citado** (posição #5 do painel).

**Padrão a explorar:** AIO usa Forprev como spine da resposta (citação no headline). Vale auditoria competitiva específica a `forprev.pt/medicina-do-trabalho/` para perceber **porquê** essa página é a top.

## Recommended Action Plan

### Phase 1 — Foundation

- [ ] **F1.** Atualizar `strategy/KEYWORDS.md` para refletir "35h → 40h" no cluster Formação. Avaliar adicionar variantes ("40 horas obrigatórias", "Lei 93/2019 formação", "40h formação contínua").
- [ ] **F2.** Decidir keyword data tool (`setup/KEYWORD_DATA_DECISION.md`) — desbloqueia confirmação quantitativa das 5 queries deste relatório.
- [ ] **F3.** Marcar URL `/saude-no-trabalho/` como "protegida" — não mexer sem plano de redirect (já citada por AIO).

### Phase 2 — Content & Structure

- [ ] **C1.** Brief P1 — Pillar "Medicina do Trabalho" (Q1). Estrutura: definição + Lei 102/2009 + tipos de exames + Ficha de Aptidão + obrigações. Schema: Article + FAQPage. Citações explícitas: pgdlisboa (Lei 102/2009 com link específico), ACT (coimas), SPMT (autoridade).
- [ ] **C2.** Brief P1 — Pillar "Segurança no Trabalho" (Q2). Estrutura: definição + diferenças S/H/S + obrigações empresa + 4 modalidades + deveres trabalhador. Tabela 4 modalidades obrigatória. Schema: Article + FAQPage.
- [ ] **C3.** Brief P1 — Pillar "HACCP" (Q3). Estrutura: definição Codex Alimentarius + 7 princípios (cada um com H4) + pré-requisitos + Reg CE 852/2004. Schema: HowTo (para os 7 princípios) + Article. Citações: ASAE (3 hyperlinks distintos), DGAV.
- [ ] **C4.** Brief P1 — Pillar "Formação obrigatória 40h" (Q4). **Iniciar com correção 35→40 explícita.** Estrutura: O que mudou (Lei 93/2019) + Quem tem direito + Cálculo proporcional + Acumulação 3 anos + Consequências incumprimento. Citações: Nota Técnica 9 ACT, Diário República.
- [ ] **C5.** Brief P1 — Guia "Como escolher empresa de medicina do trabalho" (Q5). Estrutura: replicar e superar os 5 passos AIO (DGS/ACT, Logística, Abrangência, Tecnologia, Reputação) + **6º passo** defensável (sugestão: "Indicadores de qualidade — taxa de absentismo, retenção de profissionais, tempo médio de resposta"). URL alvo: `/recursos/guias/escolher-medicina-do-trabalho/`.

### Phase 3 — Technical SEO

- [ ] **T1.** Auditoria competitiva da página `forprev.pt/medicina-do-trabalho/` — porquê é top citada Q5. Capturar: schema, estrutura H1–H4, links externos, comprimento, frequência de palavras-chave.
- [ ] **T2.** Auditoria competitiva de 1 página SEPRI (Q1 — domina com 3 citações) e 1 página Centralmed (citado Q1+Q3+Q5).
- [ ] **T3.** Garantir schema Article + FAQPage + (HowTo onde aplicável) em todas as páginas pillar. Output incluir `sameAs` e `citation` apontando para Lei 102/2009, ACT, ASAE.

### Phase 4 — Authority & Internal Linking

- [ ] **A1.** Cada pillar (C1–C5) deve ter ≥5 links internos para subtópicos e ≥5 links externos para fontes institucionais (Lei, ACT, ASAE, DGS, OA).
- [ ] **A2.** Hub `/recursos/` (ainda inexistente) — ver `setup/BASELINE_AUDIT.md` — torna-se necessário para suportar os 5 pillars.

### Phase 5 — Measurement & Iteration

- [ ] **M1.** Após GSC ligado (`setup/GSC_GA4_SETUP.md`): trackear se Previmed entra em ranking para cada uma das 5 queries.
- [ ] **M2.** Repetir captura AIO em **t+90 dias** e **t+180 dias** após publicação dos pillars (novo relatório `YYYY-MM-DD__aio-expansion.md`). Comparar: entrámos nas fontes? Em que posição?
- [ ] **M3.** Capturar pelo menos 1 vez por trimestre a AIO para Q4 (formação 35→40) — risco alto de a query ainda usar "35h" enquanto a lei diz 40h; manter conteúdo Previmed ajustado.

## Backlog Items To Add

A copiar para `../_living/BACKLOG.md` na secção certa:

- `[Content opportunity] P1` Brief Pillar "Medicina do Trabalho" — `/servicos/medicina-trabalho/`. Origem: `reports/2026-05-20__aio-expansion.md` §Q1.
- `[Content opportunity] P1` Brief Pillar "Segurança no Trabalho" — `/servicos/seguranca-trabalho/`. Origem: §Q2.
- `[Content opportunity] P1` Brief Pillar "HACCP" — `/servicos/higiene-seguranca-alimentar/`. Origem: §Q3.
- `[Content opportunity] P1` Brief Pillar "Formação 40h obrigatória" — pillar formação. Origem: §Q4. **Crítico — correção legal 35→40.**
- `[Content opportunity] P1` Guia "Como escolher empresa de medicina do trabalho" — `/recursos/guias/escolher-medicina-do-trabalho/`. Origem: §Q5.
- `[Schema/entity] P2` Adicionar schema FAQPage + Article (e HowTo onde aplicável) em todas as páginas pillar P1.
- `[Competitor gap] P2` Auditoria competitiva: forprev.pt, sepri.pt, centralmed.pt (3 páginas top citadas). Origem: §T1+T2.
- `[Technical blocker] P2` Atualizar `strategy/KEYWORDS.md` cluster Formação 35h para refletir 35→40h. Origem: §C1.
- `[Measurement] P3` Recaptura AIO t+90d e t+180d pós-publicação pillars. Origem: §M2.

## Decisions Needed

1. **Decisão keyword data tool (A–F).** Bloqueia confirmação quantitativa das 5 queries. Documentado em `../setup/KEYWORD_DATA_DECISION.md`. **Sem isto, não há volumes/dificuldade — todos os 5 pillars assumem prioridade P1 por intuição estratégica.**

2. **Brief order: pelos 5 ao mesmo tempo ou um a um?**
   - Opção A: 5 briefs em paralelo (output massivo, risco de mistura de tom/qualidade).
   - Opção B: começar por Q4 (correção 35→40 é a oportunidade mais "limpa" + diferenciador legal) ou Q5 (já temos foothold AIO).
   - Recomendação: **Q5 primeiro** (foothold) → Q4 (diferenciador legal) → Q1/Q2/Q3 em paralelo (head terms core).

3. **Investimento em vídeo?** YouTube aparece em Q1, Q3, Q4, Q5. Hipótese L1 está por validar.

## Open Questions

- A AIO PT está a misturar fontes BR — é tendência sustentada ou Google vai filtrar geograficamente nos próximos meses?
- Forprev.pt tem alguma característica técnica/editorial específica que o AIO premeia? (Auditoria T1.)
- Vale a pena fazer brief separado "Lei 102/2009 explicada" como pillar de autoridade institucional?
- Existe diferença entre AIO em mobile vs desktop? (Captura desta sessão foi desktop only.)

## Next Steps

1. **Utilizador**: decidir keyword data tool em `../setup/KEYWORD_DATA_DECISION.md`.
2. **Utilizador**: executar checklist `../setup/GSC_GA4_SETUP.md` (ligar GSC/GA4/PSI).
3. **SEO Lead (Claude)**: atualizar ficheiros vivos com sumário deste relatório (`_living/CURRENT_STATUS.md`, `_living/BACKLOG.md`, `_living/OPPORTUNITIES.md`, `_living/DECISION_LOG.md`).
4. **SEO Lead (Claude)**: atualizar `strategy/KEYWORDS.md` cluster Formação 35h → 40h (criar entry no `_living/DECISION_LOG.md` se for alteração estrutural).
5. **Utilizador + SEO Lead**: decidir ordem de produção dos 5 briefs P1 (ver Decisão #2).
6. **Após 28d GSC coleta**: relatório baseline metrics em `reports/`.

## Last Updated

2026-05-20 por Claude (SEO Lead).

---

> Após gravar este relatório:
> 1. ✅ Atualizar `_living/CURRENT_STATUS.md` (resumo curto + link).
> 2. ✅ Mover backlog items para `_living/BACKLOG.md`.
> 3. ✅ Mover oportunidades para `_living/OPPORTUNITIES.md`.
> 4. ✅ Registar decisões duradouras em `_living/DECISION_LOG.md`.
> 5. **Não duplicar** o relatório inteiro nos ficheiros vivos.
