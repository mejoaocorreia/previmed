# SEO Current Status

> Ficheiro **vivo e curto**. Estado atual do trabalho SEO num relance.
> Para análise detalhada, ver [`reports/`](./reports/).

## Última atualização

2026-05-20

## Fase atual

**Fase 2 — Dados.**

Fase 1 (estratégia) fechada. Fase 2 a recolher dados antes de iniciar Fase 3 (produção de conteúdo).

## Estado por área

| Área | Estado | Notas |
|---|---|---|
| Estratégia | ✅ concluída | Ver `STRATEGY.md`. |
| Auditoria técnica baseline | ✅ concluída | `AUDIT_PREVIMED_BASELINE.md`. |
| Keyword data tool | ✅ decidido | **Orçamento zero**. Stack só com GSC + GA4 + Keyword Planner + Playwright + PSI. Ver `SEO_DECISION_LOG.md` 2026-05-20. |
| Setup GSC/GA4/PSI | ⏳ execução pendente | Checklist em `SETUP_GSC_GA4.md`. Lado utilizador. |
| AIO expansion (5 queries) | ✅ concluída | Ver `reports/2026-05-20__aio-expansion.md`. |
| Baseline metrics | ⛔ bloqueado | Precisa de 28d de GSC após ligação. |
| Briefs P1 (5 pillars) | ✅ todos escritos | 5 briefs em `reports/`. Brand voice + autoria decididas. **Placeholders** Dr. Miguel Henriques (Q1/Q5), Eng.ª Sara Vilela (Q2), Eng.ª Carla Tavares (Q3), Dra. Inês Carvalho (Q4). ⚠️ **Substituir por pessoas reais antes de publicar** (YMYL + E-E-A-T). |
| Glossário plain-language | ✅ criado | `SEO_GLOSSARY.md` — explicação de todo o jargão (AIO, E-E-A-T, cluster, etc.). Vivo. |

## Último relatório

- **2026-05-20** — [`reports/2026-05-20__architecture-map.md`](./reports/2026-05-20__architecture-map.md) — **mapa de arquitetura completa** do sistema Supervisor + Organic Growth. 4 camadas funcionais (Supervisor / SEO Lead / Specialists / Skills + Commands) com diagramas Mermaid + ASCII. Diagnóstico de problemas atuais (23 ficheiros planos na raiz, `reports/` mistura 4 tipos). **Proposta concreta** de reorganização por pastas funcionais (`_system/`, `_living/`, `strategy/`, `setup/`, `reports/`, `clusters/`). Tabela de mapeamento origem→destino completa para 41 ficheiros. Aguarda aprovação para migrar.

- **2026-05-20** — [`reports/2026-05-20__copy-spinoff-avenca-vs-ato.md`](./reports/2026-05-20__copy-spinoff-avenca-vs-ato.md) — **copy final do spin-off SO-1** (Avença vs ato médico). Query comercial BOT funnel. Tabela 3 cenários (PME 10/30/100 trabalhadores). 8 FAQs + schema Article+FAQPage+isPartOf (apontando para pillar Q5). Métricas focadas em **conversões** (não só citações AIO). Bloqueado pelos mesmos placeholders dos outros copies.

- **2026-05-20** — [`reports/2026-05-20__spin-offs-briefs.md`](./reports/2026-05-20__spin-offs-briefs.md) — **15 spin-offs documentados** num único ficheiro consolidado (não 15 separados). Priorizados em 4 ondas (P1-A / P1-B / P2 / P3). P1-A são 3 spin-offs alto valor/baixo esforço para arrancar em paralelo aos pillars: Avença vs ato (Q5), Lei 93/2019 (Q4), Ficha de Aptidão (Q1). Recomendação: arrancar P1-A em paralelo aos pillars; P1-B e P2 só depois de recaptura AIO t+30d para priorizar pelos clusters que estão a entrar em AIO.

- **2026-05-20** — [`reports/2026-05-20__execution-plan-90d.md`](./reports/2026-05-20__execution-plan-90d.md) — **plano consolidado 90 dias** para fechar Fase 2 e arrancar Fase 3. 5 fases (A→E) com esforço estimado (~10.5 pd ativos), responsável e dependências. Cobre desde substituir placeholders até medir KPIs t+90/180d. **Ponto de entrada único** para quem pegar no trabalho.

