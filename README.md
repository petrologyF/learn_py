# Earth Science Python: はじめての地球科学データ解析

[![Python Testing](https://github.com/USER_NAME/REPO_NAME/actions/workflows/test.yml/badge.svg)](https://github.com/USER_NAME/REPO_NAME/actions/workflows/test.yml)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[English README (英語版はこちら)](./README_EN.md)

本リポジトリは、**「プログラミングは初めてだけど、研究や業務でデータを扱いたい」**という地球科学（地質・気象・海洋・環境など）分野の方々のための、実践的な学習環境です。

---

## 🌋 この教材で学べること
Excelでの手作業による解析を卒業し、Pythonを使って以下のような「再現可能な解析」ができるようになります。
- 岩石化学データの自動計算と可視化
- 地形データ（DEM）からの傾斜解析
- 顕微鏡写真の自動画像解析
- 地球化学データの統計的分類（機械学習の入り口）

---

## 🚀 はじめかた（環境構築）

初学者の方は、以下のステップで進めてください。

### 1. Python環境の準備（推奨）
最もトラブルが少ない **Anaconda** または **Miniconda** のインストールを強く推奨します。
- [Anaconda インストールガイド](https://www.anaconda.com/download)

### 2. 教材のダウンロード
以下のいずれかの方法で教材を手元に用意します。
- **(推奨)** このページの [Code] ボタンから [Download ZIP] をクリックして解凍する。
- **(経験者向け)** `git clone https://github.com/USER_NAME/REPO_NAME.git`

### 3. Jupyter Lab の起動
ターミナル（WindowsならAnaconda Prompt）を開き、教材のフォルダに移動して以下を実行します。
```bash
jupyter lab
```
ブラウザが立ち上がり、ファイル一覧が表示されます。

### 4. 最初のステップ
`notebooks/00_introduction.ipynb` を開いてください。
**「Shift + Enter」キー**でセルを実行しながら、環境チェックとデータの準備を行います。

---

## 📝 カリキュラム（全12章）
基礎から応用まで、地球科学の具体的な課題を通じてステップバイステップで学びます。

### 🟢 基礎編：プログラミングに慣れる
1.  **Pythonの基礎**: 変数、計算、地学計算（密度の計算など）の基本。
2.  **Pandasの基礎**: 表データの読み込み、統計量の確認、フィルタリング。

### 🔵 解析編：データの可視化と統計
3.  **岩石化学解析**: 元素組成からのMg#算出、データのクリーニング、PCA（主成分分析）。
4.  **時系列解析**: 古気候データのノイズ除去と、急変点（チェンジポイント）の検出。
5.  **地形解析**: デジタル標高モデル（DEM）を用いた傾斜角マップの自動生成。
6.  **画像解析**: 顕微鏡写真からの結晶サイズ分布（CSD）の自動定量化。

### 🔴 応用編：高度な解析と自動化
7.  **3Dボリューム解析**: 地下構造の3次元モデリングと可視化の基礎。
8.  **地球化学クラスタリング**: 機械学習（K-Means）を用いた火山灰の分類・同定。
9.  **地球シミュレーション**: 微分方程式による物質循環の数値計算。
10. **野外調査オートメーション**: GPS連動写真からの調査ルートマップ自動作成。
11. **鉱物分光解析**: XRDなどのスペクトルデータからのピーク抽出技術。
12. **時空間ビッグデータ解析**: 広域気候データの並列分散処理（Dask/Xarray）。

---

## 🤝 困ったときは
- プログラミングのコードがエラーになったら、まずは `00_introduction.ipynb` のセットアップを再実行してください。
- 解析手法の背景（PCAなど）は、各ノートブック内で平易に解説しています。

## 📄 ライセンス
このプロジェクトは MIT ライセンスの下で公開されています。
