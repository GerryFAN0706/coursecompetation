
Plan

PLAN.md — GitHub Pages + VitePress Competition Website Implementation Plan
Summary
Build a deploy-ready, Chinese-first competition website from your current content repository using VitePress and GitHub Pages (project site), with Phase 1 covering P0+P1 pages.
The site will prioritize judge comprehension in 30-60 seconds, evidence traceability, and fast iteration from existing Markdown assets.

Implementation Changes
1) Repository and project structure
Create website workspace at site/ (keep current teaching/project docs untouched at repo root).
Use structure:
site/docs/ for pages
site/docs/public/ for images/PDF downloadable artifacts
site/docs/.vitepress/ for config/theme/nav/sidebar
site/docs/data/ for chart/metric source files
site/.github/workflows/ for Pages deploy workflow
Keep all source-of-truth planning docs at root and map them into curated page content, not full copy-paste dumps.
2) Stack and baseline setup
Initialize VitePress with npm scripts:
docs:dev
docs:build
docs:preview
Configure base for project-site deployment:
base: "/coursecompetation/" (change only if repo name changes).
Set lang: "zh-CN" and Chinese navigation labels.
Default visual direction:
light-first design
blue/teal institutional palette (no purple bias)
custom typography and non-flat section backgrounds
lightweight motion for counters/section reveals
responsive behavior for desktop and mobile judges.
3) Route map and information architecture (Phase 1: P0+P1)
Implement routes:
/ Home
/innovation/ AI教学创新设计
/cases/lesson-15/ 核心案例：第15讲
/results/ 成效与数据
/resources/ 教学资源
Add secondary but scaffolded placeholders (not fully authored in Phase 1):
/course/, /promotion/, /about/
Home page blocks:
hero value proposition
3 innovation cards
key metrics strip
pre/in/post class loop diagram
fast links to 4 core sections.
Keep first-click navigation depth <= 2 levels for judge speed.
4) Content migration plan (source to destination)
Use website.md as page skeleton master and split into route-specific markdown.
Pull competition story logic from 网站内容映射到人工智能赛道材料.md into innovation/results narrative.
Build lesson-15 case page from:
课堂教学视频选题与AI应用方案.md
第十五讲课堂实录逐分钟讲稿.md
第十五讲存在缺陷的示例工程设计方案.md
第十五讲AI提示词与测试清单.md
Build resources page with:
prompt templates
test checklists
downloadable teaching docs/PDFs
example engineering references.
Add explicit evidence notes on each quantified claim:
source file
metric definition
sample scope/time window placeholder if not finalized yet.
5) Public interfaces and content contracts
Route contract (public URL interface):
/, /innovation/, /cases/lesson-15/, /results/, /resources/, /course/, /promotion/, /about/
Page frontmatter contract:
title
description
lastUpdated
evidenceLevel (draft|internal|public)
anonSafe (true|false)
Metrics data contract in site/docs/data/metrics.json:
id
label
value
unit
baseline
current
source
notes
Evidence asset naming contract:
Sxx_*.png for screenshots
Dxx_*.pdf for documents
Cxx_*.json for chart datasets
align with your existing checklist IDs to reduce audit friction.
6) Deployment and operations
Use GitHub Actions for Pages deployment on push to main.
Deploy from VitePress build output (site/docs/.vitepress/dist).
Enable Pages source as GitHub Actions in repository settings.
Add a pre-deploy validation gate:
build success required
no broken internal links
no missing required frontmatter fields.
Add branch policy:
main for production
optional staging for preview iterations before judge-facing release.
7) Quality, anonymity, and compliance hardening
Build two content modes:
internal/original assets
judge/anonymized assets
Enforce anonymity checklist before public build:
person names
student IDs
school-identifying marks where required by rules
account identifiers in screenshots.
Add trust guards on key numbers:
every core metric must include method note and source pointer.
Add offline fallback plan:
export static build artifact zip as backup for unstable network demos.
8) Execution milestones and Definition of Done
Milestone A (Scaffold)
VitePress runs locally, nav/sidebar configured, route skeleton pages created.
DoD: docs:build passes and local preview shows all Phase-1 routes.
Milestone B (Content Integration)
Home, innovation, lesson-15 case, results, resources populated with curated content.
DoD: Each page has complete narrative, no placeholder lorem, core visuals linked.
Milestone C (Evidence Integration)
Metrics/evidence datasets wired and rendered; resource downloads valid.
DoD: Every key claim has source mapping and one clickable evidence anchor.
Milestone D (Deployment)
GitHub Actions deploy pipeline live to project-site URL.
DoD: public URL accessible on desktop/mobile; last deployment reproducible.
Milestone E (Pre-submission hardening)
Anonymity pass, broken-link pass, final readability and performance pass.
DoD: judge-ready build and offline backup package available.
Test Plan
Local functional checks:
npm install
npm run docs:dev
npm run docs:build
npm run docs:preview
Content integrity checks:
internal links resolve
downloads are reachable
chart/metric data renders without missing fields.
Deployment checks:
workflow succeeds on main
generated Pages URL returns 200 on all Phase-1 routes
mobile viewport readability check (hero, cards, charts, tables).
Acceptance scenarios:
judge can understand innovation model from home page in < 60 seconds
judge can trace one metric to evidence in <= 3 clicks
lesson-15 page clearly shows “problem -> AI-assisted diagnosis -> fix -> verification”.
Assumptions and defaults
Pages mode: Project site (URL shape https://<user>.github.io/<repo>/).
Content language: Chinese-first with English technical terms where pedagogically needed.
Scope: P0+P1 pages only for Phase 1, with scaffold placeholders for other routes.
Build tool: VitePress official theme + targeted custom styling (no heavy third-party template dependency).
This plan is delivered as Markdown content first; implementation starts in a separate execution step.