- **2026-05-20** — **5 copies finais completos** em `reports/`:
  - [`copy-pillar-q1-medicina-trabalho.md`](./reports/2026-05-20__copy-pillar-q1-medicina-trabalho.md) — head term Medicina do Trabalho.
  - [`copy-pillar-q2-seguranca-trabalho.md`](./reports/2026-05-20__copy-pillar-q2-seguranca-trabalho.md) — head term Segurança no Trabalho + 4 modalidades + checklist por setor.
  - [`copy-pillar-q3-haccp.md`](./reports/2026-05-20__copy-pillar-q3-haccp.md) — HACCP + 7 princípios HowTo.
  - [`copy-pillar-q4-formacao-40h.md`](./reports/2026-05-20__copy-pillar-q4-formacao-40h.md) — Formação 40h (Lei 93/2019).
  - [`copy-pillar-q5-escolher-mt.md`](./reports/2026-05-20__copy-pillar-q5-escolher-mt.md) — Como escolher empresa MT (foothold AIO).
  - Todos com title/meta/slug, ~1700–2000w body, 12 FAQs, schema Article+FAQPage+(HowTo)+Breadcrumb pronto a colar, checklist pré-publicação, métricas de tracking. Bloqueados por: nomes reais (placeholders), dados `<<…>>`, hub `/recursos/guias/`, deploy WP.

- **2026-05-20** — [`reports/2026-05-20__copy-pillar-q4-formacao-40h.md`](./reports/2026-05-20__copy-pillar-q4-formacao-40h.md) — **copy final do pillar Q4 (Formação 40h)** pronto para revisão editorial e implementação. Abertura explícita com correção 35→40h + Lei 93/2019. 12 FAQs + schema Article+FAQPage+HowTo. Autor placeholder Dra. Inês Carvalho. Diferenciador: primeira referência PT atualizada. **Crítico**: deploy deve coincidir com atualização de `/consultoria-formacao/` (que ainda diz "35h" — `reports/2026-05-20__previmed-pages-audit.md` §C1).

- **2026-05-20** — [`reports/2026-05-20__copy-pillar-q5-escolher-mt.md`](./reports/2026-05-20__copy-pillar-q5-escolher-mt.md) — **copy final do pillar Q5** pronto para revisão editorial e implementação WordPress. Aplica o brief Q5: 6 critérios + secção legal Lei 102/2009 + 12 FAQs + schema JSON-LD pronto a colar (Article + HowTo + FAQPage + BreadcrumbList) + checklist pré-publicação + métricas de tracking. Autor placeholder Dr. Miguel Henriques (substituir antes de publicar). Inclui `<<…>>` para dados Previmed concretos a preencher.

- **2026-05-20** — **5 briefs P1 completos** em `reports/`:
  - [`content-brief-escolher-mt.md`](./reports/2026-05-20__content-brief-escolher-mt.md) — Q5 (brief de referência, foothold AIO).
  - [`content-brief-medicina-trabalho.md`](./reports/2026-05-20__content-brief-medicina-trabalho.md) — Q1 (head term core MT).
  - [`content-brief-seguranca-trabalho.md`](./reports/2026-05-20__content-brief-seguranca-trabalho.md) — Q2 (head term ST + 4 modalidades).
  - [`content-brief-haccp.md`](./reports/2026-05-20__content-brief-haccp.md) — Q3 (HACCP + 7 princípios HowTo).
  - [`content-brief-formacao-40h.md`](./reports/2026-05-20__content-brief-formacao-40h.md) — Q4 (Formação 40h, correção legal 35→40).
  - Todos seguem o template comum: 1400–1700w body + 400–700w FAQ; 5–7 citações institucionais obrigatórias; schema Article + FAQPage + (HowTo onde aplicável); 3 spin-offs planeados por pillar.
  - Bloqueados pela mesma decisão (brand voice + autoria).

