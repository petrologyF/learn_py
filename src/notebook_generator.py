import json
import os

def create_notebook(filename, cells):
    nb = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.10.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)

def md_cell(text):
    return {"cell_type": "markdown", "metadata": {}, "source": [text]}

def code_cell(source):
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": [source]}

# Chapter 1
ch1_cells = [
    md_cell("# Chapter 1: Basic Python and Jupyter\n\nThis notebook introduces basic Python syntax and how to use Jupyter."),
    code_cell("print('Hello, Earth Science!')"),
    md_cell("## Exercise 1-1\nImplement a function that returns the square of a number."),
    code_cell("def exercise_ch01_square(n):\n    # TODO: Implement\n    pass")
]

# Chapter 2
ch2_cells = [
    md_cell("# Chapter 2: NumPy and Pandas in Petrology\n\nHandling rock composition data."),
    code_cell("import pandas as pd\nimport numpy as np\ndf = pd.read_csv('../data/rock_composition.csv')\ndf.head()"),
    md_cell("## Exercise 2-1: Normalization\nNormalize the wt% to sum to 100%."),
    code_cell("def exercise_ch02_composition(df):\n    # TODO: Implement\n    pass")
]

# Chapter 3
ch3_cells = [
    md_cell("# Chapter 3: Matplotlib and SciPy in Structural Geology\n\nVisualizing orientation data."),
    code_cell("import pandas as pd\ndf = pd.read_csv('../data/structural_faults.csv')\ndf.head()"),
    md_cell("## Exercise 3-1: Filter Outliers\nRemove dips outside [0, 90]."),
    code_cell("def exercise_ch03_filter_outliers(df):\n    # TODO: Implement\n    pass")
]

# Chapter 4
ch4_cells = [
    md_cell("# Chapter 4: Geospatial Analysis with Geopandas and Rasterio\n\nWorking with DEM and GIS data."),
    code_cell("import rasterio\n# Open the synthetic DEM\nwith rasterio.open('../data/synthetic_dem.tif') as src:\n    data = src.read(1)\n    print(data.shape)"),
    md_cell("## Exercise 4-1: DEM Stats\nReturn min, max, mean of the DEM."),
    code_cell("def exercise_ch04_dem_stats(tif_path):\n    # TODO: Implement\n    pass")
]

# Chapter 5
ch5_cells = [
    md_cell("# Chapter 5: Automation and Curve Fitting\n\nAutomating the analysis pipeline."),
    code_cell("from scipy import optimize\nimport numpy as np\n# Sample data\nx = np.linspace(0, 10, 100)\ny = 2.5 * x + 5 + np.random.normal(0, 1, 100)"),
    md_cell("## Exercise 5-1: Linear Fitting\nFit y = ax + b and return (a, b)."),
    code_cell("def exercise_ch05_linear_fit(x, y):\n    # TODO: Implement\n    pass")
]

if __name__ == "__main__":
    notebook_dir = "notebooks"
    if not os.path.exists(notebook_dir):
        os.makedirs(notebook_dir)
    
    create_notebook(os.path.join(notebook_dir, "01_basic_syntax_and_jupyter.ipynb"), ch1_cells)
    create_notebook(os.path.join(notebook_dir, "02_numpy_pandas_petrology.ipynb"), ch2_cells)
    create_notebook(os.path.join(notebook_dir, "03_matplotlib_scipy_structural.ipynb"), ch3_cells)
    create_notebook(os.path.join(notebook_dir, "04_geospatial_analysis.ipynb"), ch4_cells)
    create_notebook(os.path.join(notebook_dir, "05_automation_and_fitting.ipynb"), ch5_cells)
    print("Notebooks generated successfully.")
