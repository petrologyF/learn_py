# Earth Science Python: 実践的学習リポジトリ

[![Python Testing](https://github.com/USER_NAME/REPO_NAME/actions/workflows/test.yml/badge.svg)](https://github.com/USER_NAME/REPO_NAME/actions/workflows/test.yml)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[English README (英語版はこちら)](./README_EN.md)

本リポジトリは、地球科学（Earth Science）および自然科学分野の研究者・学生が、データ解析、可視化、数値計算、空間解析、自動化のためのPythonスキルを習得するための実践的な学習環境を提供します。

---

## 🌋 プロジェクトの目的
手作業によるデータ解析フローを、Pythonによる自動化された再現可能なパイプラインへと置き換え、研究効率を爆発的に向上させることを目指します。

---

## 🏗️ ディレクトリ構造
- `notebooks/`: 学習用メインノートブック (00〜10)
- `src/`: 解析エンジン、検証システム、データ生成スクリプト
- `data/`: 解析対象となる地球科学データ (自動生成されます)
- `tests/`: システムの整合性を確認するための自動テスト
- `requirements.txt`: 依存ライブラリ一覧

---

## 🚀 はじめかた

本教材は、全てのセットアップと学習をJupyter Notebook内で行えるように設計されています。

1.  **リポジトリのクローン**:
    ```bash
    git clone https://github.com/USER_NAME/REPO_NAME.git
    cd REPO_NAME
    ```
2.  **Jupyter Lab の起動**:
    ```bash
    jupyter lab
    ```
3.  **セットアップ**:
    `notebooks/00_introduction.ipynb` を開き、ノートブック内のセルを順番に実行して、環境構築とデータの準備を行います。
4.  **学習の開始**:
    進捗ダッシュボードで状況を確認しながら、Module 01 から順に進めてください。

---

## 📝 カリキュラム詳細 (全10章)
本リポジトリでは以下の10のトピックを扱います。各章は `notebooks/` フォルダ内に用意されています。

1. **岩石化学データ解析**: Pandasを用いた組成計算とPCA。
2. **時系列解析と古気候**: 同位体データの統計的変化点検出。
3. **地形解析**: DEMデータからの傾斜角算出とGIS処理。
4. **画像解析**: 薄片顕微鏡写真からの結晶組織定量化。
5. **3Dボリューム解析**: PyVistaによる地下構造の可視化。
6. **地球化学クラスタリング**: 火山灰の組成に基づくK-Means分類。
7. **地球ダイナミクス・シミュレーション**: 微分方程式による物質循環モデル。
8. **野外調査オートメーション**: GPS写真からの調査マップ自動作成。
9. **鉱物分光解析**: XRD波形のピーク抽出とベースライン補正。
10. **時空間ビッグデータ解析**: Xarray/Daskを用いた広域気候データ処理。

---

## ✅ テストと採点
システムの整合性を確認するには、ターミナルで以下を実行してください：
```bash
pytest
```

## 📄 ライセンス
このプロジェクトは MIT ライセンスの下で公開されています。
