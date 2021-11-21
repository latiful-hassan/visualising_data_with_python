
##############################
""" INTRODUCTION TO FOLIUM """
##############################

"""
Folium: 
    - a library that creates several types of leaflet maps
    - enables both binding of data to a map for choropleth visualizations
      as well as passing visualisation as markers on the map
    - built-in tile-sets include: OpenStreetMap, Mapbox and Stamen and supports
      custom tile-sets with Mapbox API keys
"""

# creating world map
# define world map
import folium
world_map = folium.Map()

# display world map
world_map

# map of Canada
map_canada_1 = folium.Map(
    location=[56.130, -106.35],
    zoom_start=4
)

# we can add map styles with the stamen toner
map_canada_2 = folium.Map(
    location=[56.130, -106.35],
    zoom_start=4,
    tiles="Stamen Toner"  # good for visualising water masses
)

map_canada_3 = folium.Map(
    location=[56.130, -106.35],
    zoom_start=4,
    tiles="Stamen Terrain"  # good for visualising vegetation
)


#########################
""" MAPS WITH MARKERS """
#########################

# add a circular mark centred around Ontario
map_canada_4 = folium.Map(
    location=[56.130, -106.35],
    zoom_start=4,
)

# create a feature group
ontario = folium.map.FeatureGroup()

# style the feature group by adding child
ontario.add_child(
    folium.features.CircleMarker(
        [51.25, -85.32], radius=5,
        color="red", fill_color="Red"
    )
)

# add the feature group to the map
map_canada_4.add_child(ontario)

# add label to the marker
folium.Marker([51.25, -85.32], popup="Ontario").add_to(map_canada_4)


#######################
""" CHOROPLETH MAPS """
#######################

"""
Choropleth: 
    - areas are shaded in proportion to the measurement of the statistical variable
    - requires a geojson file
"""

# creating choropleth map
# create plain map
choro_map = folium.Map(
    zoom_start=2,
    tiles="Mapbox Bright"
)

# geojson file
world_geo = r"world_countries.json"

# create choropleth using total pop of each contry of Canada from 1980 to 2013
choro_map.choropleth(
    data=df_canada,
    colums=["Country", "Total"],
    key_on="feature.properties.name",
    fill_color="Yl0rRd",
    legend_name="Immigration to Canada"
)







