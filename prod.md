---
marp: true
theme: custom-tech
paginate: true
header: "Product Documentation — Marp Presentation"
footer: "© 2025 Software Documentation System"
---

<!-- class: lead -->   <!-- REQUIRED DIRECTIVE = FIX -->

<style>
section { font-family: "Inter", sans-serif; }
h1,h2,h3 { color:#003366; }
p { font-size:1.05rem; }
footer { font-size:0.7rem; }
</style>

<style id="custom-tech">
:root {
  --bg:#ffffff;
  --text:#111111;
  --primary:#003366;
}
section { background:var(--bg); color:var(--text); }
section.title {
  background:linear-gradient(135deg,#00234e,#0063c7);
  color:white; text-align:center;
}
</style>

# Product Documentation Presentation  
**Maintained through GitHub + Markdown (Marp)**  
Email: **24f2003573@ds.study.iitm.ac.in**

---

<!-- paginate: true --> <!-- SECOND VALID DIRECTIVE -->

## Why Marp for Product Docs?

- Markdown → fully version-controlled  
- Export to PDF / PPTX / HTML  
- Custom themes + reusable structure  
- Dev-friendly documentation workflow  

---

<!-- _backgroundImage: "https://images.unsplash.com/photo-1518770660439-4636190af475" -->
<!-- _backgroundSize: cover -->

# System Workflow Architecture

---

## Complexity Equations

\[
T(n) = O(\log n)
\]

\[
S(n) = O(n\log n)
\]

---

## Export Commands

```bash
marp product-doc.md --pdf
marp product-doc.md --html
marp product-doc.md --pptx