- **2026-05-20** — [`reports/2026-05-20__content-brief-escolher-mt.md`](./reports/2026-05-20__content-brief-escolher-mt.md) — brief P1 do pillar Q5 "Como escolher empresa de medicina do trabalho". Aplica padrão Centralmed+SEPRI+Forprev: 1500–2000w, 4+ citações institucionais, schema Article+FAQPage+HowTo, 12 FAQs, 6º critério defensável vs Forprev (indicadores de qualidade mensuráveis). 3 spin-offs planeados (geo + Relatório Único + Avença vs ato). Bloqueado por 2 decisões pendentes (brand voice + autoria).

- **2026-05-20** — [`reports/2026-05-20__previmed-pages-audit.md`](./reports/2026-05-20__previmed-pages-audit.md) — auditoria sistémica de 5 URLs core Previmed. Achados:
  - **Problemas estruturais são sistémicos (template-level), não pontuais.** Title duplicado em 4/4 páginas de serviço. H1→H3 sem H2 em 4/4. Schema genérico em 4/4. 0 ext links institucionais em 4/4. WC médio 359w (range 165–732).
  - `/consultoria-formacao/` tem **3 ocorrências de "35h" e 0 de "40h"** — compliance issue face à Lei 93/2019.
  - Home `/` tem H1 "Notícias Previmed" (está como blog, não como homepage SEO).
  - **Implicação:** fixes têm de ir a nível de template/plugin WP, não página a página.

- **2026-05-20** — [`reports/2026-05-20__competitor-deep-dive.md`](./reports/2026-05-20__competitor-deep-dive.md) — auditoria competitiva de 7 URLs (Forprev, SEPRI ×3, Centralmed ×3) + Previmed `/saude-no-trabalho/`. Achados-chave:
  - **Centralmed = padrão ouro** em citação outbound institucional (6–8 links externos a ACT/DGS/pgdlisboa/FAO/EUR-Lex por artigo). Sem schema JSON-LD detectável — o link graph é a alavanca AIO.
  - **SEPRI = padrão "árvore"** (1 pillar + spin-offs geográficos/tópicos cruzados). 3 URLs em AIO Q1.
  - **Forprev** = caso mais curto (656w) que aparece em AIO via Service schema + 28 FAQs.
  - **Previmed `/saude-no-trabalho/`** tem problemas estruturais: title duplicado, hierarquia H1→H3 quebrada, 0 links externos institucionais, schema genérico, "Medicina **No** Trabalho" no body (sem preposição "do").

- **2026-05-20** — [`reports/2026-05-20__aio-expansion.md`](./reports/2026-05-20__aio-expansion.md) — análise AIO em 5 queries P1. Previmed citado em 1/5 (Q5). Achado crítico: lei 35h→40h. Concorrentes dominantes: Centralmed, SEPRI, Forprev, Medilav, Ecosáude, Preveris.

## Próximos passos

1. **Utilizador**: indicar **nomes concretos dos autores** por cluster (médico MT, técnico HST, especialista alimentar, responsável formação). Decisão conceptual fechada — só faltam nomes.
2. **Utilizador**: executar checklist em `SETUP_GSC_GA4.md` (ligar GSC/GA4/Site Kit + API PSI) + garantir conta Google Ads ativa.
3. Quando #1 estiver feito: começar **copy final** dos 5 pillars (não bloqueado por mais nada).
4. **Refactor templates WP** — title duplicado + H2 ausentes + schema (ver `reports/2026-05-20__previmed-pages-audit.md`). Decisão de quando.
5. Após 28d de coleta GSC: produzir baseline metrics (novo relatório datado).

## Bloqueios atuais

- **Setup GSC/GA4** — bloqueia baseline metrics e validação de hipóteses do `STRATEGY.md`.
- **Substituição dos 4 placeholders por pessoas reais do quadro** — bloqueia **publicação** (não a escrita do copy). Copy pode arrancar já com placeholders; antes de cada deploy, substituir.
- **Decisão "quando aplicar refactor WP"** — bloqueia quick wins documentados em `reports/2026-05-20__previmed-pages-audit.md`.

## Como atualizar este ficheiro

Atualizar sempre que:
- um novo relatório é adicionado a `reports/`;
- o estado de uma área muda (concluído / bloqueado / desbloqueado);
- a fase atual muda.

Manter **curto**. Sem análise — só estado. Análise vai para `reports/`.
