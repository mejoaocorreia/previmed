# Project Context

> Última atualização: 2026-05-19

## Negócio

**Previmed** — empresa portuguesa de Higiene, Saúde e Segurança no Trabalho (HSST).

Modelo: **B2B** (vende a empresas), com componente de serviço ao **trabalhador/utente** (exames, resultados) e **formando** (e-learning).

Cobertura: **nacional**, via rede de clínicas parceiras em Portugal continental e Ilhas. **Sem morada física única** divulgada como sede comercial → local SEO clássico (GBP central, LocalBusiness schema) **não se aplica** da forma habitual.

## Serviços principais

1. Medicina do trabalho
2. Segurança no trabalho
3. Higiene e segurança alimentar (HACCP)
4. Ambiente / segurança ambiental
5. Formação certificada (35h DGERT, e-learning)
6. Perícias médico-legais (acidentes de trabalho)
7. Exames serológicos
8. Exames médicos para seguradoras
9. Certificações (auditorias / consultoria associada)

## Audiências

| Audiência | Jornada | CTA principal |
|---|---|---|
| **Cliente (empresa)** | Conhecer serviços → pedir proposta → contratar | Pedido de proposta |
| **Trabalhador/utente** | Aceder a portal, ver convocatórias, resultados | Portal trabalhador |
| **Formando** | Procurar formação → inscrição → e-learning | Plataforma e-learning |

→ Site precisa de **separar claramente** estas três jornadas (sem canibalização SEO) e ter dois "modos" de navegação distintos.

## Posicionamento

- Institucional, confiança, compliance regulatório.
- Diferencial real: **certificações ACT, DGS, DGERT, ISO 9001:2015**.
- Tom: profissional, sóbrio, técnico mas acessível.

## Implicações SEO (alto nível)

- **B2B com decisão longa** → conteúdo de autoridade pesa mais que volume; intenção comercial e informacional dominam.
- **Sem GBP forte** → schema `Organization` (não `LocalBusiness`); páginas por **distrito/região coberta** podem fazer sentido se houver query volume.
- **Compliance como ângulo de autoridade** → conteúdo factual citável (forte para AI Search/GEO); usar `hasCredential`, referenciar legislação (Lei 102/2009, Código do Trabalho).
- **Formação certificada** = sub-negócio com SEO próprio → hub com schema `Course`, programas, calendário.
- **Concorrência principal**: outras empresas HSST nacionais (a mapear na Fase 2) + portais institucionais (ACT, DGS) que tipicamente ranqueiam em queries informacionais.

## Estado técnico

| Item | Estado |
|---|---|
| Tema ativo | Não decidido |
| Tema em desenvolvimento | Não existe |
| Ambiente local | A configurar (LocalWP / XAMPP / Docker, decisão pendente) |
| Ambiente staging | Não existe |
| Método de deploy | Não definido |
| URL produção | https://previmed.pt (site existente, fora do scope desta reformulação até decidirmos abordagem) |
| URL staging | — |
| Plugin SEO | A confirmar (preferência inicial: Rank Math free; alternativa: Yoast free) |
| Repositório git | Iniciado em 2026-05-19 |
| GSC | Não configurado para este projeto |
| GA4 | Não configurado para este projeto |

## Precedência SEO

Para tudo o que envolva SEO/Organic Growth, usar **exclusivamente**:

- `.claude/agents/organic-growth/`
- `.claude/skills/organic-growth/`
- `.claude/commands/organic-growth/`

Versões equivalentes na raiz foram arquivadas em `.claude/_archive/` (ver `_archive/README.md`).

## Regras específicas deste projeto

- **Não tocar no site existente** `previmed.pt` em produção até existir um plano explícito de migração/refeito (TBD).
- **Não criar GBP** sem confirmação — pode haver perfis existentes que devem ser consolidados antes.
- **Não submeter formulários reais** no site existente em fase de research.
- Trabalho inicial é **estratégico e documental**, não de implementação. WordPress só entra na Fase 4.
- Conteúdo sobre saúde/medicina exige **rigor factual** — sem promessas, sem conselho médico genérico, sem inventar dados sobre legislação.

## Ambição

Site institucional premium que:
- transmita autoridade e confiança regulatória;
- separe claramente as três jornadas (cliente / trabalhador / formando);
- converta empresas em pedidos de proposta com fricção mínima;
- seja referência orgânica para queries HSST informacionais (citável em AI Overviews);
- tenha performance e acessibilidade exemplares (sector sério, expectativa alta).
