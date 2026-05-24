# Records

Registos do repositório Previmed — o que aconteceu, o que foi decidido e moldes para criar novos registos.

## Pastas
- `audits/` — auditorias (accessibility, performance, security, seo, wordpress).
- `architecture/` — decisões estruturais e evolução da arquitetura (o *porquê* da organização). Ver [`architecture/README.md`](architecture/README.md).
- `backups/` — políticas e checkpoints de backup.
- `decisions/` — logs operacionais (tarefas, comandos, acessos, dados sensíveis). Distinto de `architecture/`.
- `drafts/` — rascunhos (briefings, prompts, reports).
- `findings/` — achados não urgentes.
- `incidents/` — incidentes (dados, segurança).
- `reviews/` — revisões (agents, commands, seo, skills, supervisor, visual, wordpress).
- `rollbacks/` — planos e logs de rollback.
- `snapshots/` — snapshots (arquitetura, supervisor, tasks).
- `tasks/` — estado e histórico de tarefas.
- `templates/` — **templates reutilizáveis** para criar records (não são records reais). Ver [`templates/README.md`](templates/README.md).

## Regras
- **Templates** vivem em `templates/`; **records reais** vivem nas pastas próprias.
- **Decisões de arquitetura** vão para `architecture/`; **logs operacionais** vão para `decisions/`.
- Modules (ex.: `seo-growth-system`) **referenciam** templates de `templates/`; não guardam templates próprios.

## Estado atual
Estrutura de records coerente, com `templates/` e `architecture/` adicionados.
