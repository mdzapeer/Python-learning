import folium
import pandas

voldata=pandas.read_csv("Volcanoes_USA.txt")

def elevcolor (elev):
    if elev < 1000:
        return "green"
    elif 1000<= elev <3000:
        return "orange"
    else:
        return "red"


map1=folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="Mapbox Bright")
fg1=folium.FeatureGroup(name="Volcaonoes")

for lt,ln,name,loc,elv in zip(voldata.LAT,voldata.LON,voldata.NAME, voldata.LOCATION, voldata.ELEV):
    fg1.add_child(folium.CircleMarker(location = [lt, ln], color=elevcolor(elv), fill='TRUE', popup=folium.Popup(name+" "+loc,parse_html=True)))

fg2=folium.FeatureGroup(name="Population")
fg2.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] <= 10000000 else 'orange' if 10000000 < x['properties']['POP2005'] < 20000000 else 'red'}))

map1.add_child(fg1)
map1.add_child(fg2)
map1.add_child(folium.LayerControl())

map1.save("map6.html")
