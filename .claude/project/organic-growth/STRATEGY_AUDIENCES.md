# Strategy — Audiências e Jornadas

> Lote 1.1 da Fase 1 — Estratégia greenfield.
> Última atualização: 2026-05-19.
> Autor: SEO Lead.
> Base: `PROJECT_CONTEXT.md` + análise de previmed.pt + conhecimento do mercado HSST PT.

## Princípio

O site Previmed serve **três audiências distintas com objetivos opostos**. Tratá-las como uma só audiência é o erro mais comum no sector. O SEO desta arquitetura tem de:

1. **Maximizar aquisição** na jornada *Cliente Empresa* (a única que gera receita direta).
2. **Reduzir fricção e proteger reputação** na jornada *Trabalhador/Utente* (sem ela, perde-se clientes B2B existentes).
3. **Capturar mercado paralelo** na jornada *Formando* (sub-negócio com unit economics próprias).

Cada audiência tem o seu **hub** de páginas, o seu vocabulário, o seu schema, e idealmente o seu ponto de entrada visível na navegação.

---

## Persona 1 — Cliente Empresa (decisor HSST)

### Quem é

Pessoa responsável por contratar serviços HSST numa empresa portuguesa com pelo menos 1 trabalhador (obrigação legal: Lei 102/2009 e Código do Trabalho).

| Tamanho empresa | Decisor típico |
|---|---|
| Micro (1–9 trab.) | Sócio-gerente, contabilista, consultor externo |
| Pequena (10–49) | Responsável RH, sócio-gerente, gestor de operações |
| Média (50–249) | Diretor RH, Quality/HSE manager, COO |
| Grande (250+) | HSE/QHSE Manager, Compliance Officer, Diretor RH, Procurement |

Setores de origem mais comuns: construção civil, indústria transformadora, restauração, retalho, logística, serviços, saúde, agricultura.

### Triggers (porque procuram agora)

- Nova empresa a contratar primeiro trabalhador.
- Contrato HSST atual a expirar / má experiência com fornecedor actual.
- Inspeção ACT recente ou coima.
- Auditoria ISO 9001 / ISO 45001 / outras certificações.
- Acidente de trabalho recente.
- Crescimento — nova obra/loja/unidade, nova geografia, contratação de funcionários.
- Onboarding M&A — absorção de equipa.
- Mudança regulatória.

### Jobs-to-be-done

1. **Cumprir legislação** sem ter de a estudar.
2. **Reduzir risco** (acidentes, doenças profissionais, responsabilidade legal).
3. **Cobrir todos os trabalhadores** mesmo que dispersos geograficamente.
4. **Ter documentação pronta** para qualquer inspeção/auditoria.
5. **Não perder tempo** com gestão administrativa de exames/formações.
6. **Garantir formação obrigatória** (35h, segurança alimentar, etc.).

### Perguntas por fase de funil

**Top of funnel — informacional ("aprender")**

- "sou obrigado a ter medicina do trabalho?"
- "lei 102/2009 resumo"
- "quem precisa de medicina do trabalho"
- "o que faz um técnico superior de segurança no trabalho"
- "quem pode fazer ficha de aptidão"
- "exames de admissão obrigatórios"
- "periodicidade exames medicina do trabalho"
- "obrigações HACCP restauração"
- "formação 35 horas obrigatória quem"
- "diferença medicina trabalho e seguro acidentes"

**Mid funnel — comparativo/avaliação ("escolher")**

- "como escolher empresa medicina do trabalho"
- "preço medicina do trabalho por trabalhador"
- "[concorrente] vs [concorrente]"
- "empresas medicina trabalho [distrito]"
- "rede clínicas medicina trabalho nacional"
- "medicina do trabalho online possível"
- "empresa segurança no trabalho certificada"
- "fornecedor HSST com formação DGERT"
- "previmed avaliações"

**Bottom of funnel — transacional ("comprar")**

