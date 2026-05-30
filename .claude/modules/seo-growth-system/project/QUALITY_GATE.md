# SEO Quality Gate

Fonte de verdade do **quality gate** do `seo-growth-system`.

Este ficheiro define o standard mínimo para aprovar, bloquear, pedir dados ou pedir autorização antes de entregar, publicar, implementar ou avançar com trabalho SEO relevante.

Este ficheiro não executa validação passo a passo.
A execução operacional vive na skill [`seo-quality-gate`](../skills/seo-quality-gate/SKILL.md).
O veredito final é dado pelo agente [`seo-qa`](../agents/seo-qa.md).
A coordenação do trabalho pertence ao [`seo-lead`](../agents/seo-lead.md).
Produção, RGPD, credenciais, permissões, rollback e decisões críticas pertencem ao Supervisor/System Safety.

---

## Objetivo

Garantir que qualquer trabalho SEO relevante só avança quando melhora o utilizador, o negócio, a indexação, a confiança, a performance, a acessibilidade, a marca e a segurança do projeto.

O gate existe para impedir:

* recomendações sem evidência;
* conteúdo genérico;
* claims inventados;
* alterações técnicas perigosas;
* schema enganador;
* problemas de indexação;
* degradação de UX/performance/acessibilidade;
* alterações WordPress sem plano;
* go-live sem validação;
* produção sem autorização;
* decisões com dados, credenciais ou RGPD fora do escopo.

---

## Quando usar

Usar antes de entregar, publicar, implementar ou avançar com trabalho SEO relevante.

Usar especialmente em:

* auditorias SEO;
* recomendações técnicas;
* conteúdo importante;
* páginas de serviço;
* on-page SEO;
* internal linking;
* schema;
* local SEO;
* AI Search / GEO;
* performance / Core Web Vitals;
* WordPress SEO;
* alterações de slug;
* redirects;
* canonical;
* robots.txt;
* sitemap;
* noindex/nofollow;
* go-live;
* análises com dados de GSC/GA4;
* recomendações com impacto em indexação, tráfego, conversão, UX, performance, marca ou produção.

Usar sempre nos fluxos:

* `/seo qa`;
* `/seo go-live`;
* revisão final de `/seo audit`;
* revisão final de trabalhos SEO relevantes coordenados pelo `seo-lead`.

---

## Quando não usar

Não usar este ficheiro para substituir:

* o `seo-lead`;
* o `seo-qa`;
* a skill `seo-quality-gate`;
* o Supervisor/System Safety;
* WordPress Engineering;
* Visual Experience;
* subagentes especialistas.

Este ficheiro não decide routing.
Este ficheiro não executa alterações.
Este ficheiro não publica.
Este ficheiro não faz deploy.
Este ficheiro não autoriza produção.
Este ficheiro não autoriza RGPD.
Este ficheiro não autoriza credenciais.
Este ficheiro não define rollback.
Este ficheiro não substitui validação humana quando ela é necessária.

---

## Responsabilidades por componente

### `QUALITY_GATE.md`

Define o standard oficial de qualidade e aprovação.

### `seo-quality-gate`

Aplica este standard como procedimento operacional reutilizável.

### `seo-qa`

Executa a validação final e devolve o veredito.

### `seo-lead`

Coordena o trabalho SEO, recebe o resultado do QA e consolida a entrega final.

### `/seo`

Orquestra o fluxo por modo e chama QA quando necessário.

### Supervisor/System Safety

Decide segurança, RGPD, produção, credenciais, permissões, rollback, dados sensíveis e risco crítico.

---

## Resultados possíveis

### Aprovado

Usar quando:

* há evidência suficiente;
* não há bloqueios;
* riscos são baixos ou controlados;
* a validação necessária foi feita;
* o próximo passo é seguro;
* não há dependência de autorização crítica.

### Aprovado com notas

Usar quando:

* o trabalho pode avançar;
* existem melhorias não bloqueantes;
* o risco residual é aceitável;
* há plano claro para correções menores;
* não existe risco crítico.

### Bloqueado

Usar quando:

* existe risco crítico;
* a recomendação pode prejudicar indexação, produção, dados, UX, performance, acessibilidade, marca ou confiança;
* há conteúdo enganador;
* há schema enganador;
* há alteração técnica sensível sem plano;
* há go-live sem validação suficiente;
* há dados inventados;
* há claims sem prova;
* há risco que não deve avançar mesmo com notas.

