# Competitor Research Playbook

Fonte de verdade para análise de concorrência orgânica e SERP do **SEO Growth System**.

Este ficheiro define o processo, as regras e os standards para analisar a concorrência orgânica — quem rankeia, porquê, o que falta e como criar algo genuinamente melhor, nunca para copiar.

Este ficheiro não é um agente.  
Este ficheiro não executa análises.  
Este ficheiro não substitui o `serp-competitor-analyst`, a skill `competitor-gap-analysis` nem o Supervisor/System Safety.

---

## Objetivo

Garantir que a análise de concorrência orgânica e SERP gera insights reais e acionáveis — identificando padrões, gaps e oportunidades — de modo a criar conteúdo e páginas que sejam genuinamente superiores ao que existe, não apenas semelhantes.

---

## Âmbito

Este playbook cobre:

- análise SERP para queries prioritárias;
- classificação de tipos de concorrentes;
- análise de estrutura, conteúdo, prova, schema e UX dos top resultados;
- identificação de padrões e intenção dominante;
- identificação de gaps e oportunidades;
- observação de AI Overviews/AI Mode (quando visível);
- records datados de análises relevantes.

---

## Fora de âmbito

Este playbook não cobre:

- keyword research e clustering — ver `STRATEGY_RULES.md` e skill `keyword-cluster-map`;
- estratégia editorial — ver `CONTENT_RULES.md`;
- SEO técnico — ver `TECHNICAL_RULES.md`;
- schema semântico — ver `SCHEMA_ENTITY_MODEL.md`;
- local SEO — ver `LOCAL_SEO_PLAYBOOK.md`.

---

## Responsabilidades por componente

| Componente | Responsabilidade |
|---|---|
| `COMPETITOR_RESEARCH_PLAYBOOK.md` (este ficheiro) | Standard e processo de análise de concorrência |
| [`serp-competitor-analyst`](../agents/serp-competitor-analyst.md) | Executa análise SERP e concorrência |
| [`competitor-gap-analysis`](../skills/competitor-gap-analysis/SKILL.md) | Procedimento passo a passo de gap analysis |
| [`serp-intent-audit`](../skills/serp-intent-audit/SKILL.md) | Classifica intenção dominante da SERP |
| [`keyword-intent`](../agents/keyword-intent.md) | Fornece queries a analisar |
| [`content-brief`](../agents/content-brief.md) | Consome análise para criar brief editorial |
| [`seo-qa`](../agents/seo-qa.md) | Valida análise e recomendações antes de usar como base |

---

## Standards e regras

### Regras fundamentais

**Nunca copiar:**
- Não copiar texto de concorrentes.
- Não copiar estrutura sem adaptar genuinamente.
- Analisar para superar, não para clonar.
- Usar análise como referência estratégica, nunca como modelo a imitar.

**Sempre registar:**
- Data da análise (obrigatório — SERPs mudam).
- Mercado/idioma (ex.: "Portugal / pt-PT").
- Localização (ex.: "Lisboa" para queries locais, "Nacional" para outras).
- Dispositivo (preferir mobile — Google usa mobile-first indexing).

**Distinguir sempre:**
- Concorrente comercial vs. concorrente orgânico vs. concorrente de autoridade.
- Evidência (observado na SERP real) vs. hipótese (inferido sem verificação).

**Dados:**
- Sem scraping agressivo.
- Dados de backlinks, DA/DR, volume ou tráfego estimado apenas com ferramentas pagas autorizadas.
- Sem ferramenta paga, não inventar estes dados — declarar limitação.

---

### Tipos de concorrentes

| Tipo | Descrição | Implicação |
|---|---|---|
| Comercial | Empresa que vende o mesmo serviço ou produto | Comparar proposta de valor, prova, diferenciais |
| Orgânico | Página que rankeia para a query mas não é concorrente comercial directo (guias, diretórios, media) | Perceber que formato/conteúdo a SERP favorece |
| Autoridade | Entidade reconhecida que domina confiança (reguladores, associações, imprensa) | Entender que entidades têm credibilidade e porquê |
| Misto | Combina comercial e orgânico forte | Mais difícil de superar — requer excelência em ambos |

---

### O que observar em cada resultado

Por URL analisada, registar:

- **Identificação:** URL, domínio, tipo de concorrente.
- **Title e H1:** alinhamento com intenção, palavras-chave usadas.
- **Estrutura:** headings H2 visíveis, layout geral, secções principais.
- **Profundidade:** superficial (< 500 palavras), médio, aprofundado (> 1500 palavras).
- **Conteúdo:** específico ou genérico? Tem prova real (certificações, casos, dados)?
- **FAQs:** presentes? Respondem a perguntas reais?
- **Schema:** rich results visíveis? Que tipo?
- **UX:** legível, mobile-friendly, clara?
- **CTA:** tipo, posição, linguagem.
- **Sinais locais:** morada, GBP, telefone, service areas?
- **Diferencial:** o que esta página faz bem que outros não fazem?
- **Fraqueza:** o que faz mal ou deixa sem resposta?

---

### SERP features a registar

| Feature | O que indica |
|---|---|
| AI Overview | Intenção informacional ou de resposta directa; alto risco de zero-click |
| Featured Snippet | Query tem resposta directa dominante; tipo de snippet define formato |
| Local Pack | Intenção local forte; presença GBP importante |
| People Also Ask | Perguntas relacionadas que a página deve responder |
| Vídeos | Conteúdo explicativo/demonstrativo tem valor |
| Shopping | Intenção de compra directa |
| Notícias | Freshness importante; conteúdo editorial recente tem peso |

---

### Identificação de gaps

Após analisar top 3-5 resultados, perguntar:

- Que pergunta real fica sem resposta nos top resultados?
- Que proof point está ausente (certificações, casos, dados, processos)?
- Que formato podia ser melhor (guia completo, tabela, checklist, FAQ)?
- Que público específico está mal servido?
- Que dimensão local, sectorial ou técnica está em falta?
- Que nível de profundidade está ausente?

---

### Processo de análise

Ver procedimento detalhado na skill [`competitor-gap-analysis`](../skills/competitor-gap-analysis/SKILL.md).

Resumo:

1. Registar data, mercado, localização, dispositivo.
2. Definir queries prioritárias (com `keyword-intent`).
3. Pesquisar cada query na SERP.
4. Registar SERP features.
5. Classificar intenção dominante (com `serp-intent-audit`).
6. Analisar top 3-5 resultados.
7. Identificar padrões.
8. Identificar gaps.
9. Definir oportunidades e recomendações.
10. Persistir como record datado quando a análise for relevante.

---

## Gates

**Bloquear ou declarar limitação quando:**

- não há acesso a Browser/Search para SERP real (trabalhar com hipótese explícita);
- há dados de backlinks, tráfego ou volume sem ferramenta autorizada (não inventar);
- análise sugere copiar conteúdo de concorrentes;
- análise vai ser usada como base para página importante sem validação de `seo-qa`.

**Nunca:**

- copiar texto ou estrutura de concorrentes;
- inventar dados de backlinks, DA/DR, volume ou tráfego;
- tratar AI Overview como garantia de presença futura;
- assumir que SERP de um mercado = SERP de outro;
- assumir que SERP desktop = SERP mobile.

---

## Relação com agentes, skills e comandos

- [`serp-competitor-analyst`](../agents/serp-competitor-analyst.md) — executa análises seguindo este playbook.
- [`competitor-gap-analysis`](../skills/competitor-gap-analysis/SKILL.md) — procedimento operacional.
- [`serp-intent-audit`](../skills/serp-intent-audit/SKILL.md) — classifica intenção SERP.
- [`keyword-intent`](../agents/keyword-intent.md) — fornece queries.
- [`ai-search-visibility`](../agents/ai-search-visibility.md) — aprofunda quando AI Overviews são relevantes.
- [`content-brief`](../agents/content-brief.md) — consome análise para brief editorial.
- [`seo-qa`](../agents/seo-qa.md) — valida análise antes de usar como base para decisões.
- [`/seo competitor`](../commands/seo.md) — modo do comando SEO.

---

## Records / Persistência

Persistir como record datado quando:

- análise de concorrência cobre múltiplas queries para uma área estratégica;
- análise vai orientar criação de múltiplas páginas;
- análise é usada para decisão de arquitectura de conteúdo;
- análise será reutilizada em revisões futuras.

Records reais vivem no projeto-alvo em `.claude/records/`.  
Usar templates em [`../records-templates/`](../records-templates/README.md).

Formato de nome sugerido: `YYYY-MM-DD__competitor-research-[tema].md`.

Não guardar dados pessoais, credenciais ou informação confidencial em records.

---

## Regra final

Concorrência analisa-se para superar, não para copiar.

O valor da análise está nos gaps — no que os top resultados não têm, não fazem bem ou não respondem.

Registar sempre data e contexto. SERPs mudam. O que é verdade hoje pode não ser amanhã.
