#7-5 Movie Tickets
prompt = "\nHow old are you?"
prompt += "\n(Enter 'quit' when finished.) "

while True:
    age = input(prompt)

    if age == 'quit':
        break
    else:
        age = int(age)

        if age <= 3:
            print("\nYour fee is $0 because you are " + str(age) + " years old.")
        elif age <=12:
            print("\nYour fee is $10 because you are " + str(age) + " years old.")
        else:
            print("\nYour fee is $15 because you are " + str(age) + " years old.")