### Precisa de dados

Usar quando:

* falta evidência;
* falta URL ou página concreta;
* falta output de subagente especialista;
* falta GSC/GA4/SERP/crawl/teste;
* falta validação técnica;
* falta validação de conteúdo;
* falta validação de performance;
* falta confirmação de ambiente;
* não é possível distinguir hipótese de evidência.

### Precisa de autorização

Usar quando:

* envolve produção;
* envolve WordPress sensível;
* envolve dados pessoais;
* envolve dados sensíveis;
* envolve credenciais;
* envolve permissões;
* envolve ferramentas pagas;
* envolve Google Business Profile;
* envolve slugs, redirects, canonical, robots, sitemap ou noindex;
* envolve deploy/go-live;
* envolve rollback ou decisão humana;
* envolve risco fora do escopo SEO.

---

## Critérios obrigatórios

### 1. Utilizador

O trabalho deve:

* ajudar uma pessoa real;
* responder melhor à intenção;
* melhorar clareza;
* melhorar confiança;
* manter leitura humana;
* evitar conteúdo genérico;
* evitar manipulação de ranking.

Bloquear ou pedir correção quando:

* o conteúdo não ajuda;
* a página existe só para keyword;
* a recomendação piora a experiência;
* a intenção de pesquisa não está clara.

---

### 2. Negócio

O trabalho deve:

* servir objetivo comercial real;
* ajudar conversão;
* estar alinhado com serviços reais;
* respeitar marca;
* não prometer demais;
* não criar risco reputacional.

Bloquear ou pedir correção quando:

* inventa serviços;
* inventa certificações;
* inventa clientes;
* inventa números;
* inventa resultados;
* inventa garantias;
* cria promessa forte sem prova;
* pode induzir o utilizador em erro.

---

### 3. SEO

O trabalho deve:

* manter indexabilidade;
* preservar URLs importantes;
* evitar duplicação;
* evitar canibalização;
* evitar keyword stuffing;
* evitar conteúdo em escala sem valor;
* usar schema honesto;
* melhorar arquitetura, descoberta ou relevância;
* distinguir evidência, hipótese e recomendação.

Bloquear ou pedir correção quando:

* altera URL sem redirect plan;
* cria páginas sem intenção clara;
* cria páginas locais vazias;
* cria duplicação;
* usa schema enganador;
* tenta manipular motores de pesquisa;
* depende de métricas inventadas;
* assume rankings ou volumes sem dados.

---

### 4. Técnica / WordPress

O trabalho deve:

* respeitar ambiente;
* preservar indexação;
* preservar performance;
* preservar mobile;
* preservar acessibilidade;
* evitar alterações sensíveis sem plano;
* ter rollback quando necessário;
* validar implementação antes de go-live.

Bloquear ou pedir autorização quando envolver:

* produção;
* tema ativo;
* plugin SEO;
* slugs;
* redirects;
* canonical;
* robots.txt;
* sitemap.xml;
* noindex/nofollow;
* schema global;
* tracking scripts;
* base de dados;
* deploy;
* instalação de plugin;
* instalação de dependência;
* alteração WordPress sem ambiente seguro.

---

### 5. Conteúdo

O conteúdo deve ser:

* específico;
* útil;
* original;
* factual;
* claro;
* alinhado com a marca;
* baseado em prova;
* revisto quando necessário;
* seguro em temas sensíveis.

Bloquear ou pedir revisão humana quando:

* inventa factos;
* inventa legislação;
* inventa certificações;
* inventa números;
* faz claims médicos, legais ou técnicos sem validação;
* aborda temas YMYL sem cuidado;
* é genérico;
* copia concorrentes;
* promete resultados não garantíveis.

---

### 6. Schema e entidades

Schema deve:

* representar conteúdo visível;
* usar dados reais;
* evitar duplicação por plugin/tema;
* usar tipos adequados;
* ter propriedades obrigatórias quando aplicável;
* usar `sameAs` apenas para perfis oficiais;
* ser validado quando possível.

Bloquear quando:

