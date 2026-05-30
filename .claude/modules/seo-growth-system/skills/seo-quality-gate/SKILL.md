---
name: seo-quality-gate
description: Procedimento reutilizavel para avaliar se uma recomendacao, entrega, alteracao ou go-live SEO pode avancar; devolve veredito, riscos, correcoes obrigatorias e proximo passo.
---

# Skill: SEO Quality Gate

Procedimento operacional de validação do **SEO Growth System**.

Esta skill é usada principalmente pelo [`seo-qa`](../../agents/seo-qa.md) para chegar a um veredito final antes de entregar, publicar, implementar ou avançar com trabalho SEO relevante.

Também pode ser usada pelo [`seo-lead`](../../agents/seo-lead.md) durante consolidação, quando precisa de uma revisão estruturada antes da entrega final.

Esta skill não é um agente.  
Esta skill não coordena subagentes.  
Esta skill não executa alterações.  
Esta skill não aprova produção, RGPD, credenciais, permissões ou rollback.  
Esta skill define o procedimento para avaliar se algo pode avançar.

---

## Objetivo

Avaliar se uma recomendação, entrega, alteração, implementação ou go-live SEO pode avançar com segurança e qualidade.

O resultado deve ser um destes:

- **Aprovado** — pode avançar.
- **Aprovado com notas** — pode avançar, mas há correções ou cuidados não bloqueantes.
- **Bloqueado** — não deve avançar.
- **Precisa de dados** — falta evidência para decidir.
- **Precisa de autorização** — há risco que exige decisão humana/Supervisor/System Safety.

---

## Quando usar

Usar antes de entregar ou avançar com trabalho SEO relevante, especialmente quando envolver:

- auditoria SEO;
- recomendação técnica;
- revisão de conteúdo;
- publicação de página;
- title, meta description, H1, headings, FAQs ou CTAs;
- internal linking;
- schema;
- local SEO;
- AI Search / GEO;
- performance / Core Web Vitals;
- WordPress SEO;
- go-live;
- alteração de slug;
- redirects;
- canonical;
- robots.txt;
- sitemap;
- noindex/nofollow;
- dados de GSC/GA4;
- recomendações que afetem indexação, tráfego, conversão, UX, performance, marca ou produção.

Usar em especial nos modos:

- `/seo qa`;
- `/seo go-live`;
- revisão final de `/seo audit`;
- revisão final de trabalhos SEO relevantes coordenados pelo `seo-lead`.

---

## Quando não usar

Não usar esta skill para:

- criar estratégia SEO;
- decidir routing;
- coordenar subagentes;
- fazer auditoria técnica de raiz;
- fazer keyword research;
- escrever conteúdo final;
- analisar concorrentes do zero;
- implementar em WordPress;
- alterar ficheiros;
- publicar;
- fazer deploy;
- aprovar produção;
- aprovar RGPD;
- aprovar credenciais;
- aprovar uso de ferramentas pagas;
- substituir o `seo-qa`;
- substituir o `seo-lead`;
- substituir o Supervisor/System Safety.

Se for necessário trabalho especializado, devolver a necessidade de routing ao `seo-lead`.

---

## Quem pode usar

Principal:

- [`seo-qa`](../../agents/seo-qa.md)

Também pode usar:

- [`seo-lead`](../../agents/seo-lead.md), durante consolidação;
- comando [`/seo`](../../commands/seo.md), nos modos `qa`, `go-live` e revisões finais;
- Supervisor, quando precisa de validação SEO estruturada.

---

## Fontes de verdade

Consultar por esta ordem:

