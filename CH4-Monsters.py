monsters = ['troll', 'beholder']
print (monsters)

monsters.append('umber hulk')
print (monsters)

monsters.insert(0, 'goblin')
print (monsters)

del monsters [1]
print (monsters)

pop_monster = monsters.pop()
print (monsters)

monster_message = "Beware " + pop_monster.title() + "s, they are very deadly."
print (monster_message)
print (monsters)

monsters.append('elemental')
monsters.append('dragon')
monsters.append('lich')
print (monsters)

chromatic = 'dragon'
monsters.remove(chromatic)
print (chromatic.title() + "'s are often times not evil and don't warrant to be called monsters.")
print (monsters)


print (sorted(monsters))
print (monsters)
print (sorted(monsters, reverse=True))
print (monsters)
monsters.reverse()
print (monsters)
monsters.reverse()
print (monsters)
monsters.sort()
print (monsters)
monsters.sort(reverse=True)
print (monsters)