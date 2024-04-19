import requests
import urllib
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='myapplication')

def get_nominatim_geocode(address):
    try:
      location = geolocator.geocode(address)
      return location.raw['lon'], location.raw['lat']
    except Exception as e:
        # print(e)
        return None, None

def get_positionstack_geocode(address):
  BASE_URL = "http://api.positionstack.com/v1/forward?access_key="
  API_KEY = "YOUR_API_KEY"
  
  url = BASE_URL +API_KEY+'&query='+urllib.parse.quote(address)
  try:
      response = requests.get(url).json()
      # print( response["data"][0])
      return response["data"][0]["longitude"], response["data"][0]["latitude"]
  except Exception as e:
      # print(e)
      return None,None

def get_geocode(address):
  long,lat = get_nominatim_geocode(address)
  if long == None:
    return get_positionstack_geocode(address)
  else:
    return long,lat

