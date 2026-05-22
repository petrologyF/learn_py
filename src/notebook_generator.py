import json
import os

def create_nb(fn, cells):
    nb = {"cells": cells, "metadata": {"kernelspec": {"name": "python3", "display_name": "Python 3"}}, "nbformat": 4, "nbformat_minor": 5}
    with open(fn, "w", encoding="utf-8") as f: json.dump(nb, f, indent=1)

def md(t): return {"cell_type": "markdown", "metadata": {}, "source": [t + "\n"]}
def cd(s): return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": [s + "\n"]}

# --- 01 Numpy Module ---
nb1 = [
    md("# 01 Numpy Module: Structural Geology Orientation Analysis"),
    md("### 📥 Input Specification\n- **ファイル**: `data/numpy_data/structural_orientations.npy`\n- **形式**: `np.ndarray` (200, 3)\n- **カラム**: [Strike(0-360), Dip(0-90), DipDirection(0-360)]\n- **特記事項**: 測定エラー値（外れ値・NaN）が含まれています。"),
    md("### 📤 Output Specification\n- **形式**: `tuple` (float, float)\n- **内容**: (全体の平均走向, 全体の平均傾斜)\n- **期待動作**: エラー値を適切にフィルタリングし、法線ベクトル変換を経て平均値を算出すること。"),
    md("## 1. Background\n$$n_x = \sin\phi \sin\theta, \quad n_y = -\cos\phi \sin\theta, \quad n_z = \cos\theta$$\nwhere $\phi$ is strike and $\theta$ is dip."),
    cd("import numpy as np\ndef numpy_pipeline(data_path):\n    \"\"\"\n    Input: data_path (str) -> Output: (mean_strike, mean_dip) (tuple)\n    \"\"\"\n    data = np.load(data_path)\n    # Implementation here...\n    return (0.0, 0.0)"),
    cd("from src.verifier import verify_module\nresult = numpy_pipeline('../data/numpy_data/structural_orientations.npy')\nverify_module('numpy', result)")
]

# --- 02 Pandas Module ---
nb2 = [
    md("# 02 Pandas Module: Petrology and Harker Diagrams"),
    md("### 📥 Input Specification\n- **ファイル**: `data/pandas_data/major_elements.csv`\n- **形式**: CSV (Pandas DataFrame)\n- **項目**: 主要元素組成 ($SiO_2, TiO_2, Al_2O_3, FeO, MgO, CaO, Na_2O, K_2O$)\n- **特記事項**: 3%の欠損値(NaN)が含まれています。"),
    md("### 📤 Output Specification\n- **形式**: `pd.DataFrame`\n- **内容**: 欠損値補完済み、かつ $Mg\#$ カラムが追加されたデータフレーム。\n- **計算式**: $$Mg\\# = 100 \times \\frac{MgO/40.3}{MgO/40.3 + FeO/71.8}$$"),
    cd("import pandas as pd\ndef pandas_pipeline(data_path):\n    \"\"\"\n    Input: data_path (str) -> Output: processed_df (pd.DataFrame)\n    \"\"\"\n    df = pd.read_csv(data_path)\n    # Implementation here...\n    return df"),
    cd("from src.verifier import verify_module\nresult_df = pandas_pipeline('../data/pandas_data/major_elements.csv')\nverify_module('pandas', result_df)")
]

# --- 03 Scipy Stats Module ---
nb3 = [
    md("# 03 Scipy Module: Signal Processing and Curve Fitting"),
    md("### 📥 Input Specification\n- **ファイル**: `data/scipy_data/environmental_series.csv`\n- **形式**: CSV (time, signal)\n- **内容**: 長期トレンド + 周期変動 + ノイズが合成された時系列データ。"),
    md("### 📤 Output Specification\n- **形式**: `dict`\n- **内容**: \n  - `params`: 近似直線のパラメータ (傾き, 切片)\n  - `fft`: 抽出された周波数成分の振幅スペクトル（先頭10要素）"),
    cd("import numpy as np\nfrom scipy import fft, optimize\ndef scipy_pipeline(data_path):\n    \"\"\"\n    Input: data_path (str) -> Output: {'params': array, 'fft': array}\n    \"\"\"\n    # Implementation here...\n    return {'params': [0,0], 'fft': []}"),
    cd("from src.verifier import verify_module\nresult = scipy_pipeline('../data/scipy_data/environmental_series.csv')\nverify_module('scipy', result)")
]

# --- 04 Geospatial Module ---
nb4 = [
    md("# 04 Geospatial Module: DEM Analysis"),
    md("### 📥 Input Specification\n- **ファイル**: `data/geospatial_data/dem.tif`\n- **形式**: GeoTIFF (100x100)\n- **内容**: ガウシアン起伏を持つ標高データ (CRS: EPSG:4326)"),
    md("### 📤 Output Specification\n- **形式**: `gpd.GeoDataFrame`\n- **内容**: 特定地点（135.0, 35.0）の標高や解析結果を保持する地理空間データフレーム。"),
    cd("import rasterio\nimport geopandas as gpd\ndef geospatial_pipeline(raster_path):\n    \"\"\"\n    Input: raster_path (str) -> Output: gdf (gpd.GeoDataFrame)\n    \"\"\"\n    # Implementation here...\n    return gpd.GeoDataFrame()"),
    cd("from src.verifier import verify_module\nresult_gdf = geospatial_pipeline('../data/geospatial_data/dem.tif')\nverify_module('geospatial', result_gdf)")
]

if __name__ == "__main__":
    d = "notebooks"
    os.makedirs(d, exist_ok=True)
    create_nb(os.path.join(d, "01_numpy_module.ipynb"), nb1)
    create_nb(os.path.join(d, "02_pandas_module.ipynb"), nb2)
    create_nb(os.path.join(d, "03_scipy_stats_module.ipynb"), nb3)
    create_nb(os.path.join(d, "04_geospatial_module.ipynb"), nb4)
    print("Notebooks with Clear I/O Specs created.")
