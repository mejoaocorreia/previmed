---
name: keyword-cluster-map
description: Construir um mapa de clusters de keywords com intencao e pagina alvo, evitando canibalizacao.
---

# Skill: Keyword Cluster Map

## Objetivo
Construir um mapa de clusters de keywords com intenção e página alvo, evitando canibalização.

## Quando usar
Pesquisa de keywords, planeamento de arquitetura de conteúdo (`/seo keywords`).

## Quem pode usar
[`keyword-intent`](../../agents/keyword-intent.md) (principal), com input de [`serp-competitor-analyst`](../../agents/serp-competitor-analyst.md).

## Inputs necessários
Tema/serviço, mercado/idioma, páginas existentes, dados de GSC se disponíveis, concorrentes conhecidos.

## Procedimento
1. Construir universo de keywords (head/mid/long-tail). 2. Classificar intenção por keyword. 3. Agrupar em clusters por pilar/tópico. 4. Mapear cada cluster a uma página existente ou nova. 5. Marcar tipo de página recomendado. 6. Detetar canibalização (vários alvos para a mesma intenção). 7. Priorizar por intenção comercial + relevância + fit + dificuldade.

## Output esperado
Por cluster: keyword principal · variações · intenção · página alvo · tipo de página · prioridade · notas de conteúdo · risco de canibalização.

## Critérios de qualidade
Cada keyword tem intenção e página; clusters não canibalizam; prioridade justificada; volumes estimados marcados como hipótese.

## Erros comuns
Priorizar por volume puro; criar clusters que canibalizam; ignorar intenção; inventar volumes sem ferramenta.

## Agentes relacionados
[`keyword-intent`](../../agents/keyword-intent.md), [`content-brief`](../../agents/content-brief.md), [`internal-linking`](../../agents/internal-linking.md).

## Project docs relacionados
[`STRATEGY_RULES`](../../project/STRATEGY_RULES.md).

## Ferramentas/MCPs possíveis
Search Console, SERPs (Browser), Keyword Planner (buckets). Pagas só com autorização.

