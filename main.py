"""Entry point for the StreamLit app"""
import plotly.express as px
import streamlit as st
from utils.data_management import load_enriched_data_into_main

# LOAD DATA
data = load_enriched_data_into_main('orders')

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

# ADD GUI ITEMS
# orders radio menu
ORDERS_RADIO_BUTTON_LABEL = 'Orders from March, 2012 to March, 2015'
orders_radio_button_names = ['Items # per order',
                             'Profit % from orders',
                             'Total profit from orders']
orders_radio_button_captions = ['How many items do our orders have?',
                                'What percentage of our profit do our orders make?',
                                'What\'s the total profit our orders made?']
# create items and register it for listener
orders_radio_event = st.radio(label=ORDERS_RADIO_BUTTON_LABEL,
                              options=orders_radio_button_names,
                              captions=orders_radio_button_captions,
                              index=0)

# INTERACTION
# Conditional logic based on the selected option
if orders_radio_event == orders_radio_button_names[0]:
    fig = px.pie(values=[data[data['items_purchased'] == 1]['items_purchased'].count(),
                         data[data['items_purchased'] == 2]['items_purchased'].count()],
                         names=['One', 'Two'],
                         color_discrete_sequence=['teal', 'salmon'],
                         title='How many items do our orders have?',
                         subtitle='March, 2012 to March, 2015',
                         hole=0.5)
    st.plotly_chart(fig, width='stretch')
elif orders_radio_event == orders_radio_button_names[1]:
    fig = px.pie(values=[data[data['items_purchased'] == 1]['profit_margin_usd'].sum(),
                         data[data['items_purchased'] == 2]['profit_margin_usd'].sum()],
                         names=['One', 'Two'],
                         color_discrete_sequence=['teal', 'salmon'],
                         title='Percentage of total profit for orders with one or two items.',
                         subtitle='March, 2012 to March, 2015',
                         hole=0.5)
    st.plotly_chart(fig, width='stretch')
elif orders_radio_event == orders_radio_button_names[2]:
    # bar_plot_data
    fig = px.bar(title='Total profit for orders with one or two items.',
                 subtitle='March, 2012 to March, 2015',
                 x=['One', 'Two'],
                 y=[data[data['items_purchased'] == 1]['profit_margin_usd'].sum(),
                    data[data['items_purchased'] == 2]['profit_margin_usd'].sum()],
                    color=['One', 'Two'],
                    color_discrete_map={'One':'teal', 'Two':'salmon'},)
    st.plotly_chart(fig, width='stretch')
else:
    st.write('GUI ERROR')
