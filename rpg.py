class Currency:
    def __init__(self, gold, silver, copper):
        self.value = (gold, silver, copper)
        # because it's same as set below
        # self.gold = gold
        # self.silver = silver
        # self.copper = copper
    @property    
    def value(self):
        return self.__gold, self.__silver, self.__copper
        
    @value.setter
    def value(self, value_tuple):
        gold, silver, copper = value_tuple
        self.__gold = gold
        self.__silver = silver
        self.__copper = copper

    def add(self, gold, silver, copper):
        self.__gold += gold
        self.__silver += silver
        self.__copper += copper

    # define a string representation of the object
    # Should return a Python expression thatr reconstructs the object
    # Intended for use by developers, not users
    def __repr__(self):
        return f'Currency(gold={self.__gold}, silver={self.__silver}, copper={self.__copper})'
        # return 'Hello' 
        # ^^for test the default..
    def __str__(self):
        # for users,human readable description
        #Especially put the string into the paragraph, will show the Str,
        # differances between repr and str.
        return f'{self.__gold}G {self.__silver}S {self.__copper}C'
class Character:
    __available_races = ['Human', 'Elf', 'Orc', 'Goblin', 'Dwarf']
        # for the whole races, share together the lists^^

    def __init__(self, name, race, health=100, attack=10):
        self.name = name
        self.race = race
        self.health = health
        self.attack = attack
        self.purse = Currency(0, 0, 0)
    # character can store in purse(wallet)

    @classmethod
    def is_valid_race(cls, race):
        return race in cls.__available_races


        # self + other means fight each other
    def battle(self, other):
        print(f'{self.name} launches a brutal melee attack on {other.name}!')


class Mage(Character):
    def __init__(self, name, race, health=40, attack=50, mana=200):
        super().__init__(name, race, health=health, attack=attack)
        self.mana = mana
    # only for mage 
    def cast(self, spell):
        self.mana -= 10
    

    def battle(self, other):
        print(f'{self.name} casts a wicked spell at {other.name}!')
        self.cast('fireball')


class Chest:
    def __init__(self, item, gold, silver, copper):
        self.item = item
        self.cash = Currency(gold, silver, copper)

    # transfer contents of this chest to character
    def loot(self, character):
        # because above, self.cash
        gold, silver, copper = self.cash.value()
        character.purse.add(gold, silver, copper)
        self.cash.value = (0, 0, 0)