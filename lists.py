pets = ["Rosie", "Sherman", "Elmer"]
print(pets)

only_things_sure_in_life = ("Death", "Taxes", "Bad Coffee")
first = only_things_sure_in_life[0]
second = only_things_sure_in_life[1]

# WRONG
#only_things_sure_in_life[1] = "Ice Cream"

first, second = only_things_sure_in_life
print(first)
print(second)

pet1, pet2, pet3 = pets

print(pet1)