# SEO Strategy Rules

Fonte de verdade estrategica do **SEO Growth System**.

Este ficheiro define os standards para decidir **o que deve existir**, **por que deve existir**, **como se liga ao negocio**, **como se encaixa na arquitetura** e **como deve ser medido**.

Este ficheiro nao e um agente.  
Este ficheiro nao executa auditorias, nao escreve conteudo, nao cria briefs completos e nao implementa WordPress.  
Este ficheiro nao substitui o [`seo-lead`](../agents/seo-lead.md), [`keyword-intent`](../agents/keyword-intent.md), [`content-growth`](../agents/content-growth.md), [`internal-linking`](../agents/internal-linking.md), [`seo-qa`](../agents/seo-qa.md) nem o Supervisor/System Safety.

Producao, RGPD, credenciais, dados sensiveis, rollback, ferramentas pagas e decisoes criticas pertencem ao Supervisor/System Safety.

---

## Objetivo

Garantir que SEO comeca no **negocio**, na **intencao de pesquisa**, na **arquitetura de informacao**, na **utilidade real** e na **capacidade de execucao**, nao numa keyword isolada.

Uma decisao estrategica SEO so esta pronta quando responde:

- que objetivo de negocio serve;
- que publico ou decisor ajuda;
- que intencao satisfaz;
- que page type e adequado;
- que papel tem na arquitetura;
- que evidencia suporta a decisao;
- que riscos cria;
- que agente/skill deve executar;
- como sera medida;
- que record deve persistir a decisao.

---

## Ambito

Este documento cobre:

- SEO ligado a objetivos de negocio;
- intencao de pesquisa;
- arquitetura de informacao;
- tipos de pagina;
- clusters, hubs e supporting pages;
- decisoes de criar, consolidar, atualizar, redirecionar ou remover paginas;
- canibalizacao;
- internal linking estrategico;
- SEO local estrategico;
- entidades, marca e confianca;
- AI Search / GEO;
- priorizacao;
- roadmap 30/60/90;
- medicao estrategica;
- records e persistencia;
- gates estrategicos.

---

## Fora de ambito

Este ficheiro nao deve:

- executar auditoria tecnica detalhada — ver [`TECHNICAL_RULES.md`](TECHNICAL_RULES.md);
- escrever conteudo final — ver [`CONTENT_RULES.md`](CONTENT_RULES.md);
- gerar brief editorial completo — ver [`content-brief`](../agents/content-brief.md) e [`content-brief-generation`](../skills/content-brief-generation/SKILL.md);
- alterar WordPress — ver [`wordpress-seo-implementation`](../agents/wordpress-seo-implementation.md);
- aprovar producao, deploy, rollback, credenciais ou RGPD;
- substituir [`QUALITY_GATE.md`](QUALITY_GATE.md);
- substituir [`TOOLING_MODEL.md`](TOOLING_MODEL.md);
- guardar dados reais ou sensiveis.

---

## Regras Estrategicas

### Regras obrigatorias

- Nao criar pagina sem objetivo de negocio claro.
- Nao criar pagina sem intencao de pesquisa clara.
- Nao criar pagina sem papel na arquitetura.
- Nao criar pagina sem capacidade de manter qualidade.
- Nao criar pagina para servico, localizacao ou setor que nao existe na realidade do projeto consumidor.
- Nao criar paginas duplicadas por variacao minima de keyword.
- Nao criar paginas locais vazias ou doorway pages.
- Nao criar conteudo so para capturar AI Search.
- Nao atacar keywords que nao correspondem a servico real, prova real ou proposta real.
- Nao decidir estrategia so por volume.
- Nao copiar concorrentes.
- Nao mudar URL sem plano tecnico, redirect, validacao e autorizacao quando aplicavel.
- Nao usar ferramentas pagas sem autorizacao explicita.
- Nao inventar rankings, volumes, trafego, conversoes, legislacao, certificacoes, claims ou entidades.

### Perguntas de decisao

Antes de recomendar uma pagina, cluster ou alteracao estrategica, responder:

