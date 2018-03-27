import folium
import pandas

voldata=pandas.read_csv("Volcanoes_USA.txt")

map1=folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="Mapbox Bright")
fg1=folium.FeatureGroup(name="My Map")

for lt,ln,name,loc in zip(voldata.LAT,voldata.LON,voldata.NAME, voldata.LOCATION):
    fg1.add_child(folium.Marker(location = [lt, ln], popup=folium.Popup(name+" "+loc,parse_html=True), icon=folium.Icon(color='purple')))

map1.add_child(fg1)

map1.save("map2.html")
