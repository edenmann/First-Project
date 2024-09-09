
# Object for things that happen in the game
# name is what the event is, length is how many turns it lasts (1 and on), effect is how it affects the player (damages the player, initiates battle), description is the text describing the event
class Event:
    def __init__(self, name, length, effect, description):
        self.name = name
        self.length = length
        self.effect = effect
        self.description = description

# Effects: poison (10 damage per turn), 
    effects = {
        "poison": 10,
    }
    def activate(self):
        print(self.description)
        
        

snake = Event("Snake", 10, "poison", "Out of corner of your eye you see something on the ground move suddenly. You stop and notice that it is a plant. Upon closer inspection you see that it is not actually a plant but a snake! Quickly, before you can react, the snake slithers up to you and bites your ankle.")

# Object for places

# ** This grid was created with AI
# 
#    A   B   C   D   E
#  +---+---+---+---+---+
# 1|   |   |   |   |   |
#  +---+---+---+---+---+
# 2|   |   |   |   |   |
#  +---+---+---+---+---+
# 3|   |   | A |   |   |
#  +---+---+---+---+---+
# 4|   |   |   |   |   |
#  +---+---+---+---+---+
# 5|   |   |   |   |   |
#  +---+---+---+---+---+


class Place:
    def __init__(self, name, description):
        self.name = name
        self.description = description



events = []
paths = []

# def status():
