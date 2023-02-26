#
#@Author: Emmanuella Desruisseaux
#@Last Modified date: 2023-02-26

import folium
from phonenumbers import geocoder
from opencage.geocoder import OpenCageGeocode

import keys
import receive_sms


#get location of phone num
location = geocoder.description_for_number(receive_sms.number, "en")
print(location)

key = keys.key #unique api key

geocode = OpenCageGeocode(key) #pass out api key inside the function
query = str(location)
output = geocode.geocode(query) #pass for lat and longitude

lat = output[0]['geometry']['lat']
lng = output[0]['geometry']['lng']

print(lat, lng)
myMap = folium.Map(location=[lat,lng], zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(myMap)

myMap.save("origin.html")