| Pergunta | Bloqueia se nao houver resposta? |
|---|---|
| Que objetivo de negocio serve? | Sim |
| Que intencao de pesquisa resolve? | Sim |
| Que page type e o mais adequado? | Sim |
| Que pagina existente compete ou duplica esta ideia? | Sim |
| Onde entra na arquitetura e em que cluster? | Sim |
| Que links internos deve receber/enviar? | Sim |
| Que evidencia existe? | Nao, mas marcar hipotese |
| Que risco tecnico, legal, reputacional ou de producao existe? | Sim se medio/alto |
| Como medir sucesso? | Sim para trabalho duradouro |
| Que agente/skill executa a seguir? | Sim |

---

## Tipos De Intencao

| Intencao | Quando aparece | Page type provavel | Risco | Output esperado |
|---|---|---|---|---|
| Informacional | Utilizador quer entender tema, processo, requisito ou problema | Guia educativo, artigo, FAQ hub, glossario | Conteudo generico ou sem autoridade | Explicacao util, fontes, links para servicos |
| Comercial | Utilizador compara opcoes, fornecedores, criterios ou beneficios | Pagina de servico, comparativo honesto, guia de escolha | Claims exagerados ou comparacao injusta | Argumento claro, prova, criterios de decisao |
| Transacional | Utilizador quer agir, pedir proposta, marcar, comprar, contactar | Landing page, pagina de contacto/conversao, servico | Friccao, promessa sem prova, UX fraca | CTA claro, prova, formulario seguro |
| Local | Utilizador procura solucao numa zona | Pagina local, GBP, area de servico | Doorway pages, NAP inconsistente | Presenca real, NAP, conteudo local justificavel |
| Navegacional | Utilizador procura marca, entidade, servico nomeado | Homepage, institucional, contacto, pagina de marca | Marca confusa ou entidades dispersas | Identidade clara, contactos, schema |
| Entidade / marca | Motores ou IA precisam entender quem e a entidade | About, Organization, LocalBusiness, perfis externos | Entidades falsas, sameAs errado | Consistencia entre site, schema e referencias |
| Suporte / pos-venda | Utilizador precisa resolver duvida apos compra/servico | FAQ, guia, suporte, documentacao | Misturar suporte com landing comercial | Resposta direta, links de resolucao |

---

## Page Types

### Homepage

- **Objetivo:** explicar a entidade, proposta principal, areas servidas e caminhos para conversao.
- **Criar/otimizar quando:** marca ou entidade precisa de clareza.
- **Nao usar para:** atacar todas as keywords.
- **Conteudo necessario:** proposta, servicos principais, provas, localizacao/area, links para hubs.
- **Internal linking:** deve apontar para servicos, locais e conteudo prioritario.
- **QA:** sempre que houver alteracao de copy, schema, performance ou navegação principal.

### Pagina de servico principal

- **Objetivo:** converter intencao comercial/transacional de alto valor.
- **Criar quando:** ha servico real, procura, capacidade de entrega e prova.
- **Nao criar quando:** servico e marginal, inexistente ou duplicado.
- **Conteudo necessario:** problema, solucao, processo, publico, prova, FAQs, CTA.
- **Internal linking:** recebe links de guias e aponta para subservicos/contato.
- **QA:** obrigatorio antes de publicar.

### Pagina de subservico

- **Objetivo:** responder a intencao especifica sem sobrecarregar a pagina principal.
- **Criar quando:** intencao e distinta e ha conteudo suficiente.
- **Nao criar quando:** e apenas sinonimo ou variacao leve.
- **Risco:** canibalizacao.
- **Handoff:** `keyword-intent` + `content-brief` antes de criar.

### Pagina de setor / industria

- **Objetivo:** mostrar aplicacao de servico a um segmento real.
- **Criar quando:** ha oferta, prova e linguagem especifica para o setor.
- **Nao criar quando:** e so troca de keyword por setor.
- **Conteudo necessario:** necessidades do setor, requisitos, casos/provas, servicos relacionados.

### Pagina local

- **Objetivo:** satisfazer intencao local real.
- **Criar quando:** ha presenca, area de servico, equipa, operacao ou proposta local justificavel.
- **Nao criar quando:** nao ha relacao real com o local.
- **Risco:** doorway page.
- **Fonte:** [`LOCAL_SEO_PLAYBOOK.md`](LOCAL_SEO_PLAYBOOK.md).

### Guia educativo

- **Objetivo:** responder intencao informacional e apoiar clusters comerciais.
- **Criar quando:** educa, esclarece e liga naturalmente a servicos.
- **Nao criar quando:** nao ha manutencao ou autoridade.
- **Internal linking:** deve apontar para pagina de servico relevante.

