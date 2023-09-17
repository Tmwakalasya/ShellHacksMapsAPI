import googlemaps
with open("MapsAPIKey.text", 'r') as f:
    API_KEY = f.read()
maps_client = googlemaps.Client(key=API_KEY)
origin_address = input("Enter the origin address: ")
destination_address = input("Enter the destination address: ")

origin_response = maps_client.geocode(origin_address)
destination_response = maps_client.geocode(destination_address)

if origin_response and destination_response:
    origin_location = origin_response[0]['geometry']['location']
    origin_latitude = origin_location['lat']
    origin_longitude = origin_location['lng']

    destination_location = destination_response[0]['geometry']['location']
    destination_latitude = destination_location['lat']
    destination_longitude = destination_location['lng']

    directions_result = maps_client.directions(
        (origin_latitude, origin_longitude),
        (destination_latitude, destination_longitude),
        mode="bicycling",
        units="metric"
    )

if directions_result:
    route = directions_result[0]['legs'][0]
    distance = route['distance']['text']
    duration = route['duration']['text']
    print(f"Distance: {distance}")
    print(f"Time for cycling: {duration}")
else:
    print("No results found for the provided addresses.")

methods = dir(maps_client)
print(methods)




