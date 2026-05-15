import joblib
import pandas as pd
def make_prediction(area,lat,lon):
    """
    predict the apartment price

    Args:
        lat (float): latitude of the apartment's location
        lon (float): longitude of the apartment's location
        area (float): the are of the apartment in m2
    Returns:
        Pridected apartment price in USD: float    
    """
    model = joblib.load("../models/model.pkl")
    data = {
        "area_m2":area,
        "lat":lat,
        "lon":lon
    }
    df = pd.DataFrame(data, index=[0])
    prediction = model.predict(df).round(2)[0]
    return f"Predicted apartmen price is: {prediction} $"



