# Organic Growth / SEO System

Sistema SEO de alto nível para o projeto Previmed. **Persistente em ficheiros**, não no chat.

Scope: competitor research, keyword strategy, technical SEO, WordPress SEO, local SEO, schema/entidades, internal linking, content briefs, on-page quality, Core Web Vitals, AI Search / GEO visibility, SEO QA + reporting.

## Estrutura desta pasta

```
organic-growth/
├── README.md                ← este ficheiro (mapa de leitura)
│
├── _system/                 ← REGRAS DE TRABALHO (raras alterações)
│   ├── OPERATING_SYSTEM.md  ← persistence rule + anti-token-waste
│   ├── QUALITY_BAR.md
│   ├── KPI_MODEL.md
│   ├── GLOSSARY.md          ← jargão plain-language
│   ├── TOOLING_MCP_STACK.md ← política orçamento zero
│   └── playbooks/           ← workflows por área
│       ├── COMPETITOR_RESEARCH.md
│       ├── CONTENT_SYSTEM.md
│       ├── TECHNICAL_AUDIT.md
│       ├── SCHEMA_ENTITY_MODEL.md
│       └── LOCAL_PLAYBOOK.md
│
├── _living/                 ← ESTADO ATUAL CURTO
│   ├── CURRENT_STATUS.md    ← ponto de entrada para retomar trabalho
│   ├── BACKLOG.md           ← tarefas acionáveis priorizadas
│   ├── DECISION_LOG.md      ← decisões duradouras
│   └── OPPORTUNITIES.md     ← hipóteses por validar
│
├── strategy/                ← FASE 1 (fechada)
│   ├── STRATEGY.md          ← documento mestre
│   ├── AUDIENCES.md
│   ├── INFORMATION_ARCHITECTURE.md
│   ├── KEYWORDS.md          ← 16 clusters, ~120 queries
│   └── COMPETITORS.md
│
├── setup/                   ← DECISÕES + GUIAS SETUP
│   ├── BASELINE_AUDIT.md
│   ├── KEYWORD_DATA_DECISION.md
│   └── GSC_GA4_SETUP.md
│
├── reports/                 ← ANÁLISES DATADAS (snapshots no tempo)
│   ├── _TEMPLATE_seo-report.md
│   ├── README.md
│   └── 2026-05-20__*.md     ← análises, planos, recapturas
│
└── clusters/                ← CONTEÚDO EDITORIAL VIVO POR CLUSTER
    ├── q1-medicina-trabalho/
    │   ├── BRIEF.md         ← spec editorial
    │   ├── COPY.md          ← copy pronto a deploy
    │   └── aio-capture.yml  ← evidência bruta Playwright
    ├── q2-seguranca-trabalho/
    ├── q3-haccp/
    ├── q4-formacao-40h/
    └── q5-escolher-mt/
        ├── BRIEF.md / COPY.md / aio-capture.yml
        └── spin-offs/
            └── avenca-vs-ato/
                └── COPY.md
```

## Por onde começar

| Se queres… | Lê primeiro… |
|---|---|
| Retomar o trabalho | [`_living/CURRENT_STATUS.md`](./_living/CURRENT_STATUS.md) |
| Saber o que falta fazer | [`_living/BACKLOG.md`](./_living/BACKLOG.md) + [`reports/2026-05-20__execution-plan-90d.md`](./reports/2026-05-20__execution-plan-90d.md) |
| Perceber jargão (AIO, E-E-A-T, cluster, etc.) | [`_system/GLOSSARY.md`](./_system/GLOSSARY.md) |
| Entender a arquitetura completa do sistema | [`reports/2026-05-20__architecture-map.md`](./reports/2026-05-20__architecture-map.md) |
| Ver o copy de um pillar (Q1/Q2/Q3/Q4/Q5) | [`clusters/q<N>-*/COPY.md`](./clusters/) |
| Ver as regras de trabalho SEO | [`_system/OPERATING_SYSTEM.md`](./_system/OPERATING_SYSTEM.md) |
| Ver a estratégia (Fase 1) | [`strategy/STRATEGY.md`](./strategy/STRATEGY.md) |

## Regras-chave

1. **Análise SEO grande sem ficheiro persistente = desperdício de contexto.** Ver [`_system/OPERATING_SYSTEM.md`](./_system/OPERATING_SYSTEM.md#anti-token-waste).
2. **Snapshots datados** vão para `reports/YYYY-MM-DD__*.md`. Não editar após publicação.
3. **Conteúdo editorial vivo** (brief + copy) vive em `clusters/q<N>-<slug>/`. Brief e copy juntos = sem drift.
4. **Ficheiros vivos** (`_living/`) são índices curtos. Não duplicam análise — apontam para `reports/`.

## Convenções

- **Naming datado:** `YYYY-MM-DD__report-type.md` (Markdown, não `.txt`).
- **Brand voice:** "Medicina do Trabalho" (forma canónica). Ver [`_living/DECISION_LOG.md`](./_living/DECISION_LOG.md).
- **Autoria:** pessoa real do quadro Previmed. Placeholders atuais (substituir antes de publicar):
  - Q1+Q5 → Dr. Miguel Henriques
  - Q2 → Eng.ª Sara Vilela
  - Q3 → Eng.ª Carla Tavares
  - Q4 → Dra. Inês Carvalho

## Última reorganização

2026-05-20 — migrado de estrutura plana (23 ficheiros na raiz) para esta hierarquia funcional. Ver `reports/2026-05-20__architecture-map.md`.
