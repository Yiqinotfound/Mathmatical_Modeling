import folium
import pandas as pd
from folium.plugins import HeatMap
import webbrowser as wb

latitude = 37.77
longitude = -122.42

cdata = pd.read_csv('https://cocl.us/sanfran_crime_dataset')
cdata.head()
limit = 288
data = cdata.iloc[0:limit, :]

map = folium.Map(location=[latitude, longitude], zoom_start=12)

heatdata = data[['Y', 'X']].values.tolist()

HeatMap(heatdata).add_to(map)

map.save('map.html')
wb.open('map.html')

# 真神奇