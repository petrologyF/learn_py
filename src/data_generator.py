import numpy as np
import pandas as pd
import rasterio
from rasterio.transform import from_origin
import os
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

def generate_tabular_petrology(path="data/raw_tabular/petrology.csv"):
    """
    Generates dummy petrology data: SiO2 vs MgO correlation with some NaNs.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    n_samples = 100
    sio2 = np.linspace(45, 75, n_samples) + np.random.normal(0, 2, n_samples)
    # MgO decreases as SiO2 increases (differentiation trend)
    mgo = 15 - (sio2 - 45) * 0.4 + np.random.normal(0, 1, n_samples)
    mgo = np.clip(mgo, 0.1, 15)
    
    # Add FeO for Mg# calculation later
    feo = 10 - (sio2 - 45) * 0.1 + np.random.normal(0, 0.5, n_samples)
    feo = np.clip(feo, 1, 15)

    df = pd.DataFrame({
        'Sample_ID': [f'SR-{i:03d}' for i in range(n_samples)],
        'SiO2': sio2,
        'MgO': mgo,
        'FeO': feo
    })
    
    # Inject some NaNs
    for col in ['SiO2', 'MgO', 'FeO']:
        indices = np.random.choice(df.index, size=5, replace=False)
        df.loc[indices, col] = np.nan
        
    df.to_csv(path, index=False)
    print(f"Generated: {path}")

def generate_timeseries_isotopes(path="data/raw_timeseries/isotopes.csv"):
    """
    Generates 10 years of daily isotope data with a change point.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    dates = pd.date_range(start="2010-01-01", periods=365*10, freq='D')
    n = len(dates)
    
    # Base signal with seasonality
    t = np.arange(n)
    signal = -10 + 2 * np.sin(2 * np.pi * t / 365.25) + np.random.normal(0, 0.5, n)
    
    # Change point at t=2000
    change_idx = 2000
    signal[change_idx:] += 3.0
    
    df = pd.DataFrame({
        'Date': dates,
        'd18O': signal
    })
    df.to_csv(path, index=False)
    print(f"Generated: {path}")

def generate_geospatial_dem(path="data/raw_geospatial/dem.tif"):
    """
    Generates a 100x100 virtual DEM using 2D Gaussian.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    size = 100
    x = np.linspace(-5, 5, size)
    y = np.linspace(-5, 5, size)
    x, y = np.meshgrid(x, y)
    
    # Gaussian mountain
    z = 1000 * np.exp(-(x**2 + y**2) / 10)
    # Add some noise/texture
    z += np.random.normal(0, 10, (size, size))
    
    # CRS and Transform (WGS84, near 0,0)
    transform = from_origin(135.0, 35.0, 0.01, 0.01)
    
    new_dataset = rasterio.open(
        path, 'w', driver='GTiff',
        height=size, width=size,
        count=1, dtype=z.dtype,
        crs='EPSG:4326',
        transform=transform,
    )
    new_dataset.write(z, 1)
    new_dataset.close()
    print(f"Generated: {path}")

def generate_thin_section_image(path="data/raw_images/thin_section.png"):
    """
    Generates a mock thin section image using Voronoi-like pattern.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    width, height = 256, 256
    points = np.random.randint(0, 256, (20, 2))
    
    img = np.zeros((height, width))
    
    for y in range(height):
        for x in range(width):
            dist = np.sum((points - [x, y])**2, axis=1)
            img[y, x] = np.argmin(dist)
            
    # Normalize and save
    img = (img - img.min()) / (img.max() - img.min())
    plt.imsave(path, img, cmap='gray')
    print(f"Generated: {path}")

def generate_all_data():
    generate_tabular_petrology()
    generate_timeseries_isotopes()
    generate_geospatial_dem()
    generate_thin_section_image()

if __name__ == "__main__":
    generate_all_data()
