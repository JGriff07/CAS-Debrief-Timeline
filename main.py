#CAS Debrief Timeline Generator
#Connect PyCharm to GitHub Repo
#Connect GitHub to Streamlit, Host on Streamlit

import streamlit as st
import pandas as pd
import numpy as np

st.title("CAS TIMELINE GENERATOR")
st.subheader("This data is UNCLASS")

st.header("Input 9-Lines Here")

df = pd.DataFrame(
    [
        {"Label": "Alpha", "From": "XR99", "To": "Hog", "Nominated": "12:00:00"},
        {"Label": "Bravo", "From": "XR99", "To": "Hog", "Nominated": "12:00:00"},
        {"Label": "Charlie", "From": "XR99", "To": "Hog", "Nominated": "12:00:00"}
    ]
)

edited_df = st.data_editor(df, num_rows="dynamic")

