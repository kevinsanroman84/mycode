#!/usr/bin/python3
"""Python ISS tracker using requests library"""

import requests
import reverse_geocoder as rg
import datetime


iss_location = "http://api.open-notify.org/iss-now.json"

def main():
    """reading json from api"""
    # calling the api
    resp = requests.get(iss_location).json()

    longitude = resp["iss_position"]["longitude"]
    latitude = resp["iss_position"]["latitude"]
    time_stamp = resp["timestamp"]
    time_stamp = str(datetime.datetime.fromtimestamp(time_stamp))

    # reverse_geocoder MUST be passed a tuple as the argument!
    coords_tuple= (latitude, longitude)

    result = rg.search(coords_tuple, verbose=False)
    city_country = result[0]["name"] + ", " + result[0]["cc"]
    

    print("CURRENT LOCATION OF THE ISS:")
    print("Timestamp: " + time_stamp)
    print("Lon: " + longitude)
    print("Lat: " + latitude)
    print("City/Country: " + city_country)
    


main() 
