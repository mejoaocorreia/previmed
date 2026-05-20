# Plano de Execução 90 dias — fechar Fase 2 e arrancar Fase 3 — 2026-05-20

## Purpose

Consolidar **tudo o que precisa de ser feito** para fechar a Fase 2 (Dados) e arrancar a Fase 3 (Produção de conteúdo + deploy dos pillars). Servir de ponto de entrada único para qualquer pessoa (humano ou agente) que pegue no trabalho.

Resume os outputs de 10 relatórios desta sessão em **5 fases sequenciais** com responsável, esforço estimado, dependências e critério de "feito".

## Como ler este plano

- **Fases** estão por **ordem de execução** (não por importância).
- **Tarefas dentro de cada fase** podem ser paralelizadas se houver capacidade.
- **Esforço** é estimativa em pessoa-dias (pd).
- **Responsável**: `Utilizador` (decisor/stakeholder), `Dev WP` (quem mexe no WordPress), `SEO Lead` (Claude ou equivalente humano), `Externo` (Google, ACT, etc.).

## Estado de partida (2026-05-20)

| Ativo | Estado |
|---|---|
| Estratégia (Fase 1) | ✅ Fechada — `STRATEGY.md` + 4 docs auxiliares |
| Auditoria técnica baseline | ✅ Feita — `setup/BASELINE_AUDIT.md` |
| Auditoria sistémica páginas core | ✅ Feita — `reports/2026-05-20__previmed-pages-audit.md` |
| Análise AIO 5 queries P1 | ✅ Feita — `reports/2026-05-20__aio-expansion.md` |
| Competitor deep-dive | ✅ Feito — `reports/2026-05-20__competitor-deep-dive.md` |
| 5 briefs P1 | ✅ Escritos — `reports/2026-05-20__content-brief-*.md` |
| **5 copies finais P1** | ✅ Escritos — `reports/2026-05-20__copy-pillar-*.md` |
| Glossário plain-language | ✅ Criado — `_system/GLOSSARY.md` |
| Sistema de persistência (reports/) | ✅ Aplicado |
| Tool keyword data | ✅ Decidido — orçamento zero |
| GSC / GA4 / PSI | ⏳ Pendente — `setup/GSC_GA4_SETUP.md` |
| Refactor templates WP | ⏳ Pendente |
| Hub `/recursos/guias/` | ⏳ Pendente |
| Deploy dos 5 pillars | ⏳ Pendente |
| Nomes reais dos autores | ⏳ Pendente (placeholders ativos) |
| Dados Previmed concretos (`<<…>>`) | ⏳ Pendente |

---

## Fase A — Fundações (semanas 1–2)

**Objetivo:** desbloquear tudo o que depende de info do utilizador + ligar a infraestrutura de medição.

### A1. Recolher nomes reais dos 4 autores

- **Responsável:** Utilizador
- **Esforço:** 0.5 pd
- **Dependências:** nenhuma
- **Output:**
  - Médico do trabalho (assina Q1 + Q5).
  - Técnico/Diretor de Segurança no Trabalho (assina Q2).
  - Especialista de Segurança Alimentar (assina Q3).
  - Responsável/Diretor de Formação (assina Q4).
  - Para cada: nome, cargo, **foto profissional**, **URL LinkedIn**, **bio curta** (1–2 linhas com credenciais).
- **Feito quando:** 4 perfis prontos em formato shareável.

### A2. Recolher dados Previmed concretos (substituir `<<…>>`)

- **Responsável:** Utilizador
- **Esforço:** 0.5 pd
- **Dependências:** nenhuma
- **Output:** preencher os placeholders existentes nos copies:
  - Cobertura geográfica (lista de cidades/centros).
  - Range de preço por trabalhador/ano (PME de escritório).
  - Prazo típico de envio de proposta (X dias úteis).
  - URL real do logo Previmed em alta resolução.
  - URL real da imagem destacada OG por pillar (1200×630).
