alien_0 = {'color': 'green', 'points': 5} #dictionary stores key value pairs - key:value indicated by the {} braces

print(alien_0['color'])
print(alien_0['points'])

#you can add to and change dictionaries
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0) #the print function will print them in any order as this does not matter to python to run the code

#you can also start with an empty dictionary and populate it based on input data from users, etc.
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

#you can also modify values within the dictionary
alien_0 = {'color' : 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

#lets use the dictionary to track the movement of a object
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

#we will move the object to the right
#determine how far to move the object based on its speed

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else: #this is the fastest speed
    x_increment = 3

#the new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] = x_increment
print("New x-position: " + str(alien_0['x_position']))

#you can also alter the speed by changing the dictionary
alien_0['speed'] = 'fast' #the next cycle would assign the 3rd listed speed under else.

#you can also remove key value pairs using the del function
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)