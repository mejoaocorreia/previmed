# SEO Current Status

> Ficheiro **vivo e curto**. Estado atual num relance.
> Análises detalhadas em [`../reports/`](../reports/). Conteúdo editorial em [`../clusters/`](../clusters/).

## Última atualização

2026-05-20 (após reorganização estrutural — ver `../reports/2026-05-20__architecture-map.md`).

## Fase atual

**Fase 2 — Dados, em transição para Fase 3 — Produção/Deploy.**

- Fase 1 (estratégia) ✅ fechada — ver `../strategy/STRATEGY.md`.
- Fase 2 ✅ dados recolhidos + decisões fechadas.
- Fase 3 ⏳ 5 copies finais escritos, aguarda execução (nomes reais + dados Previmed + deploy WP).

## Estado por área

| Área | Estado | Onde |
|---|---|---|
| Estratégia | ✅ | `../strategy/STRATEGY.md` |
| Auditoria técnica baseline | ✅ | `../setup/BASELINE_AUDIT.md` |
| Keyword data tool | ✅ orçamento zero | `../setup/KEYWORD_DATA_DECISION.md` |
| Setup GSC/GA4/PSI | ⏳ execução pendente | `../setup/GSC_GA4_SETUP.md` |
| AIO expansion 5 queries | ✅ | `../reports/2026-05-20__aio-expansion.md` |
| Competitor deep-dive | ✅ | `../reports/2026-05-20__competitor-deep-dive.md` |
| Previmed pages audit | ✅ | `../reports/2026-05-20__previmed-pages-audit.md` |
| Execution plan 90 dias | ✅ | `../reports/2026-05-20__execution-plan-90d.md` |
| Briefs 5 pillars | ✅ | `../clusters/q1-q5/BRIEF.md` |
| Copies 5 pillars | ✅ | `../clusters/q1-q5/COPY.md` |
| Copy spin-off SO-1 (Avença vs ato) | ✅ | `../clusters/q5-escolher-mt/spin-offs/avenca-vs-ato/COPY.md` |
| 14 spin-offs restantes | ⏳ pós t+30d | `../reports/2026-05-20__spin-offs-briefs.md` |
| Baseline metrics | ⛔ bloqueado | precisa 28d coleta GSC |
| Deploy 5 pillars + SO-1 | ⏳ | Dev WP — ver `../reports/2026-05-20__execution-plan-90d.md` |

## Próximos passos (ordem)

1. **Tu** — nomes reais dos 4 autores + dados `<<…>>` nos copies.
2. **Tu** — executar checklist `../setup/GSC_GA4_SETUP.md`.
3. **Dev WP** — refactor templates + criar hub `/recursos/guias/` + deploy 6 copies.
4. **Eu** (t+30d pós-deploy) — recaptura AIO + decidir spin-offs prioritários.

## Bloqueios atuais

- Setup GSC/GA4 — bloqueia baseline metrics.
- Placeholders de autoria — bloqueia **publicação** (não escrita do copy).
- Decisão "quando aplicar refactor WP" — bloqueia quick wins de template.

## Estrutura desta pasta

```
organic-growth/
├── _system/    ← regras, glossário, playbooks
├── _living/    ← este ficheiro + BACKLOG/DECISION_LOG/OPPORTUNITIES
├── strategy/   ← Fase 1 (fechada)
├── setup/      ← decisões + guias setup
├── reports/    ← análises datadas (snapshots no tempo)
└── clusters/   ← BRIEF.md + COPY.md + aio-capture.yml por cluster
```

Mais detalhe em `../README.md`.
