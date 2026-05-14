import pandas as pd
def wrangle_data(path):
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
    
    # mask for the aparments
    mask_ap = df["property_type"]=="apartment"
    
    # mask for the price
    mask_pr = df["price_usd"] < 400_000
    
    # mask for Distrito federal
    mask_dr = df["state"]== "Distrito Federal"
    
    # filtering the dataset
    df = df[mask_ap & mask_pr & mask_dr]
    
    # dealing with outliers
    low, high = df["area_m2"].quantile([0.1,0.9])
    mask_ar = df["area_m2"].between(low,high)
    df = df[mask_ar]
    
    
    # drop leaky columns
    df.drop(columns=["price_usd_per_m2", "surface_total_in_m2","rooms","floor","expenses"], inplace=True)
    
    # Drop the high colrelated to each other columns
    df.drop(columns=["price_aprox_local_currency","price_aprox_usd", "price_per_m2","price"], inplace=True)
    
    # drop the low and high cardinality columns
    df.drop(columns=["currency","properati_url","operation"], inplace=True)
    
    # drop place with parents names column and lat-lon columns
    df.drop(columns=["lat-lon","place_with_parent_names"], inplace=True, errors="ignore")
    
    # reset the index
    df = df.reset_index(drop=True)
    
    return df