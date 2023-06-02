import json
import plotly.express as px
import matplotlib.pyplot as plt
import geopandas
import pandas as pd
from shapely.geometry import Point, Polygon

filename = 'data/test.json'
with open(filename, 'r', encoding='utf-8') as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

data = pd.read_json('data/readable_eq_data.json', encoding='utf-8')
data2 = data[['properties', 'geometry']]
# data
list = []
coordinates = []
for item in data2.iterrows():
    property = item[1][0]
    geometry = item[1][1]
    # print(geometry)
    coordinates = [geometry['coordinates'][0], geometry['coordinates'][1]]
    list.append({'mag': property['mag'], 'title': property['title'], 'coords': coordinates})

data3 = pd.DataFrame(list)

# data3['coords'] = list(zip(data3['lon'], data3['lat']))
data3['coords'] = data3['coords'].apply(Point)
data3 = geopandas.GeoDataFrame(data3, geometry='coords', crs='EPSG:4326')
earthquakes_osgb = data3.to_crs('EPSG:4326')
# Create the axis first
fig, ax = plt.subplots(figsize=(8, 8))

# Plot all earthquakes
earthquakes_osgb.sort_values('mag', ascending=True).plot(
    ax=ax, column='mag', legend=True, alpha=0.5)

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
# print(world.crs)
world_osgb = world.to_crs('EPSG:4326')
1e-6 * world_osgb.area
# print(world_osgb)
world_osgb.plot(ax=ax, edgecolor='black', facecolor='none')
plt.show()

# world_list_path = 'data/world_list.json'
# with open(world_list_path, 'r') as f:
#     world_list = json.load(f)

# readable_file = 'data/readable_eq_data.json'
# with open(readable_file, 'w') as f:
#     json.dump(all_eq_dicts, f, indent=4)
