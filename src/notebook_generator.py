import nbformat as nbf
import os

def create_rich_notebook(filename, title, module_id, sections):
    nb = nbf.v4.new_notebook()
    
    # 0. Setup Path & Imports (Hidden/Setup)
    setup_code = "import sys\nimport os\nsys.path.append('../')\nimport pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt\nfrom src.verifier import verify_and_log\n\n# 表示設定\npd.options.display.max_columns = None"
    nb.cells.append(nbf.v4.new_code_cell(setup_code))

    for section in sections:
        if section['type'] == 'markdown':
            nb.cells.append(nbf.v4.new_markdown_cell(section['content']))
        elif section['type'] == 'code':
            nb.cells.append(nbf.v4.new_code_cell(section['content']))
        elif section['type'] == 'template':
            # Create a markdown header for the challenge
            nb.cells.append(nbf.v4.new_markdown_cell("## 🎯 Challenge: 自動解析パイプラインの構築\nこれまでに学んだ手法を組み合わせ、1つの関数として実装してください。"))
            nb.cells.append(nbf.v4.new_code_cell(section['content']))
            # Add verification cell immediately after
            nb.cells.append(nbf.v4.new_markdown_cell("## ✅ 検証と記録\n実行してレポートをクリップボードにコピーします。"))
            nb.cells.append(nbf.v4.new_code_cell(f"result = run_module_pipeline()\nverify_and_log('{module_id}', result)"))

    with open(f"notebooks/{filename}", 'w', encoding='utf-8') as f:
        nbf.write(nb, f)
    print(f"Created Rich Notebook: notebooks/{filename}")

