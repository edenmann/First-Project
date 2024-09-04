
# Object for things that happen in the game
# name is what the event is, length is whether it lasts for 1 or more turns (from 1 to anything more), effect is how it affects the player (damages the player, initiates battle), description is the text describing the event
class Event:
    def __init__(self, name, length, effect, description):
        self.name = name
        self.length = length
        self.description = description

#snake = Event("Snake", 1, health-=10, "Out of corner of your eye you see something on the ground move suddenly. You stop and notice that it is a plant. Upon closer inspection you see that it is not actually a plant but a snake!")

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

def status():
