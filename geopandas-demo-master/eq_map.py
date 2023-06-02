import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import pyproj
import os
from shapely.geometry import Point, Polygon

# %matplotlib inline

# Load into Pandas dataframe, specifying that two columns represent date and time
earthquakes = pd.read_csv('uk_earthquakes.csv',
                          skipinitialspace=True,
                          usecols=['yyyy-mm-dd', 'hh:mm:ss.ss', 'lat', 'lon', 'depth', 'ML', 'locality'],
                          parse_dates=[['yyyy-mm-dd', 'hh:mm:ss.ss']], infer_datetime_format=True)

# Fix datetime column name and typo in locality name
earthquakes.rename(columns={'yyyy-mm-dd_hh:mm:ss.ss': 'datetime'}, inplace=True)
earthquakes.set_index('datetime', inplace=True)

# Check data within data frame
earthquakes.head()
print(earthquakes)
earthquakes.sort_values('ML', ascending=False).head(10)

# Load data form GIS file
regions = gpd.read_file('./data/ne_10m_uk.gpkg', layer='admin_1_states_provinces')
towns = gpd.read_file('./data/ne_10m_uk.gpkg', layer='populated_places')

# View attribute data for first 5 rows
regions.head()

ax = regions.plot(figsize=(8, 8), column='name')
towns.plot(ax=ax, color='black')
txt = ax.set_title('UK regions and town')

# Draw arrow to highlight Rockall, which is too small to
# have been drawn on the map (see next section).
plt.annotate('Rockall', xy=(-13.687, 57.596), xytext=(-13, 58),
             arrowprops=dict(width=0.5, headwidth=4, headlength=5))

plt.show()
## Note that you can easily save plots to file in a variety of formats e.g.
# plt.savefig('map.pdf')
# plt.savefig('map.png', dpi=300)
