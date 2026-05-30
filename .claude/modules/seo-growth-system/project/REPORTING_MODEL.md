# SEO Reporting Model

Fonte de verdade para persistência e reporting de análises SEO do **SEO Growth System**.

Este ficheiro define como as análises SEO são persistidas, que tipos de records existem, como nomear, como actualizar ficheiros de estado e quando recomendar persistência — para não desperdiçar contexto e manter histórico auditável.

Este ficheiro não é um agente.  
Este ficheiro não executa análises.  
Este ficheiro não substitui o `seo-lead`, o `seo-data-analyst` nem o Supervisor/System Safety.

---

## Objetivo

Garantir que análises SEO relevantes são persistidas de forma consistente, reutilizável e não duplicada — para que contexto não se perca, decisões sejam rastreáveis e análises futuras possam comparar com histórico.

---

## Âmbito

Este documento cobre:

- quando criar record;
- que tipo de record usar;
- onde guardar records reais;
- como nomear records;
- ficheiros datados vs ficheiros vivos;
- como actualizar estado após record;
- o que nunca guardar em records.

---

## Fora de âmbito

- conteúdo dos records — cada template define o seu formato;
- análise de dados em si — ver `seo-data-analyst` e skill `gsc-ga4-analysis`;
- ferramentas para criar records — ver `TOOLING_MODEL.md`.

---

## Responsabilidades por componente

| Componente | Responsabilidade |
|---|---|
| `REPORTING_MODEL.md` (este ficheiro) | Standard de persistência e estrutura de records |
| [`seo-lead`](../agents/seo-lead.md) | Garante que análises grandes são persistidas |
| [`seo-data-analyst`](../agents/seo-data-analyst.md) | Produz análises de dados para persistir |
| [`serp-competitor-analyst`](../agents/serp-competitor-analyst.md) | Produz análises de concorrência para persistir |
| Templates em `records-templates/` | Formatos reutilizáveis por tipo de record |

---

## Quando criar record

**Regra principal:** análise grande sem record persistente = desperdício de contexto.

Antes de continuar uma análise grande, confirmar: "isto está a ser persistido?" Se não, criar o record e só depois continuar.

Criar record para:

- auditoria SEO completa;
- auditoria técnica;
- keyword research e cluster map;
- análise de concorrência/SERP;
- content gap analysis;
- estratégia de conteúdo;
- AI Search/GEO review;
- local SEO review;
- performance/CWV review;
- plano de acção (30/60/90 dias);
- go-live SEO;
- decisão SEO duradoura (mudança de URL, schema, estrutura de arquitetura);
- baseline de KPIs;
- análise de queda/subida significativa;
- relatório periódico.

**Não criar record para:**
- respostas rápidas e simples no chat;
- tarefas que ficam resolvidas sem impacto duradouro;
- conteúdo duplicado de outro record já criado.

---

## Tipos de record

### 1. Datado — relatório/análise

Arquivo de análise completa. Snapshot no tempo.

- Não editar depois de criar (é snapshot).
- Referenciado por ficheiros vivos via link.
- Exemplos: auditoria SEO, análise de concorrência, keyword research, go-live.

**Template:** `SEO_AUDIT_TEMPLATE.md`, `SEO_REPORT_TEMPLATE.md`.

### 2. Vivo — status

Estado actual curto + apontador para o último relatório datado.

- Atualizar regularmente.
- Não duplicar o relatório — apenas resumo + link.
- Exemplo: `seo-status.md` no workspace.

### 3. Vivo — backlog

Lista de tarefas acionáveis e priorizadas.

- Atualizar após cada relatório.
- Tarefas concluídas saem da lista.
- Exemplo: `seo-backlog.md`.

### 4. Vivo — opportunities

Hipóteses e ideias antes de virarem tarefas.

- Menos urgente que backlog.
- Rever periodicamente para promover a backlog ou descartar.
- Exemplo: `seo-opportunities.md`.

### 5. Vivo — decisions

Decisões SEO duradouras que não devem ser revertidas sem contexto.

- Apenas decisões reais, não tudo.
- Exemplo: decisão de estrutura de URL, decisão de consolidação de páginas.
- **Template:** `SEO_DECISION_TEMPLATE.md`.

### 6. Task

Lote ou tarefa SEO acionável com escopo definido.

- **Template:** `SEO_TASK_TEMPLATE.md`.

### 7. Go-live checklist

Validação antes de publicar site novo, secção ou migração.

- **Template:** `SEO_GO_LIVE_CHECKLIST.md`.

---

## Onde guardar

**Templates** vivem **dentro do plugin** em:

```
.claude/modules/seo-growth-system/records-templates/
```

São genéricos, exportáveis e não contêm dados reais.

**Records reais** vivem **no projeto-alvo** em:

```
.claude/records/
```

Estrutura sugerida:

```
.claude/records/
├── audits/seo/          — relatórios datados
├── decisions/seo/       — decisões duradouras
├── tasks/seo/           — tarefas e lotes
└── status/              — ficheiros de estado vivos
```

---

## Como nomear records

Formato: `YYYY-MM-DD__report-type.md`

- Data ISO 8601: `YYYY-MM-DD`.
- Duplo underscore `__` como separador.
- report-type em kebab-case (minúsculas, hífens).
- Extensão `.md`.

Exemplos:

```
2025-03-15__seo-audit-completa.md
2025-03-15__competitor-research-medicina-trabalho.md
2025-03-15__keyword-cluster-map-seguranca.md
2025-03-15__go-live-homepage.md
2025-04-01__seo-decision-url-structure.md
```

---

## Fluxo após criar record datado

1. Criar o record datado.
2. Actualizar `status.md`: resumo do relatório + link.
3. Mover tarefas acionáveis para `backlog.md`.
4. Mover hipóteses/oportunidades para `opportunities.md`.
5. Mover decisões duradouras para `decisions/`.
6. **Nunca** duplicar o relatório inteiro em ficheiros vivos.

---

## O que nunca guardar em records

- Dados pessoais de utilizadores, clientes ou trabalhadores.
- Credenciais, tokens, API keys, passwords.
- Dados sensíveis ou confidenciais sem necessidade.
- Informação médica, financeira ou legal de pessoas.
- Dados de acesso a sistemas externos.

Se um record precisar de mencionar acesso, mencionar apenas que "autorização existe" — não copiar a credencial.

---

## Gates

**Bloquear** quando:

- análise relevante não está a ser persistida;
- record contém dados pessoais ou sensíveis;
- record duplica conteúdo já persistido.

**Recomendar** sempre que análise for relevante e duradoura.

---

## Relação com agentes, skills e comandos

- [`seo-lead`](../agents/seo-lead.md) — coordena persistência.
- [`seo-data-analyst`](../agents/seo-data-analyst.md) — produz análises a persistir.
- [`serp-competitor-analyst`](../agents/serp-competitor-analyst.md) — análises datadas a persistir.
- [`records-templates/README.md`](../records-templates/README.md) — índice de templates.
- [`/seo data`](../commands/seo.md) e todos os modos que geram análises relevantes.

---

## Regra final

Análise que não é persistida não existe no futuro.

O próximo agente que trabalhar neste projecto vai recomeçar do zero se não houver histórico.

Persistir não é burocracia — é respeito pelo trabalho feito.
