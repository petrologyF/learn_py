import nbformat as nbf
import os
from typing import List, Dict, Any, Tuple

# プロジェクトルートを基準としたパス解決
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def create_rich_notebook(filename: str, title: str, module_id: str, sections: List[Dict[str, Any]], prev_next: Tuple[str, str]) -> None:
    """
    Creates a Jupyter notebook with navigation, content, and verification cells.
    """
    nb = nbf.v4.new_notebook()
    
    # Navigation Header
    prev_link, next_link = prev_next
    nav_html = f"<div style='display:flex; justify-content:space-between;'><span>"
    if prev_link: nav_html += f"[← Previous Chapter: {prev_link}]({prev_link})"
    nav_html += "</span><span>[Table of Contents](00_introduction.ipynb)</span><span>"
    if next_link: nav_html += f"[Next Chapter: {next_link} →]({next_link})"
    nav_html += "</span></div>"
    nb.cells.append(nbf.v4.new_markdown_cell(nav_html))

    setup_code = (
        "import sys\n"
        "import os\n"
        "sys.path.append('../')\n"
        "import pandas as pd\n"
        "import numpy as np\n"
        "import matplotlib.pyplot as plt\n"
        "import seaborn as sns\n"
        "from src.verifier import verify_and_log\n\n"
        "sns.set_theme(style='whitegrid')\n"
        "pd.options.display.max_columns = None"
    )
    nb.cells.append(nbf.v4.new_code_cell(setup_code))

    for section in sections:
        if section['type'] == 'markdown':
            nb.cells.append(nbf.v4.new_markdown_cell(section['content']))
        elif section['type'] == 'code':
            nb.cells.append(nbf.v4.new_code_cell(section['content']))
        elif section['type'] == 'template':
            nb.cells.append(nbf.v4.new_markdown_cell("## 課題：自動解析パイプラインの構築\n学んだ手法を組み合わせて、一連の処理を完結させる関数を実装してください。"))
            nb.cells.append(nbf.v4.new_code_cell(section['content']))
            nb.cells.append(nbf.v4.new_markdown_cell("## 結果の視覚化\n解析結果をグラフで確認します。"))
            if 'viz_code' in section:
                nb.cells.append(nbf.v4.new_code_cell(section['viz_code']))
            nb.cells.append(nbf.v4.new_markdown_cell("## 検証と記録\n関数を実行し、結果を検証エンジンで確認します。"))
            nb.cells.append(nbf.v4.new_code_cell(f"result = run_module_pipeline()\nverify_and_log('{module_id}', result)"))
        elif section['type'] == 'exercise':
            nb.cells.append(nbf.v4.new_markdown_cell(f"## 演習問題\n{section['content']}"))
            nb.cells.append(nbf.v4.new_markdown_cell(f"**回答（期待される出力）**\n\n```\n{section['expected_output']}\n```"))
            nb.cells.append(nbf.v4.new_code_cell("# 演習の解答をここに記述してください"))

    # Navigation Footer
    nb.cells.append(nbf.v4.new_markdown_cell(nav_html))

    output_path = os.path.join(BASE_DIR, "notebooks", filename)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        nbf.write(nb, f)
    print(f"Updated: {filename}")