1. [`../../agents/seo-qa.md`](../../agents/seo-qa.md)
2. [`../../agents/seo-lead.md`](../../agents/seo-lead.md)
3. [`../../commands/seo.md`](../../commands/seo.md)
4. [`../../project/QUALITY_GATE.md`](../../project/QUALITY_GATE.md)
5. [`../../project/OPERATING_SYSTEM.md`](../../project/OPERATING_SYSTEM.md)
6. [`../../project/TECHNICAL_RULES.md`](../../project/TECHNICAL_RULES.md)
7. [`../../project/CONTENT_RULES.md`](../../project/CONTENT_RULES.md)
8. [`../../project/STRATEGY_RULES.md`](../../project/STRATEGY_RULES.md)
9. [`../../project/TOOLING_MODEL.md`](../../project/TOOLING_MODEL.md)
10. [`../../project/REPORTING_MODEL.md`](../../project/REPORTING_MODEL.md)

Quando aplicável:

- [`../../project/KPI_MODEL.md`](../../project/KPI_MODEL.md)
- [`../../project/SCHEMA_ENTITY_MODEL.md`](../../project/SCHEMA_ENTITY_MODEL.md)
- [`../../project/LOCAL_SEO_PLAYBOOK.md`](../../project/LOCAL_SEO_PLAYBOOK.md)
- [`../../project/COMPETITOR_RESEARCH_PLAYBOOK.md`](../../project/COMPETITOR_RESEARCH_PLAYBOOK.md)
- [`../../records-templates/SEO_GO_LIVE_CHECKLIST.md`](../../records-templates/SEO_GO_LIVE_CHECKLIST.md)

---

## Inputs necessários

Para aplicar o gate, recolher:

- pedido original;
- objetivo de negócio;
- objetivo SEO;
- páginas/URLs afetadas;
- recomendação, entrega ou alteração a validar;
- output do `seo-lead` ou subagentes, se existir;
- evidência disponível;
- dados usados;
- dados em falta;
- ambiente: local, staging, preview, produção ou desconhecido;
- alterações propostas;
- ficheiros/configs afetados, se aplicável;
- testes feitos;
- validações pendentes;
- riscos identificados;
- autorizações existentes;
- próximo passo pretendido.

Se estes inputs não forem suficientes, não inventar.  
Classificar como **Precisa de dados** ou **Precisa de autorização**.

---

## Procedimento

### 1. Confirmar escopo

Identificar:

- o que está a ser validado;
- que tipo de trabalho é;
- quem pediu;
- quem executaria;
- páginas/URLs afetadas;
- ambiente envolvido;
- se há produção;
- se há dados reais;
- se há WordPress/admin/plugins;
- se há alteração técnica sensível;
- se há impacto em indexação, tráfego, UX, performance ou marca.

Se o escopo for desconhecido e houver risco, não aprovar.

---

### 2. Separar evidência, hipótese e recomendação

Classificar cada ponto como:

- **Evidência** — observado, testado, medido ou fornecido.
- **Hipótese** — inferência plausível sem validação completa.
- **Recomendação** — ação proposta.
- **Desconhecido** — informação ausente.
- **Bloqueio** — algo que impede avanço seguro.

Não aprovar recomendações baseadas em dados inventados.

---

### 3. Verificar utilidade para o utilizador

Perguntar:

- ajuda uma pessoa real?
- responde melhor à intenção de pesquisa?
- melhora clareza?
- melhora confiança?
- evita conteúdo genérico?
- evita manipulação de ranking?
- mantém leitura humana?

Se não ajuda o utilizador, não está pronto.

---

### 4. Verificar impacto no negócio

Perguntar:

- serve objetivo comercial real?
- ajuda conversão?
- está alinhado com serviços reais?
- não promete demais?
- não inventa capacidade, certificação, números, clientes, resultados ou garantias?
- não cria risco reputacional?

Se houver claims sem prova, bloquear ou pedir revisão humana.

---

### 5. Verificar SEO

Perguntar:

- mantém indexabilidade?
- não quebra URLs?
- não cria duplicação?
- não cria canibalização?
- não usa schema enganador?
- não depende de keyword stuffing?
- não cria conteúdo em escala sem valor?
- não cria páginas sem intenção clara?
- não entra em conflito com fundamentos de qualidade/search?
- distingue brand/non-brand quando usa dados?
- distingue dados reais de hipótese?

