cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requested_topping = 'pepperoni'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")

age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21

age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >= 21
