import fs from "node:fs";
import path from "node:path";

const docsDir = path.resolve("docs");
const linkPattern = /\[[^\]]*]\(([^)]+)\)/g;
const ignorePrefixes = ["http://", "https://", "mailto:", "#"];

function listMarkdownFiles(dir) {
  const out = [];
  for (const item of fs.readdirSync(dir, { withFileTypes: true })) {
    if (item.name === ".vitepress" || item.name === "public") continue;
    const full = path.join(dir, item.name);
    if (item.isDirectory()) out.push(...listMarkdownFiles(full));
    if (item.isFile() && full.endsWith(".md")) out.push(full);
  }
  return out;
}

function normalizeTarget(sourceFile, rawTarget) {
  const target = rawTarget.replace(/^<|>$/g, "");
  if (ignorePrefixes.some((p) => target.startsWith(p))) return null;
  const clean = target.split("#")[0].split("?")[0];
  if (!clean) return null;

  if (clean.startsWith("/assets/")) {
    return path.join(docsDir, "public", clean.slice(1));
  }

  if (clean.startsWith("/")) {
    const abs = path.join(docsDir, clean.slice(1));
    if (path.extname(abs)) return abs;
    if (fs.existsSync(`${abs}.md`)) return `${abs}.md`;
    return path.join(abs, "index.md");
  }

  const base = path.dirname(sourceFile);
  const candidate = path.resolve(base, clean);
  if (path.extname(candidate)) return candidate;
  if (fs.existsSync(`${candidate}.md`)) return `${candidate}.md`;
  return path.join(candidate, "index.md");
}

const files = listMarkdownFiles(docsDir);
const broken = [];

for (const file of files) {
  const content = fs.readFileSync(file, "utf8");
  const matches = content.matchAll(linkPattern);
  for (const match of matches) {
    const resolved = normalizeTarget(file, match[1].trim());
    if (!resolved) continue;
    if (!fs.existsSync(resolved)) {
      broken.push(`${file}: ${match[1]} -> ${resolved}`);
    }
  }
}

if (broken.length > 0) {
  console.error("Link validation failed:");
  for (const b of broken) console.error(`- ${b}`);
  process.exit(1);
}

console.log(`Link validation passed (${files.length} markdown files).`);
