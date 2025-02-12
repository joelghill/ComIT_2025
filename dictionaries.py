""" This module is used as an example on how to rank pets with Dictionaries.

This is 100% true, no jokes here.

Seriously
"""
PI = 3.141592635
key = "radius"

circle = {
    "" + "": 3,
    "area": 3 * 3 * PI,
    "diameter": 2 * 3 
}

circle_2 = {
    "radius": 2,
    "area": 2 * 2 * PI,
    "diameter": 2 * 2 
}

circle_3 = {
    "diameter": 4,
    "area": 4/2 * 4/2 * PI,
    "radius": 4/2,
    "colour": "blue"
}

circles = [circle, circle_2, circle_3]

print(circle["area"])
print(circle_2["area"])
print(circle_3["area"])



pixel = [255, 0, 0, 255]

# The amount Joel loves his pets
pets_love = {
    "Rosie": {
        "Cuteness": 10,
        "Smarts": 5,
        "Attitude": 8,
        "Luck": 5
    }
}

print("Rosie's smartness: ", pets_love["Rosie"]["Smarts"])

# pets_love["Elmer"] = 11
# pets_love["Sherman"] = 8

# # Sherman is cute but a jerk
# pets_love["Sherman"] = 2