- **Feito quando:** lista única partilhada com SEO Lead.

### A3. Setup GSC + GA4 + Site Kit + PSI API key

- **Responsável:** Utilizador (+ Dev WP se necessário)
- **Esforço:** 1 pd
- **Dependências:** nenhuma
- **Checklist:** `setup/GSC_GA4_SETUP.md`.
- **Feito quando:** GSC recebe primeiras impressões + GA4 regista sessões + PSI API key armazenada em local seguro.

### A4. Ativar conta Google Ads

- **Responsável:** Utilizador
- **Esforço:** 0.25 pd
- **Dependências:** nenhuma
- **Output:** conta Google Ads ativa (sem necessidade de spend grande — €1/mês destrava buckets finos do Keyword Planner).
- **Feito quando:** Keyword Planner devolve volumes em valores específicos (não buckets).

**Saída da Fase A:** todas as decisões de info estão tomadas. Infraestrutura de medição ligada.

---

## Fase B — Refactor template WordPress (semanas 2–4)

**Objetivo:** corrigir os problemas estruturais sistémicos identificados em `reports/2026-05-20__previmed-pages-audit.md`.

### B1. Fix do title duplicado a nível global

- **Responsável:** Dev WP
- **Esforço:** 0.5 pd
- **Dependências:** A (acessos)
- **Problema atual:** todos os 4 templates de página de serviço geram `"<página> - Previmed - PrevimedPrevimed"`.
- **Causa provável:** plugin SEO + WP duplicam blogname no `<title>`.
- **Output:** title limpo (sem duplicação) em 4/4 páginas.
- **Validação:** view-source de `/saude-no-trabalho/` deve mostrar `<title>` sem repetição.

### B2. Refactor da hierarquia H1 → H2 → H3

- **Responsável:** Dev WP
- **Esforço:** 1 pd
- **Problema atual:** páginas saltam H1 → H3 (sem H2 visíveis).
- **Causa provável:** template usa `<h3>` no segundo nível (legacy).
- **Output:** template gera H1 → H2 → H3 em 4/4 páginas.

### B3. Adicionar schema Service + FAQPage por template

- **Responsável:** Dev WP
- **Esforço:** 1.5 pd
- **Output:** template global de página de serviço inclui JSON-LD com Service + (FAQPage onde houver FAQ) + datePublished/dateModified.
- **Validação:** Rich Results Test passa sem warnings.

### B4. Atualizar `/consultoria-formacao/` (35h → 40h)

- **Responsável:** Dev WP + SEO Lead (copy editorial)
- **Esforço:** 0.5 pd
- **Problema atual:** página cita "35h" 3 vezes; "40h" 0 vezes.
- **Output:** atualizar com correção legal Lei 93/2019 + link cross-pillar para `/recursos/guias/formacao-obrigatoria-40-horas/` (quando publicado).
- **Crítico:** evitar conteúdo contraditório quando o pillar Q4 for deployed.

### B5. Substituir H1 da home

- **Responsável:** Dev WP
- **Esforço:** 0.25 pd
- **Problema atual:** H1 da home = "Notícias Previmed" (está como feed de blog).
- **Output:** H1 SEO-otimizado tipo `"Segurança e Saúde no Trabalho para Empresas em Portugal — Previmed"`.

**Saída da Fase B:** problemas estruturais sistémicos corrigidos em batch. Site preparado tecnicamente para receber os pillars novos.

---

## Fase C — Hub `/recursos/guias/` (semanas 3–4, paralelo a B)

**Objetivo:** criar o **hub editorial** que vai alojar os 5 pillars + spin-offs futuros.

### C1. Criar CPT "Guia" (ou usar Page com template próprio)

- **Responsável:** Dev WP
- **Esforço:** 1 pd
- **Dependências:** nenhuma (independente de B)
- **Output:**
  - CPT `guia` ou Page template `/recursos/guias/` com:
    - Campos custom: H1 (long), intro, autor (`Person` real), data publicação, data modificação, imagem destacada, FAQ repeater, citation list.
    - Schema JSON-LD por template (`Article` + `FAQPage` + `HowTo` opcional + `BreadcrumbList`).
    - Layout responsivo, table of contents lateral, internal linking widget.
