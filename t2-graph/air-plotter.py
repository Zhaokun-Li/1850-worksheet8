'''
You have been provided with ‘leeds-central-air-quality.csv’ which is a file containing air quality data for Leeds from the last few years. There are 4 values – particulate matter (25), particulate matter (10), Ozone and Nitrous Oxide which are all different measures of air quality – which are recorded against the date.
Load this file into a suitable data structure.

From this data, create a line plot of the average of the 4 data points against the date.

For example, for the row:
07/09/2024,68,20,25,5

You would plot a point at (68+20+25+5)/4 = 29.5

The X-axis should be the date, the Y-axis should be the average pollution.
'''
import matplotlib.pyplot as plt
import pandas as pd

air_data = pd.read_csv("leeds-centre-air-quality.csv")
avg=air_data.groupby("date")(air_data["pm25"]+air_data["pm10"]+air_data["o3"]+air_data["no2"])/4
avg.plot(kind="line")
plt.show()

            