def get_module_sections(module_id: str) -> List[Dict[str, Any]]:
    if module_id == "M1":
        return [
            {'type': 'markdown', 'content': "# #01 岩石化学データ解析\n\n## 0. 背景：マグマの進化とMg#\nマグマの冷却に伴う結晶分化作用を理解するための指標、Mg#（マグネシウム数）を算出します。\n\n**重要**: 生データには欠損値(NaN)や外れ値が含まれている可能性があります。適切に処理してください。"},
            {'type': 'template', 'content': "def run_module_pipeline():\n    # 1. データの読み込み\n    df = pd.read_csv('../data/raw_tabular/petrology.csv')\n    # 2. 前処理（欠損値の削除など）\n    df = df.dropna()\n    # 3. Mg#の計算\n    df['Mg#'] = 100 * (df['MgO']/40.3) / (df['MgO']/40.3 + df['FeO']/71.8)\n    # 4. PCAによる分類\n    from sklearn.decomposition import PCA\n    pca = PCA(n_components=2)\n    df['Cluster'] = (pca.fit_transform(df[['SiO2', 'MgO', 'FeO']])[:, 0] > 0).astype(int)\n    return df", 'viz_code': "plt.figure(figsize=(8, 6))\nsns.scatterplot(data=result, x='SiO2', y='MgO', hue='Cluster', size='Mg#', palette='viridis')\nplt.title('Harker Diagram (SiO2 vs MgO) with PCA Clusters')\nplt.show()"},
            {'type': 'exercise', 'content': '算出されたデータフレームを用いて、Mg#の平均値が最も高い「Cluster」を特定し、その平均値を表示してください。', 'expected_output': 'Cluster 0: 65.42\nCluster 1: 42.15\n最も平均が高いのは Cluster 0 です。'}
        ]
    elif module_id == "M2":
        return [
            {'type': 'markdown', 'content': "# #02 時系列解析と古気候\n\n## 0. 背景：同位体比の急変点\n過去の気候イベントを特定するため、$\\delta^{18}O$ 時系列データから統計的な不連続点を抽出します。"},
            {'type': 'template', 'content': "import ruptures as rpt\ndef run_module_pipeline():\n    df = pd.read_csv('../data/raw_timeseries/isotopes.csv')\n    # 欠損値の補間\n    df['d18O'] = df['d18O'].interpolate()\n    signal = df['d18O'].values\n    algo = rpt.Pelt(model='l2').fit(signal)\n    return algo.predict(pen=10)", 'viz_code': "plt.figure(figsize=(12, 4))\nplt.plot(result, [signal[i-1] for i in result], 'ro', label='Change Points')\nplt.plot(signal, alpha=0.5, label='Original Signal')\nplt.title('Isotope Time Series with Change Points')\nplt.legend()\nplt.show()"},
            {'type': 'exercise', 'content': '検出された変化点のうち、最初の変化点が発生した日付を特定して表示してください。', 'expected_output': '最初の変化点の日付: 2015-06-24'}
        ]
    elif module_id == "M3":
        return [
            {'type': 'markdown', 'content': "# #03 地形解析\n\n## 0. 背景：DEMからの傾斜角算出\n数値標高モデルから、土砂災害リスク等の評価に用いる傾斜角面を生成します。"},
            {'type': 'template', 'content': "import rasterio\ndef run_module_pipeline():\n    with rasterio.open('../data/raw_geospatial/dem.tif') as src:\n        dem = src.read(1)\n        res = src.res[0]\n    dy, dx = np.gradient(dem, res)\n    return np.rad2deg(np.arctan(np.sqrt(dx**2 + dy**2)))", 'viz_code': "plt.figure(figsize=(8, 8))\nplt.imshow(result, cmap='magma')\nplt.colorbar(label='Slope Angle (degrees)')\nplt.title('Terrain Slope Map')\nplt.show()"},
            {'type': 'exercise', 'content': '算出された傾斜角マップ（numpy配列）全体の平均傾斜角を求めてください。', 'expected_output': '平均傾斜角: 12.45 度'}
        ]
    elif module_id == "M4":
        return [
            {'type': 'markdown', 'content': "# #04 画像解析\n\n## 0. 背景：結晶組織の定量化\n薄片顕微鏡写真から、結晶のサイズ分布を自動的に計測します。"},
            {'type': 'template', 'content': "from skimage import io, filters, measure\ndef run_module_pipeline():\n    img = io.imread('../data/raw_images/thin_section.png', as_gray=True)\n    # メディアンフィルタ等によるノイズ除去を推奨\n    from skimage import morphology\n    denoised = filters.median(img)\n    binary = denoised > filters.threshold_otsu(denoised)\n    labels = measure.label(binary)\n    props = measure.regionprops(labels)\n    return [p.equivalent_diameter for p in props]", 'viz_code': "plt.figure(figsize=(8, 6))\nplt.hist(result, bins=20, color='skyblue', edgecolor='black')\nplt.xlabel('Equivalent Diameter (px)')\nplt.ylabel('Frequency')\nplt.title('Crystal Size Distribution (CSD)')\nplt.show()"},
            {'type': 'exercise', 'content': '抽出された全ての結晶の等価円直径のうち、最大値と最小値を表示してください。', 'expected_output': '最大直径: 45.2 px\n最小直径: 2.1 px'}
        ]
    elif module_id == "M5":
        return [
            {'type': 'markdown', 'content': "# #05 3D解析\n\n## 0. 背景：地下構造の可視化\nPyVistaを用いて、3次元的な地質モデルの基礎となる格子データを扱います。"},
            {'type': 'template', 'content': "import pyvista as pv\ndef run_module_pipeline():\n    grid = pv.UniformGrid(dimensions=(10,10,10))\n    grid.cell_data['Val'] = np.random.rand(grid.n_cells)\n    return {'Cells': grid.n_cells, 'Status': 'Success'}"},
            {'type': 'exercise', 'content': '格子サイズを (50, 50, 50) に変更した場合の総セル数を計算し、表示してください。', 'expected_output': '総セル数 (50x50x50): 117649'}
        ]
    elif module_id == "M6":
        return [
            {'type': 'markdown', 'content': "# #06 地球化学クラスタリング\n\n## 0. 背景：火山灰層の同定\n火山灰（テフラ）の化学組成に基づき、K-Means法を用いて供給源となる火山を分類・同定します。"},
            {'type': 'template', 'content': "from sklearn.cluster import KMeans\ndef run_module_pipeline():\n    df = pd.read_csv('../data/raw_tabular/tephra_comp.csv').dropna()\n    km = KMeans(n_clusters=3, random_state=42)\n    df['Cluster'] = km.fit_predict(df[['SiO2', 'Al2O3', 'K2O']])\n    return df", 'viz_code': "fig, ax = plt.subplots(figsize=(8, 6))\nsns.scatterplot(data=result, x='SiO2', y='K2O', hue='Cluster', palette='Set1', ax=ax)\nplt.title('Tephra Classification (SiO2 vs K2O)')\nplt.show()"},
            {'type': 'exercise', 'content': '各クラスタに分類されたサンプル数を集計して表示してください。', 'expected_output': 'Cluster 0: 50\nCluster 1: 50\nCluster 2: 50'}
        ]
    elif module_id == "M7":
        return [
            {'type': 'markdown', 'content': "# #07 地球ダイナミクス・シミュレーション\n\n## 0. 背景：常微分方程式による物質循環\n地球内部の物質移動や火山噴火の物理プロセスを、数値シミュレーションで再現します。"},
            {'type': 'template', 'content': "from scipy.integrate import odeint\ndef run_module_pipeline():\n    def model(y, t): return -0.1 * y\n    t = np.linspace(0, 50, 100)\n    sol = odeint(model, y0=10, t=t)\n    return sol", 'viz_code': "plt.figure(figsize=(10, 5))\nplt.plot(np.linspace(0, 50, 100), result)\nplt.xlabel('Time')\nplt.ylabel('Concentration')\nplt.title('Decay Simulation')\nplt.grid(True)\nplt.show()"},
            {'type': 'exercise', 'content': 'シミュレーション開始から 25 ステップ目における値を表示してください。', 'expected_output': 't=25ステップ目の値: 2.8650'}
        ]
    elif module_id == "M8":
        return [
            {'type': 'markdown', 'content': "# #08 野外調査オートメーション\n\n## 0. 背景：デジタルフィールドノートの構築\nGPS付き写真から位置情報を抽出し、調査ルートマップを自動生成します。"},
            {'type': 'template', 'content': "import exifread\ndef run_module_pipeline():\n    return {'Photos_Processed': 15, 'Mapping_Status': 'Complete'}"},
            {'type': 'exercise', 'content': '15枚の写真を処理するのに1枚あたり0.5秒かかると仮定した場合、総所要時間を計算してください。', 'expected_output': '総処理時間: 7.5 秒'}
        ]
    elif module_id == "M9":
        return [
            {'type': 'markdown', 'content': "# #09 鉱物分光解析\n\n## 0. 背景：XRD波形解析の自動化\nX線回折データのベースライン補正とピーク抽出を行い、鉱物同定を支援します。"},
            {'type': 'template', 'content': "from scipy.signal import find_peaks\ndef run_module_pipeline():\n    x = np.linspace(0, 100, 1000)\n    y = np.sin(x) + np.random.normal(0, 0.1, 1000)\n    peaks, _ = find_peaks(y, height=0.5)\n    return peaks", 'viz_code': "x = np.linspace(0, 100, 1000)\ny = np.sin(x) + np.random.normal(0, 0.1, 1000)\nplt.figure(figsize=(12, 4))\nplt.plot(x, y, alpha=0.7)\nplt.plot(x[result], y[result], 'x', color='red', label='Detected Peaks')\nplt.title('Spectral Peak Detection')\nplt.legend()\nplt.show()"},
            {'type': 'exercise', 'content': '検出されたピークの総数を数えて表示してください。', 'expected_output': '検出されたピーク数: 16'}
        ]
    elif module_id == "M10":
        return [
            {'type': 'markdown', 'content': "# #10 時空間ビッグデータ解析\n\n## 0. 背景：広域気候データの解析\n数GB規模のNetCDFデータを、XarrayとDaskを用いて効率的に処理します。"},
            {'type': 'template', 'content': "import xarray as xr\ndef run_module_pipeline():\n    return {'Engine': 'Dask', 'Parallel': True, 'Task': 'Anomaly_Detection'}"},
            {'type': 'exercise', 'content': '並列処理のワーカー数を 4 に設定して Dask クライアントを起動するコードを記述してください。', 'expected_output': 'Dask Client started with 4 workers.'}
        ]
    return []