### Artigo / blog

- **Objetivo:** cobrir topicos atualizaveis, perguntas emergentes ou conteudo de suporte.
- **Criar quando:** ha utilidade e plano de refresh.
- **Nao criar quando:** o conteudo devia ser pagina evergreen.

### FAQ hub

- **Objetivo:** organizar perguntas recorrentes e reduzir friccao.
- **Criar quando:** existem perguntas reais e volume de duvidas.
- **Risco:** conteudo fino, repetido ou desatualizado.

### Pagina institucional

- **Objetivo:** reforcar confianca, entidade, equipa, certificacoes reais e compliance.
- **Criar quando:** melhora E-E-A-T, marca ou validacao humana.
- **Nao criar quando:** inventa credenciais ou prova.

### Landing page de conversao

- **Objetivo:** converter campanha ou segmento especifico.
- **Criar quando:** ha oferta, publico e tracking claros.
- **Risco:** ficar orfa, duplicar servico ou nao ser indexavel por decisao.

### Pagina de contacto / conversao

- **Objetivo:** reduzir friccao final.
- **Criar/otimizar quando:** ha perda de conversao ou falta de clareza.
- **Governance:** formularios podem envolver dados pessoais; escalar quando necessario.

### Glossario / entidade

- **Objetivo:** clarificar conceitos e entidades importantes.
- **Criar quando:** ajuda utilizador e arquitetura sem competir com servico.
- **Nao criar quando:** e conteudo massificado ou sem manutencao.

---

## Clusters E Arquitetura

### Definicoes

- **Cluster:** conjunto de paginas que cobrem um tema, servico, entidade ou necessidade.
- **Hub / pillar:** pagina principal que organiza o cluster.
- **Supporting page / spoke:** pagina que aprofunda subtema e liga de volta ao hub.
- **Pagina comercial:** pagina orientada a conversao.
- **Pagina educativa:** pagina orientada a entendimento, prova e suporte.

### Regras de cluster

Cada cluster deve definir:

- objetivo de negocio;
- hub principal;
- paginas de apoio;
- intencao de cada pagina;
- links internos obrigatorios;
- CTA principal;
- riscos de canibalizacao;
- criterio de sucesso;
- owner de manutencao.

### Internal linking estrategico

- Toda pagina nova deve ter plano de links antes de publicar.
- Toda pagina importante deve receber links de paginas relacionadas.
- Supporting pages devem ligar ao hub.
- Hubs devem ligar a supporting pages quando ajuda o utilizador.
- Links devem usar anchors naturais, nao stuffing de keywords.
- Orphan pages sao bloqueio ou divida tecnica a registar.

### Criar, atualizar, consolidar, dividir ou remover

| Acao | Quando usar | Requer cuidado |
|---|---|---|
| Criar | intencao distinta, servico real, papel claro | briefing, links, QA |
| Atualizar | pagina existente cobre a intencao mas esta fraca/desatualizada | preservar URL se possivel |
| Consolidar | duas ou mais paginas competem pela mesma intencao | redirect/canonical/plano tecnico |
| Dividir | pagina cobre intencoes diferentes com profundidade suficiente | evitar fragmentacao |
| Redirecionar | URL perde papel ou foi consolidada | plano 301, links, sitemap |
| Remover | conteudo inutil, falso, risco legal ou sem valor | avaliar trafego/indexacao/links |

---

## Canibalizacao

Canibalizacao existe quando duas ou mais paginas competem pela mesma intencao e prejudicam clareza, ranking, conversao ou arquitetura.

Sinais:

- titles/metas quase iguais;
- paginas com H1 semelhante;
- mesma keyword principal;
- GSC mostra alternancia de URLs;
- links internos apontam para paginas concorrentes;
- conteudo sobreposto;
- utilizador nao sabe qual pagina escolher.

Resolver por:

- consolidacao;
- diferenciacao de intencao;
- ajustes de internal linking;
- canonical apenas quando tecnicamente justificado;
- redirects quando ha substituicao clara;
- atualizacao de sitemap e links internos.

---

## Priorizacao

Nao priorizar apenas por volume. Priorizar por valor estrategico.

| Oportunidade | Impacto | Esforco | Risco | Confianca | Prioridade |
|---|---|---|---|---|---|
| [pagina/cluster/acao] | alto/medio/baixo | alto/medio/baixo | alto/medio/baixo | alta/media/baixa | P1/P2/P3 |

