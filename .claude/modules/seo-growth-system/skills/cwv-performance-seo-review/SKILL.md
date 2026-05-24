# Skill: Core Web Vitals / Performance SEO Review

## Objetivo
Diagnosticar Core Web Vitals e performance como fator de SEO/UX, sobretudo em mobile.

## Quando usar
Avaliar performance de páginas/templates (`/seo performance`, parte de `/seo audit`).

## Quem pode usar
[`cwv-performance-seo`](../../agents/cwv-performance-seo.md) (principal), [`technical-seo`](../../agents/technical-seo.md).

## Inputs necessários
URLs/templates a medir, acesso a PSI/Lighthouse/CrUX, contexto de tema/plugins.

## Procedimento
1. Medir LCP/INP/CLS (lab e field quando houver). 2. Identificar causa provável (imagens, fontes, JS/CSS, render-blocking, cache, lazy). 3. Priorizar por impacto. 4. Recomendar sem destruir design. 5. Definir teste de validação. 6. Marcar handoff a Visual Experience/Frontend se a causa for visual.

## Output esperado
Métrica · estado · causa provável · evidência · recomendação · impacto SEO/UX · teste de validação.

## Critérios de qualidade
Distinguir lab vs field; alvos LCP ≤ 2.5s / INP < 200ms / CLS baixo; recomendações que não degradam design; teste definido.

## Erros comuns
Confundir lab com field; otimizar desktop e ignorar mobile; adicionar scripts pesados; recomendar mudanças que partem o layout.

## Agentes relacionados
[`cwv-performance-seo`](../../agents/cwv-performance-seo.md), [`technical-seo`](../../agents/technical-seo.md), [`wordpress-seo-implementation`](../../agents/wordpress-seo-implementation.md).

## Project docs relacionados
[`TECHNICAL_RULES`](../../project/TECHNICAL_RULES.md).

## Ferramentas/MCPs possíveis
PageSpeed Insights API, Lighthouse, Chrome DevTools, CrUX. Read-only.

## Notas de consolidação
Consolidado da versão anterior do pacote SEO (skill de CWV/performance review).
