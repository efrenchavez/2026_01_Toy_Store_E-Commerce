"""Entry point for the StreamLit app"""
import plotly.express as px
import streamlit as st

# HEADER & DESCRIPTION
st.header('WORK IN PROGRESS | UNDER CONSTRUCTION')
st.header('Exploratory Data Analysis\nMaven Fuzzy Factory')
st.write('This app shows as a simple dashboard for a project in which I:')
st.write("""
         - Extracted the business data from its source.
         - Profiled the data.
         - Enriched the data (feature engineering).
         - After transforming the data, loaded results to destination.
         - Showed descriptive statistic obtained from ETL & EDA processe.
         """)

# GUI TEXTS
# radio button
radio_button_title = 'Select chart type to create'
radio_button_names = ['Histogram', 'Scatter plot', 'Donut chart']
radio_button_captions = ['Odometer readings',
                         'Price vs Odometer correlation', 'Most common fuel type']
# button
button_legend = 'Chart data'
# checkbox
checkbox_legend = 'Orange?'


# streamlit radio menu
chart_type = st.radio(radio_button_title, radio_button_names,
                      captions=radio_button_captions, index=None)
# streamlit checkbox
orange = st.checkbox(checkbox_legend)
# streamlit button
chart_button = st.button(button_legend)