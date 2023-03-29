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

  