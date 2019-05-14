#A continue loop will return to the beginning of the loop based on the result of a conditional test.
#In the below example we run a a loop that counts 1-10 but prints only the odd numers in that range.
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)