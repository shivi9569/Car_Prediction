#X_train.columnsIndex(['year', 'km_driven', 'mileage(km/ltr/kg)', 'engine']
import streamlit as st
import joblib
import numpy as np

st.title(" Car Price Prediction App ")
st.divider()

st.write("This appwill help you to predict the prices of the Car")
st.divider()

Year = st.number_input("year", min_value=0, value=0)

km_driven= st.number_input("km_driven", min_value=0,value=0)

Mileage= st.number_input("mileage(km/ltr/kg)", min_value=0,value=0)

Engine = st.number_input("engine", min_value=0, value=0)

st.divider()

model= joblib.load("model.pkl")

X=[[Year,km_driven,Mileage,Engine]]

Perdictbutton= st.button("Predict")
if Perdictbutton:
    st.balloons()
    x_array= np.array(X)
    Prediction = model.predict(x_array)
    st.write(f" The price of the car is: {Prediction}")
else:
    st.write("Please click on the Predict button")