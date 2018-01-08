import pandas as pd
import matplotlib.pyplot as plt
import sys

#input to this is data1.csv,data2.csv

read=pd.read_csv("data1.csv", header=None, names=['col1','cl1.5' ,'col2'])
read1=pd.read_csv("data2.csv", header=None, names=['col3','cl3.5' ,'col4'])

plt.scatter(read['col1'],read['col2'],color='red',label="Urban")
plt.scatter(read1['col3'],read1['col4'],color='blue',label="Rural")

plt.title("Number of poultry birds districtwise in Andhra Pradesh in the year 2007")
plt.xlabel("District code")
plt.ylabel("Number of birds")

plt.legend()
plt.show()