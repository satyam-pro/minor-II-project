import streamlit as st
import pickle
import pandas as pd
import numpy as np
from PIL import Image

# Load the model and transformers
pipe = pickle.load(open('pipe.pkl', 'rb'))

# Define teams and cities
teams = ['Australia', 'India', 'Bangladesh', 'New Zealand', 'South Africa', 'England', 'West Indies', 'Afghanistan', 'Pakistan', 'Sri Lanka']
cities = ['Colombo', 'Mirpur', 'Johannesburg', 'Dubai', 'Auckland', 'Cape Town', 'London', 'Pallekele', 'Barbados', 'Sydney', 'Melbourne', 'Durban', 'St Lucia', 'Wellington', 'Lauderhill', 'Hamilton', 'Centurion', 'Manchester', 'Abu Dhabi', 'Mumbai', 'Nottingham', 'Southampton', 'Mount Maunganui', 'Chittagong', 'Kolkata', 'Lahore', 'Delhi', 'Nagpur', 'Chandigarh', 'Adelaide', 'Bangalore', 'St Kitts', 'Cardiff', 'Christchurch', 'Trinidad']

# Streamlit layout
title ='MEN T20 WORLD CUP SCORE PREDICTOR'
st.markdown(f"<h1 style='text-align: center'>{title}</h1>", unsafe_allow_html=True)
image2 = Image.open("t20.jpg")
st.image(image2)

# Input fields
col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('Select batting team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select bowling team', sorted(teams))
city = st.selectbox('Select city', sorted(cities))

col3, col4, col5 = st.columns(3)
with col3:
    current_score = st.number_input('Current Score')
with col4:
    overs = st.number_input('Overs done (works for over > 5)')
with col5:
    wickets = st.number_input('Wickets fallen')

last_five = st.number_input('Runs scored in last 5 overs')

if st.button('Predict Score'):
    balls_left = 120 - (overs * 6)
    wickets_left = 10 - wickets
    crr = current_score / overs

    # Create input DataFrame
    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [city],
        'current_score': [current_score],
        'balls_left': [balls_left],
        'wickets_left': [wickets_left],
        'crr': [crr],
        'last_five': [last_five]
    })

    # Predict score
    try:
        result = pipe.predict(input_df)
        st.header("Predicted Score by Satyam - " + str(int(result[0])))
    except Exception as e:
        st.error("Prediction failed. Error: {}".format(e))
