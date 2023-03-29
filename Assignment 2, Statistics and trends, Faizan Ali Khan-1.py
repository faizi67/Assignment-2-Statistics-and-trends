#!/usr/bin/env python
# coding: utf-8

# # Code Functions 

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

def read_worldbank_data(filename):
    """
    Read World Bank data and return two dataframes:
    one with years as columns and one with countries as columns.
    
    Parameters:
    -----------
    filename : str
        The name of the CSV file containing the World Bank dataset.
    
    Returns:
    --------
    years : pd.DataFrame
        A DataFrame containing the World Bank data with years as columns.
    countries : pd.DataFrame
        A DataFrame containing the World Bank data with countries as columns.
    """
    # Read the dataset
    df = pd.read_csv(filename, skiprows=4)
    
    # Drop unnecessary columns
    df = df.iloc[:, :-3]
    
    # Filling missing values
    df.fillna(0, inplace=True)
    
    # Reshape the dataset with years as columns
    years = df.copy()
    
    # Reshape the dataset with countries as columns
    countries = df.set_index(["Country Name", "Indicator Name"])
    countries.drop(["Country Code", "Indicator Code"], axis=1, inplace=True)
    # Taking Transpose of Data
    countries = countries.T
    
    return years, countries

def extract_specific_data(indicators, countries, years_data, countries_data):
    """
    Extract specific data from the input dataframes based on the provided indicators and countries.
    
    Parameters:
    -----------
    indicators : list
        A list of indicators to be extracted.
    countries : list
        A list of countries to be extracted.
    years_data : pd.DataFrame
        A DataFrame containing the World Bank data with years as columns.
    countries_data : pd.DataFrame
        A DataFrame containing the World Bank data with countries as columns.
    
    Returns:
    --------
    extracted_years_data : pd.DataFrame
        A DataFrame containing the extracted data from years_data with the specified indicators and countries.
    extracted_countries_data : pd.DataFrame
        A DataFrame containing the extracted data from countries_data with the specified indicators and countries.
    """
    # Filter the years_data to keep only the specified indicators and countries
    extracted_years_data = years_data[years_data["Indicator Name"].isin(indicators)]
    extracted_years_data = extracted_years_data[extracted_years_data["Country Name"].isin(countries)]
    
    # Filter the countries_data to keep only the specified indicators and countries
    extracted_countries_data = countries_data.loc[:, (specific_countries, specific_indicators)]
    
    return extracted_years_data, extracted_countries_data


# In[2]:


# Load the World Bank Climate Change dataset
years_data, countries_data = read_worldbank_data("API_19_DS2_en_csv_v2_4902199.csv")


# In[3]:


# Indicators and countries of interest
specific_countries = ['Russian Federation', 'Japan', 'South Africa', 'Australia', 'Costa Rica']
specific_indicators = ['Nitrous oxide emissions (thousand metric tons of CO2 equivalent)',
        'Methane emissions (kt of CO2 equivalent)',
        'Total greenhouse gas emissions (kt of CO2 equivalent)',
        'CO2 emissions (kt)']

extracted_years_data, extracted_countries_data = extract_specific_data(specific_indicators, specific_countries, years_data, countries_data)


  