def generate_all_rich_notebooks():
    # --- Module 1: Tabular ---
    m1_sections = [
        {'type': 'markdown', 'content': "# #01 岩石化学データ解析 (Pandas / Scikit-Learn)\n\n## 0. 地球科学的背景: マグマの分化とMg#\nマグマが冷えて結晶が分出する過程（結晶分化作用）では、Mgなどの元素が初期の結晶（かんらん石など）に取り込まれます。そのため、マグマの分化度を示す指標として **Mg# (Magnesium Number)** が広く使われます。\n\n$$Mg\\# = 100 \\times \\frac{MgO / 40.3}{(MgO / 40.3) + (FeO / 71.8)}$$\n\n本実習では、大量の分析データからMg#を自動計算し、多変量解析（PCA）によって岩石種を分類するパイプラインを構築します。"},
        {'type': 'markdown', 'content': "## 1. ライブラリの基本操作 (写経)\nまずは、Pandasによるデータの読み込みと、Scikit-Learnによる主成分分析の基本を学びましょう。"},
        {'type': 'code', 'content': "# データの読み込み\ndf_sample = pd.read_csv('../data/raw_tabular/petrology.csv')\ndisplay(df_sample.head())\n\n# 基本統計量の確認\nprint(df_sample.describe())"},
        {'type': 'code', 'content': "from sklearn.decomposition import PCA\n\n# データの正規化（ここでは簡易的に）\nX = df_sample[['SiO2', 'MgO', 'FeO']].fillna(0)\npca = PCA(n_components=2)\ncomponents = pca.fit_transform(X)\nprint(f'寄与率: {pca.explained_variance_ratio_}')"},
        {'type': 'template', 'content': """def run_module_pipeline():
    # --- STEP 1: データの読み込み ---
    # data/raw_tabular/petrology.csv を読み込んでください
    df = pd.read_csv('../data/raw_tabular/petrology.csv')
    
    # --- STEP 2: 前処理 ---
    # 欠損値(NaN)を含む行を削除してください
    df = df.dropna()
    
    # --- STEP 3: 指標計算 ---
    # Mg# を計算し、新しい列 'Mg#' として追加してください
    # ヒント: 分母のゼロ割りに注意
    df['Mg#'] = 100 * (df['MgO']/40.3) / (df['MgO']/40.3 + df['FeO']/71.8)
    
    # --- STEP 4: 多変量解析 ---
    # SiO2, MgO, FeO を用いて PCA(n_components=2) を実行してください
    # 第1主成分が 0 より大きいか小さいかで 'Cluster' (0 or 1) を割り当ててください
    from sklearn.decomposition import PCA
    pca = PCA(n_components=2)
    features = df[['SiO2', 'MgO', 'FeO']]
    pcs = pca.fit_transform(features)
    df['Cluster'] = (pcs[:, 0] > 0).astype(int)
    
    # --- STEP 5: 永続化 ---
    # 結果を SQLite 'data/petrology_processed.db' の 'analysis' テーブルに保存してください
    import sqlite3
    conn = sqlite3.connect('../data/petrology_processed.db')
    df.to_sql('analysis', conn, if_exists='replace', index=False)
    conn.close()
    
    return df"""}
    ]

    # --- Module 2: Time-series ---
    m2_sections = [
        {'type': 'markdown', 'content': "# #02 時系列解析と古気候急変点 (SciPy / Ruptures)\n\n## 0. 地球科学付背景: 酸素同位体比と氷床量\n有孔虫殻などの $\\delta^{18}O$ は、過去の海水温や氷床量を反映する重要な指標です。地質時代において、気候システムが急激に変化した点（変化点）を特定することは、古環境学の主要な課題です。\n\n本実習では、**Ruptures** ライブラリを用いて、統計的な「変化点検出（Change Point Detection）」を自動化します。"},
        {'type': 'markdown', 'content': "## 1. ライブラリの基本操作 (写経)\n不連続な変化を捉えるための手法を学びます。"},
        {'type': 'code', 'content': "import ruptures as rpt\n\n# ダミーシグナルの生成\nn = 500\nsignal = np.concatenate([np.random.normal(0, 1, n), np.random.normal(5, 1, n)])\n\n# 変化点検出 (Pelt法)\nalgo = rpt.Pelt(model='l2').fit(signal)\nresult = algo.predict(pen=10)\nprint(f'変化点インデックス: {result}')"},
        {'type': 'template', 'content': """import ruptures as rpt

def run_module_pipeline():
    # --- STEP 1: データの読み込み ---
    # data/raw_timeseries/isotopes.csv
    df = pd.read_csv('../data/raw_timeseries/isotopes.csv')
    
    # --- STEP 2: シグナルの抽出 ---
    # 'd18O' 列の値を numpy 配列として取り出してください
    signal = df['d18O'].values
    
    # --- STEP 3: 変化点検出の実行 ---
    # PELTアルゴリズム(model='l2')を使用してください
    # ペナルティ値 pen=10 を推奨します
    algo = rpt.Pelt(model='l2').fit(signal)
    change_points = algo.predict(pen=10)
    
    # --- STEP 4: 可視化 (オプション) ---
    # plt.plot(signal); [plt.axvline(p, color='red') for p in change_points]; plt.show()
    
    return change_points"""}
    ]

    # --- Module 3: Geospatial ---
    m3_sections = [
        {'type': 'markdown', 'content': "# #03 地形データと空間解析 (Rasterio / GeoPandas)\n\n## 0. 地球科学的背景: DEMからの地形量抽出\n数値標高モデル（DEM）から傾斜角や方位を計算することは、土砂災害リスク評価や層理面の解析において不可欠です。\n\n$$\\text{Slope} = \\arctan\\left(\\sqrt{(\\partial z/\\partial x)^2 + (\\partial z/\\partial y)^2}\\right)$$\n\n本実習では、GeoTIFFをラスタデータとして読み込み、中心差分近似を用いて傾斜角面を生成します。"},
        {'type': 'markdown', 'content': "## 1. ラスタデータの操作 (写経)\nRasterio を用いた空間データの読み込みと、地理座標系の確認を行います。"},
        {'type': 'code', 'content': "import rasterio\n\nwith rasterio.open('../data/raw_geospatial/dem.tif') as src:\n    print(f'解像度: {src.res}')\n    print(f'座標系: {src.crs}')\n    dem_data = src.read(1)\n\nplt.imshow(dem_data, cmap='terrain')\nplt.colorbar(label='Elevation (m)')\nplt.show()"},
        {'type': 'template', 'content': """import rasterio

def run_module_pipeline():
    # --- STEP 1: ラスタデータの読み込み ---
    # data/raw_geospatial/dem.tif
    with rasterio.open('../data/raw_geospatial/dem.tif') as src:
        dem = src.read(1)
        res = src.res[0] # ピクセルサイズ
    
    # --- STEP 2: 傾斜角の計算 ---
    # numpy.gradient を使用して dz/dx, dz/dy を求めてください
    # 物理的な距離(res)で割るのを忘れないようにしてください
    dy, dx = np.gradient(dem, res)
    slope_rad = np.arctan(np.sqrt(dx**2 + dy**2))
    slope_deg = np.rad2deg(slope_rad)
    
    # --- STEP 3: 結果の書き出し (オプション) ---
    # data/slope_map.tif として保存しても良いでしょう
    
    return slope_deg"""}
    ]

    # --- Module 4: Image ---
    m4_sections = [
        {'type': 'markdown', 'content': "# #04 画像解析と結晶幾何学 (Scikit-Image / OpenCV)\n\n## 0. 地球科学的背景: 薄片の組織解析\n岩石薄片の顕微鏡写真から結晶のサイズ分布を求めることは、マグマの冷却速度や変成度を推定するための重要な手法です。\n\n本実習では、画像の二値化（Thresholding）、ラベリング、そして各「結晶」の物理量（等価円直径など）の自動抽出を行います。"},
        {'type': 'markdown', 'content': "## 1. 画像処理のワークフロー (写経)\n画像をデジタルデータ（行列）として扱い、特徴を抽出する手順を学びます。"},
        {'type': 'code', 'content': "from skimage import io, filters, measure\n\n# 画像の読み込み\nimg = io.imread('../data/raw_images/thin_section.png', as_gray=True)\n\n# 大津の二値化 (Otsu's Method)\nthresh = filters.threshold_otsu(img)\nbinary = img > thresh\n\nplt.imshow(binary, cmap='gray')\nplt.title('Binary Image')\nplt.show()"},
        {'type': 'template', 'content': """from skimage import io, filters, measure

def run_module_pipeline():
    # --- STEP 1: 画像の読み込み ---
    # data/raw_images/thin_section.png をグレースケールで
    img = io.imread('../data/raw_images/thin_section.png', as_gray=True)
    
    # --- STEP 2: 二値化 ---
    # 結晶と石基を分離するための閾値を決定してください
    thresh = filters.threshold_otsu(img)
    binary = img > thresh
    
    # --- STEP 3: ラベリングと計測 ---
    # skimage.measure.label と regionprops を使用してください
    label_img = measure.label(binary)
    props = measure.regionprops(label_img)
    
    # --- STEP 4: 特徴量の抽出 ---
    # 各粒子の 'equivalent_diameter' (等価円直径) をリストに格納してください
    diameters = [p.equivalent_diameter for p in props]
    
    print(f"抽出された結晶数: {len(diameters)}")
    
    return diameters"""}
    ]

    # --- Module 5: 3D/GUI ---
    m5_sections = [
        {'type': 'markdown', 'content': "# #05 3Dボリューム可視化とGUI (PyVista / Streamlit)\n\n## 0. 地球科学的背景: 空間情報の可視化\n地下構造の3次元モデリングは、資源探査や防災において極めて重要です。\n\n本実習では、**PyVista** を用いた3Dグリッド生成の基本と、解析結果を対話的に探索するための **Streamlit** の活用方法（概念）を紹介します。"},
        {'type': 'markdown', 'content': "## 1. PyVistaによる3D生成 (写経)"},
        {'type': 'code', 'content': "import pyvista as pv\n\n# 直交グリッドの生成\ngrid = pv.UniformGrid()\ngrid.dimensions = np.array([10, 10, 10])\ngrid.spacing = (1, 1, 1)\n\n# データの割り当て\nvalues = np.linspace(0, 10, grid.n_cells)\ngrid.cell_data['Values'] = values\n\n# 可視化 (Notebook上での表示には仮想フレームバッファが必要な場合があります)\n# grid.plot(show_edges=True)"},
        {'type': 'template', 'content': """def run_module_pipeline():
    # --- STEP 1: ボリュームデータの生成 ---
    # 3Dグリッドを生成し、適当な物性値を割り当ててください
    import pyvista as pv
    grid = pv.UniformGrid()
    grid.dimensions = (20, 20, 20)
    grid.cell_data['Property'] = np.random.rand(grid.n_cells)
    
    # --- STEP 2: ステータス情報の作成 ---
    status = {
        "Module": "M5_3D_Visualization",
        "Grid_Dimensions": grid.dimensions,
        "Total_Cells": grid.n_cells,
        "Status": "Success"
    }
    
    return status"""}
    ]

    # Generate all
    create_rich_notebook("01_tabular_petrology.ipynb", "Module 01: 岩石化学", "M1", m1_sections)
    create_rich_notebook("02_timeseries_granulometry.ipynb", "Module 02: 時系列解析", "M2", m2_sections)
    create_rich_notebook("03_geospatial_mapping.ipynb", "Module 03: 地形解析", "M3", m3_sections)
    create_rich_notebook("04_image_geometry.ipynb", "Module 04: 画像解析", "M4", m4_sections)
    create_rich_notebook("05_volume_gui.ipynb", "Module 05: 3D/GUI", "M5", m5_sections)

if __name__ == "__main__":
    generate_all_rich_notebooks()