- **Validação:** página de teste com lorem ipsum passa Rich Results Test.

### C2. Criar página índice `/recursos/guias/`

- **Responsável:** Dev WP
- **Esforço:** 0.5 pd
- **Output:** página listagem dos guias com filtro por cluster (MT, ST, HACCP, Formação).

### C3. Criar perfis de autor `/equipa/<slug>/`

- **Responsável:** Dev WP + Utilizador (fotos e bios)
- **Esforço:** 0.5 pd
- **Output:** 4 perfis com schema `Person` completo, linkados via `worksFor` à Organization Previmed.

**Saída da Fase C:** hub funcional. Schema validado. Perfis de autor prontos.

---

## Fase D — Deploy dos 5 pillars (semanas 4–6)

**Objetivo:** publicar os 5 copies prontos em `reports/2026-05-20__copy-pillar-*.md`.

### Sequência sugerida (ordem por valor)

1. **Pillar Q5** — `/recursos/guias/escolher-medicina-do-trabalho/` (já há foothold AIO; refrescar valida o sistema).
2. **Pillar Q4** — `/recursos/guias/formacao-obrigatoria-40-horas/` (diferenciador legal único; competidores desatualizados).
3. **Pillar Q1** — `/recursos/guias/medicina-do-trabalho/` (head term core).
4. **Pillar Q3** — `/recursos/guias/haccp/` (vertical restauração).
5. **Pillar Q2** — `/recursos/guias/seguranca-no-trabalho/` (head term mais difícil — Portal ACT domina).

### D1–D5. Para cada pillar

- **Responsável:** SEO Lead (revisão) + Dev WP (publicação)
- **Esforço:** 0.5 pd por pillar × 5 = 2.5 pd
- **Steps:**
  1. Abrir o ficheiro `copy-pillar-q<N>-*.md` em `reports/`.
  2. Substituir placeholder autor pelo perfil real criado em C3.
  3. Substituir todos os `<<…>>` pelos dados recolhidos em A2.
  4. Copiar copy + schema JSON-LD para CPT/Page.
  5. Validar no Rich Results Test.
  6. Publicar.
  7. Submeter URL no Google Search Console (Inspeção de URL → Pedir indexação).
- **Feito quando:** GSC mostra URL "Submetido e indexado".

**Saída da Fase D:** 5 URLs novas indexadas. Pillars prontos para começar a acumular impressões/cliques.

### Importante — proteger foothold existente

- **NÃO** mudar slugs/URLs das páginas atuais `/saude-no-trabalho/`, `/seguranca-no-trabalho/`, `/seguranca-higiene-alimentar/`, `/consultoria-formacao/`.
- Estas páginas continuam a existir como **páginas de serviço comercial**. Os novos pillars em `/recursos/guias/` complementam, não substituem.
- Linkar dos pillars novos para as páginas de serviço existentes (CTA contextual).

---

## Fase E — Medir + iterar (semanas 6–12+)

**Objetivo:** validar se os pillars estão a entrar em AIO + corrigir desvios.

### E1. Baseline metrics

- **Responsável:** SEO Lead
- **Esforço:** 0.5 pd
- **Dependências:** GSC ligado há ≥28 dias (Fase A3)
- **Output:** novo relatório `reports/YYYY-MM-DD__baseline-metrics-gsc.md` com impressões/cliques/posição por query e por URL no momento de partida.

### E2. Recaptura AIO t+30d

- **Responsável:** SEO Lead (Claude via Playwright)
- **Esforço:** 0.5 pd
- **Dependências:** D (todos os pillars publicados)
- **Output:** novo relatório `reports/YYYY-MM-DD__aio-expansion.md` comparando com o de 2026-05-20.
- **Métricas:** Previmed entra em quantas das 5 queries P1? Quais as fontes citadas em conjunto?

