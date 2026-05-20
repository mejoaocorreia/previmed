# Arquivo

Esta pasta contém agentes, skills e comandos **arquivados** porque foram substituídos pela suite `organic-growth/`.

Decisão tomada em 2026-05-19: `organic-growth/` tem precedência sobre versões equivalentes na raiz de `.claude/`.

Os ficheiros aqui são mantidos por:
- referência histórica;
- comparação;
- possibilidade de reaproveitar conteúdo se necessário.

**Não usar estes ficheiros.** O Supervisor e qualquer agente deve usar exclusivamente:
- `.claude/agents/organic-growth/`
- `.claude/skills/organic-growth/`
- `.claude/commands/organic-growth/`

## Mapeamento

| Arquivado | Substituído por |
|---|---|
| `agents/technical-seo.md` | `agents/organic-growth/technical-seo.md` |
| `agents/keyword-intent.md` | `agents/organic-growth/keyword-intent.md` |
| `agents/internal-linking.md` | `agents/organic-growth/internal-linking.md` |
| `agents/schema.md` | `agents/organic-growth/schema-entity.md` |
| `skills/seo-strategy-review/` | `skills/organic-growth/seo-operating-system/` |
| `skills/seo-page-brief/` | `skills/organic-growth/content-brief-generation/` |
| `skills/technical-seo-review/` | `skills/organic-growth/technical-seo-crawl-audit/` |
| `skills/local-seo-review/` | `skills/organic-growth/local-seo-review/` |
| `skills/schema-review/` | `skills/organic-growth/schema-entity-review/` |
| `skills/content-quality-review/` | `skills/organic-growth/page-quality-audit/` |
| `skills/internal-linking-review/` | `skills/organic-growth/internal-linking-architecture/` |
| `commands/seo.md` | `/seo-strategy`, `/page-review`, `/technical-audit`, etc. (suite organic-growth) |

## Nota sobre agentes mantidos

Estes agentes da raiz **continuam ativos** porque não têm equivalente em organic-growth:

- supervisor, codebase-analyst, wordpress-theme, site-structure
- frontend-ui, visual-quality, motion-3d
- content-copy (genérico; SEO content vai por content-brief de organic-growth)
- performance, accessibility, qa-preview
- security-recovery, documentation, mcp-tooling-advisor

Estes operam em todo o ciclo de desenvolvimento, não apenas SEO.
