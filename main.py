#CAS Debrief Timeline Generator
#Connect PyCharm to GitHub Repo
#Connect GitHub to Streamlit, Host on Streamlit

import streamlit as st
import pandas as pd
import numpy as np

blank_array = np.array([[1,2,3], [4,5,6], [7,8,9]], columns=['a', 'b', 'c'])
blank_dataframe = pd.DataFrame(blank_array)

st.dataframe(data=blank_dataframe)

