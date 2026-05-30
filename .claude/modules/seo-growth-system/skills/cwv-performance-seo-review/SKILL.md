---
name: cwv-performance-seo-review
description: Procedimento para diagnosticar Core Web Vitals e performance como fator de SEO/UX — medir LCP, INP e CLS, identificar causas, distinguir lab de field data, e recomendar sem destruir design.
---

# Skill: Core Web Vitals / Performance SEO Review

Procedimento operacional para diagnosticar Core Web Vitals e performance como factor de SEO e UX.

Esta skill é usada principalmente pelo [`cwv-performance-seo`](../../agents/cwv-performance-seo.md) para conduzir diagnósticos de performance estruturados.

Esta skill não é um agente.  
Esta skill não implementa optimizações.  
Esta skill não inventa métricas de performance.  
Esta skill define o procedimento para diagnosticar CWV de forma consistente.

---

## Objetivo

Diagnosticar o estado de LCP, INP e CLS de páginas prioritárias, identificar causas técnicas, distinguir lab data de field data, e recomendar correcções que melhorem performance sem comprometer design ou UX.

---

## Quando usar

Usar nos modos:

- `/seo performance` — modo principal;
- `/seo audit` — componente de performance na auditoria;
- `/seo go-live` — validação de performance antes de go-live.

---

## Quando não usar

Não usar para:

- redesign visual ou UX — coordenar com Visual Experience;
- implementar em WordPress — usar `wordpress-seo-implementation`;
- análise de dados históricos GSC CWV — usar `gsc-ga4-analysis`.

---

## Quem pode usar

Principal:

- [`cwv-performance-seo`](../../agents/cwv-performance-seo.md)

Também pode usar:

- [`technical-seo`](../../agents/technical-seo.md) para componente técnico de CWV;
- [`seo-qa`](../../agents/seo-qa.md) para validação antes de go-live.

---

## Fontes de verdade

1. [`../../project/TECHNICAL_RULES.md`](../../project/TECHNICAL_RULES.md) — alvos CWV, regras de performance.
2. [`../../project/QUALITY_GATE.md`](../../project/QUALITY_GATE.md) — critérios de aprovação.
3. [`../../project/TOOLING_MODEL.md`](../../project/TOOLING_MODEL.md) — ferramentas disponíveis.

---

## Inputs necessários

- URLs ou templates a medir;
- acesso a PageSpeed Insights (obrigatório);
- acesso a CrUX / Search Console CWV (com autorização, quando disponível);
- contexto WordPress: tema, plugins de cache, image plugins;
- ambiente: staging ou produção.

---

## Procedimento

### Passo 1 — Identificar páginas a medir

Priorizar:
- Homepage (maior tráfego, representa marca).
- Páginas de serviço principais (maior impacto comercial).
- Templates mais usados (representativos de todo o site).
- Páginas com queda de tráfego (se aplicável).

---

### Passo 2 — Medir LCP, INP, CLS

**Obrigatório: mobile first.**

**PageSpeed Insights (lab data):**
- Medir URL em mobile.
- Medir URL em desktop.
- Registar: LCP, INP, CLS, FCP, TTFB, TBT, Speed Index.
- Registar estado: Bom (verde) / Precisa de melhorias (laranja) / Mau (vermelho).

**CrUX / Search Console (field data):**
- Se disponível e autorizado: registar CrUX origin e URL.
- Separar dados mobile de desktop.
- Se não disponível: declarar "field data não disponível" — não inventar.

**Diferença lab vs field:**
- Lab data: condições controladas, conexão simulada, sem cache de utilizador.
- Field data: experiências reais de utilizadores, incluindo variações de rede, dispositivo e cache.
- Diferenças entre lab e field são comuns — declarar qual está a ser usado em cada recomendação.

---

### Passo 3 — Diagnosticar LCP

**Identificar o elemento LCP:**
- Chrome DevTools: Performance tab → LCP marker → que elemento?
- PageSpeed: "Largest Contentful Paint element" na auditoria.
- Tipo: imagem hero, bloco de texto, video thumbnail?

**Causas comuns de LCP lento:**

| Causa | Diagnóstico | Impacto típico |
|---|---|---|
| Imagem hero sem preload | LCP image não tem `<link rel="preload">` | Alto |
| Imagem hero com lazy load | `loading="lazy"` na imagem LCP | Alto |
| Imagem pesada não optimizada | Tamanho em bytes elevado, sem WebP | Alto |
| TTFB alto | Servidor lento, sem cache, redirect chain | Alto |
| Render-blocking JS | Scripts sem `defer` ou `async` above fold | Médio-alto |
| Render-blocking CSS | CSS externo não crítico above fold | Médio |
| Server-side rendering lento | PHP/WordPress a demorar | Médio-alto |

---

### Passo 4 — Diagnosticar INP

**Causas comuns de INP alto:**

