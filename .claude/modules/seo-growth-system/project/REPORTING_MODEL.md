# SEO Reporting Model

## Objetivo
Definir como análises SEO são persistidas — para não desperdiçar contexto e manter histórico auditável.

## Quando usar
Sempre que se produz uma análise grande: auditoria completa, planeamento, concorrência, auditoria técnica, keyword research/cluster map, content gap, estratégia de conteúdo, CWV/performance, schema/entidades, local SEO, AI Search/GEO, plano de ação.

## Regras principais
- **Análise grande sem record persistente = desperdício de contexto.** Antes de continuar, confirmar "isto está a ser persistido?". Se não, criar o record e só depois continuar.
- Markdown (`.md`) por defeito (renderiza no GitHub).
- Records reais vivem em `.claude/records/` (não no module). Os **templates** vivem centralizados em [`.claude/records/templates/seo/`](../../../records/templates/seo/README.md).
- Não duplicar o relatório inteiro em ficheiros de estado — estes são índices/sumários.

## Processo

### Onde guardar (no repo que usa o module)
Sugestão de convenção: `.claude/records/audits/seo/YYYY-MM-DD__report-type.md`.
Formato de nome: data ISO 8601 + `__` + `report-type` em kebab-case + `.md`.

### Ficheiros datados vs vivos
| Tipo | Função |
|---|---|
| Datado (`reports/YYYY-MM-DD__*.md`) | Análise completa, snapshot no tempo, não editar depois de publicar. |
| Vivo — status | Estado atual curto + apontador para o último relatório. |
| Vivo — backlog | Tarefas acionáveis priorizadas. |
| Vivo — opportunities | Hipóteses/ideias antes de virarem tarefas. |
| Vivo — decisions | Decisões SEO duradouras. |

Após um relatório datado: atualizar status (resumo+link), mover tarefas para backlog, oportunidades para opportunities, decisões duradouras para decisions. **Nunca** duplicar o relatório inteiro.

## Inputs
A análise produzida + o template adequado de [`.claude/records/templates/seo/`](../../../records/templates/seo/README.md).

## Outputs
Record datado consistente + ficheiros de estado atualizados.

## Agentes relacionados
[`seo-lead`](../agents/seo-lead.md) (garante persistência), [`seo-data-analyst`](../agents/seo-data-analyst.md), [`serp-competitor-analyst`](../agents/serp-competitor-analyst.md).

## Skills relacionadas
[`gsc-ga4-analysis`](../skills/gsc-ga4-analysis/SKILL.md), [`competitor-gap-analysis`](../skills/competitor-gap-analysis/SKILL.md).

## Ferramentas/MCPs possíveis
Filesystem (criar records, autorizado). 

## Critérios de qualidade
Análise grande sempre persistida; nome consistente; estado atualizado sem duplicar conteúdo.

## Notas de consolidação
Consolidado da versão anterior do pacote SEO (persistence rule, anti-token-waste, living vs dated, convenção de reports). **Generalizado:** caminhos e dados específicos de projeto ficam nos records reais; aqui fica o modelo reutilizável apontando para `.claude/records/`.
