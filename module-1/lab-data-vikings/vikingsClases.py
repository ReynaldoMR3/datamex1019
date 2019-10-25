# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
        pass


# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return '{} has received {} points of damage'.format(self.name, damage)
        else:
            return '{} has died in act of combat'.format(self.name)

    def battleCry(self):
        return "Odin Owns You All!"

    pass


# Saxon


class Saxon(Soldier):
    def __init__(self, health, strenght):
        self.health = health
        self.strength = strenght

    def receiveDamage(self, damage):
        # self.Soldier.health - damage
        self.health -= damage
        if self.health > 0:
            return 'A Saxon has received {} points of damage'.format(damage)
        else:
            return 'A Saxon has died in combat'

    pass


# War


class War:
    def __init__(self, vikingArmy=[], saxonArmy=[]):
        self.saxonArmy = saxonArmy
        self.vikingArmy = vikingArmy

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        if Saxon.receiveDamage(viking.attack) == Viking.attack() <= 0:
            self.vikingArmy.remove(Saxon)

    def saxonAttack(self):
        Viking.receiveDamage == Saxon.attack
        if Viking.receiveDamage <= 0:
            self.saxonArmy.pop(Viking)

    def showStatus(self):
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        elif self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

    pass
