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

# --------------------------------------------------------------------- #

# class Pet:
#     def __init__(self, name, hppiness):
#         self.name = name
#         self.__hppiness = hppiness
#     def play(self):
#         print(f"{self.name} is now playing fetch.")
#         self.__hppiness += 10
#     def show_status(self):
#         print(f"{self.name}’s happiness is now {self.__hppiness}")

# Dawg = Pet("Dawg", 0)
# Dawg.show_status()
# Dawg.play()
# Dawg.show_status()

# --------------------------------------------------------------------- #

# class Hero:
#     def __init__(self, name, money, inventory):
#         self.name = name
#         self.__money = money
#         self.inventory = inventory
    
#     def spend(self, amount, item):
#         if self.__money > amount:
#             self.__money -= amount
#             print(f"{self.name} have ${self.__money} left")
#             self.inventory.append(item)
#             print(self.inventory)
#         else:
#             print(f"{self.name} does not have enought money. {self.name} will need {amount - self.__money}. {self.name} have {self.__money}")

# Jimmy = Hero("Jimmy", 10000, [{"Title": "Socks", "Warmth": 5}])

# Jimmy.spend(1, {"Title": "Pants", "Warmth": 10})

# --------------------------------------------------------------------- #

