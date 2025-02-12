import random

pokemon = ['Charmander', "Snorlax", "Wartortle"]

for current_pokemon in pokemon:
    print(f"{current_pokemon}, I choose you!")
    print("*Battle noises*")
    continue
    print(f"{current_pokemon} has fainted!")
    current_pokemon = ""


print("You lose!")


"""
for (int i; i < len(pokemon); i++) :
    print(f"{pokemon[i]}, I choose you!")

"""
indexes = range(2,6,2)
print(indexes)
for i in indexes:
    print(i)


while True:
    # do stuff
    print("...running")
    running = 5 < random.randint(0, 10)
    if True:
        break
