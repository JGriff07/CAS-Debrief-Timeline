#CAS Debrief Timeline Generator
#Connect PyCharm to GitHub Repo
#Connect GitHub to Streamlit, Host on Streamlit

import streamlit as st
import pandas as pd
import numpy as np
import process_blue as pb
import process_red as pr
import matplotlib.pyplot as plt
from PIL import Image

#Title the Streamlit Page
st.title("CAS TIMELINE GENERATOR")
st.subheader("This data is :green[UNCLASS]")

#The first input DataFrame for Vul Start and KIO Times
st.header("Input the Vul Start and KIO Times")

start_df = pd.DataFrame(
    [
        {"Vul Start":"12:00:00", "Knock It Off": "13:00:00"}
    ]
)

edited_start_df = st.data_editor(start_df)

#The second input DataFrame for Blue Timeline
st.header("Input :blue[Blue Timeline] Here (9-Lines)")

blue_df = pd.DataFrame(
    [
        {"Label": "Alpha", "From": "XR99", "To": "Hog", "Nominated": "12:01:00", "Passed": "12:03:00", "First Effect": "12:05:00", "Last Effect": "12:10:00"},
        {"Label": "Bravo", "From": "XR99", "To": "Hog", "Nominated": "12:11:00", "Passed": "12:13:00", "First Effect": "12:15:00", "Last Effect": "12:20:00"},
        {"Label": "Charlie", "From": "XR99", "To": "Hog", "Nominated": "12:21:00", "Passed": "12:23:00", "First Effect": "12:25:00", "Last Effect": "12:30:00"}
    ]
)

edited_blue_df = st.data_editor(blue_df, num_rows="dynamic")
#Process blue_df to create Aircraft Timeline label, start_time, and end_time
processed_blue_df = pb.process_blue_timeline(edited_blue_df, edited_start_df)

#Process blue_df to create JTAC Timeline label, start_time, and end_time
processed_jtac_df = pb.process_jtac_timeline(edited_blue_df, edited_start_df)

#The third input DataFrame for Red Timeline
st.header("Input :red[Red Timeline] Here (IDF)")

red_df = pd.DataFrame(
    [
        {"Label": "1st IDF", "Start": "12:10:00", "End": "12:20:00"}
    ]
)

edited_red_df = st.data_editor(red_df, num_rows="dynamic")

#Process the red_df to label, start_time, and end_time
processed_red_df = pr.process_red_timeline(edited_red_df, edited_start_df)

if st.button(label='Generate Timeline', help='Must use "12:00:00" format.'):
    #Do all The MATPLOTLIB HERE
    # plot the graph
    fig, (ax0, ax1, ax2) = plt.subplots(ncols=1, nrows=3, sharex=True, figsize=(10, 8))
    ax0.invert_yaxis()
    ax1.invert_yaxis()
    ax2.invert_yaxis()

    ax0.barh(y=processed_blue_df['Asset'],
             left=processed_blue_df['rel_start'],
             width=processed_blue_df['rel_length'],
             color=processed_blue_df['Color'],
             edgecolor='black',
             hatch=processed_blue_df['Hatch'])

    ax1.barh(y=processed_jtac_df['Label'],
             left=processed_jtac_df['rel_start'],
             width=processed_jtac_df['rel_length'],
             color=processed_jtac_df['Color'],
             edgecolor='black',
             hatch=processed_jtac_df['Hatch'])

    ax2.barh(y='Red IDF',
             left=processed_red_df['rel_start'],
             width=processed_red_df['rel_length'],
             color=processed_red_df['Color'],
             edgecolor='black')

    fig.suptitle('Timeline', fontsize=30, fontweight='bold')

    st.pyplot(fig=fig)