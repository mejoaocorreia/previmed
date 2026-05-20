# Workflow

## Fluxo base

1. Pedido do utilizador.
2. Supervisor decide Planning ou Implementation.
3. Se for médio/grande, aplica Change Management.
4. Identifica risco.
5. Define escopo.
6. Divide em lotes, se necessário.
7. Garante checkpoint.
8. Executa apenas lote aprovado.
9. Valida.
10. Reporta.
11. Aguarda aprovação para próximo lote.

## Fix pequeno

- interpretar;
- alterar apenas o necessário;
- testar;
- reportar curto.

## Alteração média/grande

- análise antes;
- ficheiros prováveis;
- riscos;
- lotes;
- critérios de aceitação;
- rollback;
- testes.

## Go-live

Só com:
- preview validado;
- backup/checkpoint;
- rollback;
- aprovação explícita;
- teste pós-ativação.

## Retoma

Se sessão cair:
- ler CURRENT_TASK.md;
- verificar git status;
- verificar git diff;
- confirmar próximo passo.
