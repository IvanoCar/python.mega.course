import folium
from random import choice as c

marker_colors = ['red', 'blue', 'green', 'purple', 'orange', 'darkred',
             'beige', 'darkblue', 'cadetblue', 'pink', 'lightblue', 'black']

map = folium.Map(location=[45.327803, 14.466859], zoom_start=21)

uni = folium.FeatureGroup("Universities")

with open("universities_locations.txt", "r") as f:
    for univ in f:
        location = (univ.split(sep=";")[0]).split(sep=", ")
        location = [float(no) for no in location]
        name = univ.split(sep=";")[1]
        uni.add_child(
            folium.Marker(location=location, popup=name, icon=folium.Icon(color=c(marker_colors))))
map.add_child(uni)
map.add_child(folium.LayerControl())
map.save("map1.html")
