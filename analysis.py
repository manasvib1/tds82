# analysis_notebook.py
# Email (for grading / identification):
# 24f2003573@ds.study.iitm.ac.in

import marimo

__generated_with__ = "0.8.17"

app = marimo.App()

@app.cell
def __():
    # Cell 1: Import libraries used in later cells.
    # Exposes `mo` and `np` for downstream cells.
    import marimo as mo
    import numpy as np
    return mo, np


@app.cell
def __(mo):
    # Cell 2: Define interactive UI controls.
    # The slider's value will be used in later cells to control computation.
    samples_slider = mo.ui.slider(
        start=10,
        stop=200,
        step=10,
        value=50,
        label="Number of samples",
    )

    slope_slider = mo.ui.slider(
        start=1,
        stop=10,
        step=1,
        value=3,
        label="Slope (m)",
    )

    samples_slider, slope_slider
    return samples_slider, slope_slider


@app.cell
def __(np, samples_slider, slope_slider):
    # Cell 3: Data generation based on widget state.
    # Depends on Cell 1 (np) and Cell 2 (both sliders).
    # Data flow:
    #   samples_slider.value -> number of points
    #   slope_slider.value   -> slope of linear relation
    n = samples_slider.value
    m = slope_slider.value

    x = np.linspace(0, 1, n)
    noise = np.random.normal(0, 0.1, size=n)
    y = m * x + noise

    x, y, n, m
    return m, n, x, y


@app.cell
def __(mo, x, y, n, m, samples_slider, slope_slider):
    # Cell 4: Dynamic markdown explanation and visualization.
    # Depends on Cells 2 and 3 (variable dependencies).
    # Any change in slider state re-runs this cell.
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.set_title(f"Linear relationship: y = {m}x + noise")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    stats_md = mo.md(
        f"""
# Interactive Data Relationship Demo

This notebook demonstrates a **linear relationship** between variables:

- Number of samples: **{samples_slider.value}**
- Slope (m): **{slope_slider.value}**
- Model: $y = m x + \\text{{noise}}$

When you move the sliders:
- The underlying data `(x, y)` is regenerated in the previous cell.
- This cell re-renders the scatter plot and updates this markdown.

This creates a simple, self-documenting, interactive analysis workflow.
"""
    )

    stats_md, fig
    return fig, stats_md


if __name__ == "__main__":
    app.run()
