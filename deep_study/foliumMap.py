import folium

map_osm = folium.Map(location = [37.614776, 127.013337])
map_osm.save('map1.html')

map_osm = folium.Map(location=[37.614776, 127.013337], zoom_start=17)
map_osm.save('map2.html')

map_osm = folium.Map(location=[37.614776, 127.013337], zoom_start=17, tiles='Stamen Toner')
map_osm.save('map_StamenToner.html')


map_osm = folium.Map(location=[37.614776, 127.013337], zoom_start=17, tiles='Stamen Terrain')
map_osm.save('map_StamenTerrain.html')

map_osm = folium.Map(location=[37.614776, 127.013337], zoom_start=17)
folium.Marker([37.614776, 127.013337], popup='서경대학교').add_to(map_osm)
folium.Marker([37.615970, 127.011834], popup='북악관').add_to(map_osm)
map_osm.save('map_SKu1.html')

map_osm = folium.Map(location=[37.614776, 127.013337], zoom_start=17)
folium.Marker([37.614776, 127.013337], popup='서경대학교').add_to(map_osm)
folium.Marker([37.615970, 127.011834], popup='북악관', icon=folium.Icon(color='red', icon='info-sign')).add_to(map_osm)
folium.CircleMarker([37.614776, 127.013337], radius=250, color='#3186cc',
  fill_color='#3186cc',  popup='서경대학교').add_to(map_osm)
map_osm.save('map_SKu2.html')
