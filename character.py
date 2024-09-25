class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.recieved = False

    def talk_to_player(self, player):
        if self.recieved == False:
            print(f"{self.name} says: Hi {player.name}. I am looking for a star. Do you have one for me?")
            YN = input("Do you have a star? (Y/N): ")
            if YN == "Y":
               self.recieve_item(player.inventory["star"])
               player.inventory.remove(player.inventory["star"])
            else:
                print(f"{self.name} says: I see. Keep looking for a star.")
        else:
            print(f"{self.name} says: I already have what I need. Go away!")
            
    def receive_item(self, item):
        self.received = True
        self.inventory.append(item)
        print(f"{self.name} says: Thank you for the {item.name}. I will treasure it forever.")