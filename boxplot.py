import pandas as pd
import matplotlib.pyplot as plt
import sys

read=pd.read_csv("data3.csv", header=None, names=['col1', 'col2'])
plotMap=[]


plotMap.append(read['col1'].dropna().tolist())
plotMap.append(read['col2'].dropna().tolist())


plt.boxplot(plotMap)


plt.xticks([1,2],["Rural","Urban"])
plt.title("Poultry birds districtwise in Andhra Pradesh in the year 2007 for Rural and Urban")
plt.xlabel("")
plt.ylabel("Number of birds")


plt.legend()
plt.show()