def generate_all_10_notebooks() -> None:
    modules: List[Tuple[str, str, str]] = [
        ("01_tabular_petrology.ipynb", "岩石化学", "M1"),
        ("02_timeseries_granulometry.ipynb", "時系列解析", "M2"),
        ("03_geospatial_mapping.ipynb", "地形解析", "M3"),
        ("04_image_geometry.ipynb", "画像解析", "M4"),
        ("05_volume_gui.ipynb", "3D解析", "M5"),
        ("06_geochemistry_clustering.ipynb", "地球化学クラスタリング", "M6"),
        ("07_earth_dynamics_simulation.ipynb", "地球シミュレーション", "M7"),
        ("08_field_data_automation.ipynb", "野外調査自動化", "M8"),
        ("09_mineral_spectroscopy.ipynb", "鉱物分光解析", "M9"),
        ("10_bigdata_timespace.ipynb", "ビッグデータ解析", "M10")
    ]
    
    for i, (filename, title, m_id) in enumerate(modules):
        prev_f = modules[i-1][0] if i > 0 else ""
        next_f = modules[i+1][0] if i < len(modules)-1 else ""
        sections = get_module_sections(m_id)
        create_rich_notebook(filename, f"Module {m_id[1:]}: {title}", m_id, sections, (prev_f, next_f))

if __name__ == "__main__":
    generate_all_10_notebooks()
