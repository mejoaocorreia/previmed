---
name: schema-entity-review
description: Rever ou desenhar dados estruturados e entidades, garantindo correspondencia com conteudo visivel.
---

# Skill: Schema & Entity Review

## Objetivo
Rever/desenhar dados estruturados e entidades de uma página/site, garantindo correspondência com conteúdo visível.

## Quando usar
Adicionar/rever schema, consolidar entidades (`/seo schema`).

## Quem pode usar
[`schema-entity`](../../agents/schema-entity.md) (principal), [`technical-seo`](../../agents/technical-seo.md).

## Inputs necessários
Conteúdo visível da página, dados reais da entidade (nome, morada, contactos, perfis oficiais), schema atual.

## Procedimento
1. Identificar entidades e tipos aplicáveis. 2. Verificar correspondência schema↔conteúdo visível. 3. Confirmar propriedades obrigatórias. 4. Verificar duplicação por plugin/tema. 5. Validar `sameAs`/NAP. 6. Validar (Rich Results / Schema.org). 7. Listar riscos.

## Output esperado
Tipos recomendados · propriedades · fonte dos dados · páginas aplicáveis · riscos · validação.

## Critérios de qualidade
Schema = conteúdo visível; propriedades obrigatórias presentes; sem duplicação; sameAs só oficiais; validado.

## Erros comuns
Marcar conteúdo inexistente; reviews/ratings falsos; duplicar schema do plugin; sameAs para perfis não oficiais.

## Agentes relacionados
[`schema-entity`](../../agents/schema-entity.md), [`local-seo`](../../agents/local-seo.md), [`wordpress-seo-implementation`](../../agents/wordpress-seo-implementation.md).

## Project docs relacionados
[`SCHEMA_ENTITY_MODEL`](../../project/SCHEMA_ENTITY_MODEL.md), [`TECHNICAL_RULES`](../../project/TECHNICAL_RULES.md).

## Ferramentas/MCPs possíveis
Rich Results Test, Schema.org validator, Browser. Read-only.

