import openmeteo_requests
import requests_cache
from requests.adapters import HTTPAdapter



session = requests_cache.CachedSession('.cache', expire_after=10000)
session.mount('https://', HTTPAdapter(max_retries=5))
openmeteo = openmeteo_requests.Client(session=session)
 
# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://api.open-meteo.com/v1/forecast"
def wheather(latitude,longitude):
    params = {
	"latitude": latitude,
	"longitude": longitude,
	"current": ["temperature_2m", "relative_humidity_2m", "cloud_cover"]
	}
    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]
    current = response.Current()
    current_temperature_2m = current.Variables(0).Value()
    current_relative_humidity_2m = current.Variables(1).Value()
    current_cloud_cover = current.Variables(2).Value()
    return [current_temperature_2m,current_relative_humidity_2m,current_cloud_cover]


longitude = 36.717810
latitude= 2.958728

print(wheather(latitude=latitude,longitude=longitude))



# Current values. The order of variables needs to be the same as requested.


