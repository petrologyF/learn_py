import pyperclip
import numpy as np
import pandas as pd
from datetime import datetime
import geopandas as gpd

def verify_module(module_name, user_output):
    """
    ユーザーのパイプライン出力を検証し、Markdownレポートをクリップボードにコピーします。
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report = []
    report.append(f"## 📊 {module_name.upper()} モジュール検証レポート")
    report.append(f"- **実行日時**: {timestamp}")
    
    # モジュールごとの期待される入出力の明示
    io_info = {
        "numpy": {"input": "structural_orientations.npy", "output": "tuple (mean_strike, mean_dip)"},
        "pandas": {"input": "major_elements.csv", "output": "pd.DataFrame with Mg#"},
        "scipy": {"input": "environmental_series.csv", "output": "dict {params, fft}"},
        "geospatial": {"input": "dem.tif", "output": "gpd.GeoDataFrame"}
    }
    
    spec = io_info.get(module_name, {"input": "Unknown", "output": "Unknown"})
    report.append(f"\n### ⚙️ 仕様確認")
    report.append(f"- **対象インプット**: `{spec['input']}`")
    report.append(f"- **期待されるアウトプット**: `{spec['output']}`")
    
    status = "PASSED"
    analysis = []
    
    try:
        # 型判定と基本スキャン
        if isinstance(user_output, pd.DataFrame):
            analysis.append("- **実際のアウトプット型**: `pd.DataFrame`")
            analysis.append(f"- **形状 (Rows, Cols)**: `{user_output.shape}`")
            nan_count = user_output.isnull().sum().sum()
            analysis.append(f"- **残存欠損値数**: `{nan_count}`")
            if not user_output.empty:
                analysis.append("\n#### 📊 統計概要\n")
                analysis.append(user_output.describe().to_markdown())
            
        elif isinstance(user_output, np.ndarray):
            analysis.append("- **実際のアウトプット型**: `np.ndarray`")
            analysis.append(f"- **形状**: `{user_output.shape}`")
            analysis.append(f"- **平均値**: `{np.nanmean(user_output):.4f}`")
            
        elif isinstance(user_output, dict):
            analysis.append("- **実際のアウトプット型**: `dict`")
            analysis.append(f"- **取得キー**: `{list(user_output.keys())}`")
            
        elif isinstance(user_output, gpd.GeoDataFrame):
            analysis.append("- **実際のアウトプット型**: `gpd.GeoDataFrame`")
            analysis.append(f"- **CRS**: `{user_output.crs}`")
            analysis.append(f"- **レコード数**: `{len(user_output)}`")
            
        elif isinstance(user_output, (list, tuple)):
            analysis.append("- **実際のアウトプット型**: `list/tuple`")
            analysis.append(f"- **要素数**: `{len(user_output)}`")
            analysis.append(f"- **取得値**: `{user_output}`")
        else:
            status = "WARNING"
            analysis.append(f"- **不明な型**: `{type(user_output)}`")

        # モジュール固有のチェック
        if module_name == "numpy":
            if not isinstance(user_output, (list, tuple, np.ndarray)) or len(user_output) != 2:
                status = "WARNING"
                analysis.append("⚠️ **判定**: 要素数2の数値ペアが返されていません。")
        elif module_name == "pandas":
            if isinstance(user_output, pd.DataFrame):
                if not any(c in user_output.columns for c in ['Mg#', 'Mg_number']):
                    status = "WARNING"
                    analysis.append("⚠️ **判定**: `Mg#` カラムが見つかりません。")
        elif module_name == "scipy":
            if not isinstance(user_output, dict) or 'params' not in user_output:
                status = "WARNING"
                analysis.append("⚠️ **判定**: `params` キーが欠落しています。")

    except Exception as e:
        status = "ERROR"
        analysis.append(f"❌ **システムエラー**: {str(e)}")

    report.append(f"- **最終ステータス**: `{status}`")
    report.append("\n### 🔍 実行詳細分析")
    report.extend(analysis)
    
    final_text = "\n".join(report)
    print(final_text)
    
    try:
        pyperclip.copy(final_text)
        print("\n" + "✨" * 20)
        print("✅ 検証ログをクリップボードにコピーしました！")
        print("学習記録ノート等にペーストして活用してください。")
        print("✨" * 20)
    except Exception as cp_e:
        print(f"\n❌ クリップボード連携に失敗しました: {cp_e}")

    return status