### Fatores

- impacto de negocio;
- proximidade de conversao;
- intencao;
- qualidade da evidencia;
- dificuldade de execucao;
- risco tecnico;
- risco legal/compliance;
- prova disponivel;
- dependencias;
- capacidade de manutencao futura;
- oportunidade de internal linking;
- potencial de melhorar confianca.

---

## Roadmap Estrategico

### 30 dias — Fundacao

- validar arquitetura;
- identificar servicos/paginas prioritarias;
- resolver bloqueios tecnicos basicos;
- confirmar GSC/GA4/PageSpeed quando disponivel;
- mapear clusters principais;
- corrigir paginas com maior risco;
- criar records iniciais se houver auditoria.

### 60 dias — Crescimento controlado

- melhorar paginas de servico;
- criar briefs para lacunas reais;
- fortalecer internal linking;
- implementar schema honesto;
- rever local SEO se aplicavel;
- atualizar conteudo com baixo desempenho.

### 90 dias — Expansao e otimizacao

- expandir clusters validos;
- consolidar canibalizacao;
- criar conteudo educativo com papel claro;
- refinar AI Search/GEO;
- medir impacto e ajustar prioridades.

### Continuo

- reporting;
- refresh;
- technical health;
- CWV;
- revisao de SERP;
- records de decisoes duradouras.

---

## AI Search / GEO

AI Search readiness e SEO bem feito: conteudo claro, entidades consistentes, confianca, estrutura e indexabilidade.

Fazer:

- manter entidades consistentes;
- escrever respostas claras e completas;
- tornar conteudo importante visivel no HTML/render;
- usar schema honesto que represente conteudo visivel;
- manter paginas indexaveis quando a estrategia pedir indexacao;
- estruturar perguntas e respostas uteis;
- reforcar autoria, fontes, prova e contexto;
- ligar conteudo educativo a paginas de servico;
- declarar limites quando AI Overviews/AI Mode nao forem observaveis.

Nao fazer:

- prometer presenca em AI Overviews;
- criar conteudo massificado para bots;
- inventar mentions, fontes, reviews, certificacoes ou entidades;
- usar schema artificial;
- tratar `llms.txt` como substituto de SEO;
- criar paginas fracas so para aparecer em respostas generativas.

---

## Local SEO Estrategico

SEO local so deve avancar quando existe relacao real com a zona.

Criar pagina local quando:

- ha presenca fisica, equipa, operacao ou area de servico real;
- o conteudo consegue explicar diferenca local;
- NAP e consistente;
- ha caminho de conversao claro;
- a pagina nao duplica outra localidade.

Nao criar pagina local quando:

- a localidade e apenas keyword;
- nao ha prova de atuacao;
- o conteudo seria igual trocando o nome da zona;
- cria risco de doorway page;
- nao ha plano de manutencao.

Google Business Profile, NAP, reviews e citations seguem [`LOCAL_SEO_PLAYBOOK.md`](LOCAL_SEO_PLAYBOOK.md). Alteracoes em GBP exigem autorizacao.

---

## Estrategia Baseada Em Dados

Usar dados quando existirem, mas nao inventar quando faltarem.

Fontes possiveis:

- GSC: queries, paginas, CTR, impressões, posicao media, indexacao;
- GA4: sessoes organicas, conversoes, engagement, landing pages;
- SERP: tipo de resultado, concorrentes, features, intencao dominante;
- PageSpeed/CrUX/Lighthouse: CWV e performance;
- concorrentes: padroes, lacunas, tipos de pagina;
- inputs do projeto consumidor: servicos reais, publico, restricoes, brand.

Regras:

- separar brand vs non-brand quando relevante;
- separar evidencia de hipotese;
- declarar periodo e fonte;
- nao tratar posicao media como ranking fixo;
- nao inventar volumes;
- nao usar DA/DR/backlinks/trafego estimado sem ferramenta autorizada.

---

## Gates Estrategicos

Bloquear ou pedir revisao quando:

- pagina nao tem objetivo de negocio;
- pagina nao tem intencao clara;
- pagina nao corresponde a servico real;
- pagina duplica outra;
- ha risco de canibalizacao sem plano;
- pagina local e falsa, vazia ou doorway;
- estrategia depende de dados inventados;
- ha promessa impossivel;
- ha claims sensiveis sem revisao humana;
- ha mudanca de URL sem plano tecnico;
- ha WordPress/producao sem autorizacao;
- ha ferramenta paga sem autorizacao;
- ha dados pessoais/sensiveis ou credenciais envolvidos.

