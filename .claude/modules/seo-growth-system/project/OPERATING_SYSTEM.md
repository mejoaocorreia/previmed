# SEO Growth Operating System

Define como o module SEO Growth System trabalha. É a fonte principal de detalhe operacional.

## Objetivo
Quando usado, construir um ativo orgânico que: seja tecnicamente rastreável/indexável; responda melhor às intenções de pesquisa; represente serviços com clareza; transmita confiança; tenha conteúdo útil e diferenciado; seja rápido e bom em mobile; esteja preparado para Search clássico e AI Search; converta; e possa ser medido e melhorado.

## Quando usar
Sempre que o SEO Lead inicia trabalho médio/grande. Para microtarefas, basta a regra relevante.

## Regras principais
- Não há SEO sem intenção clara.
- Não há página nova sem papel na arquitetura.
- Não há alteração de slug sem plano de redirect.
- Não há schema sem conteúdo visível correspondente.
- Não há conteúdo SEO genérico.
- Não há design que esconda conteúdo crítico.
- Não há dependência pesada sem performance review.
- Não há análise grande sem record persistente (ver REPORTING_MODEL).
- SEO não passa por cima de segurança, produção, rollback, performance, acessibilidade, marca ou dados pessoais.

## Áreas de trabalho
Estratégia · pesquisa/intenção · concorrência/SERP · arquitetura de informação · SEO técnico · conteúdo · on-page · internal linking · schema/entidades · local SEO · performance/CWV · acessibilidade (qualidade SEO indireta) · WordPress implementation · medição/reporting · AI Search · refresh/manutenção · governance editorial.

## Processo (workflow padrão)
1. Objetivo de negócio. 2. Público e serviço. 3. Mapear intenção. 4. Concorrência/SERP. 5. Arquitetura/página. 6. Brief de conteúdo. 7. Validar SEO técnico. 8. Validar visual/mobile/performance. 9. Validar schema quando aplicável. 10. Implementar com WordPress Engineering se necessário. 11. Testar indexabilidade e experiência. 12. Medir (GSC/GA4). 13. Atualizar backlog/decisões. 14. Refresh quando necessário.

## Inputs
Objetivo, público, páginas/URLs, dados disponíveis, restrições (produção, marca, RGPD).

## Outputs
Diagnóstico/plano com evidência, prioridade (impacto/esforço/risco), próximos passos, e record persistente para análises grandes.

## Handoff entre áreas
SEO recomenda · WordPress Engineering implementa técnica · Visual Experience valida experiência · System Safety valida risco · supervisor aprova mudanças sensíveis.

## Priorização
- **Impacto:** tráfego potencial, intenção comercial, conversão, autoridade, risco técnico, nº de páginas, prioridade do negócio.
- **Esforço:** conteúdo, design, WordPress, desenvolvimento, aprovação, ferramentas, dependências.
- **Risco:** produção, slugs/redirects, indexação, performance, marca, RGPD/dados, acessibilidade.
- **Output recomendado:** quick wins · high-impact projects · technical blockers · content opportunities · long-term authority work.

## Anti-token-waste / persistência
Análise longa sem record persistente = desperdício de contexto. Antes de continuar uma análise grande, confirmar: "isto está a ser persistido?". Se não, criar o record a partir do template e só depois continuar. Ver [`REPORTING_MODEL.md`](REPORTING_MODEL.md).

## Agentes relacionados
Todos os do module, coordenados pelo [`seo-lead`](../agents/seo-lead.md).

## Skills relacionadas
Todas — ver [`../skills/`](../skills/).

## Ferramentas/MCPs possíveis
Ver [`TOOLING_MODEL.md`](TOOLING_MODEL.md).

## Critérios de qualidade
SEO só é bom se melhora utilidade, clareza para motores, confiança, performance, conversão e sustentabilidade. (Ver [`QUALITY_GATE.md`](QUALITY_GATE.md).)

## Notas de consolidação
Fusão do operating system SEO do conteúdo ativo com a versão anterior do pacote SEO (anti-token-waste, living vs dated, persistence rule). A mecânica de ficheiros vivos/datados foi generalizada para `REPORTING_MODEL`.
