# Architecture Records

Decisões estruturais e evolução da arquitetura do repositório Previmed.

## Objetivo
Guardar **decisões de arquitetura**, as suas razões, alternativas rejeitadas e a evolução da estrutura do repo — o *porquê* da forma como o Previmed está organizado.

## O que entra aqui
- Por que usamos `departments`, `workspaces`, `tools`, `manuals`, `shared`, `modules`.
- Por que tools ficam fora dos workspaces.
- Por que records/templates é centralizado.
- Por que workspaces usam modules e não os absorvem.
- Decisões sobre limpeza estrutural (ex.: remoção de migração/archive).

## O que NÃO entra aqui
- Logs operacionais (decisões de tarefas, comandos, acessos, dados sensíveis) — esses vivem em `.claude/records/decisions/` e nos logs próprios do System Safety.
- Records de execução (audits, reviews, snapshots, incidents, rollbacks, tasks) — nas pastas próprias.

## Distinção `architecture/` vs `decisions/`
- **architecture/** — decisões **estruturais** do repo (como está organizado e porquê).
- **decisions/** — logs **operacionais** (decisões de tarefas/comandos/dados), referenciados pelo supervisor/System Safety.

## Ficheiros
- [`architecture_log.md`](architecture_log.md) — registo cronológico das decisões de arquitetura.

## Estado atual
Base inicial, com as decisões da arquitetura modular Previmed registadas.
