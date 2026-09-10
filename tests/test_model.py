import pytest
from src.model import RFModel

@pytest.fixture
def rfm_model():
    """Creates a new instance of RFModel class before every single test"""
    return RFModel(path="models/rf_model.pkl")

def test_make_prediction(rfm_model):
    data = {
        "area": 60,
        "lat": 19.9,
        "lon": -99.16
    }
    prediction = rfm_model.make_prediction(**data)
    assert isinstance(prediction, float)
    assert prediction>0