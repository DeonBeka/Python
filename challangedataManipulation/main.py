import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('weather_tokyo_data.csv')

print(df.info())

temperature_overview = df['temperature']
average = df['temperature'].mean()
print(average)

max_temp = df['temperature'].max()
print(f"The hottest days of the year 2022/23 are:{max_temp}")

min_temp = df['temperature'].min()
print(f"The coldest days of the year 2022/23 are:{min_temp}")

df['month'] = df['day'].str.split("/").str[0]
month_avg = df.groupby("month")["temperature"].mean()

plt.bar(month_avg.index, month_avg.values)

plt.title("Average Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature")

plt.show()



