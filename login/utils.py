from geopy import distance
from .models import ServiceProvider

def nearestcity(district, city):
    from geopy.geocoders import Nominatim


    geolocator = Nominatim(user_agent="geoapiExercises",timeout=3)
    cbs = {
            "Kannur": ["Payyanur", "Taliparamba", "Kannur","Thalassery"],
            "Eranakulam": ["Kochi", "Aluva", "Edappally"],
            "Kozhikode": ["Balussery", "Ramanattukara", "Kunnamangalam"]
        };
    geocode={'Payyanur': (12.1059663, 75.2073158), 'Taliparamba': (12.0994756, 75.47057356867221), 'Kannur': (11.8763836, 75.3737973), 'Thalassery': (11.83565105, 75.64490544488862), 'Kochi': (9.9674277, 76.2454436), 'Aluva': (10.17039815, 76.38839448844891), 'Edappally': (10.0251551, 76.3113552), 'Balussery': (11.44197095, 75.80809921693597), 'Ramanattukara': (11.1780876, 75.8656196), 'Kunnamangalam': (11.3046779, 75.8785617)}

    values = cbs.get(district, [])
    
    c1=city
    # numerical_values = [distance.distance(((geolocator. geocode(c1).latitude, geolocator. geocode(c1).longitude)), ((geolocator. geocode(c2).latitude, geolocator. geocode(c2).longitude))) for c2 in values ]
    numerical_values = [distance.distance(geocode[c1],geocode[c2]) for c2 in values ]
    sorted_values = sorted(values, key=lambda x: numerical_values[values.index(x)])
    
    sorted_service_providers = []
    for city in sorted_values:
        providers_in_city = list(ServiceProvider.objects.filter(city=city))
        sorted_service_providers.extend(providers_in_city)
    print(sorted_service_providers)   
    return sorted_service_providers


    # These variables have the exact location of the cities.
    # l1 = geolocator. geocode(c1)
    # l2 = geolocator. geocode(c2)

    # loc1 = ((l1.latitude, l1.longitude))
    # loc2 = ((l2.latitude, l2.longitude))
    # print(distance.distance(loc1, loc2).km, "kms")


