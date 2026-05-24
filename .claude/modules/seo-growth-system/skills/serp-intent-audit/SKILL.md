# Skill: SERP Intent Audit

## Objetivo
Classificar a intenção dominante de uma SERP e o tipo de conteúdo que ela favorece, para alinhar a página certa.

## Quando usar
Antes de criar/otimizar uma página, ou ao validar a intenção de um cluster (`/seo keywords`, `/seo competitor`).

## Quem pode usar
[`serp-competitor-analyst`](../../agents/serp-competitor-analyst.md) e [`keyword-intent`](../../agents/keyword-intent.md).

## Inputs necessários
Query(ies), mercado/localização/dispositivo quando relevante.

## Procedimento
1. Observar a SERP real da query. 2. Classificar intenção dominante (informacional, comercial, local, transacional, navegacional). 3. Identificar o tipo de página que rankeia (guia, serviço, comparativo, local, etc.). 4. Registar SERP features (AIO, snippet, PAA, local pack, vídeos, imagens). 5. Concluir que formato/estrutura a página alvo deve ter para satisfazer a intenção.

## Output esperado
Query · intenção dominante · tipo de página favorecido · SERP features presentes · implicação para a nossa página.

## Critérios de qualidade
Intenção fundamentada na SERP real; distinção entre o que a query "diz" e o que o utilizador quer; data registada.

## Erros comuns
Assumir intenção pela query literal; ignorar SERP features; confundir intenção comercial com transacional.

## Agentes relacionados
[`serp-competitor-analyst`](../../agents/serp-competitor-analyst.md), [`keyword-intent`](../../agents/keyword-intent.md), [`content-brief`](../../agents/content-brief.md).

## Project docs relacionados
[`STRATEGY_RULES`](../../project/STRATEGY_RULES.md), [`COMPETITOR_RESEARCH_PLAYBOOK`](../../project/COMPETITOR_RESEARCH_PLAYBOOK.md).

## Ferramentas/MCPs possíveis
Browser/Search (SERP real). Read-only; sem scraping agressivo.

## Notas de consolidação
Consolidado da versão anterior do pacote SEO. Incluído (não deferido) porque a classificação de intenção da SERP é um procedimento reutilizável e distinto do mapa de clusters.
