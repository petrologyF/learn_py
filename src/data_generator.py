import numpy as np
import pandas as pd
import os
import rasterio
from rasterio.transform import from_origin
import json

# Set seed for reproducibility
np.random.seed(42)

def generate_rock_composition(output_path):
    """
    Generates dummy rock composition data (wt%).
    Includes SiO2, TiO2, Al2O3, FeO, MgO, CaO, Na2O, K2O.
    Total should be around 100%.
    """
    n_samples = 100
    # Base composition for a typical basalt
    base = np.array([50.0, 1.5, 15.0, 10.0, 8.0, 10.0, 2.5, 0.5])
    noise = np.random.normal(0, 0.1, (n_samples, len(base)))
    data = base + noise * base
    
    # Normalize to around 100%
    totals = data.sum(axis=1)
    data = (data.T / totals * (99.5 + np.random.normal(0, 0.2, n_samples))).T
    
    columns = ['SiO2', 'TiO2', 'Al2O3', 'FeO', 'MgO', 'CaO', 'Na2O', 'K2O']
    df = pd.DataFrame(data, columns=columns)
    df.to_csv(output_path, index=False)
    print(f"Generated: {output_path}")

def generate_structural_data(output_path):
    """
    Generates strike and dip data with some outliers.
    """
    n_samples = 50
    # Main trend: strike around 45, dip around 30
    strike = np.random.normal(45, 10, n_samples) % 360
    dip = np.random.normal(30, 5, n_samples)
    dip = np.clip(dip, 0, 90)
    
    # Add outliers
    strike[0:5] = np.random.uniform(0, 360, 5)
    dip[0:5] = np.random.uniform(0, 90, 5)
    
    df = pd.DataFrame({'strike': strike, 'dip': dip})
    df.to_csv(output_path, index=False)
    print(f"Generated: {output_path}")

def generate_climate_data(output_path):
    """
    Generates 10 years of temperature and precipitation data.
    """
    dates = pd.date_range(start='2010-01-01', end='2019-12-31', freq='D')
    n_days = len(dates)
    
    # Temperature: seasonal cycle + trend + noise
    t = np.linspace(0, 10 * 2 * np.pi, n_days)
    temp = 15 + 10 * np.sin(t) + 0.0005 * np.arange(n_days) + np.random.normal(0, 2, n_days)
    
    # Precipitation: random events
    precip = np.random.exponential(2, n_days)
    precip[np.random.random(n_days) > 0.2] = 0 # 80% dry days
    
    df = pd.DataFrame({'date': dates, 'temperature': temp, 'precipitation': precip})
    
    # Add missing values
    mask = np.random.choice([True, False], size=df.shape[0], p=[0.05, 0.95])
    df.loc[mask, 'temperature'] = np.nan
    
    df.to_csv(output_path, index=False)
    print(f"Generated: {output_path}")

def generate_dem(output_path):
    """
    Generates a synthetic DEM using Gaussian peaks and valleys.
    """
    width, height = 512, 512
    x = np.linspace(-5, 5, width)
    y = np.linspace(-5, 5, height)
    X, Y = np.meshgrid(x, y)
    
    # Combination of Gaussians
    Z = 500 + 200 * np.exp(-(X**2 + Y**2)/2) \
        - 150 * np.exp(-((X-2)**2 + (Y-3)**2)/1.5) \
        + 100 * np.exp(-((X+3)**2 + (Y+2)**2)/2)
    
    # Add some noise
    Z += np.random.normal(0, 5, Z.shape)
    
    # Transform: 1 pixel = 10 meters, centered at 135.0E, 35.0N
    transform = from_origin(135.0, 35.0, 0.0001, 0.0001)
    
    new_dataset = rasterio.open(
        output_path, 'w', driver='GTiff',
        height=height, width=width,
        count=1, dtype=Z.dtype,
        crs='+proj=latlong',
        transform=transform,
    )
    new_dataset.write(Z, 1)
    new_dataset.close()
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    data_dir = "data"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        
    generate_rock_composition(os.path.join(data_dir, "rock_composition.csv"))
    generate_structural_data(os.path.join(data_dir, "structural_faults.csv"))
    generate_climate_data(os.path.join(data_dir, "climate_timeseries.csv"))
    generate_dem(os.path.join(data_dir, "synthetic_dem.tif"))
