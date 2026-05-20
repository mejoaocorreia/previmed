# Rollback and Recovery

## Objetivo

Garantir que alterações médias, altas ou críticas podem ser revertidas.

## Antes de alterar

Verificar:

- branch atual;
- ficheiros alterados;
- ambiente;
- risco;
- backup/checkpoint;
- task state;
- dados envolvidos.

## Estratégias

### Git

- `git status`;
- `git diff`;
- branch dedicada;
- commit pequeno;
- revert por ficheiro;
- rollback por commit.

### Task continuity

Usar quando:
- tarefa é longa;
- envolve vários ficheiros;
- envolve risco médio/alto;
- pode ficar a meio.

### Backups

Usar quando:
- produção;
- base de dados;
- uploads;
- tema ativo;
- plugins;
- configurações.

## Se algo correr mal

1. parar;
2. não corrigir às cegas;
3. listar alterações;
4. identificar causa;
5. escolher opção:
   - corrigir;
   - reverter ficheiro;
   - voltar checkpoint;
   - pedir decisão humana.

## Regra

Sem rollback claro, sem alteração grande.