- "previmed pedido proposta"
- "orçamento medicina trabalho"
- "previmed contacto"
- "contratar medicina do trabalho empresa"

### Critérios de decisão

| Critério | Peso típico | Como o site responde |
|---|---|---|
| Conformidade legal real | Alto | Página "compliance/legislação", schema `hasCredential` |
| Cobertura geográfica | Alto | Mapa de cobertura + páginas regionais quando justificadas |
| Certificações (ACT, DGS, DGERT, ISO) | Alto | Badge bar + página dedicada |
| Tempo de resposta a proposta | Alto | Form curto + SLA explícito |
| Plataforma digital cliente | Médio-alto | Demo/screenshot do portal |
| Preço transparente | Médio (B2B raramente lista preços) | Faixa indicativa ou "obter proposta personalizada" |
| Reputação / casos | Médio | Logos de clientes, testemunhos, anos no mercado |
| Cobertura de serviços adjacentes (formação, HACCP, ambiente) | Médio | One-stop-shop como diferenciação |

### Friction points (a eliminar no site)

- Form de proposta longo / com campos desnecessários.
- Falta de clareza sobre cobertura geográfica real.
- Não distinguir "rede própria" de "rede parceira".
- Não saber quem trata o quê (cliente vs trabalhador).
- Ausência de contacto humano rápido (telefone visível).

### Implicações SEO

- **Hub principal do site** — máxima prioridade.
- Conteúdo de autoridade legal/regulatório → ideal para AI Search/GEO.
- Schema: `Organization` com `hasCredential`, `Service` para cada serviço, `FAQPage` em páginas informacionais.
- Forte oportunidade em **long-tail informacional** (perguntas legais específicas) — concorrência atual é institucional (ACT, DGS), portal-style, baixa conversão; Previmed pode capturar com clareza superior.
- Internal linking: páginas informacionais → páginas de serviço → CTA proposta.

---

## Persona 2 — Trabalhador / Utente

### Quem é

Colaborador de uma empresa cliente da Previmed. Não escolheu o fornecedor — foi inscrito pela empresa.

### Triggers

- Recebeu convocatória para exame.
- Quer ver resultados de análises.
- Quer 2ª via de ficha de aptidão.
- Esqueceu password do portal.
- Não recebeu convocatória prevista.
- Quer saber onde fica a clínica (rede parceira).

### Jobs-to-be-done

1. **Aceder ao portal** sem fricção.
2. **Encontrar a clínica** que lhe foi atribuída.
3. **Ver resultados** rapidamente.
4. **Contactar suporte** quando algo falha.

### Perguntas por fase

**Brand / suporte**
- "portal trabalhador previmed"
- "previmed login"
- "previmed marcação"
- "previmed resultados análises"
- "previmed clínica perto de mim"
- "previmed contacto trabalhador"
- "esqueci password previmed"

**Sem brand** (raras, mas existem)
- "como aceder resultados medicina do trabalho"
- "ficha de aptidão pedir 2ª via"

### Critérios de "decisão"

Não há decisão — há expectativa de serviço. O critério é **friction = 0**.

### Friction points (a eliminar)

- Portal de login escondido em sub-páginas.
- Não saber qual clínica.
- Erro de password sem fluxo claro de recuperação.
- Convocatória física apenas (sem digital).

### Implicações SEO

- **Não é canal de aquisição** — é canal de **retenção/reputação**.
- Queries brand devem ter resposta imediata: portal de login deve aparecer no menu principal (não em footer).
- Página dedicada "Portal Trabalhador" com FAQ, recuperação password, contacto suporte.
- Schema: não precisa de `Service` — é mais um `WebPage` informativo. Pode incluir `ContactPoint` com role "customer support".
- Importante: **não competir SEO com a jornada Cliente Empresa**. Páginas trabalhador podem ser `noindex` se não houver query volume non-brand significativo, para evitar canibalização e diluir relevância da homepage.

