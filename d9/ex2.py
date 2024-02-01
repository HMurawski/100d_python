capitals = {
    "France" : "Paris",
    "Germany" : "Berlin",

}

travel_log = {
    "France" : ["Paris", "lille", "Lyon"],
    "Germany" : ["Berlin", "Bonn", "Hamburg"]
}

travel_log = {
    "France" : {"cities_visited": ["Paris", "lille", "dijon"] },
    "Germany" : ["Berlin", "Bonn", "Hamburg"]
}

print(travel_log["France"]["cities_visited"][1])