import pandas as pd
import matplotlib.pyplot as plt
import sys



read=pd.read_csv("data4.csv", header=None, names=['col1', 'col2'])


plt.bar(read['col1'],read['col2'],color='#ddbbaa',label="bar-label")


plt.xlabel("District code")
plt.ylabel("Number of Birds")
plt.title("Total number of polutry birds(urband and rural combined)")


plt.legend()
plt.show()