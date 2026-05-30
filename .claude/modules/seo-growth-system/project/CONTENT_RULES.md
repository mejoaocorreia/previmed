# Content Growth Rules

Fonte de verdade de conteúdo do **SEO Growth System**.

Este ficheiro define os standards de qualidade para conteúdo SEO — o que torna uma página útil, confiável e relevante, como estruturar páginas de serviço, como tratar claims e compliance, e quando exigir revisão humana.

Este ficheiro não é um agente.  
Este ficheiro não executa alterações.  
Este ficheiro não substitui o `content-growth`, o `seo-qa`, a skill `content-brief-generation` nem o Supervisor/System Safety.

---

## Objetivo

Garantir que qualquer conteúdo SEO publicado ajuda uma pessoa real a entender, decidir e confiar — não existe apenas porque uma keyword existe.

Todo o conteúdo deve responder:

- Para quem é?
- Que problema ou necessidade resolve?
- Que serviço ou informação oferece?
- Porque deve o utilizador confiar?
- Que prova existe?
- O que diferencia esta página de qualquer outra?
- Qual é o próximo passo para o utilizador?
- Que perguntas reais responde?
- Que intenção de pesquisa satisfaz?

---

## Âmbito

Este documento cobre as regras para:

- páginas de serviço, subserviço e setor;
- conteúdo institucional (sobre a empresa, equipa, valores);
- guias educativos e conteúdo informacional;
- FAQs estratégicas;
- conteúdo para AI Search / GEO;
- refresh de conteúdo existente;
- conteúdo AI-assistido;
- claims e compliance;
- estrutura de página;
- E-E-A-T e confiança.

---

## Fora de âmbito

Este documento não cobre:

- keyword research e intenção de pesquisa — ver `STRATEGY_RULES.md`;
- SEO técnico de páginas (canonical, robots, schema técnico) — ver `TECHNICAL_RULES.md`;
- schema semântico (modelação de entidades) — ver `SCHEMA_ENTITY_MODEL.md`;
- local SEO e GBP — ver `LOCAL_SEO_PLAYBOOK.md`;
- ferramentas e autorização — ver `TOOLING_MODEL.md`;
- métricas e KPIs — ver `KPI_MODEL.md`.

---

## Responsabilidades por componente

| Componente | Responsabilidade |
|---|---|
| `CONTENT_RULES.md` (este ficheiro) | Standard e regras de conteúdo |
| [`content-growth`](../agents/content-growth.md) | Avaliação, estrutura e melhoria de conteúdo |
| [`content-brief`](../agents/content-brief.md) | Brief editorial para criar ou reescrever páginas |
| [`onpage-seo`](../agents/onpage-seo.md) | Optimização on-page mecânica (titles, metas, headings) |
| [`ai-search-visibility`](../agents/ai-search-visibility.md) | Citabilidade e perguntas-alvo para AI Search |
| [`seo-qa`](../agents/seo-qa.md) | Validação final de conteúdo antes de publicação |
| Supervisor/System Safety | Autorização de publicação em produção e conteúdo sensível |

---

## Standards e regras

### Critérios obrigatórios de qualidade

Para qualquer página importante, verificar:

**Utilidade:**
- Ajuda uma pessoa real a resolver um problema ou tomar uma decisão?
- O conteúdo é específico para esta empresa ou podia ser de qualquer uma?
- Responde às perguntas reais que o utilizador tem?

**Especificidade:**
- Menciona o serviço concreto que a empresa oferece?
- Usa termos precisos em vez de linguagem vaga?
- Evita "soluções inteligentes", "serviço de qualidade" e equivalentes genéricos?

**Originalidade:**
- É diferente do que qualquer concorrente publicaria?
- Tem perspectiva, experiência ou dados próprios?
- Não copia estrutura ou texto de concorrentes?

**Prova e confiança:**
- Há evidência de que a empresa faz isto (certificações reais, processos, cases)?
- Há informação verificável sobre quem está por trás (equipa, credenciais, anos de experiência reais)?
- Os números e estatísticas têm fonte?

