import folium
obj=folium.Map(location=[28.5011226, 77.4099794],zoom_start=8)
folium.Marker([10.880137, 77.022420],popup = 'karpagam engineering college').add_to(obj) 
  
folium.Marker([28.359203, 75.588095],popup = 'birla institute of technogoly').add_to(obj)
folium.PolyLine(locations =[(10.880137, 77.022420),(28.359203, 75.588095)],color='red', weight=5, fill_color='black', fill_opacity=0.6, popup=None).add_to(obj)  
obj.save("googlemap.html")
