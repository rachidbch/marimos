import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    slider = mo.ui.slider(1, 10, value=3, label="n")
    slider
    return (slider,)


@app.cell
def _(mo, slider):
    mo.md(f"the square root of n is **{slider.value ** 0.5:.3f}**")
    return


if __name__ == "__main__":
    app.run()
