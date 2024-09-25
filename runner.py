from player import Player
from player import take_damage
from item import Item
from character import Character
from wordle import playGame
from game import Event
from game import Scene
from game import dialogue
import random

# Goal: interact with friendly character then fight evil character and beat game

print("Welcome to my game.")
player_name = input("What is your name? ")
p1 = Player(player_name, 100)
print("")

print("In this game, you will be presented with multiple choices. They will be listed like this: itemA, itemB. To select an option, type it out.")
print("For example, to select itemA, type 'itemA'.")
print("")

# format: player_choice("option1, option2")
def player_choice(options, ):
    print("")
    print("What do you do? Choices available: " + options + ".")
    choice = input(" > ")
    print("")
    print("")
    return choice

# Start of game and first choice.
print("You wake in a forest. It is around mid-day. You stand up and look around.")
print("You wince in pain! You are starving! You must find food quickly or you will die!")
hungry = True

playing = True
while playing == True:
    print("Surrounding you there are a few things of note. There is a dirt pathway in front of you and a waterfall behind you.")
    choice = player_choice("pathway, waterfall")
    if choice == "pathway":
        place = pathway1
        print("You choose to walk down the pathway. The atmosphere in the forest is quite nice. ")
        print("As you walk along the path, you come across a small house. Inside the house, you hear a guitar being played.") 
        print("The melody being played reminds you of your past.")
        print("You are without food or weapons. Do you choose to ask this person for supplies or continue down the path?")
        choice = player_choice("supplies, pathway")

    if choice == "supplies":
        place == house
        print("You knock on the door and the guitar immediately stops. You hear quick footsteps as the person approaches the door.")
        print("The door opens and you see a small, old man.")
        print("He stares at you, as though he is waiting for you to speak.")

        dialogue("Hello sir, I am very hungry. Do you have any food that I could eat?", "Alright, I guess that I could spare some food. Give me one moment", "Hi, can I have food?", "okay (:")
        hungry = False
        print("You are no longer hungry.")
        choice = "pathway"
        
    if choice == "pathway":
        print("You continue down the path, beliveing that other oppurtunities will present themselves.")
        print("A nearby river, which the path has loosely been following, eventually widens into a lake.")

        if hungry == True:
            print("Your hunger becomes too much to bear.")
            take_damage(p1, "hunger", 100)
            playing = False
        else:
            print("")
