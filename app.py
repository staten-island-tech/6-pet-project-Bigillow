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

class Pet:
    def __init__(self, owner, pet_name, happiness, health, warmth, hunger):
        self.owner = owner
        self.pet_name = pet_name
        self.happiness = happiness
        self.health = health
        self.warmth = warmth
        self.hunger = hunger
    def play(self):
        if self.happiness < 100:
            print(f"{self.owner} played with {self.pet_name} and gained {self.happiness*0.05}% happiness.")
            self.happiness = self.happiness + 0.05*self.happiness
            print(f"{self.pet_name} is now at {self.happiness}% happiness.")

        if self.hunger > 0 and self.hunger < 100:
            print(f"{self.owner} lose {0.15*self.hunger}% hunger")
            self.hunger = self.hunger - 0.15*self.hunger
            print(f"{self.owner} is at {self.hunger}% hunger")
        
        if self.hunger > 50 and self.hunger < 100:
            print(f"{self.pet_name} gained {self.warmth*0.1}% warmth.")
            self.warmth = self.warmth + self.warmth*0.1
            print(f"{self.pet_name} is at {self.warmth}% warmth.")
        elif self.hunger < 50 and self.hunger > 0:
            print(f"{self.pet_name} lost {self.warmth*0.1}% warmth.")
            self.warmth = self.warmth - self.warmth*0.1
            print(f"{self.pet_name} is at {self.warmth}% warmth.")     

        if self.happiness >= 50 and self.hunger >= 50 and self.warmth >= 50:    
            print(f"{self.pet_name} gained {self.health*0.1}% warmth.")
            self.health = self.health + self.health*0.1
            print(f"{self.pet_name} is at {self.health}% warmth.")  
        elif self.happiness <= 50 and self.hunger <= 50 and self.warmth <= 50:
            print(f"{self.pet_name} lost {self.health*0.1}% warmth.")
            self.health = self.health - self.health*0.1
            print(f"{self.pet_name} is at {self.health}% warmth.")

    def food(self): 

        print(f"{self.owner} fed {self.pet_name}")
        print(f"{self.owner} gained {0.25*self.hunger}% hunger")
        self.hunger = self.hunger + 0.25*self.hunger
        print(f"{self.owner} is at {self.hunger}% hunger")

        if self.hunger > 50 and self.hunger < 100:
            print(f"{self.pet_name} gained {self.warmth*0.1}% warmth.")
            self.warmth = self.warmth + self.warmth*0.1
            print(f"{self.pet_name} is at {self.warmth}% warmth.")
        elif self.hunger < 50 and self.hunger > 0:
            print(f"{self.pet_name} lost {self.warmth*0.1}% warmth.")
            self.warmth = self.warmth - self.warmth*0.1
            print(f"{self.pet_name} is at {self.warmth}% warmth.") 

        if self.happiness >= 50 and self.hunger >= 50 and self.warmth >= 50:    
            print(f"{self.pet_name} gained {self.health*0.1}% warmth.")
            self.health = self.health + self.health*0.1
            print(f"{self.pet_name} is at {self.health}% warmth.")  
        elif self.happiness <= 50 and self.hunger <= 50 and self.warmth <= 50:
            print(f"{self.pet_name} lost {self.health*0.1}% warmth.")
            self.health = self.health - self.health*0.1
            print(f"{self.pet_name} is at {self.health}% warmth.")

        if self.hunger > 50 and self.hunger < 100:
            print(f"{self.pet_name} gained {self.health*0.1}% health.")
            self.health = self.health + self.health*0.1
            print(f"{self.pet_name} is at {self.health}% health.")
        elif self.hunger < 50 and self.hunger > 0:
            print(f"{self.pet_name} lost {self.health*0.1}% health.")
            self.health = self.health - self.health*0.1
            print(f"{self.pet_name} is at {self.health}% health.") 

Dog = Pet("Ethan", "Dog", 100, 100, 100, 100)
Dog.play()
Dog.food()
