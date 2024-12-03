import pandas as pd


file = "AQI_Data.csv"
data = pd.read_csv(file)#load the file



city_aqi = {}#dictionarie to stor the data


for index, row in data.iterrows():
    city = row['City']
    aqi = row['AQI']
    
    if city not in city_aqi:
        city_aqi[city] = {'sum': 0, 'count': 0}
    
    city_aqi[city]['sum'] += aqi
    city_aqi[city]['count'] += 1


city_avg_aqi = {}
for city, values in city_aqi.items():
    city_avg_aqi[city] = values['sum'] / values['count']


max_aqi_city = None
min_aqi_city = None
max_aqi_value = float('-inf')
min_aqi_value = float('inf')

for city, avg_aqi in city_avg_aqi.items():
    if avg_aqi > max_aqi_value:
        max_aqi_value = avg_aqi
        max_aqi_city = city
    if avg_aqi < min_aqi_value:
        min_aqi_value = avg_aqi
        min_aqi_city = city


print(f"City with the highest average AQI: {max_aqi_city} ({max_aqi_value})")
print(f"City with the lowest average AQI: {min_aqi_city} ({min_aqi_value})")

