import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# grab data
data = pd.read_csv('njtemp.csv')

#create new columns for averages
data['Winter'] = data.iloc[:, [1,2,3]].mean(axis=1)
data['Summer'] = data.iloc[:, [6,7,8,9]].mean(axis=1)

#trendline graph
sns.lmplot(x='Year',y='Winter',data=data, fit_reg=True) 
plt.ylabel("TEMP")
plt.title("NJ Average Winter Temp")

#regular line graph
data.reset_index().plot(x='Year', y=['Winter'], kind='line')
plt.title("NJ Average Winter Temp")
plt.xlabel("Years")
plt.ylabel("TEMP")

# Show the plot
plt.show()
print(data)

