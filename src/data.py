import pandas as pd
from pathlib import Path
from glob import glob

PROJECT_ROOT = Path(__file__).resolve().parent.parent



class DataHandler:
    """
    Handle loading and preprocessing of real-estate datasets.

    The DataHandler class reads raw real-estate data from CSV files,
    performs data cleaning and preprocessing, filters the data based
    on selected criteria, handles outliers, and returns cleaned
    pandas DataFrames.
    """
        
    def wrangle_data(self, path) -> pd.DataFrame: 
        """
        Manipulate the uncleaned data
        

        Args:
            path(str):the path of the data

        Returns:
            DataFrame: cleaned Dataframe
        """
        
        # creating a data frame 
        df = pd.read_csv(path)
        
        # Creating lat and lon columns
        df[["lat", "lon"]]=df["lat-lon"].str.split(",", expand=True).astype("float")
        
        # Extract the state column from "place with parents name column"
        df["state"]=df["place_with_parent_names"].str.split("|", expand=True)[2]
        
        # extracing the price_usd column
        df["price_usd"] = df["price"].apply(lambda x: x/17).astype("float")
        
        # rename the surface_covered_in_m2 column
        df.rename(columns={"surface_covered_in_m2": "area_m2"}, inplace=True)
        
        # mask for the 'aparments'
        mask_ap = df["property_type"]=="apartment"
        
        # mask for the price
        mask_pr = df["price_usd"] < 400_000
        
        # mask for Distrito federal
        mask_dr = df["state"]== "Distrito Federal"
        
        # filtering the dataset
        df = df[mask_ap & mask_pr & mask_dr]
        
        # Outliers
        low, high = df["area_m2"].quantile([0.1,0.9])
        mask_ar = df["area_m2"].between(low,high)
        df = df[mask_ar]
        
        # drop the columns that have large numbers of nulls
        df.drop(["rooms","floor","expenses"], axis=1, inplace=True)
        
        # Leakage - drop leaky columns 
        df.drop(columns=["price_usd_per_m2", "surface_total_in_m2"], inplace=True)
        
        # Multicollinarity -  Drop the high colrelated to each other columns
        df.drop(columns=["price_aprox_local_currency","price_aprox_usd", "price_per_m2","price"], inplace=True)
        
        # Low & High cardinality -  drop the low and high cardinality columns
        df.drop(columns=["currency","properati_url","operation","property_type", "state"], inplace=True)
        
        # drop 'place with parents names' column and 'lat-lon' columns
        df.drop(columns=["lat-lon","place_with_parent_names"], inplace=True)
        
        # reset the index
        df = df.reset_index(drop=True)
        
        return df
    
    
    def df_from_multiple_files(self, path:str) -> pd.DataFrame:
        """Load, wrangle, and combine data from multiple files into a single DataFrame.

        Parameters
        ----------
        path : str
            File pattern (glob pattern) used to identify the input files.
            For example, ``"data/*.csv"``.

        Returns
        -------
        pandas.DataFrame
            A single DataFrame containing the wrangled data from all matching files,
            concatenated row-wise with a reset index.

        Notes
        -----
        Each file is processed using the ``wrangle_data`` method before the
        resulting DataFrames are concatenated.
        """
        # Extracting the file paths from glob
        files = glob(path)
        
        # Exctracting the data frames list
        frames = [self.wrangle_data(file) for file in files]
        
        # Concatinating our frames list
        df = pd.concat(frames, axis=0, ignore_index=True)
        
        return df
    
    def save_data(self, df: pd.DataFrame, path: str) -> None:
        """
        Save a DataFrame to a CSV file.

        Parameters
        ----------
        df : pandas.DataFrame
            The DataFrame to save.
        path : str
            The file path where the CSV file will be saved.

        Returns
        -------
        None
            This method saves the DataFrame to a file and does not return a value.
        """        
        df.to_csv(path, index=False)
        return True
        