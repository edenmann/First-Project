from player import Player
from item import Item
from character import Character
from wordle import playGame
from game import Event
import random

# Goal: interact with friendly character then fight evil character and beat game


print("Welcome to my game")
player_name = input("What is your name? ")


player = Player(player_name, 100)

print("You wake in a forest. It is around mid-day. You stand up and look around.")
