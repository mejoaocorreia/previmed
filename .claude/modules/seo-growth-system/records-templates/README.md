# SEO Records Templates

Templates SEO do plugin [`seo-growth-system`](../README.md). Vivem dentro do plugin para que o module seja autossuficiente e exportavel.

Estes ficheiros sao **templates**, nao records reais. Copiar para o projeto consumidor, datar, preencher e guardar na estrutura de records desse projeto.

---

## Para Que Servem

Servem para manter consistencia em:

- auditorias SEO;
- relatorios datados;
- decisoes duradouras;
- tarefas/lotes;
- checklists de go-live.

Todos os templates devem seguir [`REPORTING_MODEL.md`](../project/REPORTING_MODEL.md), [`QUALITY_GATE.md`](../project/QUALITY_GATE.md), [`seo-lead`](../agents/seo-lead.md), [`seo-qa`](../agents/seo-qa.md) e o comando [`/seo`](../commands/seo.md).

---

## Templates Disponiveis

| Template | Quando usar | Record real sugerido |
|---|---|---|
| [`SEO_AUDIT_TEMPLATE.md`](SEO_AUDIT_TEMPLATE.md) | auditoria SEO completa ou por area | `.claude/records/audits/seo/` |
| [`SEO_REPORT_TEMPLATE.md`](SEO_REPORT_TEMPLATE.md) | relatorio datado de analise, performance, SERP, dados ou progresso | `.claude/records/reports/seo/` |
| [`SEO_DECISION_TEMPLATE.md`](SEO_DECISION_TEMPLATE.md) | decisao duradoura de arquitetura, URL, strategy, schema, local, roadmap | `.claude/records/decisions/seo/` |
| [`SEO_TASK_TEMPLATE.md`](SEO_TASK_TEMPLATE.md) | tarefa/lote acionavel com owner, gates e validacao | `.claude/records/tasks/seo/` |
| [`SEO_GO_LIVE_CHECKLIST.md`](SEO_GO_LIVE_CHECKLIST.md) | validacao antes/depois de publicar ou alterar indexacao | `.claude/records/go-live/seo/` |

O projeto consumidor pode adaptar as pastas, mas deve manter data ISO e nomes legiveis.

---

## Convencao De Nome

Usar data ISO 8601 + `__` + kebab-case:

```text
YYYY-MM-DD__seo-audit-homepage.md
YYYY-MM-DD__decision-consolidate-service-pages.md
YYYY-MM-DD__go-live-service-page.md
```

---

## O Que Nunca Guardar

Nunca guardar em records:

- dados pessoais desnecessarios;
- dados sensiveis;
- dados de saude;
- dados de trabalhadores;
- credenciais;
- tokens;
- API keys;
- exports completos de GSC/GA4 quando bastam agregados;
- informacao confidencial que nao seja necessaria para a decisao.

Quando houver duvida, minimizar, anonimizar ou pedir decisao ao Supervisor/System Safety.

---

## Terminologia Obrigatoria

Usar, quando aplicavel:

- evidencia;
- hipotese;
- recomendacao;
- bloqueio;
- handoff;
- risco residual;
- validacao feita;
- nao validado / a confirmar;
- proximo passo.

Estados oficiais do quality gate:

- Aprovado
- Aprovado com notas
- Bloqueado
- Precisa de dados
- Precisa de autorizacao

---

## Depois De Criar Um Record

Depois de criar um record datado:

1. atualizar status/backlog/opportunities/decisions do projeto consumidor, se existirem;
2. ligar o record a tarefas ou PRs relevantes;
3. nao duplicar o relatorio inteiro noutros ficheiros;
4. manter o record factual: separar evidencia, hipotese e recomendacao;
5. registar limitacoes e proximos passos.

Ver [`REPORTING_MODEL.md`](../project/REPORTING_MODEL.md).
