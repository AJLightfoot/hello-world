#this short program will ask the question and then repeat what the user types in.
message = input("Tell me something and I will repeat it back to you: ")
print(message)

#addint a space at the end of your input request leaves a space for the user to clearly indicate where to input
name = input("Please enter your name: ")
print("Hello, " + name + "!") #you can also print the data into a message.

#adding additional information on what or why you are asking for the info is helpful.
prompt = "If you tell us who you are we can personalize the messages you see."
prompt += "\nWhat is your first name? " #the += operator adds this line to the variable above spanning two lines now.

name = input(prompt)
print("\nHello, " + name + "!")

#you can use input, but remember that all data input will be a string
age = input("How old are you? ")

age = int(age) #converting the string to an interger converts numbers input to proper intergers in the code
age >= 18

print(age)

#using the int() function in a actual program - example:
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little taller.")

#you can use the modulo operator to show the remainder - this is a good way to tell if a number is even or odd.
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")