Se houver risco de indexação ou URLs sem plano, bloquear.

---

### 6. Verificar técnica e WordPress

Perguntar, quando aplicável:

- ambiente confirmado?
- produção envolvida?
- rollback definido?
- preview/staging validado?
- plugin/tema/fields SEO identificados?
- metadados duplicados?
- schema duplicado por plugin/tema?
- canonical correto?
- robots correto?
- sitemap correto?
- noindex/nofollow correto?
- redirects testados?
- status codes testados?
- links quebrados?
- orphan pages?
- conteúdo renderizado/indexável?
- mobile validado?
- performance afetada?
- acessibilidade básica afetada?

Se houver WordPress sensível, produção, plugin, tema ativo, slugs, redirects, canonical, robots, sitemap ou noindex sem autorização/plano, devolver **Precisa de autorização** ou **Bloqueado**.

---

### 7. Verificar conteúdo e confiança

Perguntar:

- é específico?
- é útil?
- é original?
- tem prova?
- evita texto genérico?
- não inventa factos?
- não inventa legislação?
- não inventa certificações?
- não inventa experiência, clientes, resultados ou números?
- está alinhado com tom de marca?
- precisa de revisão humana?
- envolve tema YMYL, saúde, segurança, formação ou compliance?

Se envolver claims sensíveis sem validação humana, bloquear ou pedir autorização/revisão.

---

### 8. Verificar schema e entidades

Perguntar:

- schema representa conteúdo visível?
- dados vêm de fonte real?
- não inventa reviews?
- não inventa ratings?
- não inventa preços?
- não duplica plugin/tema?
- tipos escolhidos fazem sentido?
- propriedades obrigatórias existem?
- `sameAs` aponta apenas para perfis oficiais?
- validação Rich Results/Schema.org foi feita ou está pendente?

Schema enganador deve ser bloqueado.

---

### 9. Verificar local SEO

Quando aplicável, perguntar:

- existe presença/intenção local real?
- NAP é consistente?
- áreas de serviço são reais?
- páginas locais são justificadas?
- não há doorway pages?
- não há moradas/zonas inventadas?
- GBP não é alterado sem autorização?
- schema LocalBusiness é coerente?

Páginas locais vazias ou inventadas devem ser bloqueadas.

---

### 10. Verificar performance, mobile e acessibilidade

Perguntar:

- LCP, INP e CLS foram considerados?
- mobile foi validado?
- imagens estão otimizadas?
- fontes pesam demasiado?
- JS/CSS afeta renderização?
- animações prejudicam performance?
- recomendação prejudica UX?
- acessibilidade básica é preservada?
- dados são lab, field ou hipótese?

Não aprovar SEO que melhora texto mas destrói performance, mobile ou acessibilidade.

---

### 11. Verificar AI Search / GEO

Perguntar:

- segue fundamentos SEO normais?
- conteúdo importante está visível?
- respostas são claras e citáveis?
- entidades são consistentes?
- schema ajuda sem manipular?
- não usa truques?
- não promete presença em AI Overviews?
- não cria conteúdo massificado só para IA?

AI Search readiness é SEO bem feito, não atalho separado.

---

### 12. Verificar governance

Perguntar:

- está dentro do escopo?
- precisa de dados reais?
- precisa de autorização?
- precisa de revisão humana?
- precisa de handoff?
- precisa de record persistente?
- precisa de rollback?
- precisa de validação pós-publicação?
- envolve produção, credenciais, dados pessoais, dados sensíveis ou ferramentas pagas?

Quando houver risco de segurança, RGPD, produção, rollback, credenciais ou permissões, o gate não aprova sozinho. Encaminha para Supervisor/System Safety.

---

## Severidade

Classificar problemas como:

