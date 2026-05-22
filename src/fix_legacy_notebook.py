import nbformat as nbf
import os

# プロジェクトルートを基準としたパス解決
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def update_intro_notebook():
    nb = nbf.v4.new_notebook()
    
    sections = [
        {
            "type": "markdown",
            "content": "# #00 Python & 地球科学データ解析：学習システムへようこそ\n\n本教材は、全ての操作をJupyter Notebook上で行えるように設計されています。まずはこのノートブックで環境のセットアップを行いましょう。"
        },
        {
            "type": "markdown",
            "content": "## 1. 開発環境の準備\n\n以下のセルを実行して、必要なライブラリがインストールされているか確認し、不足している場合はインストールします。"
        },
        {
            "type": "code",
            "content": "import sys\n!{sys.executable} -m pip install -r ../requirements.txt"
        },
        {
            "type": "markdown",
            "content": "## 2. 解析データの生成\n\n解析対象となる実戦的なダミーデータを生成します（欠損値やノイズが含まれます）。"
        },
        {
            "type": "code",
            "content": "import sys\nsys.path.append('../')\nfrom src.data_generator import generate_all_data\n\ngenerate_all_data()"
        },
        {
            "type": "markdown",
            "content": "## 3. 学習用ノートブックの生成・更新\n\nナビゲーション機能と視覚化テンプレートが含まれた課題ノートブックを生成します。"
        },
        {
            "type": "code",
            "content": "from src.notebook_generator import generate_all_10_notebooks\n\ngenerate_all_10_notebooks()"
        },
        {
            "type": "markdown",
            "content": "## 4. 進捗ダッシュボード\n\n現在の学習進捗状況を確認します。全てのモジュールで `SUCCESS` を目指しましょう。"
        },
        {
            "type": "code",
            "content": "from src.verifier import get_progress_summary\nfrom IPython.display import display, HTML\n\ntry:\n    df = get_progress_summary()\n    if df.empty:\n        print(\"まだ完了した課題はありません。\")\n    else:\n        display(df[['module_id', 'status', 'timestamp']].style.set_properties(**{'text-align': 'left'}))\nexcept Exception as e:\n    print(f\"進捗の読み込みに失敗しました: {e}\")"
        },
        {
            "type": "markdown",
            "content": "## 5. 学習の進め方\n\n1. `01_tabular_petrology.ipynb` から順にノートブックを開く\n2. データの視覚化を通じて、欠損値や異常値の影響を確認する\n3. 課題を実装し、検証セルで `SUCCESS` を確認する\n4. このノートブックに戻って進捗をチェックする"
        }
    ]
    
    for section in sections:
        if section['type'] == 'markdown':
            nb.cells.append(nbf.v4.new_markdown_cell(section['content']))
        else:
            nb.cells.append(nbf.v4.new_code_cell(section['content']))
            
    output_path = os.path.join(BASE_DIR, "notebooks", "00_introduction.ipynb")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        nbf.write(nb, f)
    print("Updated notebooks/00_introduction.ipynb with Progress Dashboard (Path Fixed).")

if __name__ == "__main__":
    update_intro_notebook()
