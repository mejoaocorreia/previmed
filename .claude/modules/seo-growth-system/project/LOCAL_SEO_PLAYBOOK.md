# Local SEO Playbook

Fonte de verdade para SEO local do **SEO Growth System**.

Este ficheiro define as regras, o processo e os standards para optimização de presença local orgânica — Google Business Profile, NAP, páginas locais, reviews, citations e schema LocalBusiness — apenas para presença e intenção local real.

Este ficheiro não é um agente.  
Este ficheiro não executa alterações.  
Este ficheiro não altera o GBP directamente.  
Este ficheiro não substitui o `local-seo`, a skill `local-seo-review` nem o Supervisor/System Safety.

---

## Objetivo

Garantir que a presença local orgânica de qualquer projecto que use este module reflecte localização, serviços e identidade reais — de modo a aparecer nos resultados locais certos, com informação consistente, sem doorway pages e sem inventar presença onde não existe.

---

## Âmbito

Este playbook cobre:

- verificação de presença e intenção local real;
- Google Business Profile: completude, categorias, service areas, reviews, posts;
- NAP: consistência em website, GBP e diretórios externos;
- páginas locais: critérios de criação, estrutura, conteúdo mínimo;
- service areas: mapeamento real;
- reviews: estratégia, solicitação, resposta;
- citations: diretórios relevantes, consistência;
- schema LocalBusiness: consistência com website e GBP.

---

## Fora de âmbito

- SEO técnico geral — ver `TECHNICAL_RULES.md`;
- keyword research sem dimensão local — ver `STRATEGY_RULES.md`;
- schema semântico completo — ver `SCHEMA_ENTITY_MODEL.md`;
- implementação WordPress — ver `wordpress-seo-implementation`;
- RGPD e dados pessoais de clientes — Supervisor/System Safety.

---

## Responsabilidades por componente

| Componente | Responsabilidade |
|---|---|
| `LOCAL_SEO_PLAYBOOK.md` (este ficheiro) | Standard e regras de local SEO |
| [`local-seo`](../agents/local-seo.md) | Revisão e recomendações de local SEO |
| [`local-seo-review`](../skills/local-seo-review/SKILL.md) | Procedimento passo a passo |
| [`schema-entity`](../agents/schema-entity.md) | Modelação de schema LocalBusiness |
| [`content-brief`](../agents/content-brief.md) | Brief para páginas locais justificadas |
| [`wordpress-seo-implementation`](../agents/wordpress-seo-implementation.md) | Implementação controlada |
| [`seo-qa`](../agents/seo-qa.md) | Validação final |
| Supervisor/System Safety | Autorização para alterações no GBP e externas |

---

## Standards e regras

### Regras fundamentais

**Presença real:**
- Local SEO apenas para localizações e service areas que a empresa realmente serve.
- Não criar páginas locais para cidades onde a empresa não actua.
- Não inventar moradas, telefones ou áreas.

**GBP:**
- Google Business Profile é o pilar da presença local orgânica.
- Qualquer alteração ao GBP requer autorização explícita do Supervisor.
- Informação no GBP deve ser idêntica ao website.

**NAP:**
- Name, Address, Phone devem ser consistentes em todo o ecossistema.
- Inconsistências NAP prejudicam confiança local e ranking.

**Páginas locais:**
- Só criar se houver intenção local real + conteúdo útil possível.
- Nunca criar doorway pages (conteúdo genérico com cidade trocada).
- Cada página local deve ter conteúdo específico e útil para aquela área.

**Reviews:**
- Nunca solicitar reviews com incentivo monetário ou desconto (contra regras Google).
- Responder sempre a reviews negativas com profissionalismo.
- Reviews falsas são proibidas e arriscam suspensão do GBP.

---

### Google Business Profile

**Completude mínima:**
- Nome exacto e consistente com o website.
- Endereço (se localização física) ou marcação como service area business.
- Telefone.
- URL do website.
- Categoria principal (mais relevante para o negócio).
- Horário de funcionamento.
- Descrição do negócio (sem spam de keyword).

**Boas práticas:**
- Fotos actualizadas: exterior, interior, equipa, produtos/serviços.
- Service areas definidas correctamente (não excessivamente alargadas).
- Q&A monitorizado e respondido.
- Posts GBP regulares para manter perfil activo.
- Atributos relevantes activados (acessibilidade, pagamentos, etc.).

**Regra:** qualquer alteração ao GBP exige autorização do Supervisor. Não alterar sem confirmação.

---

### NAP — Name, Address, Phone

**Onde verificar:**
- Website: footer, página de contacto, schema.
- Google Business Profile.
- Facebook, LinkedIn, Instagram.
- Diretórios principais (Portugal: Páginas Amarelas, Sapo, Infobel, Portugal Business, etc.).
- Diretórios sectoriais.

**Regras:**
- Nome exactamente igual em todas as fontes (sem variações como "Empresa Lda" vs "Empresa, Lda").
- Morada no mesmo formato.
- Telefone no mesmo formato (com ou sem +351 de forma consistente).
- Qualquer inconsistência deve ser identificada e corrigida.

