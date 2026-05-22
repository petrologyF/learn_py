import pyperclip
import numpy as np
import pandas as pd
from datetime import datetime

def check_and_copy(chapter, question, output):
    """
    Analyzes the user's output, provides feedback, and copies the result to the clipboard in Markdown format.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header = f"### [Learning Log] Chapter {chapter}, Question {question} ({timestamp})\n"
    
    analysis = ""
    status = "[SUCCESS]"
    
    # Analysis based on type
    if isinstance(output, pd.DataFrame):
        analysis += f"- **Type**: `pd.DataFrame`\n"
        analysis += f"- **Shape**: `{output.shape}`\n"
        analysis += f"- **Columns**: `{list(output.columns)}`\n"
        analysis += f"- **Basic Stats**:\n\n{output.describe().to_markdown()}\n"
    elif isinstance(output, pd.Series):
        analysis += f"- **Type**: `pd.Series`\n"
        analysis += f"- **Length**: `{len(output)}`\n"
        analysis += f"- **Mean**: `{output.mean():.4f}`\n"
    elif isinstance(output, np.ndarray):
        analysis += f"- **Type**: `np.ndarray`\n"
        analysis += f"- **Shape**: `{output.shape}`\n"
        analysis += f"- **Dtype**: `{output.dtype}`\n"
        analysis += f"- **Mean**: `{np.nanmean(output):.4f}`\n"
    elif isinstance(output, (dict, list)):
        analysis += f"- **Type**: `{type(output).__name__}`\n"
        analysis += f"- **Content**: `{output}`\n"
    elif isinstance(output, (int, float)):
        analysis += f"- **Type**: `Scalar`\n"
        analysis += f"- **Value**: `{output:.4f}`\n"
    else:
        analysis += f"- **Type**: `{type(output).__name__}`\n"
        analysis += f"- **Value**: `{output}`\n"
        status = "[INFO]"

    # Feedback Logic (Example: Validation criteria)
    feedback = ""
    if chapter == 1:
        if isinstance(output, (int, float)) and output > 0:
            feedback = "Great! The square of the number is calculated correctly."
        else:
            status = "[WARNING]"
            feedback = "Double-check the implementation. Is it returning a positive number?"

    # Assemble Markdown
    markdown_output = f"{header}\n**Status**: {status}\n\n{analysis}\n\n**Feedback**: {feedback}\n\n---\n"
    
    # Display in console/notebook
    print(markdown_output)
    
    # Copy to clipboard
    try:
        pyperclip.copy(markdown_output)
        print("✅ Result copied to clipboard in Markdown format!")
    except Exception as e:
        print(f"❌ Failed to copy to clipboard: {e}")

    return status
