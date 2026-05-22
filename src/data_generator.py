import numpy as np
import pandas as pd
import rasterio
from rasterio.transform import from_origin
import os
from skimage import io

# Set random seed for reproducibility
np.random.seed(42)

def add_geoscience_artifacts(df, columns, nan_ratio=0.05, outlier_ratio=0.02):
    """地球科学データ特有の欠損値や外れ値を注入する"""
    for col in columns:
        # 欠損値 (NaN)
        mask = np.random.rand(len(df)) < nan_ratio
        df.loc[mask, col] = np.nan
        
        # 外れ値 (測定ミス等のシミュレーション)
        outlier_mask = np.random.rand(len(df)) < outlier_ratio
        df.loc[outlier_mask, col] *= np.random.choice([0.1, 10.0])
    return df

def generate_tabular_petrology(path="data/raw_tabular/petrology.csv"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    n_samples = 150
    sio2 = np.linspace(45, 75, n_samples) + np.random.normal(0, 2, n_samples)
    mgo = 15 - (sio2 - 45) * 0.4 + np.random.normal(0, 1, n_samples)
    mgo = np.clip(mgo, 0.1, 15)
    feo = 10 - (sio2 - 45) * 0.1 + np.random.normal(0, 0.5, n_samples)
    # 微量元素の追加
    cr = 1000 * np.exp(-(sio2 - 45)/5) + np.random.normal(0, 50, n_samples)
    cr = np.clip(cr, 10, None)

    df = pd.DataFrame({
        'Sample_ID': [f'SR-{i:03d}' for i in range(n_samples)], 
        'SiO2': sio2, 'MgO': mgo, 'FeO': feo, 'Cr_ppm': cr
    })
    df = add_geoscience_artifacts(df, ['SiO2', 'MgO', 'FeO', 'Cr_ppm'])
    df.to_csv(path, index=False)

def generate_timeseries_isotopes(path="data/raw_timeseries/isotopes.csv"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    dates = pd.date_range(start="2010-01-01", periods=365*10, freq='D')
    signal = -10 + 2 * np.sin(2 * np.pi * np.arange(len(dates)) / 365.25) + np.random.normal(0, 0.5, len(dates))
    signal[2000:] += 3.0 # 急変点
    
    df = pd.DataFrame({'Date': dates, 'd18O': signal})
    # 欠損値の追加（センサー故障想定）
    mask = np.random.rand(len(df)) < 0.03
    df.loc[mask, 'd18O'] = np.nan
    df.to_csv(path, index=False)

def generate_geospatial_dem(path="data/raw_geospatial/dem.tif"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    size = 100
    x, y = np.meshgrid(np.linspace(-5, 5, size), np.linspace(-5, 5, size))
    z = 1000 * np.exp(-(x**2 + y**2) / 10) + 50 * np.sin(x) # 地形にノイズ追加
    with rasterio.open(path, 'w', driver='GTiff', height=size, width=size, count=1, dtype=z.dtype, crs='EPSG:4326', transform=from_origin(135.0, 35.0, 0.01, 0.01)) as dst:
        dst.write(z, 1)

def generate_thin_section_image(path="data/raw_images/thin_section.png"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    points = np.random.randint(0, 256, (30, 2))
    img = np.zeros((256, 256), dtype=np.uint8)
    for y in range(256):
        for x in range(256):
            img[y, x] = np.argmin(np.sum((points - [x, y])**2, axis=1)) * 8
    # 画像ノイズの追加
    noise = np.random.randint(0, 20, img.shape, dtype=np.uint8)
    img = np.clip(img + noise, 0, 255)
    io.imsave(path, img)

def generate_tephra_data(path="data/raw_tabular/tephra_comp.csv"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    n = 150
    c1 = np.random.multivariate_normal([60, 15, 2], [[1,0,0],[0,0.5,0],[0,0,0.2]], 50)
    c2 = np.random.multivariate_normal([70, 12, 4], [[1,0,0],[0,0.5,0],[0,0,0.2]], 50)
    c3 = np.random.multivariate_normal([75, 10, 5], [[1,0,0],[0,0.5,0],[0,0,0.2]], 50)
    data = np.vstack([c1, c2, c3])
    df = pd.DataFrame(data, columns=['SiO2', 'Al2O3', 'K2O'])
    df['Tephra_ID'] = [f'TP-{i:03d}' for i in range(150)]
    df = add_geoscience_artifacts(df, ['SiO2', 'Al2O3', 'K2O'], nan_ratio=0.02)
    df.to_csv(path, index=False)

def generate_all_data():
    generate_tabular_petrology()
    generate_timeseries_isotopes()
    generate_geospatial_dem()
    generate_thin_section_image()
    generate_tephra_data()
    print("All realistic geoscientific dummy data generated.")

if __name__ == "__main__":
    generate_all_data()

if __name__ == "__main__":
    generate_all_data()
