#find  latitude and longttude
from geopy.geocoders import Nominatim
place = input("enter a place name")
geo = Nominatim(user_agent = "geo_program")
location = geo.geocode(place)
print("location: ",location.address)
print("location: ",location.latitude)
print("location: ",location.longitude)