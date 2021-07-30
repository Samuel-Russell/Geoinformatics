## Basic Time-Series Plot Using Pandas

# Reading Packages
import pandas as pd
import matplotlib.pyplot as plt

# Reading Data
# Data Source: https://gmao.gsfc.nasa.gov/reanalysis/MERRA-2/
df = pd.read_csv('weather_data_GER_2016.csv') 

# Creating Variables
date = pd.to_datetime(df['timestamp'])
pressure = df['p']

# Plotting Data
fig, ax = plt.subplots()
ax.plot(date, pressure)
plt.title('Air Pressure, Germany, MERRA-2 weather data, 2016')
plt.xlabel('Date')
plt.ylabel('Air Pressure [Pa]')
