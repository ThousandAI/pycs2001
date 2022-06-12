# Module
"""
import utils

numbers = [30,60,50,80,100,57,90]
utils.say_hello("Thousand")
utils.introduce(name="Thousand",age=30,gender="Male")

print(utils.get_max(numbers=numbers))
print(utils.get_distance(point1=[3,5],point2=[6,1]))
print(f"This is main.py: {__name__}")
"""
"""
# Package
import helper.show as show
import helper.calculate as calculate
numbers = [30,60,50,80,100,57,90]
show.say_hello(guest="Thousand")
show.introduce(name="Thousand",age=30,gender="Male")
print(calculate.get_max(numbers=numbers))
print(calculate.get_distance(point1=(3,5),point2=(6,1)))
"""

class Warrior:
    def __init__(self,name,gender,weapon):
        self.level = 1
        self.exp = 0
        self.n = name
        self.g = gender
        self.w = weapon
        #print("This is Warrior Class.")
        #print(f"Self is {self}")

    def __str__(self):
        return f"Name: {self.n}, Gender: {self.g}, Weapon: {self.w}, Level: {self.level}, Exp: {self.exp}"

    # instance method
    def attack(self,enemy):
        self.exp += 40
        enemy.hp -= 10
        if enemy.hp == 0:
            del enemy
        self.level_up()
        print(f"{self.n} attack {enemy.n}, Enemy hp: {enemy.hp}")

    def level_up(self):
        if self.exp >= 100:
            self.level += 1
            self.exp -= 100
            print(f"升級!! 已到達 {self.level}")

import random
class Enemy:
    def __init__(self,name):
        self.n = name
        self.hp = 100


warrior1 = Warrior(name="Thousand",gender="Male",weapon='Sword')
#print(f"Warrior1 {warrior1}")
warrior2 = Warrior(name="Allie",gender="Female",weapon='Arrow')
#print(f"Warrior2 {warrior2}")
enemy1 = Enemy("Frank")

while True:
    try:
        warrior1.attack(enemy1)
    except UnboundLocalError:
        print("戰勝敵人")
        break