- **Crítico** — bloqueia avanço.
- **Alto** — deve bloquear salvo autorização explícita.
- **Médio** — pode avançar apenas com plano de correção.
- **Baixo** — melhoria ou nota não bloqueante.
- **Informativo** — observação.

Exemplos de problemas críticos:

- produção sem autorização;
- credenciais expostas;
- dados pessoais/sensíveis sem autorização;
- alteração de slug sem redirect;
- noindex indevido;
- robots a bloquear páginas importantes;
- canonical errado em página crítica;
- schema enganador;
- conteúdo com claims inventados;
- go-live sem rollback;
- recomendação baseada em dados inventados.

---

## Decisão

### Aprovado

Usar quando:

- há evidência suficiente;
- não há bloqueios;
- riscos são baixos ou controlados;
- validação necessária foi feita;
- próximo passo é seguro.

### Aprovado com notas

Usar quando:

- há pequenas melhorias pendentes;
- risco residual é aceitável;
- correções não bloqueiam avanço;
- há próximo passo claro.

### Bloqueado

Usar quando:

- existe risco crítico;
- há erro que pode prejudicar indexação, produção, dados, marca, UX ou performance;
- há conteúdo enganador;
- há schema enganador;
- há alteração sensível sem plano;
- há recomendação baseada em dados inventados.

### Precisa de dados

Usar quando:

- falta evidência;
- falta GSC/GA4/SERP/crawl/teste;
- falta URL/página concreta;
- falta output do subagente certo;
- não foi possível validar.

### Precisa de autorização

Usar quando:

- envolve produção;
- envolve WordPress sensível;
- envolve dados pessoais/sensíveis;
- envolve credenciais;
- envolve ferramentas pagas;
- envolve GBP;
- envolve slugs/redirects/canonical/robots/sitemap/noindex;
- envolve deploy/go-live;
- envolve rollback ou decisão humana.

---

## Output esperado

Usar este formato:

```md
## SEO Quality Gate

Resultado: [Aprovado / Aprovado com notas / Bloqueado / Precisa de dados / Precisa de autorização]

### 1. Escopo validado
[o que foi validado]

### 2. Evidência usada
[dados, URLs, testes, outputs ou documentos usados]

### 3. O que está bom
[pontos que passam no gate]

### 4. Problemas encontrados
| Área | Problema | Evidência | Severidade | Correção obrigatória |
|---|---|---|---|---|

### 5. Riscos
[risco técnico, conteúdo, WordPress, produção, dados, marca, performance, UX, indexação]

### 6. Correções obrigatórias
[lista objetiva]

### 7. Não validado / a confirmar
[o que não foi possível confirmar]

### 8. Risco residual
[o que continua a existir mesmo depois das correções]

### 9. Precisa de autorização?
[sim/não + porquê]

### 10. Próximo passo
[o que o seo-lead, seo-qa, supervisor ou agente executor deve fazer]
```

---

## Validation honesty

Nunca dizer que algo foi validado se não foi.

Usar explicitamente:

- “Validado com evidência”
- “Validado parcialmente”
- “Não validado”
- “A confirmar”
- “Depende de dados não fornecidos”
- “Depende de autorização”
- “Hipótese, não evidência”

Se uma ferramenta não estava disponível, dizer.  
Se uma URL não foi testada, dizer.  
Se não houve GSC/GA4, não inventar métricas.  
Se não houve crawl, não afirmar que a parte técnica está limpa.  
Se não houve acesso ao WordPress, não afirmar que a implementação está correta.

---

## Gates de segurança

Read-only por defeito.

Esta skill deve bloquear ou pedir autorização quando houver:

- produção;
- deploy;
- go-live;
- credenciais;
- tokens;
- cookies;
- API keys;
- dados pessoais;
- dados de trabalhadores;
- dados de saúde;
- documentos sensíveis;
- Search Console com dados reais;
- GA4 com dados reais;
- Google Business Profile;
- WordPress admin;
- plugins;
- tema ativo;
- base de dados;
- slugs;
- redirects;
- canonical;
- robots.txt;
- sitemap.xml;
- noindex/nofollow;
- schema global;
- tracking scripts;
- ferramentas pagas;
- instalação de dependências.

