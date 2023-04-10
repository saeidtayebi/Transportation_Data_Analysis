#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

# Read in the dataset
df = pd.read_csv("Merged_ttc-bus-delay-data-2022.csv")

# Convert the "Date" column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Extract the month from the "Date" column
df["Month"] = df["Date"].dt.month_name()

# Calculate the average delay time by month
avg_delay_by_month = df.groupby("Month")["Min Delay"].mean()

# Create a bar plot of the average delay time by month
fig, ax = plt.subplots(figsize=(13, 10))
ax.bar(avg_delay_by_month.index, avg_delay_by_month.values)
ax.set_xlabel("Month")
ax.set_ylabel("Average Delay Time (Minutes)")
ax.set_title("Average TTC Bus Delay Time by Month in 2022")
plt.show()


# In[12]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

# Read in the dataset
df = pd.read_csv("Merged_ttc-bus-delay-data-2022.csv")

# Convert delay time from minutes to hours
df["Delay (Hours)"] = df["Min Delay"] / 60

# Group the data by location and sum the delay time for each location
total_delay_by_location = df.groupby("Location")["Delay (Hours)"].sum()

# Sort the locations by total delay time in descending order
total_delay_by_location = total_delay_by_location.sort_values(ascending=False)

# Select the top 5 locations by total delay time
top_5_locations = total_delay_by_location[:5]

# Create a vertical bar chart of the total delay time by location for the top 5 locations
fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(top_5_locations.index, top_5_locations.values)
ax.set_xlabel("Location")
ax.set_ylabel("Total Delay Time (Hours)")
ax.set_title("Top 5 TTC Bus Delay Locations in 2022 by Total Delay Time (in hours)")
plt.xticks(rotation=45)
plt.show()


# In[13]:


import pandas as pd

# Read in the dataset
df = pd.read_csv("Merged_ttc-bus-delay-data-2022.csv")

# Convert delay time from minutes to hours
df["Delay (Hours)"] = df["Min Delay"] / 60

# Group the data by location and incident, and sum the delay time for each group
total_delay_by_location_incident = df.groupby(["Location", "Incident"])["Delay (Hours)"].sum()

# Sort the groups by total delay time in descending order
total_delay_by_location_incident = total_delay_by_location_incident.sort_values(ascending=False)

# Get the top 5 locations by total delay time
top_5_locations = df.groupby("Location")["Delay (Hours)"].sum().sort_values(ascending=False)[:5]

# For each of the top 5 locations, print the top 3 incidents by delay time
for location in top_5_locations.index:
    print(f"\nTop 3 incidents contributing to delay time in {location}:")
    location_df = total_delay_by_location_incident.loc[location].sort_values(ascending=False)[:3]
    print(location_df)


# In[19]:


import pandas as pd
import matplotlib.pyplot as plt

# Read in the dataset
df = pd.read_csv("Merged_ttc-bus-delay-data-2022.csv")

# Convert the "Time" column to a datetime object
df["Time"] = pd.to_datetime(df["Time"])

# Extract the hour from the datetime object
df["Hour"] = df["Time"].dt.hour

# Group the data by hour and count the number of incidents for each hour
incidents_by_hour = df.groupby("Hour")["Incident"].count()

# Create a line plot of the incidents by hour
plt.figure(figsize=(10, 6))
plt.plot(incidents_by_hour.index, incidents_by_hour.values)

# Set the title and axis labels
plt.title("Trend in Number of Incidents by Hour of Day")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Incidents")

# Set the x-axis ticks to be the hours
hours = range(24)
plt.xticks(hours)

# Show the plot
plt.show()


# In[21]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('Merged_ttc-bus-delay-data-2022.csv')

# Convert Date column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Group by date and calculate the average delay time
daily_avg_delay = df.groupby(pd.Grouper(key='Date', freq='D'))['Min Delay'].mean()

# Plot the trend as a bar chart
plt.figure(figsize=(12, 6))
plt.bar(daily_avg_delay.index, daily_avg_delay.values)
plt.xlabel('Date')
plt.ylabel('Average Delay Time (Minutes)')
plt.title('Trend of TTC Bus Delays in 2022 (Daily Average)')
plt.show()

