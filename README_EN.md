# Earth Science Python: A Practical Learning Repository

[![Python Testing](https://github.com/USER_NAME/REPO_NAME/actions/workflows/test.yml/badge.svg)](https://github.com/USER_NAME/REPO_NAME/actions/workflows/test.yml)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository provides a structured, hands-on curriculum for Earth and Natural Science researchers and students to master Python for data analysis, visualization, and automation.

## 🌋 Project Goal
Transform manual analysis workflows into automated, reproducible Python pipelines. This project focuses on five core pillars:
1. **Data Processing**: Handling messy laboratory and field data.
2. **Visualization**: Creating publication-quality plots and maps.
3. **Numerical Computation**: Statistical modeling and signal processing.
4. **Geospatial Analysis**: Working with DEMs, Shapefiles, and satellite imagery.
5. **Automation**: Building robust pipelines for large-scale datasets.

---

## 🏗️ Repository Structure
```text
.
├── data/               # Auto-generated Earth Science datasets (CSV, GeoTIFF)
├── notebooks/          # Progressive Jupyter Notebooks (Tutorials & Exercises)
│   ├── 01_basics.ipynb        # Python & Jupyter fundamentals
│   ├── 02_petrology.ipynb     # Rock compositions with NumPy/Pandas
│   ├── 03_structural.ipynb    # Orientation data & Stereonets
│   ├── 04_geospatial.ipynb    # GIS, Rasterio, & Mapping
│   └── 05_automation.ipynb    # Curve fitting & Pipeline automation
├── src/                # Backend scripts
│   ├── data_generator.py      # Realistic dummy data engine
│   ├── solutions.py           # Model answers for exercises
│   └── notebook_generator.py  # Curriculum maintenance script
├── tests/              # Automated grading & validation suite
├── requirements.txt    # Project dependencies
└── README.md           # You are here
```

---

## 🛠️ Tech Stack
- **Core**: `numpy`, `pandas`, `matplotlib`, `seaborn`
- **Science**: `scipy`, `sympy`, `statsmodels`, `scikit-learn`
- **Geospatial**: `geopandas`, `rasterio`, `xarray`, `cartopy`
- **Environment**: `jupyterlab`, `pytest`

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/USER_NAME/REPO_NAME.git
cd REPO_NAME
```

### 2. Set up the environment
It is recommended to use a virtual environment or Conda.
```bash
pip install -r requirements.txt
```

### 3. Generate datasets and notebooks
Initialize the project by generating the training data and exercise files:
```bash
python src/data_generator.py
python src/notebook_generator.py
```

### 4. Launch Jupyter
```bash
jupyter lab
```

---

## 📝 Curriculum Overview

### 01: Basic Syntax and Jupyter
Introduction to Python basics specifically for scientists who are transitioning from Excel or specialized GUI software.

### 02: NumPy/Pandas in Petrology
- Normalizing major element compositions (wt%).
- Handling missing data in laboratory spreadsheets.
- Visualizing chemical trends (Harker diagrams).

### 03: Matplotlib/SciPy in Structural Geology
- Analyzing strike and dip data.
- Implementing coordinate transformations for stereographic projections.
- Filtering outliers from field observations.

### 04: Geospatial Analysis
- Reading/writing Digital Elevation Models (DEM) with `rasterio`.
- Coordinate Reference System (CRS) management.
- Creating maps with `cartopy` and `geopandas`.

### 05: Automation and Curve Fitting
- Implementing linear and non-linear regression using `scipy.optimize`.
- Building an end-to-end pipeline: "Read -> Filter -> Fit -> Plot".

---

## ✅ Validation and Testing
Each exercise in the notebooks has a corresponding test case. You can verify your solutions by running:
```bash
pytest
```

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
