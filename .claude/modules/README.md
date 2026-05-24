# Modules

Unidades reutilizáveis e exportáveis dentro do `.claude/`.

## O que é um module
Um **module** é uma unidade completa e reutilizável de capacidade. Pode conter:
- `agents/` — agentes especializados;
- `commands/` — comando(s) de entrada;
- `project/` — regras, operating system e playbooks;
- `skills/` — procedimentos reutilizáveis.

Os **templates de records** que um module usa **não vivem dentro do module** — vivem centralizados em `.claude/records/templates/` (ex.: SEO em `.claude/records/templates/seo/`). O module apenas os referencia.

## Princípios
- Modules são **reutilizáveis** — podem ser usados por vários workspaces.
- Modules são **exportáveis** — podem ser copiados para outros repos/projetos com pouca adaptação.
- Modules **não substituem o supervisor geral** da Previmed. O supervisor continua a ser o router e o dono da governação (segurança, RGPD, produção, rollback).
- Modules são **chamados pelo supervisor ou por comandos**, não se auto-ativam.
- Um module tem sempre um `manifest.md` (o que é, quando usar, o que inclui, como exportar).
- Templates de records vivem em `.claude/records/templates/`, não dentro do module.

## Nota de compatibilidade com Claude Code
O Claude Code **não descobre automaticamente** agentes/skills/commands dentro de `.claude/modules/`. Só descobre os que estão em `.claude/agents/`, `.claude/commands/`, `.claude/skills/`.

Por isso, cada module que precise de ser invocável tem **pontes** nos caminhos nativos:
- um comando global em `.claude/commands/` que aponta para o module;
- pontes curtas em `.claude/agents/<module>/` quando for preciso que o Claude Code descubra os agentes.

A **fonte da verdade** é sempre o module. As pontes encaminham, não duplicam conteúdo.

## Modules existentes
- [`seo-growth-system/`](seo-growth-system/README.md) — equipa SEO / crescimento orgânico (primeiro module estruturado).

## Modules futuros (apenas ideia, não criar agora)
careview, compliance, wordpress, visual, communications, operations. A arquitetura está preparada para os acolher, mas **só o `seo-growth-system` existe por agora**.

## Estado atual
Base inicial. Um module estruturado (`seo-growth-system`).
