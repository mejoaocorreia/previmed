# Instalar o plugin `seo-growth-system`

Este module e um **plugin Claude Code**. Os agentes, o comando oficial `/seo` e as skills so passam a ser descobertos nativamente depois de o plugin ser instalado.

## Estrutura Do Plugin

```text
seo-growth-system/
├── .claude-plugin/plugin.json   # manifesto obrigatorio
├── agents/                      # 15 subagentes com frontmatter
├── commands/seo.md              # comando oficial /seo
├── skills/<nome>/SKILL.md       # 11 skills com frontmatter
├── project/                     # regras/playbooks lidos pelos agentes
├── records-templates/           # templates exportaveis
├── manifest.md · README.md · INSTALL.md
```

## Instalar Neste Repo

O repo tem `.claude-plugin/marketplace.json` na raiz a apontar para este module.

```text
/plugin marketplace add .
/plugin install seo-growth-system@previmed-marketplace
```

Opcao via Git:

```text
/plugin marketplace add https://github.com/mejoaocorreia/previmed
/plugin install seo-growth-system@previmed-marketplace
```

Depois recarregar:

```text
/reload-plugins
```

Confirmar:

```text
/agents
/seo
```

## Comando Oficial

O comando principal visivel ao utilizador e:

```text
/seo
```

O ficheiro que define o comando e:

```text
commands/seo.md
```

Nao usar nomes alternativos ou comandos namespaced como comando principal. Se alguma instalacao do Claude Code mostrar comandos com namespace por configuracao local, confirmar no runtime, mas a documentacao deste module assume `/seo` como comando oficial.

## Namespaces De Subagentes

O module continua a chamar-se `seo-growth-system`.

Subagentes de plugin usam namespace:

```text
seo-growth-system:<agent-name>
```

Exemplos:

```text
seo-growth-system:seo-lead
seo-growth-system:technical-seo
seo-growth-system:seo-qa
```

O comando `/seo` instrui o uso do prefixo no `subagent_type`.

## Ordem Correta

1. Adicionar marketplace.
2. Instalar plugin.
3. Recarregar plugins ou reiniciar Claude Code.
4. Confirmar `/agents`.
5. Confirmar `/seo`.

Reiniciar antes de instalar nao carrega nada.

## Orquestracao Paralela

O comando `/seo` corre no topo, ao nivel do agente principal. E ele que faz fan-out de `Task()` em paralelo para subagentes quando necessario.

Um subagente folha nao deve lancar outros subagentes. Por isso, `seo-lead` continua a ser coordenador/planner/consolidador, mas o fan-out operacional vive no comando `/seo`.

## Exportar Para Outro Repo

Opcao A — apontar para este repo como marketplace Git:

```text
/plugin marketplace add <git-url-deste-repo>
/plugin install seo-growth-system@previmed-marketplace
```

Opcao B — copiar a pasta `seo-growth-system/` para um marketplace proprio e instalar a partir dai.

O module e fonte unica: nao copiar agentes/skills/comandos manualmente para outras pastas.

## Notas

- `project/` nao e componente executavel de plugin; vai junto como referencia lida pelos agentes.
- `records-templates/` contem templates; records reais ficam no projeto consumidor em `.claude/records/`.
- Se comandos `/plugin` devolverem erro de schema, confirmar a documentacao oficial do Claude Code para o formato atual de `plugin.json`/`marketplace.json`.
