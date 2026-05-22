import numpy as np
import pandas as pd
import os
import rasterio
from rasterio.transform import from_origin

def generate_all_data():
    np.random.seed(42)
    base_data_dir = "data"
    
    # 1. numpy_data/: Structural Geology (Strike, Dip)
    # 200x3 ndarray: Strike (0-360), Dip (0-90), Dip Direction
    numpy_dir = os.path.join(base_data_dir, "numpy_data")
    os.makedirs(numpy_dir, exist_ok=True)
    
    strikes = np.random.uniform(0, 360, 200)
    dips = np.random.uniform(0, 90, 200)
    dip_directions = (strikes + 90) % 360
    
    structural_data = np.stack([strikes, dips, dip_directions], axis=1)
    
    # Introduce errors
    structural_data[10, 1] = -5.0
    structural_data[25, 0] = 400.0
    structural_data[50, 2] = np.nan
    
    np.save(os.path.join(numpy_dir, "structural_orientations.npy"), structural_data)
    
    # 2. pandas_data/: Petrology Major Elements
    pandas_dir = os.path.join(base_data_dir, "pandas_data")
    os.makedirs(pandas_dir, exist_ok=True)
    
    elements = ['SiO2', 'TiO2', 'Al2O3', 'FeO', 'MgO', 'CaO', 'Na2O', 'K2O']
    n_samples = 150
    comp_data = np.random.dirichlet(np.ones(len(elements)), size=n_samples) * 100
    df_petro = pd.DataFrame(comp_data, columns=elements)
    
    # Add 3% NaNs
    mask = np.random.random(df_petro.shape) < 0.03
    df_petro[mask] = np.nan
    
    df_petro.to_csv(os.path.join(pandas_dir, "major_elements.csv"), index=False)
    
    # 3. scipy_data/: Time Series Environmental Data
    scipy_dir = os.path.join(base_data_dir, "scipy_data")
    os.makedirs(scipy_dir, exist_ok=True)
    
    t = np.linspace(0, 100, 1000)
    trend = 0.5 * t
    seasonality = 10 * np.sin(2 * np.pi * t / 10)
    noise = np.random.normal(0, 2, 1000)
    signal = trend + seasonality + noise
    
    df_env = pd.DataFrame({'time': t, 'signal': signal})
    df_env.to_csv(os.path.join(scipy_dir, "environmental_series.csv"), index=False)
    
    # 4. geospatial_data/: DEM GeoTIFF
    geospatial_dir = os.path.join(base_data_dir, "geospatial_data")
    os.makedirs(geospatial_dir, exist_ok=True)
    
    width, height = 100, 100
    x = np.linspace(-3, 3, width)
    y = np.linspace(-3, 3, height)
    X, Y = np.meshgrid(x, y)
    Z = 1000 * np.exp(-(X**2 + Y**2) / 2)
    Z = Z.astype('float32')
    
    transform = from_origin(135.0, 35.0, 0.001, 0.001)
    
    with rasterio.open(
        os.path.join(geospatial_dir, "dem.tif"),
        'w',
        driver='GTiff',
        height=height,
        width=width,
        count=1,
        dtype=Z.dtype,
        crs='EPSG:4326',
        transform=transform,
    ) as dst:
        dst.write(Z, 1)

if __name__ == "__main__":
    generate_all_data()
    print("All data generated successfully.")
