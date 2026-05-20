# SEO Operating System

Este ficheiro define a forma de trabalhar SEO no projeto.

## Visão

SEO é uma disciplina central do projeto, não uma camada final.

O objetivo é construir um website que:
- responda melhor às intenções de pesquisa;
- seja tecnicamente excelente;
- seja rápido;
- seja confiável;
- tenha conteúdo útil e diferenciado;
- tenha arquitetura clara;
- seja fácil de rastrear, indexar e entender;
- converta visitantes em leads/clientes.

## Áreas SEO

1. Estratégia
2. Pesquisa de keywords
3. Análise de concorrência
4. Arquitetura de informação
5. SEO técnico
6. Conteúdo
7. On-page
8. Internal linking
9. Schema/entidades
10. Local SEO
11. Performance/Core Web Vitals
12. Acessibilidade
13. WordPress implementation
14. Medição e reporting
15. AI Search visibility

## Workflow

1. Definir objetivo de negócio.
2. Definir páginas prioritárias.
3. Mapear intenção de pesquisa.
4. Analisar concorrência.
5. Fazer auditoria técnica.
6. Criar arquitetura SEO.
7. Produzir briefs de página.
8. Validar conteúdo e UX.
9. Implementar com segurança.
10. Testar indexabilidade, performance e schema.
11. Medir no Search Console/GA4.
12. Iterar.

## Regras

- Não há SEO sem intenção clara.
- Não há página nova sem papel na arquitetura.
- Não há alteração de slug sem plano de redirect.
- Não há schema sem conteúdo visível correspondente.
- Não há conteúdo SEO genérico.
- Não há design que esconda conteúdo crítico.
- Não há dependência pesada sem performance review.
- Não há análise SEO grande sem ficheiro persistente (ver Persistence Rule abaixo).

## Persistence Rule

Sempre que o utilizador pede uma destas análises, o resultado **não pode ficar apenas no chat**:

- análise SEO completa;
- planeamento SEO;
- análise de concorrência;
- auditoria técnica;
- keyword research / cluster map;
- content gap analysis;
- estratégia de conteúdos;
- Core Web Vitals / performance;
- schema / entidades;
- local SEO;
- AI Search / GEO;
- plano de ação SEO.

O resultado vai para um ficheiro datado em:

```
.claude/project/organic-growth/reports/YYYY-MM-DD__report-type.md
```

Usar sempre o template em [`reports/_TEMPLATE_seo-report.md`](./reports/_TEMPLATE_seo-report.md).

**Markdown (`.md`) por defeito**, não `.txt` — para renderizar no GitHub.

Ver [`reports/README.md`](./reports/README.md) para o detalhe completo do formato.

## Anti-token-waste

> **Análise longa sem ficheiro persistente = desperdício de contexto.**

Antes de continuar uma análise SEO grande, qualquer agente (em particular o Supervisor / Change Manager) deve verificar:

> *"Esta análise está a ser persistida em ficheiro?"*

Se a resposta for **não**, parar imediatamente e:
1. Criar o ficheiro em `reports/YYYY-MM-DD__*.md` a partir do template.
2. Despejar para lá o que já foi analisado.
3. Só depois continuar.

A regra aplica-se tanto a relatórios completos como a análises parciais que o utilizador pediu como blocos de uma análise maior.

## Living vs dated files

A pasta `organic-growth/` separa **ficheiros datados** (snapshots históricos) de **ficheiros vivos** (estado atual curto):

| Tipo | Localização | Função |
|---|---|---|
| Datado | `reports/YYYY-MM-DD__*.md` | Análise completa, snapshot no tempo, não editar depois de publicar. |
| Vivo | `_living/CURRENT_STATUS.md` | Estado atual curto + apontador para último relatório. |
| Vivo | `_living/BACKLOG.md` | Tarefas acionáveis priorizadas. |
| Vivo | `_living/OPPORTUNITIES.md` | Hipóteses/ideias antes de virarem tarefas. |
| Vivo | `_living/DECISION_LOG.md` | Decisões SEO importantes e duradouras. |

**Após criar um relatório datado**, atualizar os ficheiros vivos:

1. `_living/CURRENT_STATUS.md` — resumo curto + link para o novo relatório.
2. `_living/BACKLOG.md` — adicionar tarefas acionáveis identificadas.
3. `_living/OPPORTUNITIES.md` — adicionar oportunidades novas.
4. `_living/DECISION_LOG.md` — registar **apenas** decisões reais e duradouras.

**Nunca duplicar** o relatório inteiro nos ficheiros vivos — os ficheiros vivos são índices/sumários.
