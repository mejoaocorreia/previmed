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
| Briefs P1 (5 pillars) | 🟡 a iniciar | Decorrente da AIO expansion. Ver backlog. |

## Último relatório

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

1. Utilizador executa checklist em `SETUP_GSC_GA4.md` (ligar GSC/GA4/Site Kit + API PSI) + garantir conta Google Ads ativa (mesmo sem spend) para Keyword Planner.
2. Decidir ordem de produção dos 5 briefs P1 + brand voice + autoria (ver `reports/2026-05-20__competitor-deep-dive.md` §Decisions Needed).
3. Atualizar `STRATEGY_KEYWORDS.md` cluster Formação para 35→40h.
4. Após 28d de coleta GSC: produzir baseline metrics (novo relatório datado).
5. Atualizar `SEO_TOOLING_MCP_STACK.md` para refletir stack zero-cost (já decidido).

## Bloqueios atuais

- **Decisão keyword data tool** — bloqueia depth analysis de volumes/concorrência.
- **Setup GSC/GA4** — bloqueia baseline metrics e validação de hipóteses do `STRATEGY.md`.

## Como atualizar este ficheiro

Atualizar sempre que:
- um novo relatório é adicionado a `reports/`;
- o estado de uma área muda (concluído / bloqueado / desbloqueado);
- a fase atual muda.

Manter **curto**. Sem análise — só estado. Análise vai para `reports/`.
