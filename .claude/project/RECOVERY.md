# Recovery

## Antes de alterações médias/grandes

- git status;
- criar branch se fizer sentido;
- checkpoint/commit;
- atualizar CURRENT_TASK.md;
- atualizar TASK_SNAPSHOT.md.

## Se correr mal

Parar.

Não remendar às cegas.

Opções:
1. corrigir em cima;
2. reverter ficheiros específicos;
3. voltar ao checkpoint;
4. usar rewind da ferramenta;
5. abandonar branch.

## Commits recomendados

Antes:
- `Checkpoint before <task>`

Depois:
- `Implement <lote> - <descrição>`

## Regra

Sem rollback claro, sem alteração grande.
