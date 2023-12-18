import json
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

f = open("../data/childDetails.json", "r")
children = json.load(f)
f.close()

def name_length(childList):
    longest = ""
    shortest = "aaaaaaaa"
    for child in children:
        if len(child["name"]) > len(longest):
            longest = child["name"]
        if len(child["name"]) < len(shortest):
            shortest = child["name"]
        for guardian in child["guardians"]:
            if len(guardian["name"]) > len(longest):
                longest = guardian["name"]
            if len(guardian["name"]) < len(shortest):
                shortest = guardian["name"]
        for sibling in child["siblings"]:
            if len(sibling["name"]) > len(longest):
                longest = sibling["name"]
            if len(sibling["name"]) < len(shortest):
                shortest = sibling["name"]
    return longest, shortest

def household_incomes(childlist):
    kids = []
    for child in children:
        item = []
        income = 0
        for guardian in child["guardians"]:
            income += guardian["salary"]
        item.append(child["name"])
        item.append(income)
        kids.append(item)
    biggest  = kids[0]
    smallest  = kids[0]
    for child in kids[1:]:
        if child[1] > biggest[1]:
            biggest = child
        if child[1] < smallest[1]:
            smallest = child
    return biggest, smallest

def inheritance(childlist):
    kids = []
    for child in children:
        item = []
        income = 0
        number = len(child["siblings"]) + 1
        for guardian in child["guardians"]:
            income += guardian["salary"]
        income = income/number
        item.append(child["name"])
        item.append(income)
        kids.append(item)
    biggest  = kids[0]
    smallest  = kids[0]
    for child in kids[1:]:
        if child[1] > biggest[1]:
            biggest = child
        if child[1] < smallest[1]:
            smallest = child
    return biggest, smallest

print(inheritance(children))