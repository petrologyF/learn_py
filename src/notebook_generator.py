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
    md_cell("# Chapter 1: Basic Python and Interactive Learning\n\nThis notebook introduces basic Python and the interactive verification system."),
    md_cell("## Exercise 1-1\nImplement a function that returns the square of a number."),
    code_cell("def exercise_ch01_square(n):\n    \"\"\"\n    Return the square of n.\n    \"\"\"\n    # TODO: Implement\n    pass"),
    md_cell("## Verification and Paste\nRun the cell below to verify your code and copy the result to your clipboard for your learning log."),
    code_cell("from src.verifier import check_and_copy\nresult = exercise_ch01_square(5)\ncheck_and_copy(chapter=1, question=1, output=result)")
]

# Chapter 2
ch2_cells = [
    md_cell("# Chapter 2: Petrology with Pandas\n\nHandling rock composition data and calculating Magnesium Number ($Mg#$)."),
    md_cell("## Background: Magnesium Number ($Mg#$)\n$Mg#$ is an important indicator of mantle melting and differentiation.\n\n$$Mg\\# = 100 \\times \\frac{MgO/40.3}{MgO/40.3 + FeO/71.8}$$\n(Assuming all Fe as FeO for simplicity)"),
    code_cell("import pandas as pd\nimport numpy as np\ndf = pd.read_csv('../data/rock_composition.csv')\ndf.head()"),
    md_cell("## Exercise 2-1: Calculate Mg#\nImplement a function to calculate Mg# for each row and return the updated DataFrame."),
    code_cell("def exercise_ch02_mg_number(df):\n    # TODO: Calculate Mg# and add it as a new column 'Mg_number'\n    pass"),
    md_cell("## Verification"),
    code_cell("from src.verifier import check_and_copy\nresult_df = exercise_ch02_mg_number(df)\ncheck_and_copy(chapter=2, question=1, output=result_df)")
]

# (Other chapters omitted for brevity in this generator update, but follow same pattern)

if __name__ == "__main__":
    notebook_dir = "notebooks"
    if not os.path.exists(notebook_dir):
        os.makedirs(notebook_dir)
    
    create_notebook(os.path.join(notebook_dir, "01_basics_interactive.ipynb"), ch1_cells)
    create_notebook(os.path.join(notebook_dir, "02_petrology_pandas.ipynb"), ch2_cells)
    # create_notebooks for 03, 04, 05 with similar structure...
    print("Interactive Notebooks generated successfully.")
