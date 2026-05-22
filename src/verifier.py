import pandas as pd
import numpy as np
import pyperclip
from datetime import datetime
import traceback
import sqlite3
import os
from typing import Any, Dict, List, Callable, Optional

# Jupyter Notebook内でのリッチ表示用
try:
    from IPython.display import display, Markdown, HTML
    HAS_IPYTHON = True
except ImportError:
    HAS_IPYTHON = False

# プロジェクトルートを基準としたパス解決
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "learning_progress.db")

def init_progress_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS progress (
            module_id TEXT PRIMARY KEY,
            status TEXT,
            timestamp TEXT,
            summary TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_progress(module_id: str, status: str, summary: str):
    init_progress_db()
    conn = sqlite3.connect(DB_PATH)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn.execute("""
        INSERT OR REPLACE INTO progress (module_id, status, timestamp, summary)
        VALUES (?, ?, ?, ?)
    """, (module_id, status, timestamp, summary))
    conn.commit()
    conn.close()

def get_progress_summary() -> pd.DataFrame:
    init_progress_db()
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM progress", conn)
    conn.close()
    return df

def verify_m0_1(output_obj: Any) -> List[str]:
    # 期待される密度は約 3.125
    if not isinstance(output_obj, (float, int, np.float64, np.int64)):
        raise TypeError(f"Expected number, got {type(output_obj)}")
    if not (3.12 <= output_obj <= 3.13):
        raise ValueError(f"Density calculation is incorrect: {output_obj}")
    return [f"- Calculated density: {output_obj:.2f} (Correct)"]

def verify_m0_2(output_obj: Any) -> List[str]:
    # 期待されるのは列名のリストやIndexオブジェクト
    expected_cols = {'Sample_ID', 'SiO2', 'MgO', 'FeO', 'Cr_ppm'}
    actual_cols = set(output_obj)
    if not expected_cols.issubset(actual_cols):
        raise ValueError(f"Missing expected columns. Found: {actual_cols}")
    return [f"- Found columns: {', '.join(actual_cols)} (Correct)"]

def verify_m1(output_obj: Any) -> List[str]:
    if not isinstance(output_obj, pd.DataFrame): 
        raise TypeError("Expected pd.DataFrame")
    return [
        f"- Sample count: {len(output_obj)}",
        f"- Mean Mg#: {output_obj['Mg#'].mean():.2f}"
    ]

def verify_m2(output_obj: Any) -> List[str]:
    return [f"- Detected {len(output_obj)} change points."]

def verify_m3(output_obj: Any) -> List[str]:
    return [
        f"- Output shape: {output_obj.shape}",
        f"- Max slope: {np.nanmax(output_obj):.2f}"
    ]

def verify_m4(output_obj: Any) -> List[str]:
    return [f"- Counted {len(output_obj)} crystals."]

def verify_m5(output_obj: Any) -> List[str]:
    return [f"- {k}: {v}" for k, v in output_obj.items()]

def verify_m6(output_obj: Any) -> List[str]:
    if not isinstance(output_obj, pd.DataFrame): 
        raise TypeError("Expected pd.DataFrame")
    return [
        f"- Tephra samples clustered: {len(output_obj)}",
        f"- Distinct groups: {output_obj['Cluster'].nunique()}"
    ]

def verify_m7(output_obj: Any) -> List[str]:
    return [
        f"- Simulation steps: {len(output_obj)}",
        f"- Final state: {output_obj[-1][0]:.4f}"
    ]

def verify_m8(output_obj: Any) -> List[str]:
    return [f"- {k}: {v}" for k, v in output_obj.items()]

def verify_m9(output_obj: Any) -> List[str]:
    return [f"- Peaks identified: {len(output_obj)}"]

def verify_m10(output_obj: Any) -> List[str]:
    return [f"- {k}: {v}" for k, v in output_obj.items()]

VERIFIERS: Dict[str, Callable[[Any], List[str]]] = {
    'M0_1': verify_m0_1,
    'M0_2': verify_m0_2,
    'M1': verify_m1,
    'M2': verify_m2,
    'M3': verify_m3,
    'M4': verify_m4,
    'M5': verify_m5,
    'M6': verify_m6,
    'M7': verify_m7,
    'M8': verify_m8,
    'M9': verify_m9,
    'M10': verify_m10,
}

def verify_and_log(module_id: str, output_obj: Any) -> Optional[str]:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = "SUCCESS"
    logs = []
    
    try:
        if module_id in VERIFIERS:
            logs.extend(VERIFIERS[module_id](output_obj))
        else:
            raise ValueError(f"Unknown module ID: {module_id}")

    except Exception:
        status = "FAILED"
        logs.append(f"### Error Details\n```python\n{traceback.format_exc()}\n```")

    summary_text = "\n".join(logs)
    log_progress(module_id, status, summary_text)

    color = "#28a745" if status == "SUCCESS" else "#dc3545"
    md_output = (
        f"## Module {module_id} Verification Result <span style='color:{color}'>[{status}]</span>\n"
        f"- Timestamp: {timestamp}\n"
        f"- Status: {status}\n\n"
        f"### Analysis Summary\n" + summary_text
    )
    
    if HAS_IPYTHON:
        display(Markdown(md_output))
    else:
        print(md_output)
    
    try:
        pyperclip.copy(md_output)
    except Exception:
        pass

    return None
