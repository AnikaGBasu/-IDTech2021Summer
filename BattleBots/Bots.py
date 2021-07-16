class Bots:
    def __init__(self, botName, botHealth, botAttackDamage, botRegen):
        self.name = botName
        self.health = botHealth
        self.attackDamage = botAttackDamage
        self.regen = botRegen

    def attack(self):
        self.health -= bot2.attackDamage
        print(self.name + " attacks")

    def defend(self):
        self.health -= bot2.attackDamage-self.regen
        print(self.name + " defends")

    def heal(self):
        self.health += self.regen
        print(self.name + " regenerates")

    def get_status(self):
        print(bot1.name + "'s health is " +  str(bot1.health) + "\t\t\t|\t\t" + bot2.name + "'s health is " + str(bot2.health) + ".")

        print(bot1.name + "'s attack is  worth " + str(bot1.attackDamage) + "\t\t|\t\t" + bot2.name + "'s attack is worth " + str(
        bot2.attackDamage) + ".")

bot1 = Bots("Coffee Turtle", 15, 3, 0)
bot2 = Bots("Tea Turtle", 10, 6, 0)


print(bot1.name)
print(bot2.name)

bot2.get_status()
bot1.attack()
bot1.defend()
bot2.heal()

