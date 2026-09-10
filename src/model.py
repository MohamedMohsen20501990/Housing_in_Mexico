import pandas as pd
import pickle

class RFModel:
    """
    Handle loading and making predictions with a trained linear regression model.

    The LRModel class loads a trained machine learning model from a pickle
    file and uses it to predict apartment prices based on the apartment's
    area and geographical location.

    Methods
    -------
    load(path)
        Load a trained machine learning model from a pickle file.
    make_prediction(area, lat, lon)
        Predict the apartment price in USD based on its area and location.
    """
        
    def __init__(self, path:str):
        self.path = path
        self.__load()
            
    def __load(self):
        """
        Load a trained machine learning model from a pickle file.

        Returns
        -------
        model
            The trained model loaded from the file specified by ``self.path``.
        """
        with open(self.path, mode="rb") as f:
            self.model=pickle.load(f)
            
        
    def make_prediction(self,area,lat,lon):
        """
        predict the apartment price

        Args:
            lat (float): latitude of the apartment's location
            lon (float): longitude of the apartment's location
            area (float): the are of the apartment in m2
        Returns:
            Pridected apartment price in USD: float    
        """

        data = {
            "area_m2":area,
            "lat":lat,
            "lon":lon
        }
        df = pd.DataFrame(data, index=[0])
        prediction = self.model.predict(df).round(2)[0]
        return prediction



