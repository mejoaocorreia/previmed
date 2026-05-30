# SEO Growth System (Module)

Equipa SEO / crescimento organico como **module reutilizavel e exportavel**.

## O Que E

O SEO Growth System e a capacidade de crescimento organico, visibilidade, autoridade, conteudo estrategico, SEO tecnico, schema/entidades, local SEO, performance/Core Web Vitals, AI Search e medicao — organizada como **um module unico**, com SEO Lead, subagentes, skills, project docs, records templates e comando oficial `/seo`.

**A fonte da verdade e este module/plugin.** Antigas pastas e pontes SEO fora do module foram removidas. Nao ha duplicacao: cada agente, skill e comando existe uma unica vez aqui.

Este module nao contem automacoes externas proprias, nao contem dados especificos da Previmed e nao guarda dados reais do projeto consumidor. Dados reais, decisoes e records ficam no workspace/projeto que usa o module.

## Plugin Claude Code

Este module e um plugin Claude Code com:

- `.claude-plugin/plugin.json`;
- `agents/` com 15 subagentes;
- `commands/seo.md` com o comando oficial `/seo`;
- `skills/<nome>/SKILL.md` com 11 skills;
- `project/` com regras e playbooks;
- `records-templates/` com templates exportaveis.

Depois de instalado (ver [`INSTALL.md`](INSTALL.md)), os componentes passam a ser descobertos pelo Claude Code.

## Arquitetura Operacional

- **`/seo`** — comando principal por modos; orquestra o fluxo no topo.
- **`seo-lead`** — coordena estrategia, routing e consolidacao.
- **Especialistas** — technical, content, keyword, schema, local, data, performance, AI Search, WordPress SEO.
- **`seo-qa`** — gate final antes de entrega/go-live.
- **`seo-quality-gate`** — skill operacional para aplicar o quality gate.
- **`QUALITY_GATE.md`** — fonte de verdade do standard de aprovacao.
- **Records templates** — modelos para auditorias, reports, decisions, tasks e go-live.

## Fasquia

Alta. O objetivo e trabalho SEO profissional, nao basico. SEO excelente alinha intencao, qualidade, tecnica, autoridade, velocidade, experiencia, negocio, governanca e medicao.

Se uma proposta melhora ranking teorico mas piora confianca, UX, performance, seguranca ou manutencao, ainda nao esta pronta.

## Como Esta Organizado

- [`manifest.md`](manifest.md) — identidade do module, contrato, quando usar, o que inclui.
- [`INSTALL.md`](INSTALL.md) — instalacao e comando oficial.
- [`agents/`](agents/) — SEO Lead + 14 subagentes especializados.
- [`commands/seo.md`](commands/seo.md) — comando oficial `/seo` com modos.
- [`project/`](project/) — operating system, strategy, technical/content rules, quality gate, tooling, KPIs, reporting e playbooks.
- [`skills/`](skills/) — procedimentos reutilizaveis.
- [`records-templates/`](records-templates/README.md) — templates de records SEO.

## Como E Chamado

1. O Supervisor identifica que o pedido toca SEO, web/search/content, AI Search, performance SEO ou WordPress SEO.
2. Encaminha para `/seo` ou para `seo-lead`.
3. O comando `/seo` atua no topo, escolhe modo, faz fan-out para subagentes quando necessario e consolida.
4. Trabalhos relevantes passam por `seo-qa`.
5. Analises, decisoes e tarefas duradouras recomendam records no projeto consumidor.

## Limites

Seguranca, RGPD/dados pessoais, producao, WordPress safety, credenciais, ferramentas pagas, rollback e escopo pertencem ao Supervisor/System Safety.

O SEO recomenda; nao passa por cima destes limites.

## Referencias Externas Base

- Google Search Essentials — https://developers.google.com/search/docs/essentials
- Google SEO Starter Guide — https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- Helpful, reliable, people-first content — https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- AI features and your website — https://developers.google.com/search/docs/appearance/ai-features
- Structured data general guidelines — https://developers.google.com/search/docs/appearance/structured-data/sd-policies
- Structured data introduction — https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- Core Web Vitals and Google Search — https://developers.google.com/search/docs/appearance/core-web-vitals
- URL Inspection API — https://developers.google.com/search/blog/2022/01/url-inspection-api
- URL Inspection Tool — https://support.google.com/webmasters/answer/9012289
- Search spam policies — https://developers.google.com/search/docs/essentials/spam-policies
- Google Business Profile local ranking — https://support.google.com/business/answer/7091
- Schema.org — https://schema.org

## Exportabilidade

O module e generico. Dados especificos de marca, servicos, leis, entidades, clusters, ferramentas autenticadas e records reais ficam no projeto consumidor.

## Estado Atual

Module operacional v1.1 — 15 agentes, 11 skills, comando `/seo` com 14 modos, 12 project docs e 5 records templates. Pronto para uso com Claude Code apos instalacao do plugin.
