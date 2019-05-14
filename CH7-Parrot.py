#the while loop below allows the user to end the program by inputting the key prhase quit
propmt = "\nTell me something, and I will repeat it back to you: "
propmt += "\nEnter 'quit' to end the program. "

#adding in a flag so that we can potentially have multiple conditions potentially end the program and not just the quit value.
active = True #this is the flag, while it remains true the while loop will run looping the program
while active:
    message = input(propmt)

    if message == 'quit':
        active = False
    else:
        print(message)