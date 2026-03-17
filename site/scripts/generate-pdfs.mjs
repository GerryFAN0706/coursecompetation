import fs from "node:fs";
import path from "node:path";
import PDFDocument from "pdfkit";

const root = process.cwd();
const repoRoot = path.resolve(root, "..");
const outputDir = path.resolve(root, "docs/public/assets/docs");

const sources = [
  {
    inPath: path.join(repoRoot, "课堂教学视频选题与AI应用方案.md"),
    outPath: path.join(outputDir, "D03_课堂视频选题与AI应用方案.pdf"),
    title: "D03 课堂教学视频选题与AI应用方案"
  },
  {
    inPath: path.join(repoRoot, "第十五讲存在缺陷的示例工程设计方案.md"),
    outPath: path.join(outputDir, "D04_存在缺陷的示例工程设计方案.pdf"),
    title: "D04 第十五讲存在缺陷的示例工程设计方案"
  },
  {
    inPath: path.join(repoRoot, "第十五讲课堂实录逐分钟讲稿.md"),
    outPath: path.join(outputDir, "D05_课堂实录逐分钟讲稿.pdf"),
    title: "D05 第十五讲课堂实录逐分钟讲稿"
  },
  {
    inPath: path.join(repoRoot, "第十五讲AI提示词与测试清单.md"),
    outPath: path.join(outputDir, "D06_AI提示词与测试清单.pdf"),
    title: "D06 第十五讲AI提示词与测试清单"
  },
  {
    inPath: path.join(repoRoot, "第十五讲录课示例工程-问题版/README.md"),
    outPath: path.join(outputDir, "D07_问题版工程README.pdf"),
    title: "D07 问题版工程 README"
  }
];

function pickFont() {
  const candidates = [
    "C:/Windows/Fonts/simhei.ttf",
    "C:/Windows/Fonts/msyh.ttf",
    "C:/Windows/Fonts/arialuni.ttf"
  ];
  for (const f of candidates) {
    if (fs.existsSync(f)) return f;
  }
  return null;
}

function toPdf({ inPath, outPath, title }, fontPath) {
  if (!fs.existsSync(inPath)) {
    throw new Error(`Missing source file: ${inPath}`);
  }
  const text = fs.readFileSync(inPath, "utf8");

  const doc = new PDFDocument({ margin: 48, size: "A4" });
  const stream = fs.createWriteStream(outPath);
  doc.pipe(stream);

  if (fontPath) {
    doc.font(fontPath);
  }

  doc.fontSize(16).text(title, { align: "left" });
  doc.moveDown(0.8);
  doc.fontSize(10).fillColor("#666666").text(`Source: ${path.basename(inPath)}`);
  doc.moveDown(1.2);
  doc.fillColor("#111111").fontSize(11).text(text, {
    width: 500,
    align: "left",
    lineGap: 2
  });
  doc.end();

  return new Promise((resolve, reject) => {
    stream.on("finish", resolve);
    stream.on("error", reject);
  });
}

async function main() {
  fs.mkdirSync(outputDir, { recursive: true });
  const fontPath = pickFont();
  for (const item of sources) {
    await toPdf(item, fontPath);
    console.log(`Generated ${path.basename(item.outPath)}`);
  }
}

main().catch((err) => {
  console.error(err.message);
  process.exit(1);
});
