# PLAN.md — GitHub Pages + VitePress Competition Website Implementation Plan

Status: `Implemented (Phase 1 scaffold + content + CI wiring)`

## Summary

Build a deploy-ready, Chinese-first competition website from the current content repository using `VitePress` and `GitHub Pages (project site)`, with Phase 1 covering `P0+P1` pages.

## Implemented scope

1. `site/` workspace with VitePress structure
2. Phase 1 routes:
   - `/`
   - `/innovation/`
   - `/cases/lesson-15/`
   - `/results/`
   - `/resources/`
3. Placeholder routes:
   - `/course/`
   - `/promotion/`
   - `/about/`
4. Data/evidence contracts:
   - `site/docs/data/metrics.json`
   - `site/docs/public/assets/charts/C01-C03`
   - `site/docs/evidence-index.md`
5. Validation gates:
   - frontmatter check
   - internal link check
6. GitHub Actions Pages deploy workflow at:
   - `.github/workflows/deploy-vitepress-pages.yml`

## Assumptions

- GitHub Pages mode is project-site (`/coursecompetation/` base).
- Content language is Chinese-first.
- Node.js 20+ is available in CI and required locally for build commands.

## Next execution checkpoint

Run locally after Node install:

```bash
cd site
npm install
npm run validate
npm run docs:build
```
