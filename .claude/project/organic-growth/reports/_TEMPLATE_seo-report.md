# [Report Title] — YYYY-MM-DD

> **Este é um template.** Copiar para `YYYY-MM-DD__report-type.md` e preencher. Não editar este ficheiro com análise real.

## Purpose

Explicar para que serve este relatório e em que situações deve ser consultado no futuro.

Exemplo: *"Auditoria técnica SEO baseline antes do redesign WordPress. Serve como referência de partida para medir impacto das alterações futuras."*

## Scope

O que esta análise cobre e o que **não** cobre.

Exemplo:
- Coberto: indexabilidade, sitemap, robots, schema atual, Core Web Vitals, on-page das 12 URLs P1.
- Não coberto: análise de backlinks, off-page, local SEO multi-localização.

## Data Sources Used

Listar todas as fontes/ferramentas usadas, com estado:

| Fonte | Estado |
|---|---|
| Codebase analysis (templates atuais) | completed |
| Live site crawl (Playwright/Screaming Frog) | completed |
| Google Search Console | not connected / pending / completed |
| GA4 | not connected / pending / completed |
| PageSpeed Insights / Lighthouse | completed |
| SERP research (Modo IA, Google.pt) | completed |
| Sitemap.xml | reviewed |
| robots.txt | reviewed |
| Manual review | completed |
| Outros (especificar) | — |

## Confidence Level

- **High** / **Medium** / **Low**.

Explicar limitações:
- Que dados faltam?
- Que parte é hipótese vs facto observado?
- Que ferramentas estavam offline/não-ligadas no momento?

## Executive Summary

3–5 parágrafos curtos. Quem ler só esta secção tem de sair com:
- estado geral;
- 3 achados mais importantes;
- 1 decisão pendente que bloqueia trabalho;
- direção recomendada.

## Priority Findings

Ordenar do mais crítico para o menos:

### Critical
- Achado 1 — descrição curta + impacto + onde está.
- Achado 2 — …

### High
- …

### Medium
- …

### Low
- …

## Current SEO State

### Strengths
- O que já está bem.

### Weaknesses
- O que está mal e precisa de correção.

### Opportunities
- Onde há ganho relativo a competidores ou intenções não cobertas.

### Risks
- O que pode degradar tráfego/ranking se nada for feito.

## Detailed Analysis

Incluir **apenas as secções aplicáveis** ao tipo de relatório. Apagar as que não interessam.

### Site Structure Review
- Mapa de URLs, hierarquia, profundidade de cliques.

### Technical SEO Review
- Indexabilidade, canonicals, hreflang, sitemap, robots, redirects, status codes.

### Content & Search Intent Review
- Mapeamento intenção ↔ página, gaps de conteúdo, qualidade editorial.

### Competitor / SERP Review
- Quem domina cada cluster, padrões SERP (AIO, FAQ, vídeos), lacunas exploráveis.

### Keyword & Cluster Opportunities
- Clusters por prioridade, volume estimado, dificuldade, página alvo.

### Internal Linking Review
- Hubs, orphan pages, distribuição de PageRank interno, anchors.

### Schema / Entity SEO Review
- Schemas presentes, esquemas em falta, knowledge graph, sameAs.

### Local SEO Review
- GBP, NAP, citações, schema LocalBusiness, multi-location se aplicável.

### Performance / Core Web Vitals Review
- LCP, INP, CLS por template, em mobile e desktop. Quem pesa mais.

### AI Search / GEO Review
- Presença em AIO (Modo IA), Perplexity, ChatGPT search; fontes citadas pelos rivais.

### WordPress Implementation Notes
- Plugins SEO, custom fields, ACF/blocos, blockers conhecidos. **Sem alterar nada — só observar.**

## Recommended Action Plan

Separar por fases. Cada item deve poder virar tarefa em `_living/BACKLOG.md`.

### Phase 1 — Foundation
- [ ] …

### Phase 2 — Content & Structure
- [ ] …

### Phase 3 — Technical SEO
- [ ] …

### Phase 4 — Authority & Internal Linking
- [ ] …

### Phase 5 — Measurement & Iteration
- [ ] …

## Backlog Items To Add

Lista crua de tarefas que devem ser copiadas para `_living/BACKLOG.md` na secção certa. Formato curto:

- `[Quick win]` Corrigir titles duplicados em /servicos/*.
- `[Technical blocker]` Sitemap.xml não inclui CPTs de formação.
- `[Content opportunity]` Criar pillar "Como escolher empresa de medicina do trabalho".

## Decisions Needed

Decisões que requerem input do utilizador antes de prosseguir. Cada decisão com:
- contexto;
- opções A/B/C;
- recomendação se houver.

## Open Questions

Perguntas que ainda não têm resposta e que afetam a continuação da análise.

## Next Steps

Próximos 3–5 passos concretos, ordenados. Quem faz, o quê, quando.

## Last Updated

YYYY-MM-DD por [autor/agente].

---

> Após gravar este relatório:
> 1. Atualizar `_living/CURRENT_STATUS.md` (resumo curto + link).
> 2. Mover backlog items para `_living/BACKLOG.md`.
> 3. Mover oportunidades para `_living/OPPORTUNITIES.md`.
> 4. Registar decisões duradouras em `_living/DECISION_LOG.md`.
> 5. **Não duplicar** o relatório inteiro nos ficheiros vivos.
