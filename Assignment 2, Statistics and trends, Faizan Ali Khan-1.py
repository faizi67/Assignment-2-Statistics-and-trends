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


# In[4]:


indicators_shortname = {
        'Nitrous oxide emissions (thousand metric tons of CO2 equivalent)': 'Nitrous Oxide Emission',
       'Methane emissions (kt of CO2 equivalent)': 'Methane Emission',
       'Total greenhouse gas emissions (kt of CO2 equivalent)': 'Total Greenhouse Gas Emission',
        'CO2 emissions (kt)': 'CO2 Emission'
}

# Changing Indicator Names
extracted_years_data["Indicator Name"] = extracted_years_data["Indicator Name"].map(indicators_shortname)


# In[7]:


# Statistical Properties
extracted_countries_data.describe()


# In[5]:


# Create a pivot table with Country Name as index and Indicator Name as columns
temp = pd.pivot_table(extracted_years_data, values="2019", index="Country Name", columns=["Indicator Name"])

# Set up the figure and subplots
plt.figure(figsize=(16, 10))

# First subplot: CO2 Emission in 2019
plt.subplot(221)
sns.barplot(x=temp.index, y=temp["CO2 Emission"])
plt.title("CO2 Emission of Countries by 2019")
plt.xticks(rotation=8)  # Rotate x-axis labels for readability
plt.xlabel("")  # Remove x-axis label

# Second subplot: Methane Emission in 2019
plt.subplot(222)
sns.barplot(x=temp.index, y=temp["Methane Emission"])
plt.title("Methane Emission of Countries by 2019")
plt.xticks(rotation=8)  # Rotate x-axis labels for readability
plt.xlabel("")  # Remove x-axis label

# Third subplot: Nitrous Oxide Emission in 2019
plt.subplot(223)
sns.barplot(x=temp.index, y=temp["Nitrous Oxide Emission"])
plt.title("Nitrous Oxide Emission of Countries by 2019")
plt.xticks(rotation=8)  # Rotate x-axis labels for readability

# Fourth subplot: Total Greenhouse Gas Emission in 2019
plt.subplot(224)
sns.barplot(x=temp.index, y=temp["Total Greenhouse Gas Emission"])
plt.title("Total Greenhouse Gas Emission of Countries by 2019")
plt.xticks(rotation=8)  # Rotate x-axis labels for readability

# Display the plots
plt.show()


# In[6]:


# Nitrous Oxide Emission trends
# Extract Nitrous Oxide Emission data for the specified countries
temp = extracted_countries_data.loc[:, (specific_countries, "Nitrous oxide emissions (thousand metric tons of CO2 equivalent)")]
temp.columns = [i[0] for i in temp.columns]  # Simplify column names
# Plot Nitrous Oxide Emission trends for the last 30 years
temp.iloc[30:, :].plot(kind="line", figsize=(8, 4), xlabel="Years", ylabel="Nitrous Oxide Emissions", title="Nitrous Oxide Emission over the Years")

# Methane Emission trends
# Extract Methane Emission data for the specified countries
temp = extracted_countries_data.loc[:, (specific_countries, "Methane emissions (kt of CO2 equivalent)")]
temp.columns = [i[0] for i in temp.columns]  # Simplify column names
# Plot Methane Emission trends for the last 30 years
temp.iloc[30:, :].plot(kind="line", figsize=(8, 4), xlabel="Years", ylabel="Methane Emissions", title="Methane Emission over the Years")

# Total Greenhouse Gas Emission trends
# Extract Total Greenhouse Gas Emission data for the specified countries
temp = extracted_countries_data.loc[:, (specific_countries, "Total greenhouse gas emissions (kt of CO2 equivalent)")]
temp.columns = [i[0] for i in temp.columns]  # Simplify column names
# Plot Total Greenhouse Gas Emission trends for the last 30 years
temp.iloc[30:, :].plot(kind="line", figsize=(8, 4), xlabel="Years", ylabel="Total greenhouse gas Emissions", title="Total greenhouse gas Emission over the Years")

# CO2 Emission trends
# Extract CO2 Emission data for the specified countries
temp = extracted_countries_data.loc[:, (specific_countries, "CO2 emissions (kt)")]
temp.columns = [i[0] for i in temp.columns]  # Simplify column names
# Plot CO2 Emission trends for the last 30 years
temp.iloc[30:, :].plot(kind="line", figsize=(8, 4), xlabel="Years", ylabel="CO2 Emissions", title="CO2 Emission over the Years")

# Display the plots
plt.show()


  
