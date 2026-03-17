# VitePress Competition Website (Phase 1)

This folder contains the deployable website for the AI competition track.

## Local development

```bash
npm install
npm run docs:dev
```

## Validation and build

```bash
npm run validate
npm run docs:build
npm run docs:preview
```

## Deployment

- GitHub Pages mode: project site
- Base path: `/coursecompetation/`
- Active workflow: `/.github/workflows/deploy-vitepress-pages.yml`

## Content contracts

- Required frontmatter fields:
  - `title`
  - `description`
  - `lastUpdated`
  - `evidenceLevel` (`draft|internal|public`)
  - `anonSafe` (`true|false`)
- Metrics contract: `docs/data/metrics.json`
- Evidence naming:
  - `Sxx_*.png`
  - `Dxx_*.pdf` or `Dxx_*.md`
  - `Cxx_*.json`

## Branch policy

- `main`: production deployment
- `staging` (optional): preview and review before merging to `main`
