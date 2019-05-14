#creating a dictionary for each individual alien, then nesting the dictionarys into a list called aliens.
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens: #calling and printing each aliens dictionary individually
    print(alien)

#a more realistic example - using code to generate each alien using range()
#make an empty list to store the alines.
aliens = []

#make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

#show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

#show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))

#we can alter any individual aliens in the nested dictionary by adding in the following for loop.
aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

#for loop set to change the values for the first three aliens in the nested dictionary
for alien in aliens[0:3]:
    if alien['color'] == 'green':#use an if statement to only affect the 'green' aliens
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yello':#use an elif statement to only affect the 'yellow' aliens
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:5]:
    print(alien)
print("...")
