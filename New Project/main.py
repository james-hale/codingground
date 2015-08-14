f = open("pokedex.csv", "r")
pokedex = f.read()

name = input("What's your name? ")

print("Nice to meet you, " + (name))

answer = input("Tell me, " + (name) + ", would it offend you if I called you an idiot? ")
answer = answer.lower()

if (answer == "yes" or answer == "y"):
    print("Your surname must be Hale then.")
elif (answer == "no" or answer == "n"):
    print("Good, because you're a complete moron.")
    
def pokemon_question():
    pokemon = input("What is your favourite Pokemon? ")

pokemon = input("What is your favourite Pokemon? ")

if pokemon in pokedex:
    print("Awful choice. " + (pokemon) + " is rubbish.")
    print((name) + " and " + (pokemon) + (" set off on their journey to Mordor to destroy the ring. They arrive at a crossroads. The road to the left (l) points to Tom Bombadil's house, the road to the right (r) points to Rivendell."))
else:
    pokemon_question()
    

left_or_right = input("Which road do you take? (l or r) ")
left_or_right = left_or_right.lower()

if left_or_right == "l" or left_or_right == "left":
    print("You chose to visit Tom Bombadil. He challenges you to a Pokemon battle! Bombadil sends out Bulbasaur!")
    water_or_fire = input("Do you try to knock out Bulbasaur with water or fire moves? ")
    water_or_fire = water_or_fire.lower()
    if water_or_fire == "water" or water_or_fire == "water moves":
        print("Bulbasaur destroys " + (name) + " and " + (pokemon) + ". Game over.")
    if water_or_fire == "fire" or water_or_fire == "fire moves":
        print("Bulbasaur is burnt to cinders by " + (pokemon) + "! Tom Bombadil has been defeated, and you laugh as the forest burns. The ring is yours to keep!")
    
if left_or_right == "r" or left_or_right == "right":
    print("You chose to go to Rivendell. Lord Elrond offers to cast you into the fire with his Charmander!")
    grass_or_water = input("Do you try to knock out Charmander with grass or water moves? ")
    grass_or_water = grass_or_water.lower()
    if grass_or_water == "grass" or grass_or_water == "grass moves":
        print("Charmander destroys " + (name) + " and " + (pokemon) + ". Game over.")
    if grass_or_water == "water" or "water moves":
        print("Charmander is doused by " + (pokemon) + "! Elrond has been defeated. The ring of power is " + (name) + "'s forever! Gollum, gollum!")