| Causa | Diagnóstico |
|---|---|
| Long tasks > 50ms | Performance timeline no DevTools |
| Third-party scripts pesados | Scripts externos (analytics, chat, ads) a bloquear |
| Event handlers pesados | Click/scroll handlers com muito JS |
| Page builder JS excessivo | Elementor, Divi, etc. a carregar JS global |
| Input delay em mobile | Thread principal ocupada no load |

---

### Passo 5 — Diagnosticar CLS

**Identificar elementos que causam shift:**
- Chrome DevTools: Layout Shift markers na Performance tab.
- PageSpeed: "Avoid large layout shifts" auditoria.

**Causas comuns de CLS:**

| Causa | Diagnóstico |
|---|---|
| Imagens sem width/height | HTML sem atributos de dimensão |
| Fontes web com FOUT | `font-display: swap` não activo ou problemático |
| Ads sem espaço reservado | Banner sem dimensão fixa definida |
| Conteúdo injectado por JS | Dinâmico a aparecer acima de conteúdo fixo |
| Animações com transform | CSS que muda layout em vez de transform |
| Cookie banners | Aparecem sobre o conteúdo sem espaço reservado |

---

### Passo 6 — Verificar outras métricas relevantes

- **FCP (First Contentful Paint):** < 1.8s (bom). Alta correlação com LCP.
- **TTFB (Time to First Byte):** < 800ms (bom). Indica velocidade do servidor.
- **TBT (Total Blocking Time):** < 200ms (bom). Relacionado com INP.
- **Speed Index:** menor é melhor. Indica rapidez de preenchimento visual.

---

### Passo 7 — Priorizar recomendações

Para cada problema:

- **Impacto na métrica:** Crítico / Alto / Médio / Baixo.
- **Impacto na UX:** melhora, neutro, ou pode piorar?
- **Esforço de implementação:** pequeno, médio, grande.
- **Handoff:** WordPress Engineering, Visual Experience, wordpress-seo-implementation?

Priorizar: impacto alto + esforço baixo + sem risco visual.

---

### Passo 8 — Declarar validação

**Declarar explicitamente:**
- "Medido com PageSpeed Insights em [data] — lab data, mobile."
- "CrUX não disponível para esta URL."
- "Field data do Search Console: não autorizado / não disponível."
- "Não testado: [o que ficou por verificar]."

---

## Output esperado

```md
## CWV Performance SEO Review — [URL/Template] — YYYY-MM-DD

### Dados usados
- Lab data: PageSpeed Insights [data]
- Field data: [disponível via CrUX / não disponível / não autorizado]

### Estado actual
| Métrica | Mobile | Desktop | Estado |
|---|---|---|---|
| LCP | X.Xs | X.Xs | [Bom/Precisa/Mau] |
| INP | Xms | Xms | [...] |
| CLS | X.XX | X.XX | [...] |
| TTFB | Xms | — | [...] |

### Diagnóstico

#### LCP
Elemento LCP: [...]
Causa principal: [...]
Causas adicionais: [...]

#### INP
Causa principal: [...]

#### CLS
Elementos com shift: [...]
Causas: [...]

### Recomendações
| Prioridade | Recomendação | Métrica | Impacto UX | Esforço | Handoff |
|---|---|---|---|---|---|

### Não validado / a confirmar
[field data, dispositivos específicos, impacto visual das correcções]

### Handoff
[wordpress-seo-implementation / Visual Experience / Supervisor]
```

---

## Gates de segurança

- Não recomendar optimizações que destroem design ou UX.
- Distinguir sempre lab data de field data.
- Não dizer "CWV bom" com apenas lab data sem field data.
- Não inventar métricas ou scores.
- Não implementar em produção — handoff para wordpress-seo-implementation.

---

## Relação com agentes e docs

- [`cwv-performance-seo`](../../agents/cwv-performance-seo.md) — agente principal.
- [`technical-seo`](../../agents/technical-seo.md) — correlaciona renderização técnica.
- [`wordpress-seo-implementation`](../../agents/wordpress-seo-implementation.md) — implementa correcções.
- [`seo-qa`](../../agents/seo-qa.md) — valida antes de implementação.
- [`TECHNICAL_RULES.md`](../../project/TECHNICAL_RULES.md) — alvos CWV.

---

## Exemplos de pedidos que aceita

- "Aplica o procedimento de CWV review a esta página."
- "Diagnostica os Core Web Vitals do site seguindo este processo."
- "Mede e diagnostica LCP desta landing page."

---

## Erros comuns a evitar

- Medir apenas desktop e ignorar mobile.
- Confundir lab data com field data.
- Inventar CrUX quando não disponível.
- Não identificar elemento LCP específico.
- Recomendar sem indicar handoff.
- Recomendar correcções que partem o design.

---

## Regra final

Performance diagnosticada com evidência.

Lab data mostra o potencial. Field data mostra a realidade.  
O que não foi medido não pode ser declarado como bom.
