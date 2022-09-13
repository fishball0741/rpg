# from person import Person

# p1 = Person(name='John', age=40)
# p2 = Person('Mary', 35)

# # p1.name = 'John'
# # print(p1)
# p1.greet()
# p2.greet()

# print(p1.greet())
# print(p2)

import rpg

conan = rpg.Character('Conan', 'Human')
galadriel = rpg.Mage('Galadriel', 'Elf')
galadriel.purse.value = (10, 5, 1)
grok = rpg.Character('Grok', 'Orc', health=130)
chest = rpg.Chest(['longword', 'iron helmet'], 2, 50, 25)

# conan.battle(galadriel)
# galadriel.battle(grok)

# galadriel.purse.__gold = 1000


print(conan.__dict__)
print(galadriel.__dict__)
print(grok.__dict__)

# rpg.Character.available_races.append('Ogre')
    # even create the new race in conan, but still in grok
    # share the same races > available_races
print(rpg.Character.is_valid_race('Human'))


# galadriel.purse.value = (20, 10, 5)
    # called destructuring, must = the amount of value, 3:3
# g, s, c = galadriel.purse.value

# print(f'{galadriel.name} has {g} gold.')
# chest.loot(galadriel)

# print(chest.__dict__)
# print(galadriel.__dict__)

# print(chest.cash)
# print(f'{galadriel.name} has {galadriel.purse} in her pocket')
