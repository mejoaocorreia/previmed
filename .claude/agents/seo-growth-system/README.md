# .claude/agents/seo-growth-system/ (pontes)

Esta pasta já **não** é a fonte da verdade do SEO. É um conjunto de **pontes de compatibilidade** para o Claude Code descobrir os agentes SEO e encaminhar para o module.

## Fonte da verdade
[`.claude/modules/seo-growth-system/`](../../modules/seo-growth-system/README.md) — equipa completa de 15 agentes, comando `/seo`, project docs, skills e templates.

## Porque existem pontes
O Claude Code descobre agentes em `.claude/agents/`, mas não dentro de `.claude/modules/`. Estas pontes mantêm o sistema a funcionar enquanto a lógica vive no module.

## Pontes aqui
- `seo-lead.md` → module `agents/seo-lead.md`
- `technical-seo.md` → module `agents/technical-seo.md`
- `content-growth.md` → module `agents/content-growth.md`
- `competitor-research.md` → module `agents/serp-competitor-analyst.md` (renomeado)

Os restantes 11 agentes da equipa vivem **só** no module (não precisam de ponte por agora; o SEO Lead chama-os). Se for preciso que o Claude Code os descubra individualmente, criar pontes curtas aqui no mesmo formato.

## Estado
Conteúdo canónico consolidado no module (estes ficheiros são apenas pontes).