* marca conteúdo invisível;
* inventa reviews;
* inventa ratings;
* inventa preços;
* inventa moradas;
* inventa serviços;
* duplica schema de forma perigosa;
* usa tipo inadequado para manipular rich results.

---

### 7. Local SEO

Local SEO deve:

* refletir presença ou área de serviço real;
* manter NAP consistente;
* evitar páginas locais vazias;
* evitar doorway pages;
* alinhar website, GBP e schema;
* respeitar autorização para alterações externas.

Bloquear ou pedir autorização quando:

* inventa moradas;
* inventa áreas servidas;
* cria páginas locais sem conteúdo útil;
* altera Google Business Profile sem autorização;
* cria LocalBusiness schema sem base real.

---

### 8. Performance / Mobile / Acessibilidade

O trabalho não deve prejudicar:

* LCP;
* INP;
* CLS;
* mobile;
* acessibilidade básica;
* renderização;
* navegação;
* clareza visual;
* experiência do utilizador.

Bloquear ou pedir correção quando:

* adiciona peso desnecessário;
* esconde conteúdo crítico;
* prejudica mobile;
* prejudica acessibilidade;
* adiciona JS/CSS sem necessidade;
* usa animações que prejudicam performance;
* melhora texto mas piora UX.

---

### 9. AI Search / GEO

AI Search readiness deve seguir SEO bem feito.

O trabalho deve:

* ter conteúdo original;
* ter respostas claras;
* manter texto importante visível;
* reforçar entidades reais;
* usar schema correto;
* melhorar citabilidade;
* não prejudicar pessoas para agradar bots.

Bloquear quando:

* promete presença em AI Overviews;
* cria conteúdo massificado para IA;
* inventa mentions;
* inventa entidades;
* usa schema artificial;
* cria páginas fracas só para capturar respostas generativas.

---

### 10. Governance

Antes de avançar, confirmar:

* está dentro do escopo?
* há evidência suficiente?
* precisa de dados reais?
* precisa de autorização?
* precisa de revisão humana?
* precisa de handoff?
* precisa de record?
* precisa de rollback?
* precisa de validação pós-publicação?
* há risco para produção?
* há risco para dados?
* há risco para credenciais?
* há risco para permissões?

Quando houver dúvida séria, não aprovar como se estivesse validado.

---

## Severidade

Classificar problemas como:

### Crítico

Bloqueia avanço.

Exemplos:

* produção sem autorização;
* credenciais expostas;
* dados pessoais/sensíveis sem autorização;
* alteração de slug sem redirect;
* noindex indevido;
* robots a bloquear páginas importantes;
* canonical errado em página crítica;
* schema enganador;
* conteúdo com claims inventados;
* go-live sem rollback;
* recomendação baseada em dados inventados.

### Alto

Deve bloquear salvo autorização explícita ou plano de correção aprovado.

Exemplos:

* performance mobile degradada;
* conteúdo importante sem revisão;
* alteração técnica sem validação suficiente;
* internal linking que cria confusão;
* schema incompleto em página crítica;
* redirects não testados.

### Médio

Pode avançar apenas com plano de correção.

Exemplos:

* title/meta melhoráveis;
* headings pouco claros;
* links internos insuficientes;
* falta de prova complementar;
* melhoria de CTA pendente.

### Baixo

Não bloqueia, mas deve ser registado como melhoria.

Exemplos:

* copy ajustável;
* pequenas melhorias de legibilidade;
* oportunidade adicional de FAQ;
* alt text melhorável em imagem secundária.

### Informativo

Observação sem impacto direto.

---

## Gates de segurança

Read-only por defeito.

O SEO Growth System não deve aprovar sozinho:

* produção;
* deploy;
* go-live;
* credenciais;
* tokens;
* cookies;
* API keys;
* dados pessoais;
* dados de trabalhadores;
* dados de saúde;
* documentos sensíveis;
* Search Console com dados reais;
* GA4 com dados reais;
* Google Business Profile;
* WordPress admin;
* plugins;
* tema ativo;
* base de dados;
* slugs;
* redirects;
* canonical;
* robots.txt;
* sitemap.xml;
* noindex/nofollow;
* schema global;
* tracking scripts;
* ferramentas pagas;
* instalação de dependências.

Nestes casos, o resultado deve ser **Precisa de autorização** ou **Bloqueado**, conforme o risco.

---

## Validation honesty

