# """
# In this simple RPG game, the hero fights the goblin. He has the options to:
#
# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
#
# """
#
# hero_health = 10
# hero_power = 5
# health = 6
# power = 2
#

class Character(object):

    def __init__(self):
        self.name = ""
        self.health = 0
        self.power = 0

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if enemy.name != "zombie":

            enemy.health -= self.power
            print "%s do %d damage to the %s." % (self.name, self.power, enemy.name)
            if enemy.health <= 0:
                print "The %s is dead." % (enemy.name)

        else:
            print "Zombie is invincible. Good luck!"


    def print_status(self):
        print "%s have %d health and %d power." % (self.name, self.health, self.power)


class Hero(Character):
    def __init__(self):
        self.name = 'hero'
        self.health = 10
        self.power = 5



class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 6
        self.power = 2

class Zombie(Character):
    def __init__(self):
        self.name = 'zombie'
        self.health = 10
        self.power = 5

hero = Hero()


goblin = Goblin()

zombie = Zombie()


while zombie.alive() and hero.alive():

    zombie.print_status()
    hero.print_status()
    print
    print "What do you want to do?"
    print "1. fight zombie"
    print "2. do nothing"
    print "3. flee"
    print "> ",
    input = raw_input()

    if input == "1":
        # Hero attacks goblin
        hero.attack(zombie)
    elif input == "2":
        pass
    elif input == "3":
        print "Goodbye."
        break
    else:
        print "Invalid input %r" % input

    if zombie.health > 0:
        # Goblin attacks hero
        zombie.attack(hero)
