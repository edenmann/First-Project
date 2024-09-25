class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.inventory = []

    def pick_up_item(self, item):
        print("You picked up a", item.name)
        self.inventory.append(item)

    def give_item(self, item, character):
        if item in self.inventory:
            character.inventory.append(item)
            self.inventory.remove(item)

# cause is what did the damage. damage is how much damage was done.
def take_damage(self, cause, damage):
    print("")
    print("You took", damage, "damage from", cause + ".")
    self.health -= damage
    if self.health <= 0:
        print("You died ):")
    else:
        print("You have", self.health, "health left.")

