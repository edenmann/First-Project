
# Object for things that happen in the game
# name is what the event is, length is whether it lasts for 1 or more turns (from 1 to anything more), effect is how it affects the player (damages the player, initiates battle), description is the text describing the event
class Event:
    def __init__(self, name, length, effect, description):
        self.name = name
        self.length = length
        self.description = description

snake = Event("Snake", 1, , "Out of corner of your eye you see something on the ground move suddenly. You stop notice that it is a plant. It is a a small plant, about 2 inches tall with multiple branching leaves. It sways from side to side as if something ")

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




class Path:
    def __init__(self, name, description):
        self.name = name
        self.description = description

events = []
paths = []