# Creating Nested Data Structures
# What we can do instead is to have a list as value for the "Panos" key. So, for example, we can rewrite the dictionary as:

#
phones = {
    "Panos": ["212-998-0803", "917-888-4455"],
    "Maria": ["656-233-5555"],
    "John": ["693-232-5776"],
    "Jake": ["415-794-3423"],
}
print(phones["Panos"])

#
phones["Panos"].append("800-929-2923")
phones["Jake"].append("343-342-5455")
phones["Jake"].append("343-656-8766")
phones["Jake"].pop(0)  # Remove the first phone for Jake
print(phones)

# Alternatively, instead of having a list, we can use a dictionary as a value for each key. For example, we can use key values "Work", "Cell", "Home", etc for each phone, and have something like:
phones = {
    "Panos": {"Work": "212-998-0803", "Cell": "917-888-4455"},
    "Maria": {"Work": "656-233-5555"},
    "John": {"Cell": "693-232-5776"},
    "Jake": {"Home": "415-794-3423"},
}
print(phones)

#
phones = {
    "Jake": ["343-342-5455", "343-656-8766"],
    "John": ["693-232-5776"],
    "Maria": ["656-233-5555"],
    "Panos": ["212-998-0803", "917-888-4455", "800-929-2923"],
}
print(phones["Panos"]) # print(phones.get("Panos"))

#
# Now, if we want to access the second phone on the returned list, we write:
print(phones["Panos"][1])
print(phones.get("Panos")[1])

# Similarly, when we have a dictionary that contains dictionaries:
phones = {
    "Panos": {"Work": "212-998-0803", "Cell": "917-888-4455"},
    "Maria": {"Work": "656-233-5555"},
    "John": {"Cell": "693-232-5776"},
    "Jake": {"Home": "415-794-3423"},
}
print(phones["Panos"]["Cell"])

# 
citibike_stations = [
    {
        "station_id": 72,
        "capacity": 39,
        "coords": {"lon": -73.9939, "lat": 40.7673},
        "name": "W 52 St & 11 Ave",
    },
    {
        "station_id": 79,
        "capacity": 33,
        "coords": {"lon": -74.0067, "lat": 40.7191},
        "name": "Franklin St & W Broadway",
    },
    {
        "station_id": 82,
        "capacity": 27,
        "coords": {"lon": -74.0002, "lat": 40.7673},
        "name": "St James Pl & Pearl St",
    },
    {
        "station_id": 83,
        "capacity": 62,
        "coords": {"lon": -73.9763, "lat": 40.6838},
        "name": "Atlantic Ave & Fort Greene Pl",
    },
    {
        "station_id": 116,
        "capacity": 39,
        "coords": {"lon": -74.0015, "lat": 40.7418},
        "name": "W 17 St & 8 Ave",
    },
]
# Returns the first station entry
print(citibike_stations[0])
# Get the name for the first station
print(citibike_stations[0]["name"])
# access the coordinates
print(citibike_stations[0]["coords"])
#  access the latitude, from the coordinates:
print(citibike_stations[0]["coords"]["lat"])