players = ['anna', 'casey', 'tony', 'anna2', 'nathan', 'danni']
print(players[0:3])
print(players[3:6])
print(players[:4])
print(players[4:])
print(players[-2:])

print("\nThe Misadventuers are:")
for player in players[:3]:
    print(player.title())

my_foods = ['nachos', 'pizza', 'burritos']
frend_foods = my_foods[:]

my_foods.append('ice cream')
frend_foods.append('candy')

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friends favorite foods are:")
print(frend_foods)

pizzas = ['fultano', 'round table', 'schmizza']
frend_pizza = pizzas[:]

pizzas.append('stark street')
frend_pizza.append('little cesars')

print("\nMy favorite pizzas are:")
print(pizzas)

print("\nMy friends favorite pizzas are:")
print(frend_pizza)

for pizza in pizzas:
    print(pizza.title())

for food in my_foods:
    print(food.title())