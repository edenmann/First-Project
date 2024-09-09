from player import Player
from player import take_damage
from item import Item
from character import Character
from wordle import playGame
from game import Event
from game import Place
import random

# Goal: interact with friendly character then fight evil character and beat game

print("Welcome to my game.")
player_name = input("What is your name? ")
player = Player(player_name, 100)

print("In this game, you will be presented with multiple choices. They will be listed like this: itemA, itemB. To select an option, type it out.")
print("For example, to select itemA, type 'itemA'.")
print("")

# format: player_choice("option1, option2")
def player_choice(options):
    choice = input("What do you do? Choices available: " + options + ".")
    return choice

# Start of game and first choice.
print("You wake in a forest. It is around mid-day. You stand up and look around.")
print("You wince in pain! You are starving! You must find food quickly or you will die!")

print("Surrounding you there are a few things of note. There is a dirt pathway to your front and a waterfall behind you.")
choice = input("What do you do? Choices available: pathway, waterfall.")
if choice == "pathway":
    print("You choose to walk down the pathway. The atmosphere in the forest is quite nice. ")
    print("As you walk along the path, you come across a small house. Inside the house, you hear a guitar being played.") 
    print("The melody being played reminds you of your past.")
    print("You are without food or weapons and danger is approaching. Do you choose to ask this person for supplies or continue down the path?")
    player_choice("pathway, supplies")
    if choice == "pathway":
        print("You continue down the path, beliveing that other oppurtunities will present themselves.")
        print("A nearby river which the path has loosely been following, eventually widens into a lake. ")