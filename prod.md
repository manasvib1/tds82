---
marp: true
theme: custom-tech
paginate: true
header: "Product Documentation — Marp Presentation"
footer: "© 2025 Software Documentation System"
---

<!-- ================= Custom Global Theme ================= -->

<style>
section {
  font-family: "Inter", sans-serif;
}
h1, h2, h3 {
  color: #003366;
}
p {
  font-size: 1.05rem;
}
footer {
  font-size: 0.7rem;
}
</style>

<style id="custom-tech">
:root {
  --bg: #ffffff;
  --text: #111111;
  --primary: #003366;
}

section {
  background: var(--bg);
  color: var(--text);
}
section.title {
  background: linear-gradient(135deg, #00234e, #0063c7);
  color: white;
  text-align: center;
}
</style>

<!-- ================= Slide 1 ================= -->

# Product Documentation Presentation  
**Maintained through GitHub + Markdown (Marp)**  
Email: **24f2003573@ds.study.iitm.ac.in**

---

## Why Marp for Product Docs?

- Markdown → fully version-controlled  
- Render to PDF / PPTX / HTML from one file  
- Custom themes + templates reusable  
- Ideal for engineering documentation workflows  

---

<!-- ================= Background Image Slide ================= -->

![bg](https://images.unsplash.com/photo-1518770660439-4636190af475)
# System Workflow Overview

- Docs authored in Markdown  
- Marp engine compiles slides → Dev-friendly  
- CI/CD automated builds possible  

---

## Equation + Complexity

Search Module Complexity:

\[
T(n)=O(\log n)
\]

Full-scale indexed documentation:

\[
S(n)=O(n\cdot\log n)
\]

---

## Export Commands

```bash
marp product-doc.md --pdf
marp product-doc.md --html
marp product-doc.md --pptx
