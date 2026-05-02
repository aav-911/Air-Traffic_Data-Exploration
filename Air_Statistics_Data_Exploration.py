"""
Assignment 2

avega24@georgefox.edu
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats


# Open the CSV data file using Numpy
data = np.genfromtxt('Air_Traffic_Passenger_Statistics.csv',
                     dtype=None, delimiter=',', encoding='utf8', skip_header=0, names=True)

# Filter out any data that is less than zero
data = data[np.where(data['Passenger_Count'] > 0)]

# Filter out any data with an invalid date
data_with_valid_date = data[np.where(data['Activity_Period'] > 0)]

# Only keep the low-fare flights
data = data[np.where(np.char.startswith(data['Price_Category_Code'], 'Low Fare'))]

# Set a variable to hold all passengers from 2014 to 2019
all_passengers = data['Passenger_Count']
num_flights = len(all_passengers)
print(f'There are a total of {num_flights} recorded flights.')

# Setting variables to hold domestic and international flights
domestic_flights = data[np.where(np.char.startswith(data['GEO_Summary'], 'Domestic'))]
international_flights = data[np.where(np.char.startswith(data['GEO_Summary'], 'International'))]

# Count and print the number of both domestic and international flights
num_domestic = len(domestic_flights)
print(f'{num_domestic} of them are domestic flights.')
num_international = len(international_flights)
print(f'{num_international} of them are international flights.')

# Set a variable to hold the passenger count
average_passengers = np.nanmean(all_passengers)

# Month and year with the biggest passenger count
index_of_most_passengers = np.nanargmax(all_passengers)
max_row = data[index_of_most_passengers]
max_passengers = max_row['Passenger_Count']
max_date = max_row['Activity_Period_Start_Date']
max_airline = max_row['Operating_Airline']
max_region = max_row['GEO_Region']
max_type = max_row['GEO_Summary']
print(f'On {max_date}, "{max_airline}" is the airline with the most passenger count of {max_passengers} '
      f'headed to {max_region} in an {max_type} flight.')

# Month and year with the smallest passenger count
index_of_least_passengers = np.nanargmin(all_passengers)
min_row = data[index_of_least_passengers]
min_passengers = min_row['Passenger_Count']
min_date = min_row['Activity_Period_Start_Date']
min_airline = min_row['Operating_Airline']
min_region = min_row['GEO_Region']
min_type = min_row['GEO_Summary']
print(f'On {min_date}, "{min_airline}" is the airline with the least passenger count of {min_passengers} '
      f'headed to {min_region} in an {min_type} flight.')

# Describe the flights
describe_results = scipy.stats.describe(all_passengers)
print(describe_results)

# Create a graph to show the amount of airlines and their number of domestic flights (plot1)
fig, ax = plt.subplots()
plt.hist(domestic_flights['Operating_Airline'])
plt.title('Domestic Flights')
plt.xlabel('Airlines')
plt.ylabel('Flights')
ax.tick_params("x", rotation=45)
plt.show()

# Create a graph to show the amount of airlines and their number of international flights (plot2)
fig, ax = plt.subplots()
plt.hist(international_flights['Operating_Airline'])
plt.xlabel('Airlines')
plt.title('International Flights')
plt.ylabel('Flights')
ax.tick_params("x", rotation=45)
plt.show()

# Create a graph to show the amount of flights towards different regions (plot3)
fig, ax = plt.subplots()
plt.hist(data_with_valid_date['GEO_Region'])
plt.xlabel('Region')
plt.title('Flights around the world')
plt.ylabel('Flights')
ax.tick_params("x", rotation=45)
plt.show()