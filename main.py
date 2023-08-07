#CAS Debrief Timeline Generator
#Connect PyCharm to GitHub Repo
#Connect GitHub to Streamlit, Host on Streamlit

import streamlit as st
import pandas as pd
import numpy as np

st.title("CAS TIMELINE GENERATOR")
st.subheader("This data is :green[UNCLASS]")

#The first input DataFrame for Vul Start and KIO Times
st.header("Input the Vul Start and KIO Times")

start_df = pd.DataFrame(
    [
        {"Vul Start":"12:00:00", "Knock It Off": "12:00:00"}
    ]
)

edited_start_df = st.data_editor(start_df)

#The second input DataFrame for Blue Timeline
st.header("Input :blue[Blue Timeline] Here (9-Lines)")

blue_df = pd.DataFrame(
    [
        {"Label": "Alpha", "From": "XR99", "To": "Hog", "Nominated": "12:00:00", "Passed": "12:00:00", "First Effect": "12:00:00", "Last Effect": "12:00:00"},
        {"Label": "Bravo", "From": "XR99", "To": "Hog", "Nominated": "12:00:00", "Passed": "12:00:00", "First Effect": "12:00:00", "Last Effect": "12:00:00"},
        {"Label": "Charlie", "From": "XR99", "To": "Hog", "Nominated": "12:00:00", "Passed": "12:00:00", "First Effect": "12:00:00", "Last Effect": "12:00:00"}
    ]
)

edited_blue_df = st.data_editor(blue_df, num_rows="dynamic")

#The third input DataFrame for Red Timeline
st.header("Input :red[Red Timeline] Here (IDF)")

red_df = pd.DataFrame(
    [
        {"Label": "1st IDF", "Start": "12:00:00", "End": "12:00:00"}
    ]
)

edited_red_df = st.data_editor(red_df, num_rows="dynamic")