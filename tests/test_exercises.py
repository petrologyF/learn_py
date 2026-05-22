import pytest
import numpy as np
import pandas as pd
import os
from src import solutions, data_generator

@pytest.fixture(scope="module", autouse=True)
def setup_data():
    """テスト実行前にダミーデータを生成する"""
    data_generator.generate_all_data()

def test_solve_m1():
    df = solutions.solve_m1()
    assert isinstance(df, pd.DataFrame)
    assert 'Mg#' in df.columns
    assert 'Cluster' in df.columns
    assert not df['Mg#'].isnull().any()

def test_solve_m2():
    result = solutions.solve_m2()
    assert isinstance(result, list)
    assert len(result) > 0

def test_solve_m3():
    slope = solutions.solve_m3()
    assert isinstance(slope, np.ndarray)
    assert slope.ndim == 2

def test_solve_m4():
    diameters = solutions.solve_m4()
    assert isinstance(diameters, list)
    if len(diameters) > 0:
        assert isinstance(diameters[0], (float, np.float64))

def test_solve_m5():
    res = solutions.solve_m5()
    assert res['GUI_Ready'] is True

def test_solve_m6():
    df = solutions.solve_m6()
    assert isinstance(df, pd.DataFrame)
    assert 'Cluster' in df.columns
    assert df['Cluster'].nunique() <= 3

def test_solve_m7():
    sol = solutions.solve_m7()
    assert isinstance(sol, np.ndarray)
    assert sol.shape == (100, 1)

def test_solve_m8():
    res = solutions.solve_m8()
    assert res['Photos_Processed'] == 15

def test_solve_m9():
    peaks = solutions.solve_m9()
    assert isinstance(peaks, np.ndarray)

def test_solve_m10():
    res = solutions.solve_m10()
    assert res['Engine'] == 'Dask'