Resultado estrategico deve usar os estados do gate quando aplicavel:

- Aprovado
- Aprovado com notas
- Bloqueado
- Precisa de dados
- Precisa de autorizacao

---

## Relação Com Agentes, Skills E Comandos

- [`/seo`](../commands/seo.md) — entrada operacional; usa estrategia para escolher modo e fluxo.
- [`seo-lead`](../agents/seo-lead.md) — coordena routing e consolida estrategia.
- [`keyword-intent`](../agents/keyword-intent.md) — mapeia keywords/intencao a paginas.
- [`content-growth`](../agents/content-growth.md) — transforma estrategia em melhorias de conteudo.
- [`content-brief`](../agents/content-brief.md) — transforma oportunidade em brief.
- [`onpage-seo`](../agents/onpage-seo.md) — aplica elementos on-page.
- [`internal-linking`](../agents/internal-linking.md) — materializa arquitetura via links.
- [`serp-competitor-analyst`](../agents/serp-competitor-analyst.md) — valida SERP e concorrencia.
- [`schema-entity`](../agents/schema-entity.md) — representa entidades e page types com schema honesto.
- [`local-seo`](../agents/local-seo.md) — valida estrategia local.
- [`ai-search-visibility`](../agents/ai-search-visibility.md) — avalia citabilidade e entidades para AI Search/GEO.
- [`seo-data-analyst`](../agents/seo-data-analyst.md) — valida dados e medicao.
- [`seo-qa`](../agents/seo-qa.md) — aplica gate final.

Skills relacionadas:

- [`keyword-cluster-map`](../skills/keyword-cluster-map/SKILL.md)
- [`serp-intent-audit`](../skills/serp-intent-audit/SKILL.md)
- [`content-brief-generation`](../skills/content-brief-generation/SKILL.md)
- [`seo-quality-gate`](../skills/seo-quality-gate/SKILL.md)

---

## Output Estrategico Recomendado

```md
## SEO Strategy Recommendation

### Objetivo de negocio
[objetivo e resultado esperado]

### Publico e intencao
[publico, decisor, intencao dominante e secundarias]

### Page type recomendado
[homepage / servico / subservico / local / guia / etc.]

### Arquitetura / cluster
[hub, supporting pages, links internos, risco de canibalizacao]

### Evidencia
[GSC, GA4, SERP, pagina atual, concorrentes, inputs confirmados]

### Hipoteses
[o que foi assumido e precisa confirmacao]

### Recomendacao
[criar / atualizar / consolidar / dividir / redirecionar / remover]

### Alternativas consideradas
[opcao A/B/C e trade-offs]

### Riscos
[tecnico, conteudo, compliance, producao, UX, manutencao]

### Prioridade
[P1/P2/P3 + impacto/esforco/risco/confianca]

### Handoff
[agente/skill/proximo modo /seo]

### Record recomendado?
[sim/nao + tipo de record]

### Proximo passo
[acao concreta]
```

---

## Records E Persistencia

Criar ou recomendar record quando:

- ha decisao duradoura de arquitetura;
- ha criacao/consolidacao/remocao de paginas;
- ha roadmap 30/60/90;
- ha auditoria estrategica;
- ha decisao com risco, trade-off ou autorizacao;
- ha oportunidade que deve entrar em backlog.

Templates relacionados:

- [`SEO_DECISION_TEMPLATE.md`](../records-templates/SEO_DECISION_TEMPLATE.md)
- [`SEO_TASK_TEMPLATE.md`](../records-templates/SEO_TASK_TEMPLATE.md)
- [`SEO_REPORT_TEMPLATE.md`](../records-templates/SEO_REPORT_TEMPLATE.md)

Records reais vivem no projeto consumidor em `.claude/records/`, nao dentro do plugin.

Nunca guardar dados pessoais, dados sensiveis, credenciais, tokens ou informacao confidencial desnecessaria em records.

---

## Regra Final

Estrategia SEO so e boa se liga negocio, utilizador, intencao, arquitetura, confianca, execucao e medicao.

Se uma proposta melhora ranking teorico mas piora clareza, confianca, UX, manutencao, seguranca ou governanca, ainda nao esta pronta.
