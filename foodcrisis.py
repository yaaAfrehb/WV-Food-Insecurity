# This code is written in python
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
# The GWCutilities has functions to help format data printed to the console
import GWCutilities as util

# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame

#data set
fdwv=pd.read_csv("FOODDATA-2023.csv")
print("--------------------------------")

fdwv['Food Insecurity %'] = fdwv['Food Insecurity %'].str.rstrip('%').astype(float)

listOfcounties = fdwv[['County','Food Insecurity %', 'RUCC']].copy()

#RUCC 1-3- urban
urban_counties = fdwv[fdwv['RUCC'] <=3]

#RUCC 4-9 - rural
rural_counties = fdwv[fdwv['RUCC'] > 3]

print(listOfcounties)

print("---------------------------------------")

#yoooo

#urban
plt.scatter(x = "RUCC", y = "Food Insecurity %", data= urban_counties , color = "blue")

#rural
plt.scatter(x = "RUCC", y = "Food Insecurity %", data = rural_counties, color = "red")
plt.ylabel("Food Insecurity % in 2023")
plt.xlabel("RUCC rankings: 1-3 = Urban. 4-9 = Rural")
plt.grid(True)
plt.title("WV Food Insecurity Percentages in 2023 ")
plt.show()

    
# bar graph
plt.figure(figsize=(18,6))
fdwv = fdwv.sort_values(by = "Food Insecurity %")

bar_colors = ['blue' if rucc <= 3 else 'red' for rucc in fdwv['RUCC']]

plt.bar(fdwv['County'], fdwv['Food Insecurity %'], color = bar_colors)


plt.xticks(rotation=90)
plt.xlabel("County")
plt.ylabel("Food Insecurity %")
plt.title("WV Food Insecurity % by County in 2023")
plt.tight_layout()

plt.show()
