# Structure Map

Mapa da estrutura do repositório Previmed e o significado de cada parte.

## Objetivo
Dar à equipa de agentes uma visão única do que existe e do papel de cada pasta, para navegar sem ambiguidade.

## Mapa de topo
```text
previmed/
├── 000_previmed.md     # entrada principal
├── README.md           # identidade do repo
├── SOURCES.md          # fontes e pesquisa
├── departments/        # estrutura/departamentos da empresa (quem/que área)
├── workspaces/         # espaços concretos de trabalho (onde) — não é VS Code workspace
├── tools/              # ferramentas reutilizáveis (com o quê)
├── manuals/            # manuais e procedimentos (como se faz)
├── shared/             # contexto, glossário, marca, referências, templates (base comum)
└── .claude/            # equipa: agents, commands, connectors, modules, project, records, skills
```

### Dentro de `.claude/`
- **modules/** — unidades reutilizáveis e exportáveis. Module ativo: `seo-growth-system` (SEO Lead + 14 subagentes, comando `/seo`, project docs, skills). Fonte da verdade do SEO. Os modules **não guardam templates de records** — usam os de `records/templates/`.
- **agents/seo-growth-system/** e **commands/seo.md** — pontes para o Claude Code descobrir/invocar o module (a lógica vive no module).
- **project/seo-growth-system/** e **skills/seo-growth-system/** — superseded pelo module (mantidos por compatibilidade, com README a apontar para o module).
- **records/** — registos reais + `templates/` (templates reutilizáveis) + `architecture/` (decisões estruturais). Ver `records/README.md`.

## Significado de cada parte
- **departments/** — responsabilidade. commercial, operations, communications, web, compliance, health_safety, training. (`web` inclui SEO/WordPress como capacidade.)
- **workspaces/** — frentes de trabalho concretas: previmed_pt, careview, archive.
- **tools/** — capacidades reutilizáveis: browser_rules_engine, email_escape, archive.
- **manuals/** — procedimentos por área (commercial, operations, communications, web, compliance, careview, archive).
- **shared/** — context, glossary, brand, references, templates.
- **.claude/** — agents, commands, connectors, project, records, skills (preservados da base existente).

## Relação department ↔ workspace ↔ tool
- Departamentos descrevem *responsabilidade*.
- Workspaces descrevem *onde o trabalho acontece* e são servidos por vários departamentos.
- Tools são *reutilizáveis* e vivem fora dos workspaces; os workspaces apenas as referenciam.

## Estado atual
Mapa alinhado com a estrutura base inicial.

## Próximos passos
- [ ] atualizar este mapa sempre que a estrutura mudar
