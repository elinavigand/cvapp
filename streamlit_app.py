# Standard imports
import pandas as pd

#plotly
import plotly.express as px
import plotly.graph_objects as go

import streamlit as st

st.title("MPG")

df = pd.read_csv("data/mpg.csv")

# Basic set-up of the page:
# First the checkbox to show the data frame
if st.sidebar.checkbox('Show dataframe'):
    st.header("dataframe")
    st.dataframe(df.head())

st.header("Highway Fuel Efficiency")
years = ["All"]+sorted(pd.unique(df['year']))
year = st.sidebar.selectbox("choose a Year", years)   # Here the selection of the year.
car_classes = ['All'] + sorted(pd.unique(df['class']))
car_class = st.sidebar.selectbox("choose a Class", car_classes)  # and the selection of the class.

show_means = st.sidebar.radio(
    label='Show Class Means', options=['Yes', 'No'])

st.subheader(f'Fuel efficiency vs. engine displacement for {year}')



