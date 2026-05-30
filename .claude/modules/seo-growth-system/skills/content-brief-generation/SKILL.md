---
name: content-brief-generation
description: Gerar um brief editorial SEO acionavel a partir de pesquisa e intencao.
---

# Skill: Content Brief Generation

## Objetivo
Transformar pesquisa e intenção num brief editorial que permita escrever uma página superior à concorrência.

## Quando usar
Antes de criar/reescrever uma página importante (`/seo brief`).

## Quem pode usar
[`content-brief`](../../agents/content-brief.md) (principal), com input de [`keyword-intent`](../../agents/keyword-intent.md) e [`serp-competitor-analyst`](../../agents/serp-competitor-analyst.md).

## Inputs necessários
Cluster/keyword e intenção, objetivo comercial, padrão da SERP a superar, provas/credenciais reais disponíveis.

## Procedimento
1. Confirmar intenção e público. 2. Definir page type e objetivo. 3. Título e meta sugeridos. 4. Outline H1/H2/H3. 5. Must-answer questions (FAQs reais). 6. Trust elements (prova/E-E-A-T). 7. Internal links (origem/destino). 8. Schema potencial. 9. CTA. 10. Quality bar de aceitação.

## Output esperado
Brief com: page type · target intent · primary keyword/topic · secondary topics · suggested title · meta · outline · must-answer questions · trust elements · internal links · conversion CTA · quality bar.

## Critérios de qualidade
Permite escrever página melhor que a concorrência (não apenas semelhante); intenção e prova claras; CTA definido.

## Erros comuns
Brief genérico; pedir keywords sem intenção; ignorar prova/CTA; copiar estrutura do concorrente sem superar.

## Agentes relacionados
[`content-brief`](../../agents/content-brief.md), [`content-growth`](../../agents/content-growth.md), [`onpage-seo`](../../agents/onpage-seo.md).

## Project docs relacionados
[`CONTENT_RULES`](../../project/CONTENT_RULES.md), [`STRATEGY_RULES`](../../project/STRATEGY_RULES.md).

## Ferramentas/MCPs possíveis
Browser/Search (referência SERP), Search Console (queries reais). Read-only.

