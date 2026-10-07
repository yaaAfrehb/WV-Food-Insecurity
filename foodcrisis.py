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

fig1, ax1 = plt.subplots()

#urban
ax1.scatter(x = "RUCC", y = "Food Insecurity %", data= urban_counties , color = "blue")

#rural
ax1.scatter(x = "RUCC", y = "Food Insecurity %", data = rural_counties, color = "red")

ax1.set_ylabel("Food Insecurity % in 2023")
ax1.set_xlabel("RUCC rankings: 1-3 = Urban. 4-9 = Rural")
ax1.grid(True)
ax1.set_title("WV Food Insecurity Percentages in 2023 ")

st.pyplot(fig1)

    
# bar graph
fig2, ax2 = plt.subplots(figsize=(18,6))
fdwv = fdwv.sort_values(by = "Food Insecurity %")

bar_colors = ['blue' if rucc <= 3 else 'red' for rucc in fdwv['RUCC']]

ax2.bar(fdwv['County'], fdwv['Food Insecurity %'], color = bar_colors)


ax2.tick_params(axis ='x', rotation=90)
ax2.set_xlabel("County")
ax2.set_ylabel("Food Insecurity %")
ax2.set_title("WV Food Insecurity % by County in 2023")
plt.tight_layout()

st.pyplot(fig2)
