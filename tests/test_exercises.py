import pytest
import numpy as np
import pandas as pd
import os
from src import solutions

def test_ch02_composition():
    data = {
        'SiO2': [50, 60],
        'MgO': [10, 5]
    }
    df = pd.DataFrame(data)
    result = solutions.exercise_ch02_composition(df)
    assert result.iloc[0].sum() == pytest.approx(100.0)
    assert result.iloc[1].sum() == pytest.approx(100.0)
    assert result['SiO2'].iloc[0] == pytest.approx(50 / 60 * 100)

def test_ch03_filter_outliers():
    data = {
        'strike': [10, 20, 30],
        'dip': [30, 110, -5]
    }
    df = pd.DataFrame(data)
    result = solutions.exercise_ch03_filter_outliers(df)
    assert len(result) == 1
    assert result['dip'].iloc[0] == 30

def test_ch03_stereonet_coords():
    # 0 strike, 90 dip -> North on the edge
    x, y = solutions.exercise_ch03_stereonet_coords(0, 90)
    # sin(45) * sin(0) = 0
    # sin(45) * cos(0) = 0.707
    assert x == pytest.approx(0)
    assert y == pytest.approx(np.sin(np.radians(45)))

def test_ch05_linear_fit():
    x = np.array([0, 1, 2, 3])
    y = np.array([1, 3, 5, 7]) # y = 2x + 1
    a, b = solutions.exercise_ch05_linear_fit(x, y)
    assert a == pytest.approx(2.0)
    assert b == pytest.approx(1.0)
