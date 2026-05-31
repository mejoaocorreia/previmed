# Worklog — Auditoria SEO/UX/Concorrência Previmed

**Projeto:** previmed.pt  
**Data de início:** 2026-05-31  
**Tipo:** Auditoria read-only completa  
**Autor:** SEO Growth System / Análise assistida  

---

## Ferramentas disponíveis

- WebFetch (fetch + parse de HTML para markdown)
- WebSearch (pesquisa web para descoberta de concorrentes)
- Write/Read/Edit (criação de ficheiros)
- Bash + Python stdlib (para gerar .docx)
- Playwright MCP: NÃO disponível nesta sessão (não encontrado no runtime)

**Limitação de screenshots:** sem Playwright, screenshots reais não são possíveis. Análise visual feita via HTML/markdown renderizado pelo WebFetch.

---

## Log de trabalho

### 2026-05-31

- [x] Estrutura de pastas criada
- [ ] Homepage Previmed analisada
- [ ] robots.txt analisado
- [ ] sitemap.xml analisado
- [ ] Páginas de serviço analisadas
- [ ] Concorrentes descobertos
- [ ] Concorrentes analisados um a um
- [ ] Ficheiros intermédios escritos
- [ ] Relatório Word gerado

---

## Decisões tomadas

- Análise baseada em WebFetch (HTML→markdown) + WebSearch
- Screenshots: não disponíveis sem Playwright MCP — registado como limitação
- Word gerado via Python stdlib (zipfile + OOXML) via Bash
- Nenhuma alteração em produção

---

## Limitações registadas

1. Sem Playwright MCP → sem screenshots reais
2. Sem GSC/GA4 → sem dados de tráfego/queries reais
3. Sem crawl completo → análise página a página via URLs encontradas
4. Sem PageSpeed API autenticado → performance não medida com CrUX/field data
5. Sem acesso WordPress admin → configurações internas não visíveis
