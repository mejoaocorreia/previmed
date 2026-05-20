# Skill: SEO Quality Gate

## Objetivo

Avaliar se uma recomendação, alteração ou implementação SEO pode avançar.

## Entrada

- pedido;
- página/ficheiro afetado;
- recomendação;
- risco;
- dados disponíveis.

## Processo

1. Verificar intenção.
2. Verificar impacto no utilizador.
3. Verificar impacto no negócio.
4. Verificar risco técnico.
5. Verificar risco WordPress/produção.
6. Verificar conteúdo e confiança.
7. Verificar performance/mobile/accessibility.
8. Verificar AI Search sem manipulação.
9. Verificar se precisa de autorização.
10. Dar decisão.

## Output

```md
## SEO Quality Gate

Resultado: [Aprovado / Aprovado com notas / Bloqueado / Precisa de dados / Precisa de autorização]

### O que está bom
...

### O que bloqueia
...

### Correções obrigatórias
...

### Próximo passo
...
```

## Regras

- Não aprovar alteração de slug/redirect/indexação sem plano.
- Não aprovar schema enganador.
- Não aprovar conteúdo genérico.
- Não aprovar SEO que estrague UX/performance.
- Não aprovar recomendação baseada em dados inventados.
