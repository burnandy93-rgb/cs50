from geopy.geocoders import Nominatim
from geopy.distance import geodesic

geo = Nominatim(user_agent= "distance_program")
city1 = input("enter first cty: ")
city2 = input("enter 2nd cty: ")

loc1 = geo.geocode(city1)
loc2 = geo.geocode(city2)

coord1 =( loc1.latitude, loc1.longitude)
coord2 =( loc2.latitude, loc2.longitude )

distance =geodesic(coord1, coord2).km
print("distance between cities" ,distance,"km")
