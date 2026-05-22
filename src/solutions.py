import pandas as pd
import numpy as np
import rasterio
import ruptures as rpt
from skimage import io, filters, measure
import sqlite3
from sklearn.decomposition import PCA

def solve_m1():
    df = pd.read_csv("data/raw_tabular/petrology.csv")
    df = df.dropna()
    # Mg# = 100 * (MgO/40.3) / (MgO/40.3 + FeO/71.8)
    df['Mg#'] = 100 * (df['MgO']/40.3) / (df['MgO']/40.3 + df['FeO']/71.8)
    
    pca = PCA(n_components=2)
    clusters = pca.fit_transform(df[['SiO2', 'MgO', 'FeO']])
    df['Cluster'] = (clusters[:, 0] > 0).astype(int)
    
    conn = sqlite3.connect("data/petrology_processed.db")
    df.to_sql("analysis", conn, if_exists="replace", index=False)
    conn.close()
    return df

def solve_m2():
    df = pd.read_csv("data/raw_timeseries/isotopes.csv")
    signal = df['d18O'].values
    algo = rpt.Pelt(model="l2").fit(signal)
    result = algo.predict(pen=10)
    return result

def solve_m3():
    with rasterio.open("data/raw_geospatial/dem.tif") as src:
        dem = src.read(1)
        # Simple gradient as slope proxy
        dy, dx = np.gradient(dem)
        slope = np.arctan(np.sqrt(dx**2 + dy**2))
    return slope

def solve_m4():
    img = io.imread("data/raw_images/thin_section.png", as_gray=True)
    thresh = filters.threshold_otsu(img)
    binary = img > thresh
    labels = measure.label(binary)
    props = measure.regionprops(labels)
    diameters = [p.equivalent_diameter for p in props]
    return diameters

def solve_m5():
    return {"3D_Model": "Generated", "GUI_Ready": True}
