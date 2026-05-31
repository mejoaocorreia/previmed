# AI Search, Schema e Entidades — Previmed

**Data:** 2026-05-31

---

## 1. Estado atual do schema

**Schema JSON-LD detectado:** NENHUM em qualquer página analisada.

Este é um problema significativo:
- Sem schema, o Google não tem dados estruturados para rich snippets
- Sem schema, entidades da Previmed não são reconhecidas formalmente
- Sem FAQPage schema, não há eligibilidade para FAQ rich results
- Sem LocalBusiness schema, local SEO fica mais fraco

---

## 2. Schema recomendado por página

### Homepage

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Previmed",
  "alternateName": "Previmed – Centro de Medicina Ocupacional, Lda.",
  "url": "https://previmed.pt",
  "logo": "https://previmed.pt/[logo-url]",
  "foundingDate": "1995",
  "description": "Serviços de Segurança e Saúde no Trabalho, Medicina Ocupacional e Formação Profissional certificados pela ACT, DGS e DGERT.",
  "hasCredential": ["ACT", "DGS", "DGERT", "ISO 9001:2015"],
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+351213161899",
    "contactType": "customer service",
    "areaServed": "PT",
    "availableLanguage": "Portuguese"
  },
  "sameAs": [
    "https://pt.linkedin.com/company/previmed",
    "https://www.facebook.com/PrevimedGrupo/"
  ]
}
```

**Nota:** Usar apenas URLs e dados reais e verificados. Não inventar sameAs ou hasCredential.

---

### /contactos/ — LocalBusiness (2 localizações)

```json
{
  "@context": "https://schema.org",
  "@type": "MedicalBusiness",
  "name": "Previmed Lisboa",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Avenida da Liberdade, 244, 3.º andar",
    "postalCode": "1250-149",
    "addressLocality": "Lisboa",
    "addressCountry": "PT"
  },
  "telephone": "+351213161899",
  "url": "https://previmed.pt/contactos/"
}
```

*(Repetir para Porto com dados reais)*

**Nota:** Confirmar morada exata e telefone antes de implementar.

---

### /saude-no-trabalho/ — Service + FAQPage

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "Medicina do Trabalho",
  "provider": {
    "@type": "Organization",
    "name": "Previmed"
  },
  "description": "Serviço de Medicina do Trabalho certificado pela ACT e DGS...",
  "areaServed": "PT",
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Exames de Saúde Ocupacional",
    "itemListElement": [
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Exames Periódicos"}},
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Exames de Admissão"}}
    ]
  }
}
```

*(Mais esquema FAQPage quando FAQs forem adicionadas)*

---

### Páginas de formação — Course

```json
{
  "@context": "https://schema.org",
  "@type": "Course",
  "name": "[Nome do Curso]",
  "description": "[Descrição]",
  "provider": {
    "@type": "Organization",
    "name": "Previmed"
  },
  "courseMode": "blended",
  "educationalCredentialAwarded": "[Certificação emitida]"
}
```

**Nota:** Usar apenas quando dados reais do curso (nome, duração, certificação) estiverem visíveis e verificados.

---

## 3. Citabilidade para AI Search (AI Overviews / AI Mode)

### O que torna uma página citável em AI Overviews

1. **Resposta direta à pergunta** no início do conteúdo
2. **Estrutura clara:** H2 com pergunta, parágrafo com resposta
3. **FAQs bem escritas** (visíveis, não só em schema)
4. **Autoridade:** ACT/DGS/DGERT são sinais de autoridade reconhecíveis
5. **Sem contradições:** conteúdo consistente em todo o site

### Estado atual da Previmed para AI Search

