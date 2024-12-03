import numpy as np
import pandas as pd

file_path = "AQI_Data.csv"#the path of the file
data = pd.read_csv(file_path)#load the file

df = pd.DataFrame(data)

print("A")
print("First 5 rows of the dataset: ")#printing first five rows
print(df.head(5))#extracting the first five data from the dataset
print("B")
print("Last 6 rows of the dataset: ")#printing last six rows
print(df.tail(6))#extracting last six data from the datsert

print("C")
print("The summary statistics for all numeric columns: ")#printing the summary statiscs fo all numeric columnns
print(df.describe())#statistics for all numeric


ctm = ['AQI', 'PM2.5', 'PM10']

print("D")
for column in ctm:
    if column in df.columns:
        mv = np.mean(df[column].dropna())  #using numpy calculating mean
        print(f"Mean of {column}: {mv}")
    else:
        print(f"Column {column} not found in the dataset.")
mean_values_per_city=data.groupby('City')[['AQI',"PM2.5","PM10"]].mean()#mean value per city
print("/nMean AQI,PM2.5,and PM10 values for each city")
print(mean_values_per_city)#output for mean value per city