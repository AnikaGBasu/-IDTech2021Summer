class Bots:
    def __init__(self, botName, botHealth, botAttackDamage, botRegen):
        self.name = botName
        self.health = botHealth
        self.attackDamage = botAttackDamage
        self.regen = botRegen

    def attack(self, opponent):
        opponent.health -= self.attackDamage
        print(self.name + " attacks")

    def defend(self):
        self.health -= bot2.attackDamage-self.regen
        print(self.name + " defends")

    def heal(self):
        self.health += self.regen
        print(self.name + " regenerates")

    def get_status(self, opponent):
        print(self.name + "'s health is " +  str(self.health) + "\t\t\t|\t\t" + opponent.name + "'s health is " + str(opponent.health) + ".")

        print(self.name + "'s attack is  worth " + str(self.attackDamage) + "\t\t|\t\t" + opponent.name + "'s attack is worth " + str(
        opponent.attackDamage) + ".")

bot1 = Bots("Coffee Turtle", 15, 3, 0)
bot2 = Bots("Tea Turtle", 10, 6, 0)


print(bot1.name)
print(bot2.name)

bot2.get_status(bot1)

bot1.attack(bot2)

bot2.get_status(bot1)

bot2.attack(bot1)


bot2.get_status(bot1)

bot2.heal()

bot2.get_status(bot1)

