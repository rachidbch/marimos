import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    # Playground

    A notebook edited live by Claude through *Pair an agent*, saved back to GitHub.
    """)
    return


@app.cell
def _(mo):
    slider = mo.ui.slider(1, 10, value=3, label="n")
    slider
    return (slider,)


@app.cell
def _(mo, slider):
    mo.md(f"n squared is **{slider.value ** 2}**")
    return


if __name__ == "__main__":
    app.run()
