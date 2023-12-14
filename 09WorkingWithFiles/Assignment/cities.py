import json
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

f = open("../data/1000-largest-us-cities.json", "r")
cities = json.load(f)
f.close()

def kansas_city_finder(citylist):
    kansascities = []
    for city in cities:
        if city["state"] == "Kansas":
            kansascities.append(city["city"])
    return kansascities


def longest_name(citylist):
    longest = ""
    for city in cities:
        if len(city["city"]) > len(longest):
            longest = city["city"]
    return longest



def most_direction(citylist):
    north = cities[0]
    east = cities[0]
    south = cities[0]
    west = cities[0]
    for city in cities[1:]:
        if city["latitude"] > north["latitude"]:
            north = city
        if city["latitude"] < south["latitude"]:
            south = city
        if city["longitude"] > east["longitude"]:
            east = city
        if city["longitude"] < west["longitude"]:
            west = city
    return "north", north["city"], "east", east["city"], "south", south["city"], "west",  west["city"]
          


def growth_rates(citylist):
    fastest_growth = cities[0]
    fastest_decay = cities[0]
    for city in cities[1:]:
        if city["growth_from_2000_to_2013"] != "":
            if float(city["growth_from_2000_to_2013"].replace("%", "")) > float(fastest_growth["growth_from_2000_to_2013"].replace("%", "")):
                fastest_growth = city
            if float(city["growth_from_2000_to_2013"].replace("%", "")) < float(fastest_decay["growth_from_2000_to_2013"].replace("%", "")):
                fastest_decay = city
    return "decay", fastest_decay["city"], "growth", fastest_growth["city"]

def largest_state(citylist):
    states = {}
    biggest = 0
    for city in cities:
        if city["state"] in states:
            states[city["state"]] += city["population"]
        else:
            states.update({city["state"]: city["population"]})
    for state in states:
        if str(states[states[state]]) > str(biggest):
            biggest = state
    return biggest 
print(largest_state(cities))

