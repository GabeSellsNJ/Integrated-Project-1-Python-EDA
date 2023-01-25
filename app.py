import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

#create new column for just the manufacturer
df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])

#fill missing values with 0. and change column to int type
df['model_year'] = df['model_year'].fillna(0)
df['model_year'] = df['model_year'].astype('Int64')

#fill missing values with -1. and change column to int type
df['odometer'] = df['odometer'].fillna(-1)
df['odometer'] = df['odometer'].astype('Int64')

#fill missing values with -0. and change column to int type
df['is_4wd'] = df['is_4wd'].fillna(0)
df['is_4wd'] = df['is_4wd'].astype('Int64')

#fill missing values with unknown
df['paint_color'] = df['paint_color'].fillna('unknown')

#fill missing values with unknown
df['date_posted'] = pd.to_datetime(df['date_posted'], format='%Y-%m-%d')

#filter out all sales of $1
df = df.query("price > 1")

st.header('Data viewer')
st.dataframe(df)


#scatterplot of mileage vs price
st.header('Mileage Vs Price')
scatterplot = px.scatter(df, x='odometer', y='price')
st.write(scatterplot)


#distribution of price based on manufacturer
st.header('Compare price distribution based on manufacturer')
# get a list of car manufacturers
manufac_list = sorted(df['manufacturer'].unique())
# get user's inputs from a dropdown menu
manufacturer_0 = st.selectbox(
                              label='Select manufacturer', # title of the select box
                              options=manufac_list, # options listed in the select box
                              index=manufac_list.index('chevrolet') # default pre-selected option
                              )

mask_filter_0 = (df['manufacturer'] == manufacturer_0)

# add a checkbox if a user wants to pick all manufacturers
choose_all= st.checkbox('All Manufacturers', value=True)
if choose_all:
    df_filtered_0 = df
else: 
    df_filtered_0 = df[mask_filter_0] #filter the dataframe if unchecked

# create a plotly histogram figure
fig4 = px.histogram(df_filtered_0,
                      x='price',
                      nbins=30,
                      color='condition',
                      barmode='overlay')
# display the figure with streamlit
st.write(fig4)


