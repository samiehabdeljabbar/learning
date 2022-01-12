inty = 5
listy = [6, 7]
stringy = "Hi"

import folium
from IPython.display import display
LDN_Coordinates = (38, -27)
azores = folium.folium.Map(location = LDN_Coordinates , zoom_start = 6)


#all objects have a type
display(azores)

