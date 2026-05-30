---
name: gsc-ga4-analysis
description: Analisar dados de Search Console e GA4 para insights e acoes, com limitacoes explicitas.
---

# Skill: GSC / GA4 Analysis

## Objetivo
Analisar dados de Search Console e GA4 para insights e ações, com leitura correta e limitações explícitas.

## Quando usar
Análise de dados orgânicos, quedas/subidas, CTR, conversões (`/seo data`).

## Quem pode usar
[`seo-data-analyst`](../../agents/seo-data-analyst.md) (principal).

## Inputs necessários
Acesso autorizado a GSC/GA4 (e PSI/CrUX quando útil), períodos a comparar, páginas/queries de interesse, objetivo.

## Procedimento
1. Definir pergunta e período comparável. 2. Recolher dados (read-only). 3. Separar brand vs non-brand. 4. Segmentar por página/query. 5. Identificar quedas/subidas e CTR. 6. Ligar a ações realizadas. 7. Formular hipótese e ação. 8. Definir métrica a monitorizar. 9. Declarar limitações/amostragem.

## Output esperado
Insight · evidência · páginas/queries afetadas · hipótese · ação recomendada · métrica para monitorizar.

## Critérios de qualidade
Períodos comparáveis; brand vs non-brand separados; agregado vs bruto distinguido; sem conclusões sem dados; limitações explícitas.

## Erros comuns
Somar métricas incorretamente; confundir posição média com ranking fixo; ignorar amostragem; concluir sem amostra suficiente.

## Agentes relacionados
[`seo-data-analyst`](../../agents/seo-data-analyst.md), [`seo-lead`](../../agents/seo-lead.md).

## Project docs relacionados
[`KPI_MODEL`](../../project/KPI_MODEL.md), [`REPORTING_MODEL`](../../project/REPORTING_MODEL.md).

## Ferramentas/MCPs possíveis
Search Console API, GA4 Data API, PageSpeed/CrUX. Read-only; cuidado com quotas/amostragem.

