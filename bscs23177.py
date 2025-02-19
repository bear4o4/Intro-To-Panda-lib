import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#TASK1
print("task1")
housing_df = pd.read_csv("housing.csv")

#TASK2
print("task2")
# display the first 5 rows of the DataFrame
print(housing_df.head())
print("###")

# Display the last 5 rows of the DataFrame
print(housing_df.tail())
print("###")

# get the number of rows in the DataFrame
print(len(housing_df))
print("###")

# Get the list of column names in the DataFrame
print(housing_df.columns)
print("###")

#TASK3
print("task3")
# display a concise summary of the DataFrame, including null values
print(housing_df.info())
print("###")

# find out the rows having a null value in any column
rows_with_nulls = housing_df[housing_df.isnull().any(axis=1)]
print(rows_with_nulls)
print("###")

# find out the number of null values in each column
null_values_per_column = housing_df.isnull().sum()
print(null_values_per_column)
print("###")

# find out the total null values in the DataFrame
total_null_values = housing_df.isnull().sum().sum()
print(total_null_values)
print("###")

# find out the number of null values for each type in the ocean_proximity column
null_values_ocean_proximity = housing_df['ocean_proximity'].isnull().sum()
print(null_values_ocean_proximity)

#TASK4
print("task4")
selected_columns = housing_df[['longitude', 'latitude', 'total_rooms', 'total_bedrooms']]
print(selected_columns)

#TASK5
print("task5")
# inspect the type of the 'housing_median_age' column
column_type = type(housing_df['housing_median_age'])
print(column_type)

#TASK6
print("task6")
# select Row 1
row_1 = housing_df.loc[1]
print(row_1)
print("###")

# select Row 1 and column 'longitude'
row_1_longitude = housing_df.loc[1, 'longitude']
print(row_1_longitude)
print("###")

# select Rows 1 to 10 and column 'longitude'
rows_1_to_10_longitude = housing_df.loc[1:10, 'longitude']
print(rows_1_to_10_longitude)
print("###")

# select Rows 1 to 10 and columns 'longitude' and 'latitude'
rows_1_to_10_long_lat = housing_df.loc[1:10, ['longitude', 'latitude']]
print(rows_1_to_10_long_lat)
print("###")

# select Rows 1 to 10 and columns 'longitude' up to 'population'
rows_1_to_10_long_to_pop = housing_df.loc[1:10, 'longitude':'population']
print(rows_1_to_10_long_to_pop)

#TASK7
print("task7")
# select Row 1
row_1 = housing_df.iloc[1]
print(row_1)
print("###")

# Select Row 1 and column 'longitude'
row_1_longitude = housing_df.iloc[1, housing_df.columns.get_loc('longitude')]
print(row_1_longitude)
print("###")

# Select Rows 1 to 10 and column 'longitude'
rows_1_to_10_longitude = housing_df.iloc[1:11, housing_df.columns.get_loc('longitude')]
print(rows_1_to_10_longitude)
print("###")

# Select Rows 1 to 10 and columns 'longitude' and 'latitude'
rows_1_to_10_long_lat = housing_df.iloc[1:11, [housing_df.columns.get_loc('longitude'), housing_df.columns.get_loc('latitude')]]
print(rows_1_to_10_long_lat)
print("###")

# Select Rows 1 to 10 and columns 'longitude' up to 'population'
rows_1_to_10_long_to_pop = housing_df.iloc[1:11, housing_df.columns.get_loc('longitude'):housing_df.columns.get_loc('population')+1]
print(rows_1_to_10_long_to_pop)


#TASK8
print("task8")
# filter out rows where median_house_value is greater than 100,000
filtered_df_1 = housing_df[housing_df['median_house_value'] > 100000]
print(filtered_df_1)
print("###")

# filter out rows where both median_house_value is greater than 100,000 and housing_median_age is greater than 28
filtered_df_2 = housing_df[(housing_df['median_house_value'] > 100000) & (housing_df['housing_median_age'] > 28)]
print(filtered_df_2)

#TASK9
print("task9")
# find out how many districts belong to each category in the ocean_proximity column
ocean_proximity_counts = housing_df['ocean_proximity'].value_counts()
print(ocean_proximity_counts)

#TASK10
print("task10")
# plot a histogram of the median_income column
housing_df['median_income'].plot(kind='hist', bins=50, figsize=(10, 6))
plt.xlabel('Median Income')
plt.ylabel('Frequency')
plt.title('Histogram of Median Income')
plt.show()

# define the income categories
income_bins = [0, 15000, 30000, 45000, 60000, np.inf]
income_labels = [1, 2, 3, 4, 5]

# create the income_category column
housing_df['income_category'] = pd.cut(housing_df['median_income']*10000, bins=income_bins, labels=income_labels, right=False)

# display the first few rows to verify the new column
print(housing_df.head())


#TASK11
print("task11")
# plot a histogram to inspect the number of districts in each income category
housing_df['income_category'].value_counts().sort_index().plot(kind='bar', figsize=(10, 6))
plt.xlabel('Income Category (x10000)')
plt.ylabel('Number of Districts')
plt.title('Number of Districts in Each Income Category')
plt.show()


#TASK12
print("task12")
# create a scatterplot of all the districts using latitude and longitude
housing_df.plot(kind='scatter', x='longitude', y='latitude', alpha=0.1, figsize=(10, 6))
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Scatterplot of Districts by Latitude and Longitude')
plt.show()

#TASK13
print("task13")
# create a scatter plot of all the districts using latitude and longitude
# color-code the points based on the median_house_value
# adjust the size of the points based on the population
# add a legend and labels

housing_df.plot(kind='scatter', x='longitude', y='latitude', alpha=0.4,
                s=housing_df['population']/100, label='Population',
                c=housing_df['median_house_value'], cmap=plt.get_cmap('jet'), colorbar=True,
                figsize=(10, 6))

plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Housing Prices and Location')
plt.legend()
plt.show()