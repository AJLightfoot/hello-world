invites = ['Vader', 'han', 'leia', 'luke']

invites.append('lando')
print (invites)

invites.insert(0, 'yoda')
print (invites)

del invites [1]
print (invites)

pop_inv = invites.pop()
print (invites)

uninvite_message = "Hey " + pop_inv.title() + ", sorry but Han asked if you could sit this one out."

died = 'yoda'
invites.remove(died)

print ("Hey everyone, it is with a heavy heart that I remove " + died.title() + ", he recently passed.")

invite_message1 = "Hello " + invites[0].title() + ", I would like to invite you to dinner."
invite_message2 = "Hello " + invites[1].title() + ", I would like to invite you to dinner."
invite_message3 = "Hello " + invites[2].title() + ", I would like to invite you to dinner."

print (uninvite_message)
print (invite_message1)
print (invite_message2)
print (invite_message3)
print (invites)
print (len(invites))

del invites [0]
print (invites)

del invites [0]
print (invites)

del invites [0]
print (invites)