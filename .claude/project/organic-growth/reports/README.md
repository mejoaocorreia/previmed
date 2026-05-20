# SEO Reports — snapshots datados

Esta pasta contém relatórios SEO **completos, datados e históricos**.

Cada relatório representa o estado de uma análise num momento específico — não é editado depois de publicado. Se o estado mudar, cria-se um novo relatório.

## Formato de nome

```
YYYY-MM-DD__report-type.md
```

Exemplos válidos:
- `2026-05-20__seo-full-audit.md`
- `2026-05-20__competitor-analysis.md`
- `2026-05-20__keyword-research.md`
- `2026-05-20__technical-seo-audit.md`
- `2026-05-20__seo-strategy-plan.md`
- `2026-05-20__content-gap-analysis.md`
- `2026-05-20__seo-action-plan.md`
- `2026-05-20__core-web-vitals-audit.md`
- `2026-05-20__schema-entity-review.md`
- `2026-05-20__local-seo-audit.md`
- `2026-05-20__ai-search-geo-review.md`
- `2026-05-20__aio-expansion.md`

Regras:
- Data ISO 8601 (`YYYY-MM-DD`).
- Dois underscores entre data e tipo (`__`).
- `report-type` em kebab-case, descritivo, sem espaços.
- Sempre `.md` (não `.txt`) — Markdown renderiza no GitHub e é mais legível.

## Quando criar novo relatório

Cria-se um novo ficheiro em `reports/` sempre que o utilizador pede uma destas análises:

- análise SEO completa;
- planeamento SEO;
- análise de concorrência;
- auditoria técnica;
- keyword research / cluster map;
- content gap analysis;
- estratégia de conteúdos;
- Core Web Vitals / performance;
- schema / entidades;
- local SEO;
- AI Search / GEO;
- plano de ação SEO.

Análise grande **sem** ficheiro persistente = desperdício de contexto. Ver [Anti-token waste](../_system/OPERATING_SYSTEM.md#anti-token-waste) no operating system.

## Template obrigatório

Usar [`_TEMPLATE_seo-report.md`](./_TEMPLATE_seo-report.md) como base para qualquer relatório novo. Copiar e adaptar — não criar estruturas alternativas.

O prefixo `_` no template é proposital:
- ordena primeiro alfabeticamente;
- sinaliza que **não é um relatório real**.

## Relação com ficheiros vivos

Os relatórios datados aqui dentro são a **fonte detalhada e arquivada**.

Em paralelo, existem 4 ficheiros vivos curtos em [`../`](..) que servem para consulta rápida:

| Ficheiro vivo | Função |
|---|---|
| [`_living/CURRENT_STATUS.md`](../_living/CURRENT_STATUS.md) | Estado atual curto do SEO + apontador para o último relatório. |
| [`_living/BACKLOG.md`](../_living/BACKLOG.md) | Tarefas acionáveis priorizadas. |
| [`_living/OPPORTUNITIES.md`](../_living/OPPORTUNITIES.md) | Oportunidades, ideias, hipóteses antes de virarem tarefas. |
| [`_living/DECISION_LOG.md`](../_living/DECISION_LOG.md) | Decisões SEO importantes e duradouras. |

**Depois de criar um relatório datado**, o autor deve:

1. atualizar `_living/CURRENT_STATUS.md` com um resumo curto + link para o relatório novo;
2. adicionar tarefas acionáveis ao `_living/BACKLOG.md` (não duplicar o relatório inteiro);
3. adicionar oportunidades ao `_living/OPPORTUNITIES.md`;
4. adicionar decisões ao `_living/DECISION_LOG.md` **apenas** se forem decisões reais e duradouras;
5. **não** copiar o relatório inteiro para os ficheiros vivos — os ficheiros vivos são índices/sumários, não cópias.

## Quem consulta esta pasta

- **Supervisor / Change Manager** — para validar persistência e ler análise detalhada.
- **SEO Lead e agentes Organic Growth** — para consultar análise anterior antes de produzir nova.
- **Utilizador (humano)** — para ler análise completa em GitHub.

## O que NÃO está aqui

- **Briefs editoriais e copies finais** dos clusters → vivem em [`../clusters/q<N>-<slug>/BRIEF.md`](../clusters/) e [`COPY.md`](../clusters/). Brief + copy juntos = sem drift.
- **Snapshots brutos Playwright** (aio-capture.yml) → vivem dentro da pasta do cluster correspondente em [`../clusters/`](../clusters/).
- **Regras de trabalho e playbooks** → vivem em [`../_system/`](../_system/).
- **Estado vivo** (status, backlog, decisões, oportunidades) → vivem em [`../_living/`](../_living/).
- **Estratégia Fase 1** → vive em [`../strategy/`](../strategy/).
- **Decisões + guias setup técnico** → vivem em [`../setup/`](../setup/).
- Templates WordPress, código de implementação — fora do scope.
- Roadmaps de produto que não sejam SEO — fora do scope.