| Critério | Estado | Problema |
|---------|--------|---------|
| Respostas diretas no topo das páginas | ❌ Ausente | Conteúdo não orientado à resposta |
| FAQs estruturadas | ❌ Ausente | Nenhuma FAQ em nenhuma página |
| Conteúdo específico e verificável | ⚠️ Parcial | Lei 102/2009 citada mas pouco mais |
| Autoridade institucional comunicada | ✅ ACT/DGS/DGERT | Forte, mas não em todas as páginas |
| Entidades nomeadas e consistentes | ⚠️ Parcial | "Previmed", "Medicina do Trabalho" OK |
| Dados concretos (anos, números) | ❌ Ausente | Sem métricas de impacto |
| Schema | ❌ Ausente | Sem dados estruturados |

**Conclusão:** A Previmed não está preparada para AI Search. Zero FAQs + zero schema + conteúdo breve = probabilidade baixa de ser citada em AI Overviews.

---

## 4. Entidades relevantes para schema/AI

### Entidades que a Previmed deve reforçar

| Entidade | Tipo | Como reforçar |
|---------|------|--------------|
| Previmed | Organization | Homepage + sameAs LinkedIn/Facebook |
| Medicina do Trabalho | Service | Página de serviço + schema |
| Segurança e Saúde no Trabalho | Service | Página pilar + schema |
| ACT | CredentialOf | Mencionada mas sem link oficial |
| DGS | CredentialOf | Mencionada mas sem link oficial |
| DGERT | CredentialOf | Mencionada mas sem link oficial |
| ISO 9001 | CertificationOf | Mencionada, certificado linkado |
| Lei 102/2009 | LegalDocument | Citada — manter e expandir |
| Lisboa | Place | LocalBusiness schema |
| Porto | Place | LocalBusiness schema |

---

## 5. Perguntas prioritárias para responder (AI-ready)

Estas são as perguntas mais prováveis de aparecer em AI Search para o setor da Previmed.  
Devem ter resposta clara e direta em páginas relevantes:

1. **"É obrigatório ter medicina do trabalho na empresa?"**  
   → Resposta: Sim, Lei 102/2009. Empresas com pelo menos 1 trabalhador.  
   → Página: /saude-no-trabalho/ + /guias/medicina-no-trabalho-obrigatoria/

2. **"Quantos exames de medicina do trabalho por ano?"**  
   → Resposta: Periódicos anuais (<18, >50, trabalho noturno) ou bienais.  
   → Página: FAQ em /saude-no-trabalho/

3. **"O que é uma avaliação de riscos profissionais?"**  
   → Resposta: Processo de identificar, avaliar e controlar riscos no posto de trabalho.  
   → Página: /avaliacoes-de-riscos-profissionais/ + FAQ

4. **"Que formação é obrigatória em segurança no trabalho?"**  
   → Resposta: Depende do setor; evacuação, primeiros socorros, SST básico são comuns.  
   → Página: /formacao/ + guia

5. **"Que diferença há entre saúde ocupacional e medicina do trabalho?"**  
   → Resposta: Termos frequentemente usados como sinónimos. Diferenças subtis.  
   → Página: FAQ ou guia

---

## 6. Recomendações prioritárias

| Prioridade | Ação | Impacto |
|-----------|------|---------|
| 1 | Implementar schema Organization na homepage | Médio |
| 2 | Implementar schema LocalBusiness em /contactos/ | Alto (local SEO) |
| 3 | Implementar schema Service nas páginas de serviço | Médio |
| 4 | Adicionar FAQs em /saude-no-trabalho/ + schema FAQPage | Alto (AI Search) |
| 5 | Adicionar FAQs em /seguranca-no-trabalho/ + schema FAQPage | Alto (AI Search) |
| 6 | Implementar schema Course em /oferta-formativa/ e /e-learning/ | Médio |
| 7 | Implementar BreadcrumbList em todas as páginas | Médio |
| 8 | Criar conteúdo orientado a perguntas diretas | Alto (AI Search) |

**Nota:** Implementar schema APENAS quando o conteúdo visível na página for consistente com o schema. Nunca criar schema para conteúdo que não existe.
