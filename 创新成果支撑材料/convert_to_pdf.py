"""Convert all markdown files in 学生作品证据 to PDF using markdown + xhtml2pdf."""
import os
import sys
import io
import markdown
from xhtml2pdf import pisa

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

INPUT_DIR = os.path.join(os.path.dirname(__file__), "学生作品证据")
OUTPUT_DIR = os.path.join(INPUT_DIR, "PDF")
os.makedirs(OUTPUT_DIR, exist_ok=True)

CSS = """
@page {
    size: A4;
    margin: 2cm 2.5cm;
}
body {
    font-family: "SimSun", "Microsoft YaHei", Arial, sans-serif;
    font-size: 11px;
    line-height: 1.8;
    color: #222;
}
h1 { font-size: 20px; color: #1a3a6c; border-bottom: 2px solid #1a3a6c; padding-bottom: 6px; margin-top: 0; }
h2 { font-size: 16px; color: #1a3a6c; margin-top: 20px; border-bottom: 1px solid #ddd; padding-bottom: 4px; }
h3 { font-size: 14px; color: #333; margin-top: 14px; }
h4 { font-size: 12px; color: #555; }
blockquote {
    border-left: 3px solid #1a3a6c;
    background: #f4f7fc;
    padding: 8px 14px;
    margin: 10px 0;
    color: #333;
}
code {
    font-family: "Courier New", monospace;
    font-size: 10px;
    background: #f5f5f5;
    padding: 1px 3px;
}
pre {
    background: #f8f9fa;
    border: 1px solid #e0e0e0;
    padding: 10px 14px;
    font-size: 9px;
    line-height: 1.5;
    white-space: pre-wrap;
    word-wrap: break-word;
}
pre code { background: none; padding: 0; }
table {
    border-collapse: collapse;
    width: 100%;
    margin: 10px 0;
    font-size: 10px;
}
th { background: #1a3a6c; color: #fff; padding: 6px 8px; text-align: left; }
td { padding: 5px 8px; border-bottom: 1px solid #e0e0e0; }
hr { border: none; border-top: 1px solid #ddd; margin: 16px 0; }
strong { color: #1a3a6c; }
"""

EXTENSIONS = ["tables", "fenced_code", "toc", "nl2br"]

md_files = sorted(f for f in os.listdir(INPUT_DIR) if f.endswith(".md"))

for md_file in md_files:
    md_path = os.path.join(INPUT_DIR, md_file)
    pdf_name = md_file.replace(".md", ".pdf")
    pdf_path = os.path.join(OUTPUT_DIR, pdf_name)

    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    html_body = markdown.markdown(md_text, extensions=EXTENSIONS)
    full_html = f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><style>{CSS}</style></head>
<body>{html_body}</body>
</html>"""

    with open(pdf_path, "wb") as pdf_file:
        status = pisa.CreatePDF(full_html, dest=pdf_file)

    if status.err:
        print(f"ERR {md_file}")
    else:
        print(f"OK  {md_file} -> {pdf_name}")

print(f"\nDone. {len(md_files)} files processed. Output: {OUTPUT_DIR}")
