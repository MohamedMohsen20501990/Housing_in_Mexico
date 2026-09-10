import pytest
from src.data import DataHandler
import pandas as pd



@pytest.fixture
def data_handler():
    """Creates a new instance of DataHandler class before every single test"""
    return DataHandler()


def test_wrangle_data(data_handler):
    
    result = data_handler.wrangle_data("data/raw/mexico-city-real-estate-1.csv")
    assert isinstance(result, pd.DataFrame), "Output is not a DataFrame"
    

def test_df_from_multiple_files(data_handler):
    result = data_handler.df_from_multiple_files("data/raw/mexico-city-real-estate-*.csv") 
    assert isinstance(result, pd.DataFrame), "Output is not a DataFrame"
    
    
def test_save_data(data_handler):
    result = data_handler.wrangle_data("data/raw/mexico-city-real-estate-1.csv")
    data_handler.save_data(result,"data/processed/test.csv") ==True    