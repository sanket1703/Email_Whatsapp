#This code gives distance between two address , lat long of an address, travel time between two address
from math import radians, cos, sin, asin, sqrt 
import requests
api_key = 'AIzaSyBc3tvk8dfja8r0ABh65c-14YZJula3wXs'
def distance(lat1, lat2, lon1, lon2): 
      
    # The math module contains a function named 
    # radians which converts from degrees to radians. 
    lon1 = radians(lon1) 
    lon2 = radians(lon2) 
    lat1 = radians(lat1) 
    lat2 = radians(lat2) 
       
    # Haversine formula  
    dlon = lon2 - lon1  
    dlat = lat2 - lat1 
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
  
    c = 2 * asin(sqrt(a))  
     
    # Radius of earth in kilometers. Use 3956 for miles 
    r = 6371
       
    # calculate the result 
    return(c * r) 
      
def get_lat_lng(apiKey,address):
    """
    Returns the latitude and longitude of a location using the Google Maps Geocoding API. 
    API: https://developers.google.com/maps/documentation/geocoding/start

    # INPUT -------------------------------------------------------------------
    apiKey                  [str]
    address                 [str]

    # RETURN ------------------------------------------------------------------
    lat                     [float] 
    lng                     [float] 
    """
   
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'
           .format(address.replace(' ','+'), apiKey))
    try:
        response = requests.get(url)
        resp_json_payload = response.json()
        lat = resp_json_payload['results'][0]['geometry']['location']['lat']
        lng = resp_json_payload['results'][0]['geometry']['location']['lng']
    except:
        print('ERROR: {}'.format(address))
        lat = 0
        lng = 0
    return lat, lng

def get_drive_time(apiKey, origin, destination):
    """
    Returns the driving time between using the Google Maps Distance Matrix API. 
    API: https://developers.google.com/maps/documentation/distance-matrix/start


    # INPUT -------------------------------------------------------------------
    apiKey                  [str]
    origin                  [str]
    destination             [str]

    # RETURN ------------------------------------------------------------------
    drive_tim               [float] (minutes)
    """
    import requests
    url = ('https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins={}&destinations={}&key={}'
           .format(origin.replace(' ','+'),
                   destination.replace(' ','+'),
                   apiKey
                  )
          )
    try:
        response = requests.get(url)
        resp_json_payload = response.json()
        drive_time = resp_json_payload['rows'][0]['elements'][0]['duration']['value']/60
    except:
        print('ERROR: {}, {}'.format(origin, destination))
        drive_time = 0
    return drive_time

# driver code  
lat1, lon1 = get_lat_lng(api_key,'Vile Parle')
lat2,lon2 = get_lat_lng(api_key,'Mira Road')
print(get_drive_time(api_key,'Vile Parle','Andheri'))
print(distance(lat1, lat2, lon1, lon2), "K.M") 