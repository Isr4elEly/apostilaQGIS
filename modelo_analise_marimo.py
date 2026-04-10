import marimo

__generated_with = "0.19.9"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    import geopandas as gpd
    import pandas as pd
    import locale
    import numpy as np
    import os
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    from IPython.display import display, Markdown
    pd.options.display.float_format = '{:.4f}'.format
    pd.set_option('display.precision', 4)
    pd.set_option('display.max_rows',500)
    pd.set_option('display.max_column', 20)
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    import warnings
    warnings.filterwarnings('ignore')
    return


if __name__ == "__main__":
    app.run()