Nunca declarar como validado algo que não foi testado.

Usar linguagem explícita:

* “Validado com evidência”
* “Validado parcialmente”
* “Não validado”
* “A confirmar”
* “Depende de dados não fornecidos”
* “Depende de autorização”
* “Hipótese, não evidência”

Se não houve crawl, não afirmar que a técnica está limpa.

Se não houve GSC/GA4, não inventar métricas.

Se não houve SERP real, não afirmar intenção dominante como facto.

Se não houve PageSpeed/CrUX/Lighthouse, não afirmar performance como validada.

Se não houve acesso ao WordPress, não afirmar implementação como correta.

Se não houve autorização, não tratar risco como aprovado.

---

## Formato de veredito recomendado

O `seo-qa` e a skill `seo-quality-gate` devem devolver:

```md
## SEO Quality Gate

Resultado: [Aprovado / Aprovado com notas / Bloqueado / Precisa de dados / Precisa de autorização]

### Escopo validado
[...]

### Evidência usada
[...]

### O que está bom
[...]

### Problemas encontrados
| Área | Problema | Evidência | Severidade | Correção obrigatória |
|---|---|---|---|---|

### Riscos
[...]

### Correções obrigatórias
[...]

### Não validado / a confirmar
[...]

### Risco residual
[...]

### Precisa de autorização?
[...]

### Próximo passo
[...]
```

---

## Go-live SEO

Antes de go-live SEO, o gate deve confirmar:

* ambiente confirmado;
* preview/staging validado;
* rollback definido;
* autorização explícita;
* páginas importantes em status 200;
* robots correto;
* sitemap correto;
* canonical correto;
* noindex/nofollow correto;
* redirects testados;
* internal links rastreáveis;
* conteúdo visível/indexável;
* schema validado;
* mobile validado;
* performance considerada;
* acessibilidade básica considerada;
* plano pós-go-live para GSC/GA4/URL Inspection;
* record/checklist preparado quando aplicável.

Sem estes pontos, o resultado deve ser **Bloqueado**, **Precisa de dados** ou **Precisa de autorização**.

---

## Records e persistência

Quando o trabalho for relevante ou tiver impacto duradouro, verificar se precisa de record.

Exemplos:

* auditoria SEO;
* go-live;
* decisão de URL;
* decisão de schema;
* decisão de arquitetura;
* plano de redirects;
* análise de concorrência;
* content gap;
* AI Search review;
* local SEO review;
* performance review;
* plano 30/60/90 dias.

Records reais vivem no projeto-alvo em `.claude/records/`.

Não guardar dados pessoais, dados sensíveis, credenciais ou informação confidencial desnecessária em records.

---

## Relação com outros ficheiros

* [`seo-lead.md`](../agents/seo-lead.md) — coordena e consolida.
* [`seo-qa.md`](../agents/seo-qa.md) — aplica o gate e dá veredito final.
* [`seo-quality-gate`](../skills/seo-quality-gate/SKILL.md) — procedimento operacional do gate.
* [`commands/seo.md`](../commands/seo.md) — chama QA nos modos relevantes.
* [`TECHNICAL_RULES.md`](TECHNICAL_RULES.md) — detalhe técnico.
* [`CONTENT_RULES.md`](CONTENT_RULES.md) — detalhe de conteúdo.
* [`STRATEGY_RULES.md`](STRATEGY_RULES.md) — estratégia, intenção e arquitetura.
* [`TOOLING_MODEL.md`](TOOLING_MODEL.md) — ferramentas, permissões e limites.
* [`REPORTING_MODEL.md`](REPORTING_MODEL.md) — persistência e records.
* [`SEO_GO_LIVE_CHECKLIST.md`](../records-templates/SEO_GO_LIVE_CHECKLIST.md) — checklist de go-live.

---

## Regra final

Se melhora ranking mas prejudica o utilizador, não está pronto.

Se melhora SEO mas prejudica confiança, não está pronto.

Se melhora conteúdo mas prejudica performance, não está pronto.

Se melhora técnica mas cria risco de produção, não está pronto.

Se parece correto mas não foi validado, não está aprovado.

SEO excelente só avança quando é útil, verdadeiro, seguro, rastreável, indexável, rápido, acessível, confiável, alinhado com o negócio e validado com honestidade.
