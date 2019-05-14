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
print(age_0 >= 21 and age_1 >= 21) #statement to check if both conditions are met

age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21) #statement to check if one or the other conditions are met

requested_topping = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_topping) #statement to check if value is in the list - True
print('pepperoni' in requested_topping) #statement to check if value is in the list - False

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print("\n" + user.title() + ", you can post a response if you wish.")

car = 'subaru'
print("\nIs car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')