---

### Páginas locais

**Quando criar:**

1. Há intenção local confirmada: SERP mostra Local Pack ou resultados locais para a query.
2. A empresa serve realmente essa área.
3. É possível criar conteúdo útil específico para essa área (não apenas trocar o nome da cidade).

**Critérios de conteúdo mínimo para página local válida:**
- Referência clara ao serviço na área específica.
- Informação relevante para utilizadores locais (proximidade, acesso, contexto local).
- Diferenciação do que a empresa faz nessa área.
- CTA específico.
- Links internos para serviços relacionados.
- Schema LocalBusiness (quando há morada real).

**O que nunca fazer:**
- Criar página local com texto genérico e apenas o nome da cidade trocado.
- Criar dezenas de páginas locais com conteúdo idêntico.
- Criar páginas locais para zonas onde a empresa não actua.

---

### Service areas

**Definir service areas realistas:**
- Que cidades/distritos/países a empresa realmente serve?
- Há deslocações a locais específicos?
- Há serviços remotos?

**Consistência:**
- Service areas no GBP devem reflectir a realidade.
- Service areas no website devem ser iguais ao GBP.
- Schema `areaServed` deve reflectir as mesmas zonas.

---

### Reviews

**Estratégia de solicitação:**
- Pedir review após entrega de serviço satisfatório.
- Facilitar o link directo para review no GBP.
- Sem incentivo monetário ou desconto (proibido pelo Google).
- Sem pressão ou coerção.

**Resposta:**
- Responder a reviews positivas: breve agradecimento, personalizado.
- Responder a reviews negativas: profissional, sem defensividade, oferecer resolução.
- Responder em tempo razoável (< 7 dias).

**Reviews falsas:**
- Proibidas pelas regras Google.
- Risco de suspensão do GBP.
- Nunca criar, solicitar ou promover reviews falsas.

---

### Citations

**Diretórios principais (Portugal):**
- Páginas Amarelas.
- Infobel.
- Portugal Business.
- Sapo Finanças.
- Google Maps (via GBP).
- Diretórios sectoriais relevantes.

**Regras:**
- NAP exactamente igual em todos os diretórios.
- Manter diretórios actualizados quando há mudança de morada, telefone ou nome.

---

## Processo

Ver procedimento detalhado na skill [`local-seo-review`](../skills/local-seo-review/SKILL.md).

Resumo:

1. Confirmar presença e intenção local real.
2. Verificar GBP (completude, categorias, service areas, reviews).
3. Verificar NAP (website, GBP, diretórios).
4. Avaliar páginas locais existentes.
5. Identificar páginas locais justificadas a criar.
6. Mapear service areas.
7. Avaliar reviews e estratégia.
8. Verificar citations.
9. Verificar schema LocalBusiness (handoff para `schema-entity`).
10. Garantir coerência website ↔ GBP ↔ schema.

---

## Gates

**Bloquear ou pedir autorização** quando:

- alteração ao GBP (qualquer alteração);
- criação de páginas locais em produção;
- alteração de NAP em produção;
- gestão de reviews em plataformas externas;
- uso de dados de clientes para reviews.

**Bloquear sem condições** quando:

- é pedido criar páginas locais sem intenção real;
- é pedido inventar moradas ou áreas;
- é pedido solicitar reviews com incentivo indevido;
- é pedido criar reviews falsas.

---

## Relação com agentes, skills e comandos

- [`local-seo`](../agents/local-seo.md) — executa seguindo este playbook.
- [`local-seo-review`](../skills/local-seo-review/SKILL.md) — procedimento operacional.
- [`schema-entity`](../agents/schema-entity.md) — schema LocalBusiness e NAP.
- [`keyword-intent`](../agents/keyword-intent.md) — confirma intenção local.
- [`serp-competitor-analyst`](../agents/serp-competitor-analyst.md) — analisa SERP local.
- [`content-brief`](../agents/content-brief.md) — brief para páginas locais.
- [`wordpress-seo-implementation`](../agents/wordpress-seo-implementation.md) — implementação.
- [`seo-qa`](../agents/seo-qa.md) — validação.
- [`SCHEMA_ENTITY_MODEL.md`](SCHEMA_ENTITY_MODEL.md) — LocalBusiness e NAP detalhado.
- [`/seo local`](../commands/seo.md) — modo do comando SEO.

---

## Records / Persistência

Recomendar record quando:

- local SEO review relevante;
- decisão de criar ou remover páginas locais;
- mudança de NAP ou GBP significativa;
- análise de reviews e reputação local.

Records reais vivem no projeto-alvo em `.claude/records/`.

---

## Regra final

Local SEO funciona quando reflecte realidade.

NAP consistente. GBP completo e honesto. Páginas locais com conteúdo útil. Reviews genuínas.

Tudo o resto é ruído — ou risco.
