import requests

query_parms = {
    "placeid": "ChIJN1t_tDeuEmsRUsoyG83frY4",
    "fields": "name,rating,formatted_phone_number",
    "key": "AIzaSyDsg_UmCKWc6LoDwCDu5E4tgXKFBEMbMWA"
}

# result = requests.get("https://maps.googleapis.com/maps/api/place/details/")

# result = requests.get("https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=mongolian%20grill"
#                        "&inputtype=textquery&fields=photos,formatted_address,name,opening_hours,"
#                        "rating&locationbias=circle:2000@47.6918452,"
#                        "-122.2226413&key=AIzaSyBu00PuXvgCYyYaZvgQn5pZxu6q6U5iV2E")
result = requests.get("https://maps.googleapis.com/maps/api/place/details/json?placeid=ChIJN1t_tDeuEmsRUsoyG83frY4"
                      "&fields=name,rating,formatted_phone_number&key=AIzaSyBu00PuXvgCYyYaZvgQn5pZxu6q6U5iV2E")

print(result.status_code)

print(result.text)
