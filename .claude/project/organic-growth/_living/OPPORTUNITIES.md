# SEO Opportunities

> Ficheiro **vivo**. Oportunidades, ideias e hipóteses **antes** de virarem tarefas.
> Quando uma oportunidade for validada e tiver dono, **mover** para `./BACKLOG.md`.
> Análise que justifica cada oportunidade vive em `reports/`.

## Como usar

- **Adicionar** sempre que um relatório (`reports/*`) ou conversa identifica algo aproveitável que ainda não está pronto para virar tarefa concreta.
- **Marcar estado**: `hipótese`, `por validar`, `validada`, `descartada`.
- **Mover** para `./BACKLOG.md` quando validada e priorizada.
- **Não duplicar** análise detalhada — apontar para o relatório de origem.

## Formato

```
### [Título curto da oportunidade]

- **Estado**: hipótese | por validar | validada | descartada
- **Origem**: link para relatório ou conversa
- **Impacto estimado**: alto | médio | baixo
- **Esforço estimado**: alto | médio | baixo
- **Hipótese**: 1–2 linhas
- **Como validar**: 1–3 passos
- **Próximo passo**: quem/o quê
```

## Oportunidades ativas

### Pillar "Como escolher empresa de medicina do trabalho"

- **Estado**: por validar
- **Origem**: [`.../reports/2026-05-20__aio-expansion.md`](../reports/2026-05-20__aio-expansion.md) §Q5
- **Impacto estimado**: alto
- **Esforço estimado**: médio
- **Hipótese**: Previmed já é citado em AIO Q5 (foothold confirmado). Pillar dedicado em `/recursos/guias/escolher-medicina-do-trabalho/` superando os 5 critérios AIO (DGS/ACT, Logística, Abrangência, Tecnologia, Reputação) com 6º critério defensável (indicadores qualidade) pode consolidar a posição.
- **Como validar**: confirmar volume via DataForSEO/Keyword Planner (pendente decisão A–F); recaptura AIO Q5 a t+30d para verificar estabilidade da citação Previmed.
- **Próximo passo**: SEO Lead — brief P1 quando ordem de produção for decidida.

### Diferenciação por correção legal "35h → 40h"

- **Estado**: por validar
- **Origem**: [`.../reports/2026-05-20__aio-expansion.md`](../reports/2026-05-20__aio-expansion.md) §Q4
- **Impacto estimado**: alto
- **Esforço estimado**: baixo (correção factual)
- **Hipótese**: AIO já corrige automaticamente 35→40h (Lei 93/2019). Maioria do conteúdo PT existente ainda fala em 35h. Pillar Previmed que abra com "O que mudou: 35→40h" + Lei 93/2019 + Nota Técnica 9 ACT é defensável legalmente e diferenciador editorialmente.
- **Como validar**: confirmar quantos competidores diretos já atualizaram para 40h (rápido crawl manual a forprev.pt, sepri.pt, centralmed.pt, factorialhr.pt); validar manutenção da query "35 horas" via Keyword Planner (provavelmente volume ainda alto).
- **Próximo passo**: SEO Lead — atualizar `../strategy/KEYWORDS.md` cluster Formação; brief P1.

### Hub editorial "Lei 102/2009 explicada"

- **Estado**: hipótese
- **Origem**: [`.../reports/2026-05-20__aio-expansion.md`](../reports/2026-05-20__aio-expansion.md) §Open Questions
- **Impacto estimado**: médio
- **Esforço estimado**: alto (conteúdo jurídico-técnico)
- **Hipótese**: Lei 102/2009 é citada em 3/5 queries AIO. Pillar institucional Previmed que explique a lei artigo a artigo (com link para pgdlisboa em cada secção) pode tornar-se referência citada AIO em queries head + tail.
- **Como validar**: confirmar que nenhum competidor PT já tem hub robusto; volume de queries jurídicas ("Lei 102/2009 medicina trabalho", "art. 5 lei 102/2009", etc.).
- **Próximo passo**: pendente decisão keyword data tool.

### Auditoria competitiva da página Forprev (top citada AIO Q5)

- **Estado**: hipótese
- **Origem**: [`.../reports/2026-05-20__aio-expansion.md`](../reports/2026-05-20__aio-expansion.md) §T1
- **Impacto estimado**: médio
- **Esforço estimado**: baixo
- **Hipótese**: `forprev.pt/medicina-do-trabalho/` é a primeira citada em Q5 AIO — tem alguma característica técnica/editorial específica que vale replicar (com superioridade).
- **Como validar**: crawl técnico + leitura editorial. Capturar schema, H1–H4, comprimento, links externos, frequência de palavras-chave, presença de tabelas.
- **Próximo passo**: relatório de auditoria competitiva dedicado em `reports/`.

### Padrão "Centralmed" de citação institucional outbound

- **Estado**: validada (cross-confirmada em 3 páginas Centralmed em 3 clusters distintos)
- **Origem**: [`.../reports/2026-05-20__competitor-deep-dive.md`](../reports/2026-05-20__competitor-deep-dive.md) §H4
- **Impacto estimado**: alto
- **Esforço estimado**: baixo (editorial, não técnico)
- **Hipótese**: AIO premia páginas que linkam para fontes institucionais (ACT, DGS, pgdlisboa, FAO, EUR-Lex) mais do que páginas com schema rico. Centralmed não tem JSON-LD detectável e domina 3 clusters AIO. Densidade outbound institucional = sinal E-E-A-T forte.
- **Como validar**: aplicar regra "4+ links externos institucionais" aos primeiros 2 briefs P1 (Q5 + Q4) e medir entrada na AIO em t+90d.
- **Próximo passo**: SEO Lead — promover a regra fixa dos briefs (já no `./BACKLOG.md`).

### Padrão "SEPRI" de árvore pillar + spin-offs

- **Estado**: por validar
- **Origem**: [`.../reports/2026-05-20__competitor-deep-dive.md`](../reports/2026-05-20__competitor-deep-dive.md) §H1
- **Impacto estimado**: alto
- **Esforço estimado**: médio
- **Hipótese**: SEPRI domina AIO Q1 com 3 URLs distintas (pillar + Lisboa + Ficha Aptidão). Padrão replicável: 1 pillar → spin-off geográfico (cidade) + spin-off tópico (sub-conceito). Multiplica share-of-citation.
- **Como validar**: produzir 1 pillar + 2 spin-offs para o cluster Medicina do Trabalho e medir share-of-citation em t+90/180d.
- **Próximo passo**: planear spin-offs desde início ao escrever os briefs P1 (não como afterthought).

### Vídeo curto como acelerador de citação AIO

- **Estado**: hipótese
- **Origem**: [`.../reports/2026-05-20__aio-expansion.md`](../reports/2026-05-20__aio-expansion.md) §L1
- **Impacto estimado**: médio
- **Esforço estimado**: alto (produção)
- **Hipótese**: YouTube aparece em 4/5 AIOs capturadas (Q1, Q3, Q4, Q5). Vídeo curto (1–5 min) explicativo embebido numa página textual pode reforçar a citação AIO.
- **Como validar**: ver se as páginas textuais que ranqueiam **e** têm vídeo embebido têm citação AIO mais estável; experimento controlado (1 pillar com vídeo, 1 sem).
- **Próximo passo**: parquear até pillars textuais P1 estarem publicados.

## Oportunidades descartadas

*Vazio.*
