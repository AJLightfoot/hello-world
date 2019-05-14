# 7-1 Rental Car
car_type = input("What kind of car do you want? ")
print("Let me check to see if we have a " + car_type.title() + " available.")

#7-2 Restaurant Seating
party_size = input("\nHow many people are in your party? ")
party_size = int(party_size)

if party_size >= 8:
    print("\nYou will need to wait a few minutes for seating.")
else:
    print("\nYour table is ready.")

#7-3 Multiples of 10
number = input("\nEnter a number and I can tell you if is divisible by 10. ")
number = int(number)

if number % 10 == 0:
    print("\nThe number " + str(number) + " is divisible by 10.")
else:
    print("\nThe number " + str(number) + " is not divisible by 10.")