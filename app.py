#TITLE: CAR SALES ANALYSIS

import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

#create new column for just the manufacturer
df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])

#fill missing values with the median year. and change column to int type
year_avg = df['model_year'].median()
df['model_year'] = df['model_year'].fillna(year_avg)
df['model_year'] = df['model_year'].astype('Int64')

#fill in missing values for cylinders columns with most median cylinder type
cylinders_mode =  df['cylinders'].median()
df['cylinders'] = df['cylinders'].fillna(cylinders_mode)
df['cylinders'] = df['cylinders'].astype('Int64')

#fill missing values with the meadian odometer reading. and change column to int type
mileage_avg = df['odometer'].median()
df['odometer'] = df['odometer'].fillna(mileage_avg)
df['odometer'] = df['odometer'].astype('Int64')

#fill missing values with 0. and change column to int type
df['is_4wd'] = df['is_4wd'].fillna(0)
df['is_4wd'] = df['is_4wd'].astype('Int64')

#fill missing values with unknown
df['paint_color'] = df['paint_color'].fillna('unknown')

#fill missing values with unknown
df['date_posted'] = pd.to_datetime(df['date_posted'], format='%Y-%m-%d')

#filter out all sales of $1
df = df.query("price > 1000  & price <= 80000")

df.info()

st.header('Data viewer')
st.dataframe(df)

#scatterplot of mileage vs price
st.header('Mileage Vs Price')
#removing any outliers above 450,000 miles
mileage_mask = df['odometer'] < 450000
df_mileage = df[mileage_mask]
scatterplot = px.scatter(df_mileage, x='odometer', y='price')
st.write(scatterplot)


#distribution of price based on manufacturer
st.header('Compare price distribution based on manufacturer')
# get a list of car manufacturers
manufac_list = sorted(df['manufacturer'].unique())
# get user's inputs from a dropdown menu
manufacturer = st.selectbox(
                              label='Select manufacturer', # title of the select box
                              options=manufac_list, # options listed in the select box
                              index=manufac_list.index('chevrolet') # default pre-selected option
                              )

mask_filter = (df['manufacturer'] == manufacturer)

# add a checkbox if a user wants to pick all manufacturers
choose_all= st.checkbox('All Manufacturers', value=True)
if choose_all:
    df_filtered = df
else: 
    df_filtered = df[mask_filter] #filter the dataframe if unchecked

# create a plotly histogram figure
fig4 = px.histogram(df_filtered,
                      x='price',
                      nbins=30,
                      color='condition',
                      barmode='overlay')
# display the figure with streamlit
st.write(fig4)


