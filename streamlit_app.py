#######################
# Import libraries
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import numpy as np


#######################
# Page configuration
st.set_page_config(
    page_title="Air quality Dashboard",
    page_icon="🌬",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")


#######################
# Random data TODO: Load data
np.random.seed(0)  # for reproducibility
samples = 1000
years = np.random.randint(1998, 2024, samples)
months = np.random.randint(1, 13, samples)
days = np.random.randint(1, 31, samples)
cnnaqi = np.random.rand(samples)
insitu = np.random.rand(samples)

# Create DataFrame
data = {
    "year": years,
    "month": months,
    "day": days,
    "cnnaqi": cnnaqi,
    "insitu": insitu
}
df = pd.DataFrame(data)

#######################
# Sidebar
with st.sidebar:
    st.title('🌬 Air quality Dashboard')
    
    year_list = list(df.year.unique())[::-1]
    
    selected_year = st.selectbox('Select a year', year_list)
    df_selected_year = df[df.year == selected_year]


    # df_selected_year_sorted = df_selected_year.sort_values(by="population", ascending=False)
    plot_list = ['comparison', 'diff']
    selected_plot = st.selectbox('Select a plot', plot_list)



#######################
# Dashboard Main Panel
col = st.columns((1.5, 4.5, 2), gap='medium')

# st.title('Air quality graph')    
st.header(f'Air quality graph: {selected_plot}')
st.subheader(f'year: {selected_year}')
df_selected_year_sorted = df_selected_year.sort_values(by=['month', 'day'])
df_selected_year_sorted['diff'] = df_selected_year_sorted['cnnaqi'] - df_selected_year_sorted['insitu']
if selected_plot=='comparison':
    st.line_chart(df_selected_year_sorted[['cnnaqi', 'insitu']])
elif selected_plot=='diff':
    st.line_chart(df_selected_year_sorted[['diff']])

