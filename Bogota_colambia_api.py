import requests
import pprint
import json
import csv
# place_id = requests.get('https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Bogota%20Colombia'
#                          '&inputtype=textquery&fields=place_id&key=AIzaSyBmBotF32wnzjY1QhrY0KvoPHnBaFFfi38')
#
#
# Bogota_Colombia_place_id = place_id["candidates"][0]['place_id']
#
# place_url = "https://maps.googleapis.com/maps/api/place/details/json?placeid=" + Bogota_Colombia_place_id + "&fields=name," \
#                                                                                                       "address_component, adr_address, formatted_address,formatted_phone_number, international_phone_number, opening_hours, website, price_level, rating, review, user_ratings_total, permanently_closed&key=AIzaSyBmBotF32wnzjY1QhrY0KvoPHnBaFFfi38 "
#
# restaurants_details = requests.get(url=place_url)


# read file
with open('restaurants.json', 'r') as myfile:
    data = myfile.read()

obj = json.loads(data)
row = obj["candidates"][0]['opening_hours']
print(row)
restu_list = []

for value in row.values():
    restu_list.append(value)

print(restu_list)

with open('Restaurants.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(restu_list)
csvFile.close()