→ **Decisão pendente para Fase 4**: indexar páginas trabalhador? Hipótese inicial: **sim, mas com title/H1 muito específicos** ("Portal Trabalhador — Previmed") para queries brand, sem canibalizar termos comerciais.

---

## Persona 3 — Formando

### Quem é

Pessoa a procurar formação certificada DGERT, tipicamente:

- Trabalhador a obter/renovar certificação obrigatória (ex: HACCP em restauração, CAP segurança).
- Pessoa em transição de carreira para área HSST.
- Profissional HSST a manter atualização.
- Empresa a inscrever colaboradores em massa (sobreposição com Persona 1).

### Triggers

- Obrigação legal (HACCP, segurança alimentar, formação contínua).
- Mudança de função.
- Recrutamento (CAP TST/TSST).
- Empresa cliente a contratar pack de formação.

### Jobs-to-be-done

1. **Validar certificação DGERT** (sem isso, não interessa).
2. **Ver datas e modalidade** (online/presencial/blended).
3. **Ver preço**.
4. **Inscrição rápida**.
5. **Acesso a plataforma e-learning** funcional.

### Perguntas por fase

**Top — informacional**
- "formação 35 horas obrigatória"
- "o que é o CAP segurança no trabalho"
- "curso HACCP online certificado"
- "formação técnico superior segurança trabalho preço"

**Mid — comparativo**
- "melhor formação HACCP online Portugal"
- "formação DGERT online"
- "[concorrente] formação"
- "formação segurança alimentar reconhecida"

**Bottom — transacional**
- "inscrição formação 35 horas previmed"
- "previmed e-learning login"
- "comprar curso HACCP"

### Critérios de decisão

- Certificação DGERT explícita.
- Modalidade (online ganha em 2026 para a maioria dos cursos curtos).
- Calendário visível.
- Preço visível (ao contrário de Persona 1, aqui é B2C — preço opaco = abandono).
- Plataforma e-learning credível.

### Friction points

- Não ver datas/preços.
- Confusão entre cursos (CAP, formação contínua, formação específica).
- Plataforma e-learning lenta/quebrada.
- Pagamento não óbvio.

### Implicações SEO

- **Sub-hub próprio** com vida própria: `/formacao/`.
- Schema: `Course`, `CourseInstance`, `EducationalOrganization` para a Previmed Formação como ramo.
- Cada curso = página individual com `Course` schema (volume e datas).
- Forte oportunidade em **queries informacionais sobre obrigações de formação** (HACCP, segurança alimentar, formação 35h) que cruzam com Persona 1 — pontes de internal linking entre empresas e formação.
- Pricing visible (mesmo que "a partir de") — sector B2C tolera mal opacidade.

---

## Síntese: prioridades SEO por audiência

| Audiência | Prioridade | % esforço SEO sugerido | Tipo de páginas dominante |
|---|---|---|---|
| **Cliente Empresa** | **#1** | ~65% | Hub serviços + pillar informacional + landing comercial |
| **Formando** | **#2** | ~25% | Hub formação + páginas curso + guias certificação |
| **Trabalhador** | **#3** | ~10% | Portal + FAQ + recuperação acesso (apenas brand+suporte) |

## Pontes entre audiências (oportunidades internal linking)

- **Empresa → Formando**: empresa contrata medicina trabalho + precisa formar trabalhadores → link de página serviço para formação relevante.
- **Formando → Empresa**: pessoa que faz formação CAP TST/TSST pode trabalhar numa empresa cliente → link discreto "para empresas, ver serviços HSST".
- **Empresa → Trabalhador**: cliente quer saber como funciona o portal → demo/screenshot na página comercial.
- **Trabalhador → Empresa**: bloqueado. Não criar ponte (audiências têm objectivos opostos).

## Próximo lote

**Lote 1.2 — Arquitetura de Informação top-level** usará este documento para:
- decidir hubs e sub-hubs;
- regras de URL (`/servicos/`, `/formacao/`, `/portal/`);
- relação menu principal vs SEO;
- páginas regionais (sim/não/quando).
