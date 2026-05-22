import pandas as pd
import numpy as np
import matplotlib.figure
import pyperclip
from datetime import datetime
import traceback

def verify_and_log(module_id, output_obj):
    """
    Verifies the output of a module pipeline and logs the result to clipboard.
    
    Args:
        module_id (str): Identifier of the module (e.g., 'M1', 'M2', ...)
        output_obj: The object to be verified.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = "SUCCESS"
    logs = []
    
    try:
        if module_id == 'M1': # Tabular Petrology
            # Expecting a DataFrame with Mg# and Cluster columns
            if not isinstance(output_obj, pd.DataFrame):
                raise TypeError(f"Expected pd.DataFrame, got {type(output_obj)}")
            
            required_cols = ['Mg#', 'Cluster']
            for col in required_cols:
                if col not in output_obj.columns:
                    raise ValueError(f"Missing required column: {col}")
            
            mg_mean = output_obj['Mg#'].mean()
            logs.append(f"- Sample count: {len(output_obj)}")
            logs.append(f"- Mean Mg#: {mg_mean:.2f}")
            logs.append(f"- Found {output_obj['Cluster'].nunique()} distinct clusters.")

        elif module_id == 'M2': # Time-series Granulometry
            # Expecting a list of change points (integers)
            if not isinstance(output_obj, (list, np.ndarray)):
                 raise TypeError(f"Expected list or np.ndarray, got {type(output_obj)}")
            
            logs.append(f"- Detected {len(output_obj)} change points.")
            logs.append(f"- Indices: {output_obj}")

        elif module_id == 'M3': # Geospatial Mapping
            # Expecting a slope array or similar
            if not isinstance(output_obj, np.ndarray):
                raise TypeError(f"Expected np.ndarray, got {type(output_obj)}")
            
            logs.append(f"- Output shape: {output_obj.shape}")
            logs.append(f"- Max slope: {np.nanmax(output_obj):.2f}")

        elif module_id == 'M4': # Image Geometry
            # Expecting a list of crystal diameters
            if not isinstance(output_obj, (list, np.ndarray)):
                raise TypeError(f"Expected list or np.ndarray, got {type(output_obj)}")
            
            logs.append(f"- Counted {len(output_obj)} crystals.")
            logs.append(f"- Mean diameter: {np.mean(output_obj):.2f} pixels.")

        elif module_id == 'M5': # Volume GUI
            # Expecting a status dict
            if not isinstance(output_obj, dict):
                raise TypeError(f"Expected dict, got {type(output_obj)}")
            for k, v in output_obj.items():
                logs.append(f"- {k}: {v}")
        
        else:
            raise ValueError(f"Unknown module ID: {module_id}")

    except Exception as e:
        status = "FAILED"
        logs.append(f"### Error Details\n```python\n{traceback.format_exc()}\n```")

    # Construct Markdown
    md_output = f"""
## Module {module_id} Verification Result [{status}]
- **Timestamp:** {timestamp}
- **Status:** {status}

### Analysis Summary
{"".join(logs if status == "SUCCESS" else [logs[0]])}

---
*Verified by learn-py system*
"""
    if status == "FAILED":
        md_output += f"\n{logs[-1]}"

    try:
        pyperclip.copy(md_output)
        print("✅ 検証が完了しました。Markdown形式のレポートがクリップボードにコピーされました。")
        print("Obsidianなどのノートアプリにペーストして記録してください。")
    except Exception as e:
        print(f"❌ クリップボードへのコピーに失敗しました: {e}")
        print("以下の内容を手動でコピーしてください：")
        print(md_output)

    return md_output

if __name__ == "__main__":
    # Test M1 failure
    verify_and_log('M1', None)
