# Earth Science Python: 実践的学習リポジトリ

[![Python Testing](https://github.com/USER_NAME/REPO_NAME/actions/workflows/test.yml/badge.svg)](https://github.com/USER_NAME/REPO_NAME/actions/workflows/test.yml)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[English README (英語版はこちら)](./README_EN.md)

本リポジトリは、地球科学（Earth Science）および自然科学分野の研究者・学生が、データ解析、可視化、数値計算、空間解析、自動化のためのPythonスキルを習得するための実践的な学習環境を提供します。

> **Note**: 学習コンテンツ（Jupyter Notebook）およびソースコードは、国際的な研究環境を想定し、**英語ベース**で作成されています。

## 🌋 プロジェクトの目的
手作業によるデータ解析フローを、Pythonによる自動化された再現可能なパイプラインへと置き換え、研究効率を爆発的に向上させることを目指します。

1. **データ処理 (Data Processing)**: 研究室やフィールドで得られる複雑なデータの整形・クリーニング。
2. **可視化 (Visualization)**: 論文品質のグラフ、3次元プロット、地図の作成。
3. **数値計算 (Numerical Computation)**: 統計モデリング、信号処理、数式処理。
4. **空間解析 (Geospatial Analysis)**: DEM（数値標高モデル）、Shapefile、衛星データの解析。
5. **自動化 (Automation)**: 大規模データに対する一括処理パイプラインの構築。

---

## 🏗️ リポジトリ構造
```text
.
├── data/               # 自動生成された地球科学データセット (CSV, GeoTIFF)
├── notebooks/          # 段階的なJupyter Notebook教材 (解説 & 演習)
│   ├── 01_basics.ipynb        # Python & Jupyterの基礎
│   ├── 02_petrology.ipynb     # 岩石化学データ (NumPy/Pandas)
│   ├── 03_structural.ipynb    # 構造地質方位データ & ステレオネット
│   ├── 04_geospatial.ipynb    # GIS, Rasterio, & マッピング
│   └── 05_automation.ipynb    # カーブフィッティング & 自動化パイプライン
├── src/                # バックエンドスクリプト
│   ├── data_generator.py      # 地球科学ダミーデータ生成エンジン
│   ├── solutions.py           # 演習問題の模範解答
│   └── notebook_generator.py  # 教材ノートブック生成スクリプト
├── tests/              # 自動採点・バリデーションスイート (pytest)
├── requirements.txt    # 依存ライブラリ
└── README.md           # 本ファイル
```

---

## 🛠️ 技術スタック
- **Core**: `numpy`, `pandas`, `matplotlib`, `seaborn`
- **Science**: `scipy`, `sympy`, `statsmodels`, `scikit-learn`
- **Geospatial**: `geopandas`, `rasterio`, `xarray`, `cartopy`
- **Environment**: `jupyterlab`, `pytest`

---

## 🚀 はじめかた

### 1. リポジトリのクローン
```bash
git clone https://github.com/USER_NAME/REPO_NAME.git
cd REPO_NAME
```

### 2. 環境構築
仮想環境（venv）または Conda の使用を推奨します。
```bash
pip install -r requirements.txt
```

### 3. データセットとノートブックの生成
学習用のダミーデータと演習用ファイルを初期化します（初回のみ）：
```bash
python src/data_generator.py
python src/notebook_generator.py
```

### 4. Jupyter Labの起動
```bash
jupyter lab
```

---

## 📖 学習の進め方（インタラクティブ学習）

本リポジトリは、ローカル環境での「手を動かす学習」を重視しています。

1.  **ノートブックを開く**: `notebooks/` フォルダ内の `.ipynb` ファイルを開きます。
2.  **理論を学ぶ**: 理論背景や数式（LaTeX形式）を確認します。
3.  **コードを実装する**: `# TODO` と書かれたセルに、課題となる関数を実装します。
4.  **検証とコピー**:
    *   演習のすぐ下にある「検証用セル」を実行します。
    *   `src/verifier.py` が実装を自動解析し、結果を表示します。
    *   **重要**: 解析結果は自動的にクリップボードにMarkdown形式でコピーされます。
5.  **学習ログの保存**: コピーされた内容を、ObsidianやNotion、自分の学習ノートにペーストして記録を残します。

---

## 📝 カリキュラム詳細 (English Content)

### 01: Basic Syntax and Jupyter
Excel等のGUIソフトからPythonへ移行する科学者向けの、Python基礎文法とJupyterの効率的な使い方。

### 02: NumPy/Pandas in Petrology
- 主要元素組成 (wt%) の規格化と比率計算。
- 分析データの欠損値（NaN）処理。
- 化学組成トレンド（ハーカー図）の自動プロット。

### 03: Matplotlib/SciPy in Structural Geology
- 走向・傾斜（Strike and Dip）データの統計解析。
- 等積投影（ステレオネット）のための座標変換の実装。
- フィールド観測データからの外れ値除去。

### 04: Geospatial Analysis
- `rasterio` を用いたDEM（数値標高モデル）の読み書き。
- 座標参照系 (CRS) の管理と投影変換。
- `cartopy` と `geopandas` を用いた科学的地図作成。

### 05: Automation and Curve Fitting
- `scipy.optimize` を用いた線形・非線形回帰。
- 「一括読み込み -> フィルタリング -> 解析 -> グラフ出力」を完結させる自動化パイプライン。

---

## ✅ テストと採点
各ノートブックの演習問題には対応するテストケースが用意されています。実装した関数が期待通りに動作するか確認するには、ターミナルで以下を実行してください：
```bash
pytest
```

## 📄 ライセンス
このプロジェクトは MIT ライセンスの下で公開されています。詳細は LICENSE ファイルを参照してください。
