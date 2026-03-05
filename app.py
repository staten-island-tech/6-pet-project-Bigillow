# class Hero:
#     def __init__(self, name, money, inventory):
#         self.name = name
#         self.money = money
#         self.inventory = inventory

#     def buy(self, item):
#         self.inventory.append(item)
#         print(self.inventory)

# Jimmy = Hero("Jimmy", 1000000, [{"Title": "Socks", "Warmth": 5}])

# Jimmy.buy({"Title": "Pants", "Warmth": 10})

# print(Jimmy.__dict__)

class Pet:
    def __init__(self, name, hppiness):
        self.name = name
        self.__hppiness = hppiness
    def play(self):
        print(f"{self.name} is now playing fetch.")
        self.__hppiness += 10
    def show_status(self):
        print(f"{self.name}’s happiness is now {self.__hppiness}")

Dawg = Pet("Dawg", 0)


    