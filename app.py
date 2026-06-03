import streamlit as st
import pandas as pd
import joblib


st.write(
    """
    ## Housing price in Mexico prediction app
    this app predicts the house's prices in **Mexico**
    
    
    """
)
st.image("mexico.jpg")

st.sidebar.header("User Input Parameters")

def user_input_features():
    area_m2= st.sidebar.slider("area [m2]", 40.5 , 160.0, 79.5)
    lat	= st.sidebar.slider("Lat", 19.0 , 25.0, 19.3)
    lon = st.sidebar.slider("Loan", -105.0, -90.0, -99.0)
    
    data={
        "area_m2": area_m2,
        "lat": lat,
        "lon": lon
    }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader("User Input Parameters")
st.write(df)

model = joblib.load("models/model.pkl")

prediction = model.predict(df)
st.subheader("Price for this house in USD is: ")
st.write(prediction)


    
