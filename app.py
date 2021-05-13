import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache
def load.data():
    data = pd.read_csv('https://opendata.ecdc.europa.eu/covid19/nationalcasedeath/csv')
    data['week'] = data.year_week.apply(lambda x: convert(x))
    return data

def convert(x):
    year, week = x.split('-')
    year = (int(year) - 2020) * 54
    return year + int(week)

data = load_data()

st.title('covid-app')
country = st.selectbox('Select a country', ['Hungary', 'Belgium'])
st.write(f'The selected country is {country}')
st.plotly_chart(fig)

countries = data['country'].unique()
countries_select= st.sidebar.selectbox('Select the country:', countries)

fig = px.line(data_frame = data.country, x = 'week', y = 'cumulative_count', color = 'indicator')

st.plotly_chart(fig)