---

### E-E-A-T e confiança

Para temas de saúde, segurança, formação, compliance, medicina, financeiro e legal (YMYL), a confiança é crítica.

Incluir quando possível e quando for real:

- identidade clara da empresa (nome, morada, contacto);
- experiência demonstrada (anos de actividade, casos reais, processos);
- especialização comprovada (certificações reais, metodologias, equipa);
- autoridade reconhecida (parceiros, entidades reguladoras, reconhecimentos);
- revisão humana em claims sensíveis;
- fontes oficiais quando citadas;
- linguagem precisa e verificável;
- CTA claro que não engana.

**Não inventar:**

- certificações que não existem;
- anos de experiência inflacionados;
- clientes não confirmados;
- resultados garantidos;
- legislação ou normas incorrectas;
- garantias que a empresa não pode cumprir;
- números sem fonte real.

---

### Estrutura padrão de página de serviço

Modelo recomendado (adaptar à realidade de cada serviço):

1. **H1 claro** — alinhado com a keyword principal e a intenção.
2. **Proposta de valor acima do fold** — porquê este serviço, para quem, que resultado.
3. **Problema ou necessidade** — que problema o cliente tem que este serviço resolve.
4. **Serviço explicado** — o que é exactamente, como funciona, o que inclui.
5. **Como funciona** — processo claro e específico (não vago).
6. **Benefícios concretos** — o que o cliente ganha (não "benefícios genéricos").
7. **Prova e confiança** — certificações, parceiros, números reais, cases.
8. **FAQs** — perguntas reais que clientes fazem, com respostas específicas.
9. **Links internos** — para serviços relacionados, guias, contacto.
10. **CTA** — claro, natural, sem pressão excessiva.

---

### FAQs

FAQs boas respondem a perguntas que clientes realmente fazem.

FAQs más são perguntas de marketing disfarçadas ("Porque escolher-nos?").

Verificar:

- a pergunta é real? Um cliente perguntaria isto?
- a resposta é específica e útil?
- a resposta não é evasiva ou genérica?
- há schema FAQPage associado? (apenas se as FAQs são visíveis no HTML)

---

### Conteúdo AI-assistido

**Permitido quando:**

- foi revisto por humano antes de publicar;
- é útil e factual;
- está adaptado à marca e à realidade da empresa;
- não é massificado (não são 50 páginas iguais com slug diferente);
- não copia a estrutura de concorrentes;
- foi validado com `seo-qa` antes de publicar.

**Não permitido:**

- conteúdo automático em escala sem revisão;
- paráfrases de concorrentes;
- páginas quase iguais para capturar variações de keyword;
- texto genérico que podia ser de qualquer empresa;
- conteúdo criado para manipular ranking ou AI Overviews;
- factos inventados ou não verificados.

---

### Claims e compliance

Bloquear ou exigir revisão humana quando o conteúdo:

- faz promessa forte de resultado ("garantimos X", "100% de sucesso");
- menciona obrigações legais ou regulatórias (verificar se é correcto e actual);
- toca em saúde, medicina, medicina do trabalho, segurança;
- menciona certificações, acreditações, parcerias (verificar se são reais);
- compara directamente com concorrentes;
- usa números ou estatísticas sem fonte;
- pode induzir o utilizador em erro sobre o serviço;
- aborda formação certificada (verificar se é reconhecida pela entidade competente);
- aborda área financeira ou jurídica.

**Critério de decisão:** se a empresa não consegue fornecer prova do claim, o claim não deve estar na página.

---

### Conteúdo para AI Search / GEO

AI Search readiness é SEO bem feito, não uma camada separada.

Preparar para AI Search significa:

- conteúdo original, específico e verificável;
- respostas claras a perguntas directas;
- texto importante visível (não escondido em JS, tabs ou accordions);
- blocos citáveis: definição, processo, lista, comparação, FAQ, resumo;
- entidade da empresa consistente;
- internal linking claro;
- schema correto quando aplicável.