Esta skill não concede autorização.  
Apenas identifica a necessidade de autorização e encaminha para o agente/área correta.

---

## Relação com outros componentes

### `seo-qa`

Utilizador principal desta skill. Usa o procedimento para chegar ao veredito final.

### `seo-lead`

Usa o resultado do gate para consolidar e entregar ao utilizador/Supervisor.

### `/seo`

Usa esta skill em modos de QA, go-live e revisões finais de trabalhos relevantes.

### `QUALITY_GATE.md`

Fonte principal das regras de aprovação.

### Subagentes especialistas

Se a skill detetar falta de análise especializada, deve indicar que o `seo-lead` deve encaminhar para o subagente certo.

Exemplos:

- falta técnica → `technical-seo`;
- falta conteúdo → `content-growth`;
- falta on-page → `onpage-seo`;
- falta schema → `schema-entity`;
- falta performance → `cwv-performance-seo`;
- falta dados → `seo-data-analyst`;
- falta implementação → `wordpress-seo-implementation`.

### Supervisor/System Safety

Entram quando houver produção, dados, credenciais, permissões, RGPD, rollback, ferramentas pagas ou risco crítico.

---

## Exemplos de pedidos que aceita

- “Aplica o quality gate a esta recomendação.”
- “Valida este output antes da entrega.”
- “Revê se esta página pode ser publicada.”
- “Diz se este schema pode avançar.”
- “Valida este plano de redirects.”
- “Faz QA antes do go-live.”
- “Verifica se esta recomendação SEO tem riscos.”
- “Classifica esta entrega: aprovado, bloqueado ou precisa de dados.”
- “Revê se este conteúdo tem claims perigosos.”
- “Confirma se esta alteração precisa de autorização.”

---

## Exemplos de pedidos que deve recusar ou encaminhar

Encaminhar para `seo-lead`:

- “Define a estratégia SEO.”
- “Escolhe os subagentes.”
- “Organiza a auditoria completa.”
- “Prioriza todo o roadmap.”

Encaminhar para subagente especialista:

- “Faz auditoria técnica de raiz.”
- “Escreve o conteúdo final.”
- “Cria schema completo.”
- “Faz keyword research.”
- “Analisa concorrentes.”
- “Diagnostica Core Web Vitals profundamente.”
- “Implementa no WordPress.”

Encaminhar para Supervisor/System Safety:

- “Aprova produção.”
- “Usa credenciais.”
- “Ignora rollback.”
- “Lê dados pessoais.”
- “Usa ferramenta paga sem autorização.”
- “Mexe no Google Business Profile.”
- “Altera slugs sem plano.”
- “Remove noindex agora.”

---

## Erros comuns a evitar

- Aprovar sem evidência.
- Aprovar produção sem autorização.
- Aprovar alteração de URL sem redirect plan.
- Aprovar schema enganador.
- Aprovar conteúdo genérico.
- Aprovar claims inventados.
- Aprovar SEO que prejudica UX.
- Aprovar SEO que prejudica performance.
- Aprovar SEO que prejudica acessibilidade.
- Aprovar recomendações baseadas em métricas inventadas.
- Dizer “validado” quando foi apenas revisto teoricamente.
- Substituir o `seo-qa`.
- Substituir o `seo-lead`.
- Substituir Supervisor/System Safety.

---

## Regra final

Esta skill existe para tornar a validação SEO consistente.

Se está bom, aprova.  
Se está quase bom, aprova com notas.  
Se está perigoso, bloqueia.  
Se faltam dados, pede dados.  
Se exige decisão humana, pede autorização.

Qualidade SEO não é só ranking.  
Só deve avançar o que melhora o utilizador, o negócio, a indexação, a confiança, a performance, a acessibilidade, a marca e a segurança do projeto.