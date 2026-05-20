# Setup — Google Search Console + GA4

> **Lote 2.4 da Fase 2.** Guia passo-a-passo para o utilizador ligar GSC e GA4 e expor os dados ao trabalho SEO.
> Data: 2026-05-20.
> Estado: **aguarda execução do utilizador**.

---

## 0. Antes de começar

Confirmar acessos disponíveis:

- [ ] Conta Google com permissões administrativas no domínio `previmed.pt`.
- [ ] Acesso ao DNS de `previmed.pt` (para verificação por TXT record) **OU** acesso FTP/admin WordPress (para verificação por upload de ficheiro).
- [ ] Conta Google que vai gerir GA4 (idealmente conta de empresa, não pessoal).
- [ ] Confirmar que **GA4 ainda não está configurado** — se Universal Analytics legacy estiver presente, decidir se migrar dados (Google já desligou UA em julho 2023; provavelmente não há nada para migrar).

---

## 1. Google Search Console (GSC)

### 1.1 Criar propriedade

1. Abrir [search.google.com/search-console](https://search.google.com/search-console).
2. Clicar em **"Add property"**.
3. Escolher **"Domain"** (não "URL prefix") — captura todos os subdomínios e protocolos: `previmed.pt`, `www.previmed.pt`, `portal.previmed.pt`, http e https. Recomendado.
4. Inserir `previmed.pt`.
5. GSC pede verificação por **DNS TXT record**.
6. Adicionar o TXT record no painel DNS do registar do domínio (provavelmente um provedor PT — DonDominio, GoDaddy, Cloudflare DNS, etc.). Aguardar propagação (5min a 48h, normalmente <15min).
7. Voltar ao GSC e clicar **"Verify"**.

### 1.2 Submeter sitemap

1. Sidebar → **Sitemaps**.
2. Inserir `sitemaps.xml` (não `/sitemap.xml` — o robots.txt do Previmed aponta para `sitemaps.xml`, plural).
3. Submit. Aguardar **"Success"** com contagem de URLs (devia ser ~56 entre pages, posts e categories).

### 1.3 Inspecionar URLs prioritárias

Confirmar indexação de:
- [ ] `https://previmed.pt/`
- [ ] `https://previmed.pt/saude-no-trabalho/`
- [ ] `https://previmed.pt/seguranca-no-trabalho/`
- [ ] `https://previmed.pt/seguranca-higiene-alimentar/`
- [ ] `https://previmed.pt/seguranca-ambiental/`
- [ ] `https://previmed.pt/consultoria-formacao/`
- [ ] `https://previmed.pt/sobre-a-previmed/`
- [ ] `https://previmed.pt/contactos/`
- [ ] `https://previmed.pt/pedido-de-proposta/`

Para cada uma, abrir **URL Inspection** e verificar:
- Coverage: `URL is on Google` (✓) ou `URL is not on Google` (⚠️).
- Última crawl date.
- User-declared canonical vs Google-selected canonical (se divergem é red flag).
- Rendered HTML (live test) vs source — para confirmar render JS.

### 1.4 Conceder acesso

Adicionar utilizadores com permissão `Owner` (não `Full user`) para evitar lock-out futuro:
- [ ] me.joaocorreia@gmail.com (já é o teu email)
- [ ] Conta de backup (recomendado — 2.ª conta tua ou outro membro da equipa)

### 1.5 Dados que vamos extrair (depois de 16-28 dias de coleta)

- **Performance** (top queries, top pages) — exportar CSV com filtros: 28d, country=PT, search type=Web.
- **Indexing → Pages** — quantas indexadas vs descobertas, motivos de exclusão.
- **Experience → Core Web Vitals** — quantos URLs em "Poor", "Needs improvement", "Good" para mobile e desktop.
- **Enhancements → Breadcrumbs / Sitelinks searchbox** — validar se schema é reconhecido.
- **Links → External / Internal** — backlinks orgânicos atuais (free, mas amostra limitada).

⚠️ **Nota:** GSC só mostra dados após coletar. Idealmente 16 dias mínimo para qualquer análise, 28d para análise comparativa, 90d+ para tendência.

---

## 2. Google Analytics 4 (GA4)

### 2.1 Criar property

1. Abrir [analytics.google.com](https://analytics.google.com).
2. **Admin** (engrenagem) → **Create** → **Account** se ainda não existe Account ("Previmed - Centro de Medicina Ocupacional Lda").
3. Dentro da Account → **Create property**: nome `previmed.pt — Production`, timezone `(GMT+00:00) Lisbon`, currency `EUR`.
4. **Business details**: HSST B2B, ~10-50 employees, primary objective: leads.
5. **Data streams** → **Web** → URL `https://previmed.pt` → Stream name `previmed.pt Web`.

### 2.2 Instalar tag

Duas opções:

**Opção A — Plugin "Site Kit by Google" (recomendado para WP existente)**
1. WP Admin → Plugins → Add new → "Site Kit by Google" (autor: Google).
2. Activar → Setup wizard → ligar conta Google → autorizar GSC + GA4 + PSI.
3. Site Kit injecta tag GA4 automaticamente.

**Opção B — Google Tag Manager (mais flexível, recomendado para Fase 4 redesign)**
1. Criar container GTM em [tagmanager.google.com](https://tagmanager.google.com) para `previmed.pt`.
2. Inserir snippet GTM no `<head>` e `<body>` do tema WP (via tema custom ou plugin como "Insert Headers and Footers").
3. Dentro do GTM, criar tag **Google Analytics: GA4 Configuration** com Measurement ID da property criada em 2.1.
4. Publish.

**Para já (greenfield, antes da Fase 4):** **Opção A** desbloqueia coleta rapidamente. Migrar para GTM (Opção B) durante o redesign WP em Fase 4.

### 2.3 Configurar eventos & conversões

Eventos automáticos GA4 (enhanced measurement) cobrem: page_view, scroll, click (outbound), file_download, video_*, site_search.

**Eventos custom a configurar:**

| Event name | Trigger | Conversion? |
|---|---|---|
| `lead_form_submit` | Submit do form em `/pedido-de-proposta/` (Contact Form 7) | ✅ sim |
| `phone_click` | Click em `tel:` links (`213 161 899`, `213 161 423`) | ✅ sim |
| `email_click` | Click em `mailto:geral@previmed.pt` | ✅ sim |
| `formacao_inscription` | Submit de form em página de inscrição em curso (quando existir) | ✅ sim |
| `portal_login_attempt` | Click em link para `portal.previmed.pt/login` | ❌ não (engagement) |
| `proposta_intent` | Click em CTA "Pedir proposta" em qualquer página | ❌ não (engagement micro) |

**Como criar:**
- Site Kit / GA4 admin → **Events** → **Create event** (ou via GTM Triggers).
- Marcar como conversão: GA4 Admin → **Conversions** → **New conversion event**.

### 2.4 Conectar GA4 ↔ GSC

GA4 admin → **Search Console links** → **Link** → escolher a property GSC criada em 1.1. Permite ver landing pages orgânicas + queries dentro do GA4.

### 2.5 Dimensions custom (opcional, recomendado)

- `audience` (string) — `empresa` | `formando` | `trabalhador` — populado via dataLayer push baseado em hub visitado.
- `service_area` (string) — `medicina-trabalho` | `seguranca` | `alimentar` | `ambiental` | `formacao`.

Isto desbloqueia análise por audiência (alinhado com 3 personas do `strategy/AUDIENCES.md`).

### 2.6 Acessos

Conceder permissão `Editor` (não `Administrator`) a:
- [ ] me.joaocorreia@gmail.com (já és o owner)
- [ ] Conta backup

---

## 3. PageSpeed Insights API (bónus, free)

### 3.1 Criar API key

1. [console.cloud.google.com](https://console.cloud.google.com).
2. Criar projeto `previmed-seo` (ou usar existente).
3. **APIs & Services** → **Enable APIs** → procurar "PageSpeed Insights API" → Enable.
4. **Credentials** → **Create credentials** → **API key**.
5. **Restrict key** → "HTTP referrers" se for usar do browser, "IP addresses" se for só servidor. Para uso via Claude/scripts locais, restringir por IP do utilizador.

### 3.2 Guardar

Adicionar a `.env` (na raiz do projeto):
```
GOOGLE_PSI_API_KEY=AIza...
```

⚠️ **Não commitar `.env`** — já está em `.gitignore`.

### 3.3 Verificar

```powershell
$key = (Get-Content .env | Select-String 'GOOGLE_PSI_API_KEY=').ToString().Split('=')[1]
Invoke-RestMethod "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://previmed.pt/&strategy=mobile&key=$key"
```

Deve retornar JSON com `lighthouseResult`.

---

## 4. Acessos para o Claude / MCPs (Fase 5)

Quando estes serviços estiverem ligados, há MCPs comunitários para:

- **GSC MCP** — leitura de queries, performance, URL inspection.
- **GA4 MCP** — leitura de eventos, sessions, conversions.

Para esses MCPs precisamos de:

1. **Service Account JSON key** (Google Cloud Console) com permissões:
   - `Search Console: Restricted view` para a property `sc-domain:previmed.pt`.
   - `GA4: Viewer` para a property GA4.
2. Guardar JSON em `~/.config/previmed/gcp-sa.json` (ou similar fora do repo).
3. Adicionar path a `.env`:
   ```
   GOOGLE_APPLICATION_CREDENTIALS=C:\Users\mejoa\.config\previmed\gcp-sa.json
   ```

Não é urgente — fazer só quando houver >= 28 dias de dados em GSC para valer a pena automatizar.

---

## 5. Checklist de extração inicial (após 28d de coleta)

Quando GSC tiver dados (>= 2026-06-17 se ligado hoje), executar:

- [ ] Export CSV: GSC Performance → 28d → tabela queries com >= 5 impressões.
- [ ] Export CSV: GSC Performance → 28d → tabela pages com >= 5 impressões.
- [ ] Anotar **non-brand queries** (excluir "previmed") com impressões mas CTR < 2% → candidatas a otimização imediata.
- [ ] Anotar **queries em posição 11-30** → quick wins para subir a top 10.
- [ ] GA4: sessões orgânicas mensais, top landing pages, conversões `lead_form_submit`.
- [ ] GA4 ↔ GSC: landing pages orgânicas com clicks vs sem clicks → mismatch SERP vs comportamento.
- [ ] PSI: snapshot LCP/INP/CLS para top 10 pages.

Output esperado: `BASELINE_METRICS.md` (Lote 2.5).

---

## 6. Riscos / pitfalls comuns

- **Verificação GSC por meta tag** funciona mas não cobre subdomínios — preferir DNS TXT.
- **Property URL prefix** mostra apenas variantes específicas — sempre **Domain** se possível.
- **Universal Analytics legacy** ainda visível no GSC ou no WP — desligar (já não recolhe desde julho 2023).
- **Site Kit double-tagging** se GTM também estiver instalado: GA4 vai contar tudo 2x. Escolher uma estratégia e seguir.
- **Sampling no GA4** acontece a partir de 10M eventos/mês na property — irrelevante na fase atual.
- **Filtros internal traffic**: criar uma data filter em GA4 admin → **Data Streams** → **Configure tag settings** → **Define internal traffic** → IPs do escritório Previmed. Evita inflacionar métricas.
- **Consent**: se GTM/Site Kit servir tags antes de consentimento, RGPD pode ser quebrado. Validar com a Política de Privacidade existente e com o cookieadmin já instalado.

---

## 7. Próximos passos

| # | Ação | Quem | Quando |
|---|---|---|---|
| 1 | Verificar GSC + submeter sitemap | João | dia 1 |
| 2 | Instalar Site Kit ou GA4 (Opção A) | João | dia 1 |
| 3 | Configurar eventos custom GA4 + marcar conversões | João + Claude | dias 1-7 |
| 4 | Criar API key PSI | João | dia 1 |
| 5 | Aguardar 16-28 dias de coleta | — | até ~2026-06-17 |
| 6 | Executar Lote 2.5 (Baseline Metrics) | Claude | após dia 28 |
| 7 | Avaliar necessidade de MCPs GSC/GA4 com service account | Claude + João | Fase 5 |
