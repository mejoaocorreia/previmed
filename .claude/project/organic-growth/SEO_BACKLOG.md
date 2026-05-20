# SEO Backlog

> Ficheiro **vivo**. Tarefas SEO **acionáveis e priorizadas**.
> Análise detalhada que justifica cada tarefa vive em [`reports/`](./reports/).
> Hipóteses ainda não validadas vivem em [`SEO_OPPORTUNITIES.md`](./SEO_OPPORTUNITIES.md).

## Como usar

- Adicionar tarefas que **já passaram** o filtro de oportunidade → têm dono, esforço estimado e impacto esperado.
- Cada tarefa deve apontar para a **origem** (relatório em `reports/` ou conversa).
- Marcar `[done]` quando concluído, ou mover para arquivo se for ruído.
- Manter **curto** — se cresce demasiado, dividir por fase ou produzir novo relatório de planeamento em `reports/`.

## Formato

```
- [estado] [prioridade] descrição curta — origem: reports/YYYY-MM-DD__*.md
```

- `estado`: `todo` | `wip` | `done` | `blocked`
- `prioridade`: `P1` | `P2` | `P3`

## Quick wins

- `todo` `P1` **Fix title duplicado a nível de template** (afeta 4/4 páginas de serviço, não só `/saude-no-trabalho/`). Origem: `reports/2026-05-20__previmed-pages-audit.md` §F1.
- `todo` `P1` **`/consultoria-formacao/`**: atualizar "35h" (3 ocorrências) → "40h (Lei 93/2019)" — compliance editorial. Origem: §C1.
- `todo` `P2` Home `/`: substituir H1 "Notícias Previmed" por H1 SEO. Origem: §H1.
- `todo` `P2` Proteger URL `/saude-no-trabalho/` — já citada por AIO. Não mexer sem plano de redirect. Origem: `reports/2026-05-20__aio-expansion.md` §Q5.

## Technical blockers

- `done` `P2` Atualizar `STRATEGY_KEYWORDS.md` cluster "Formação 35h" → 40h. Origem: `reports/2026-05-20__aio-expansion.md` §C1+§Q4. Commit `70b8c95`.
- `done` `P2` Auditoria rápida páginas core Previmed — confirmou padrão sistémico. Ver `reports/2026-05-20__previmed-pages-audit.md`.
- `todo` `P1` **Refatorar template páginas de serviço** — H1→H2 (não H3). Afeta 4/4 páginas. Origem: `reports/2026-05-20__previmed-pages-audit.md` §F2.
- `todo` `P1` Adicionar schema Service + FAQPage por template — afeta 4 páginas em batch. Origem: §S1+§S2.

## Content opportunities

- `todo` `P1` Brief Pillar "Medicina do Trabalho" — `/servicos/medicina-trabalho/`. Origem: `reports/2026-05-20__aio-expansion.md` §Q1.
- `todo` `P1` Brief Pillar "Segurança no Trabalho" — `/servicos/seguranca-trabalho/`. Origem: §Q2.
- `todo` `P1` Brief Pillar "HACCP" — `/servicos/higiene-seguranca-alimentar/`. Origem: §Q3.
- `todo` `P1` Brief Pillar "Formação 40h obrigatória" — pillar formação (correção legal 35→40). Origem: §Q4.
- `wip` `P1` Guia "Como escolher empresa de medicina do trabalho" — `/recursos/guias/escolher-medicina-do-trabalho/`. **Brief escrito** em `reports/2026-05-20__content-brief-escolher-mt.md`. Bloqueado por decisões pendentes (brand voice + autoria). Origem: §Q5.
- `todo` `P2` Spin-offs Q5: `relatorio-unico-anexo-d-medicina-trabalho`, `medicina-trabalho-avenca-ou-ato-medico`, geo Norte/Lisboa. Origem: `reports/2026-05-20__content-brief-escolher-mt.md` §Spin-offs.
- `todo` `P1` Criar CPT/template para hub `/recursos/guias/` antes da publicação do pillar Q5. Origem: §Riscos.

## Competitor gaps

- `todo` `P2` Auditoria competitiva: forprev.pt/medicina-do-trabalho/ — entender porquê é top citada em AIO Q5. Origem: §T1.
- `todo` `P2` Auditoria competitiva: sepri.pt (3 entradas AIO Q1) + centralmed.pt (Q1+Q3+Q5). Origem: §T2.

## Performance issues

- A preencher (pendente PSI ligado — ver `SETUP_GSC_GA4.md`).

## Schema/entity improvements

- `todo` `P1` **Regra fixa dos briefs P1:** mínimo 4 links externos institucionais por pillar (ACT + pgdlisboa Lei 102/2009 + 2 outros conforme tema: DGS, DGERT, ASAE, DGAV, FAO/Codex, EUR-Lex, APSEI, OA). Origem: `reports/2026-05-20__competitor-deep-dive.md` §C0.
- `todo` `P1` **Regra fixa dos briefs P1:** Schema por tipo de página — Article + FAQPage em pillars informacionais; HowTo em "como escolher" e HACCP 7 princípios; Service em página de serviço comercial. Origem: §C3.
- `todo` `P2` Adicionar `datePublished` + `dateModified` ao schema de todas as páginas pillar. Origem: §T2.
- `todo` `P2` Estratégia "árvore" SEPRI — cada pillar P1 deve ter 2–3 spin-offs planeados (geo / tópico). Origem: §A1.
- `todo` `P2` Adicionar `author` (Person) com identificação real ao schema Article — decidir quem assina. Origem: §C5+Decision #2.

## Local SEO

- A preencher.

## Measurement

- `done` `P1` Decidir keyword data tool — **decisão: orçamento zero (Cenário Z)**. Registado em `SEO_DECISION_LOG.md` 2026-05-20.
- `done` `P2` Atualizar `SEO_TOOLING_MCP_STACK.md` para refletir stack zero-cost. Origem: `DECISION_KEYWORD_DATA_TOOL.md` §Plano #3.
- `todo` `P2` Garantir conta Google Ads ativa (mesmo sem spend) para destravar buckets finos do Keyword Planner. Origem: `DECISION_KEYWORD_DATA_TOOL.md` §Plano #2.
- `todo` `P1` Ligar GSC, GA4, Site Kit, criar API key PSI — origem: `SETUP_GSC_GA4.md`.
- `blocked` `P1` Produzir baseline metrics — bloqueado por 28d de coleta GSC.
- `todo` `P3` Recaptura AIO t+90d e t+180d pós-publicação pillars (novo relatório). Origem: `reports/2026-05-20__aio-expansion.md` §M2.
- `todo` `P3` Captura trimestral AIO Q4 (formação 35→40) — risco de query usar "35h" enquanto lei diz 40h. Origem: §M3.
