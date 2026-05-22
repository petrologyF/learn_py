# Earth Science Python: Beginner's Guide to Geoscience Data Analysis

[![Python Testing](https://github.com/USER_NAME/REPO_NAME/actions/workflows/test.yml/badge.svg)](https://github.com/USER_NAME/REPO_NAME/actions/workflows/test.yml)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[Japanese README (日本語版はこちら)](./README.md)

This repository is a hands-on learning environment for those in the Earth Sciences (Geology, Meteorology, Oceanography, Environmental Science, etc.) who are **"new to programming but want to handle data in research or work."**

---

## 🌋 What You Can Learn
Move beyond manual analysis in Excel and learn to build "reproducible analysis" using Python:
- Automated calculation and visualization of rock chemistry data.
- Terrain analysis from Digital Elevation Models (DEM).
- Automated image analysis of thin section micrographs.
- Statistical classification of geochemical data (Intro to Machine Learning).

---

## 🚀 Getting Started (Environment Setup)

If you are a beginner, please follow these steps:

### 1. Prepare Python Environment (Recommended)
We strongly recommend installing **Anaconda** or **Miniconda** for the smoothest experience.
- [Anaconda Installation Guide](https://www.anaconda.com/download)

### 2. Download Materials
Get the materials using one of the following methods:
- **(Recommended)** Click the [Code] button on this page and select [Download ZIP], then extract it.
- **(For Advanced Users)** `git clone https://github.com/USER_NAME/REPO_NAME.git`

### 3. Launch Jupyter Lab
Open your terminal (Anaconda Prompt on Windows), navigate to the project folder, and run:
```bash
jupyter lab
```
Your browser will open with the file list.

### 4. First Step
Open `notebooks/00_introduction.ipynb`.
Follow the instructions and execute cells using the **"Shift + Enter"** keys to check your environment and prepare the data.

---

## 📝 Curriculum (12 Modules)
Learn step-by-step through specific Earth Science problems.

### 🟢 Fundamentals: Getting Used to Programming
1.  **Python Basics**: Variables, arithmetic, and basic geoscience calculations (e.g., density).
2.  **Pandas Basics**: Loading CSV files, checking statistics, and filtering data.

### 🔵 Analysis: Visualization and Statistics
3.  **Petrology Analysis**: Calculating Mg#, data cleaning, and PCA (Principal Component Analysis).
4.  **Time Series Analysis**: Denoising paleoclimate data and detecting change points.
5.  **Terrain Analysis**: Generating slope maps from Digital Elevation Models (DEM).
6.  **Image Analysis**: Automated quantification of Crystal Size Distribution (CSD) from micrographs.

### 🔴 Applications: Advanced Analysis and Automation
7.  **3D Volume Analysis**: Basics of 3D modeling and visualization of subsurface structures.
8.  **Geochemical Clustering**: Classification and identification of tephra using K-Means.
9.  **Earth Dynamics Simulation**: Numerical modeling of material cycles using differential equations.
10. **Field Data Automation**: Automated調査 route map generation from GPS-tagged photos.
11. **Mineral Spectroscopy**: Peak extraction techniques from spectral data (e.g., XRD).
12. **Spatiotemporal Big Data**: Parallel processing of large-scale climate data (Dask/Xarray).

---

## 🤝 Troubleshooting
- If you encounter code errors, try re-running the setup cells in `00_introduction.ipynb`.
- Background information for analysis methods (like PCA) is explained simply within each notebook.

## 📄 License
This project is licensed under the MIT License.
