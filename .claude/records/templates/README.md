# Records Templates

Templates reutilizáveis para records do repositório Previmed.

## O que é
Esta pasta guarda **templates** — moldes reutilizáveis para criar records. **Não são records reais.**

## Regras
- **Templates não são records reais.** Copiar o template, datar e preencher no sítio certo.
- **Records reais** ficam nas pastas adequadas dentro de `.claude/records/` (ex.: `audits/`, `tasks/`, `reviews/`, `snapshots/`, `architecture/`, `incidents/`, `rollbacks/`).
- Templates podem ser **gerais** ou **específicos por module/área**.
- **Modules devem referenciar estes templates**, em vez de guardarem templates próprios. Um module guarda capacidade reutilizável; os templates de records vivem aqui.

## Organização
- `seo/` — templates do module `seo-growth-system` (auditorias, reports, decisões, tasks, go-live). Ver [`seo/README.md`](seo/README.md).
- (futuro) outras subpastas por module/área conforme surgirem.

## Convenção de nome (ao criar um record real)
`YYYY-MM-DD__report-type.md` (data ISO 8601 + `__` + kebab-case). Markdown sempre.

## Estado atual
Base inicial. Uma subpasta: `seo/`.
