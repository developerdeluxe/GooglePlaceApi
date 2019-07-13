# import googlemaps
# import json
# import pprint
# import time
#
# # Define the API Key.
# API_KEY = 'AIzaSyDsg_UmCKWc6LoDwCDu5E4tgXKFBEMbMWA'
#
# # Define the Client
# gmaps = googlemaps.Client(key = API_KEY)
#
# # Do a simple nearby search where we specify the location
# # in lat/lon format, along with a radius measured in meters
# places_result = gmaps.places_nearby(location='-33.8670522,151.1957362', radius = 40000, open_now =False , type = 'restaurant')
#
# pprint(places_result)
