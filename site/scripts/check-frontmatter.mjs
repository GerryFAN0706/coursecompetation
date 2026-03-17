import fs from "node:fs";
import path from "node:path";

const docsDir = path.resolve("docs");
const requiredFields = ["title", "description", "lastUpdated", "evidenceLevel", "anonSafe"];
const validEvidence = new Set(["draft", "internal", "public"]);

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

function parseFrontmatter(content) {
  if (!content.startsWith("---\n")) return null;
  const end = content.indexOf("\n---\n", 4);
  if (end === -1) return null;
  const raw = content.slice(4, end).trim();
  const map = {};
  for (const line of raw.split("\n")) {
    const idx = line.indexOf(":");
    if (idx === -1) continue;
    const k = line.slice(0, idx).trim();
    const v = line.slice(idx + 1).trim();
    map[k] = v;
  }
  return map;
}

const files = listMarkdownFiles(docsDir);
const errors = [];

for (const file of files) {
  const content = fs.readFileSync(file, "utf8");
  const fm = parseFrontmatter(content);
  if (!fm) {
    errors.push(`${file}: missing frontmatter`);
    continue;
  }
  for (const field of requiredFields) {
    if (!(field in fm) || fm[field] === "") {
      errors.push(`${file}: missing field "${field}"`);
    }
  }
  if ("evidenceLevel" in fm && !validEvidence.has(fm.evidenceLevel)) {
    errors.push(`${file}: invalid evidenceLevel "${fm.evidenceLevel}"`);
  }
  if ("anonSafe" in fm && !["true", "false"].includes(fm.anonSafe)) {
    errors.push(`${file}: anonSafe must be true or false`);
  }
}

if (errors.length > 0) {
  console.error("Frontmatter validation failed:");
  for (const err of errors) console.error(`- ${err}`);
  process.exit(1);
}

console.log(`Frontmatter validation passed (${files.length} markdown files).`);
