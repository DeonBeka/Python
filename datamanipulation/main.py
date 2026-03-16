import pandas as pd

df = pd.read_csv('avgIQpercountry.csv')

print(df.info())

first_row = df.head()
print(first_row)

country_data = df['Country']
print(country_data)

subset = df[['Country', 'Average IQ']]
print(subset)

filtered_df = subset[subset['Average IQ']>100]
print(filtered_df)

null_mask = df.isnull()
null_count = null_mask.sum()

print("Count of the null values in each column")
print(null_count)

df.dropna(inplace=True)
print(df.info())

duplicate_count = df.duplicated().sum()

print("Count of duplicate rows")
print(duplicate_count)

average_iq_continent = df.groupby('Continent')['Average IQ'].mean()
print(average_iq_continent)

sorted_average_iq_per_continent = average_iq_continent.sort_values(ascending=False)
print(sorted_average_iq_per_continent)