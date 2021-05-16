import random


class Pokemon:
    def __init__(self, name, startingHealth, attack, defense):
        self.name = name
        self.health = startingHealth
        self.att = attack
        self.defense = defense

    def __str__(self):
        return self.name + \
               "\n" + "Health: " + str(self.health) + \
               "\n" + "Attack: " + str(self.att) + \
               "\n" + "Defense: " + str(self.defense)

    def calculateDamage(self, other):
        # (12/5 * A/D + 2)r
        # where A is self's attack strength, D is the other Pokemon's defense, and r is a random floating point number
        # from 0.85 to 1.
        r = random.randint(85, 100) / float(100)
        print("r: " + str(r))
        output = (12/5 * self.att / other.defense + 2)*r
        return output

    def attack(self, other):
        if other.health - round(self.calculateDamage(other)) <= 0:
            other.health = 0
            print(other.name + " has fainted!")

        else:
            other.health -= round(self.calculateDamage(other))
            print(self.name + " does " + str(round(self.calculateDamage(other))) + " damage!")


b = Pokemon('Bulbasaur', 45, 49, 49)
print(b)
c = Pokemon('Charmander', 39, 52, 43)
print(c)

c.attack(b)
print(b)
