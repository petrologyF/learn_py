import numpy as np
import pandas as pd
from scipy import optimize
import rasterio

def exercise_ch02_composition(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the normalized weight percentage so that the sum of each row is 100%.
    """
    # Exclude non-numeric columns if any
    numeric_df = df.select_dtypes(include=[np.number])
    normalized = numeric_df.div(numeric_df.sum(axis=1), axis=0) * 100
    return normalized

def exercise_ch03_filter_outliers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filter out structural data outliers where dip > 90 or dip < 0.
    """
    return df[(df['dip'] >= 0) & (df['dip'] <= 90)]

def exercise_ch03_stereonet_coords(strike: float, dip: float) -> tuple:
    """
    Calculate (x, y) coordinates for equal-area projection (stereonet).
    Simplified: x = R * sin(dip/2) * sin(strike), y = R * sin(dip/2) * cos(strike)
    Assume strike/dip in degrees, R=1.
    """
    s = np.radians(strike)
    d = np.radians(dip)
    r = np.sin(d / 2.0)
    x = r * np.sin(s)
    y = r * np.cos(s)
    return x, y

def exercise_ch04_dem_stats(tif_path: str) -> dict:
    """
    Read DEM and return basic statistics (min, max, mean).
    """
    with rasterio.open(tif_path) as src:
        data = src.read(1)
        return {
            'min': float(np.min(data)),
            'max': float(np.max(data)),
            'mean': float(np.mean(data))
        }

def exercise_ch05_linear_fit(x: np.ndarray, y: np.ndarray) -> tuple:
    """
    Perform a simple linear regression y = ax + b.
    Return (a, b).
    """
    def model(x, a, b):
        return a * x + b
    
    # Handle NaNs
    mask = ~np.isnan(x) & ~np.isnan(y)
    params, _ = optimize.curve_fit(model, x[mask], y[mask])
    return tuple(params)