**Não fazer para "AI Search":**

- criar conteúdo massificado só para capturar AI Overviews;
- inventar entidades ou mentions;
- usar schema artificial;
- criar páginas fracas só para aparecer em respostas generativas;
- prometer presença em AI Overviews.

---

## Processo

### Content lifecycle

```
Brief → draft → revisão de intenção → revisão de confiança/compliance
→ revisão visual/UX → revisão SEO técnica → aprovação humana
→ publicação segura → medição → refresh quando necessário
```

Cada fase deve estar completa antes da seguinte.  
Conteúdo sensível (YMYL) exige aprovação humana explícita antes de publicar.

---

### Refresh

Rever conteúdo quando:

- dados de GSC mostram queda de impressões ou clicks;
- CTR cai com impressões estáveis (title/meta ou relevância);
- conteúdo está desactualizado (serviço mudou, legislação mudou, dados envelheceram);
- concorrentes melhoraram significativamente;
- AI/Search mudou a forma de apresentar respostas para a query;
- tráfego existe mas conversão é baixa.

**Regra de refresh:**

- manter URL estável quando possível;
- não alterar slug sem plano de redirect 301;
- manter e enriquecer o que está bom;
- actualizar ou remover o que está desactualizado;
- validar com `seo-qa` antes de publicar.

---

## Gates

**Bloquear ou exigir revisão humana** quando:

- conteúdo faz promessa forte sem prova;
- menciona obrigações legais, de saúde ou segurança sem verificação;
- usa certificações não confirmadas;
- usa números sem fonte;
- foi gerado por AI sem revisão humana;
- toca em tema YMYL sem especialista;
- pode ser enganoso para o utilizador.

**Bloquear publicação** quando:

- conteúdo está abaixo do standard de qualidade desta secção;
- claims não foram verificados;
- revisão humana obrigatória não foi feita;
- publicação em produção sem autorização explícita.

---

## Relação com agentes, skills e comandos

- [`content-growth`](../agents/content-growth.md) — avalia e melhora conteúdo segundo estas regras.
- [`content-brief`](../agents/content-brief.md) — cria briefs que respeitam estas regras.
- [`content-brief-generation`](../skills/content-brief-generation/SKILL.md) — procedimento de brief.
- [`onpage-seo`](../agents/onpage-seo.md) — optimiza on-page dentro destes standards.
- [`onpage-optimization-pass`](../skills/onpage-optimization-pass/SKILL.md) — procedimento de on-page.
- [`ai-search-visibility`](../agents/ai-search-visibility.md) — avalia citabilidade e perguntas-alvo.
- [`seo-qa`](../agents/seo-qa.md) — valida conteúdo antes de publicação.
- [`STRATEGY_RULES.md`](STRATEGY_RULES.md) — intenção, arquitetura e AI Search.
- [`/seo content`](../commands/seo.md) — modo do comando SEO para conteúdo.
- [`/seo brief`](../commands/seo.md) — modo do comando para brief editorial.

---

## Records / Persistência

Recomendar record quando houver:

- revisão de conteúdo importante (página de serviço, guia estratégico);
- decisão sobre conteúdo a criar ou remover;
- content gap analysis;
- refresh de conteúdo com impacto em tráfego;
- decisão sobre claims ou compliance.

Records reais vivem no projeto-alvo em `.claude/records/`.  
Usar templates em [`../records-templates/`](../records-templates/README.md).

Não guardar dados pessoais, credenciais ou informação confidencial em records.

---

## Regra final

Conteúdo bom serve pessoas, não bots.

Uma página que existe só para capturar uma keyword, sem valor real para quem a visita, não está pronta.

Uma página com claims não verificados, legislação inventada ou certificações falsas é um risco para a empresa e para o utilizador.

O standard é simples: se um cliente real chegasse a esta página, ficaria mais informado, mais confiante e mais perto de decidir?

Se a resposta for não — o conteúdo não está pronto.
