# File Map

> Última atualização: 2026-05-19
> Estado: **greenfield** — sem tema WordPress instalado ainda.

## Estado atual

Este projeto só tem `.claude/` neste momento. Não existem:

- tema WordPress;
- templates;
- assets;
- páginas WP;
- ficheiros PHP de site.

Este ficheiro será preenchido a partir da **Fase 4** (instalação WordPress local + criação/seleção de tema), conforme definido em `PROJECT_CONTEXT.md`.

## Estrutura esperada (a confirmar na Fase 4)

```
previmed.pt/
├── .claude/                     # equipa AI (já existe)
├── wp-content/
│   ├── themes/
│   │   └── previmed/            # tema custom OU child theme
│   │       ├── style.css
│   │       ├── functions.php
│   │       ├── header.php
│   │       ├── footer.php
│   │       ├── template-parts/
│   │       ├── assets/
│   │       │   ├── css/
│   │       │   ├── js/
│   │       │   └── img/
│   │       └── inc/
│   │           ├── enqueue.php
│   │           ├── schema.php   # JSON-LD custom (Organization, Course, etc.)
│   │           └── seo.php      # integração com plugin SEO
│   └── plugins/
│       └── [plugin-seo]/        # Rank Math ou Yoast (a decidir)
└── wp-config.php                # gitignored
```

## Mapeamento por área (placeholder)

### Homepage
- Template: _a definir_
- Template parts: _a definir_
- CSS: _a definir_
- JS: _a definir_

### Serviços (hub + páginas individuais)
- Template hub: _a definir_
- Template single service: _a definir_

### Formação (sub-hub)
- Template hub: _a definir_
- Template single course: _a definir_
- Schema: `Course`

### Portal trabalhador
- _Decisão pendente_: página WP ou aplicação separada (subdomínio)?

### E-learning
- _Decisão pendente_: plataforma própria, LMS WP (LearnDash/LifterLMS), ou serviço externo?

### Páginas institucionais
- Sobre, Certificações, Contactos, Recrutamento, Notícias/Campanhas

### SEO técnico
- Schema central: `Organization` (+ `hasCredential` para ACT/DGS/DGERT/ISO)
- Sitemap: gerado pelo plugin SEO
- Robots: standard + bloquear áreas portal
- Meta: gerada pelo plugin SEO + overrides em campos custom

## Regra

À medida que se criam/alteram ficheiros do tema, atualizar este mapa com:
- caminho real;
- responsabilidade;
- agente responsável pela manutenção.
