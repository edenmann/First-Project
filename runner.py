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

print("In this game, you will be presented with multiple choices. They will be listed like this: itemA, itemB. To select an option, type its corresponding number.")
print("For example, to select itemA, type '1'.")
print("")


        
    


# Start of game and first choice.
print("You wake in a forest. It is around mid-day. You stand up and look around.")



print("Surrounding you there are a few things of note. There is a dirt pathway to your front and a waterfall behind you.")
print("Choices available: pathway, waterfall.")
choice = input("What do you do? ")
if choice == "pathway":
    print("You choose to walk down the pathway. The atmosphere in the forest is quite nice. ")
    print("As you walk along the path, you come across a small house. Inside the house, you hear 2 people talking talking to each other.") 
    choice = input("")