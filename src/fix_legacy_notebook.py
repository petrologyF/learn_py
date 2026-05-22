import nbformat as nbf

def fix_basic_notebook():
    nb = nbf.v4.new_notebook()
    
    sections = [
        {
            "type": "markdown",
            "content": "# #00 Python & Jupyter 入門\n\n地球科学解析を始める前に、Pythonの基本的な文法とJupyter Notebookの使い方を確認しましょう。"
        },
        {
            "type": "markdown",
            "content": "## 1. Pythonの基本演算\nPythonでのべき乗（二乗など）は `**` 演算子を使います。`^` はビット演算（XOR）なので注意が必要です。\n\n$$y = x^2$$\n\nこれをPythonで書くと `y = x ** 2` となります。"
        },
        {
            "type": "code",
            "content": "def exercise_ch00_square(n):\n    \"\"\"数値 n の二乗を返す関数\"\"\"\n    y = n ** 2\n    return y\n\n# テスト実行\nprint(f'3の二乗は: {exercise_ch00_square(3)}')"
        },
        {
            "type": "markdown",
            "content": "## 2. 地球科学の計算例：密度の計算\n密度 $\\rho$ は、質量 $m$ と体積 $V$ から以下の式で求められます。\n\n$$\\rho = \\frac{m}{V}$$\n\n以下のセルで、岩石の密度を計算する関数を作成してみましょう。"
        },
        {
            "type": "code",
            "content": "def calculate_density(mass, volume):\n    \"\"\"\n    質量(g)と体積(cm^3)から密度(g/cm^3)を計算する\n    \"\"\"\n    if volume == 0:\n        return 0\n    return mass / volume\n\n# 質量 100g, 体積 37cm^3 の岩石の密度\nrho = calculate_density(100, 37)\nprint(f'密度: {rho:.2f} g/cm^3')"
        }
    ]
    
    for section in sections:
        if section['type'] == 'markdown':
            nb.cells.append(nbf.v4.new_markdown_cell(section['content']))
        else:
            nb.cells.append(nbf.v4.new_code_cell(section['content']))
            
    with open("notebooks/01_basic_syntax_and_jupyter.ipynb", 'w', encoding='utf-8') as f:
        nbf.write(nb, f)
    print("Fixed and updated notebooks/01_basic_syntax_and_jupyter.ipynb")

if __name__ == "__main__":
    fix_basic_notebook()
