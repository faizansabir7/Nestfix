from geopy import distance
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises",timeout=3)
cbs = {
            "Kannur": ["Payyanur", "Taliparamba", "Kannur","Thalassery"],
            "Eranakulam": ["Kochi", "Aluva", "Edappally"],
            "Kozhikode": ["Balussery", "Ramanattukara", "Kunnamangalam"]
        };
a={}
for i in cbs:
     for j in cbs[i]:
             c1=j
             a[j]=(geolocator. geocode(c1).latitude, geolocator. geocode(c1).longitude)
print(a)