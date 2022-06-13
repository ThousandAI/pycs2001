class Character:
    def __init__(self,name,gender,weapon):
        self.level = 1
        self.exp = 0
        self.n = name
        self.g = gender
        self.w = weapon
        print("This is Character class.")

    def __str__(self):
        return f"Name: {self.n}, Gender: {self.g}, Weapon: {self.w}"

    def attack(self):
        print(f"{self.n} attack.")

class Warrior(Character):
    def __init__(self, name, gender, weapon):
        super().__init__(name,gender,weapon)
        self.sp = 100

    def attack(self):
        super().attack()
        print(f"{self.n} use {self.w}")

    def bash(self):
        if self.level >= 5:
            print(f"{self.n} use bash.")
        else:
            print(f"等級5等才能使用 ")

class Wizard(Character):
    def __init__(self, name, gender, weapon):
        super().__init__(name,gender,weapon)
        self.mp = 100

    def fireball(self):
        if self.level >= 5:
            print(f"{self.n} use fireball.")
        else:
            print(f"等級5等才能使用 ")


warrior = Warrior(name='Thousand',gender='Male',weapon='Sword')
wizard = Wizard(name='Allie',gender='Female',weapon='wand')
print(warrior)
print(wizard)
warrior.attack()
wizard.attack()
warrior.bash()
wizard.fireball()