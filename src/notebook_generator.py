import nbformat as nbf
import os

def create_notebook(filename, title, module_id, intro_text, input_desc, pipeline_template):
    nb = nbf.v4.new_notebook()
    
    # 1. Title and Intro
    nb.cells.append(nbf.v4.new_markdown_cell(f"# {title}\n\n{intro_text}"))
    
    # 2. Input Data Description
    nb.cells.append(nbf.v4.new_markdown_cell(f"## 1. インプットデータの確認\n\n{input_desc}"))
    
    # Setup cell (imports)
    nb.cells.append(nbf.v4.new_code_cell(f"import sys\nsys.path.append('../')\nimport pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt\nfrom src.verifier import verify_and_log"))

    # 3. Pipeline implementation
    nb.cells.append(nbf.v4.new_markdown_cell(f"## 2. パイプラインの実装\n\n以下の関数を完成させて、データの読み込み、加工、解析、出力を一気通貫で行うパイプラインを構築してください。"))
    nb.cells.append(nbf.v4.new_code_cell(pipeline_template))
    
    # 4. Verification
    nb.cells.append(nbf.v4.new_markdown_cell(f"## 3. 検証と記録\n\n関数を実行し、結果を検証エンジンに渡します。"))
    nb.cells.append(nbf.v4.new_code_cell(f"result = run_module_pipeline()\nverify_and_log('{module_id}', result)"))
    
    with open(f"notebooks/{filename}", 'w', encoding='utf-8') as f:
        nbf.write(nb, f)
    print(f"Created: notebooks/{filename}")

def generate_all_notebooks():
    # Module 1
    create_notebook(
        "01_tabular_petrology.ipynb",
        "Module 01: 岩石化学データ解析 (Pandas / Scikit-Learn)",
        "M1",
        "このモジュールでは、主要元素組成データを用いて $Mg\\#$ を計算し、PCA（主成分分析）によるクラスタリングを行います。\n\n$$Mg\\# = 100 \\times \\frac{MgO/40.3}{MgO/40.3 + FeO/71.8}$$",
        "インプットデータ `data/raw_tabular/petrology.csv` には、複数のサンプルの $SiO_2, MgO, FeO$ 含有量が含まれています。",
        """def run_module_pipeline():
    # 1. データの読み込み (data/raw_tabular/petrology.csv)
    
    # 2. 欠損値の処理 (dropna または fillna)
    
    # 3. Mg# の計算 (列 'Mg#' として追加)
    
    # 4. Scikit-Learn による PCA クラスタリング (列 'Cluster' として追加)
    
    # 5. SQLite への保存 (data/petrology_processed.db)
    
    # 6. 結果の DataFrame を返す
    return None # 実装してください"""
    )

    # Module 2
    create_notebook(
        "02_timeseries_granulometry.ipynb",
        "Module 02: 時系列解析と古気候急変点 (SciPy / Ruptures)",
        "M2",
        "同位体比（$\\delta^{18}O$）の時系列データから、気候の急激な変化点（Change-point）を検出します。\n`ruptures` ライブラリを使用して、統計的な不連続点を抽出しましょう。",
        "インプットデータ `data/raw_timeseries/isotopes.csv` には、10年間の日単位データが含まれています。",
        """import ruptures as rpt

def run_module_pipeline():
    # 1. データの読み込み (data/raw_timeseries/isotopes.csv)
    
    # 2. シグナルの準備 (d18O 列を numpy 配列へ)
    
    # 3. ruptures による変化点検出 (Pelt法など)
    # algo = rpt.Pelt(model="l2").fit(signal)
    # result = algo.predict(pen=10)
    
    # 4. 変化点のインデックス（リスト）を返す
    return [] # 実装してください"""
    )

    # Module 3
    create_notebook(
        "03_geospatial_mapping.ipynb",
        "Module 03: 地形データと空間補間 (Rasterio / PyKrige)",
        "M3",
        "標高データ（DEM）から傾斜角を算出し、空間的な特徴を理解します。\n\n$$\\text{Slope} = \\arctan\\left(\\sqrt{(\\partial z/\\partial x)^2 + (\\partial z/\\partial y)^2}\\right)$$",
        "インプットデータ `data/raw_geospatial/dem.tif` は GeoTIFF 形式の標高ラスタです。",
        """import rasterio

def run_module_pipeline():
    # 1. Rasterio で DEM を読み込む
    
    # 2. 標高勾配（Slope）の計算
    
    # 3. 計算結果（numpy 配列）を返す
    return np.array([]) # 実装してください"""
    )

    # Module 4
    create_notebook(
        "04_image_geometry.ipynb",
        "Module 04: 薄片画像解析と粒径分布 (Scikit-Image)",
        "M4",
        "顕微鏡写真から結晶粒の境界を抽出し、それぞれの等価円直径を算出します。\nまた、`mplstereonet` を用いた構造方位の投影についても学びます。",
        "インプットデータ `data/raw_images/thin_section.png` は模擬薄片画像です。",
        """from skimage import io, filters, measure

def run_module_pipeline():
    # 1. 画像の読み込み
    
    # 2. 二値化とラベリング
    
    # 3. 各粒子のプロパティ抽出 (等価円直径)
    
    # 4. 直径のリスト（または配列）を返す
    return [] # 実装してください"""
    )

    # Module 5
    create_notebook(
        "05_volume_gui.ipynb",
        "Module 05: 3D可視化とStreamlit (PyVista / Streamlit)",
        "M5",
        "地球科学における3次元構造の可視化と、簡易的なWeb GUIによるデータ検索を体験します。",
        "このモジュールでは、これまでの解析結果を統合したメタデータを使用します。",
        """def run_module_pipeline():
    # 1. 3Dグリッドの生成 (PyVista)
    
    # 2. ステータス情報の作成 (dict)
    status = {"3D_Model": "Generated", "GUI_Ready": True}
    
    # 3. dict を返す
    return status"""
    )

if __name__ == "__main__":
    generate_all_notebooks()