### E3. Recaptura AIO t+90d e t+180d

- **Responsável:** SEO Lead
- **Esforço:** 0.5 pd cada
- **Critério de sucesso:**
  - t+90d: Previmed citado em **≥2 das 5 queries P1** (Q5 mantém-se + 1 nova).
  - t+180d: Previmed citado em **≥3 das 5** + posição top 3 em Q5.

### E4. Auditoria competitiva trimestral

- **Responsável:** SEO Lead
- **Esforço:** 1 pd
- **Output:** relatório `reports/YYYY-MM-DD__competitor-deep-dive.md` reciclando metodologia de 2026-05-20.

### E5. Captura trimestral cluster Formação 35→40h

- **Responsável:** SEO Lead
- **Esforço:** 0.25 pd
- **Razão:** query "35 horas" continua a ter volume residual; alguma alteração legal nova pode mudar tudo. Manter conteúdo Previmed atualizado.

**Saída da Fase E:** loop de medição ativo. Decisões baseadas em dados reais GSC + AIO real, não em hipóteses.

---

## Resumo numérico

| Fase | Esforço total (pd) | Janela | Bloqueia |
|---|---|---|---|
| A — Fundações | ~2.25 | semanas 1–2 | Tudo |
| B — Refactor WP | ~3.75 | semanas 2–4 | Quick wins |
| C — Hub /recursos/guias/ | ~2 | semanas 3–4 | Deploy pillars |
| D — Deploy 5 pillars | ~2.5 | semanas 4–6 | Métricas |
| E — Medir + iterar | ~2.75 (recorrente) | semanas 6–12+ | — |
| **Total ativo (A→D)** | **~10.5 pd** | 6 semanas | — |

## Spin-offs (Fase F, opcional, semanas 8–12)

Após validação dos 5 pillars em D+E1, planear os **15 spin-offs** documentados nos briefs:

- **Q1**: `/medicina-do-trabalho-norte/`, `/ficha-de-aptidao-trabalho/`, `/periodicidade-exames-medicina-trabalho/`
- **Q2**: `/modalidades-servico-seguranca-trabalho/`, `/plano-prevencao-riscos-empresa/`, geo
- **Q3**: `/haccp-restauracao/`, `/haccp-limites-criticos-temperatura/`, `/haccp-registos-diarios/`
- **Q4**: `/credito-horas-formacao-continua/`, `/lei-93-2019-formacao-trabalhadores/`, `/coimas-act-formacao-obrigatoria/`
- **Q5**: `/relatorio-unico-anexo-d-medicina-trabalho/`, `/medicina-trabalho-avenca-ou-ato-medico/`, geo

Cada spin-off: ~0.5 pd brief + 0.5 pd copy + 0.25 pd deploy = ~1.25 pd × 15 = **~19 pd**.

**Priorizar pelos que t+30d AIO recapture mostrar serem mais necessários** — não fazer todos.

## Decisões pendentes (a fechar antes de Fase B)

1. **Quando aplicar refactor WP?** Greenfield vs progressivo? — recomendação: greenfield em staging, validar, depois deploy.
2. **Hub `/recursos/guias/` é CPT ou Page template?** — recomendação: CPT para escalar.
3. **Spin-offs em CPT separado ou no mesmo `guia`?** — recomendação: mesmo CPT com taxonomia "tipo" (pillar / spin-off).
4. **Quem revê o copy editorial antes de publicar?** — recomendação: pessoa real (médico/técnico) cujo nome assina, para conferência factual.

## Como manter este plano vivo

Atualizar `_living/CURRENT_STATUS.md` à medida que as fases avançam. Quando o plano estiver desactualizado, **criar novo plano datado em `reports/YYYY-MM-DD__execution-plan.md`** — não editar este.

## Last Updated

2026-05-20 por Claude (SEO Lead).
