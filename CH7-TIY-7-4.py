#7-4 Pizza Toppings
prompt = "\nWhat pizza topping would you like on your pizza?"
prompt += "\n(Enter 'quit' when finished.) "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print("\nWe are adding " + topping + " to your pizza!")