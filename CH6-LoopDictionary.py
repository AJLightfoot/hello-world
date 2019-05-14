#looping through a dictionary and calling key and value items
user0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

#using a for loop you can access all users data in the dictionary
for key, value in user0.items():
    print("\nKey: " + key)
    print("value: " + value)

#another example of looping through a dictionary
fav_langs = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, lang in fav_langs.items():
    print(name.title() + "'s favorite language is " + lang.title() + ".")

#using the keys() method you can call only the keys when the value is not necessary
#keys() method is the default method so it is not always necesarry to type it

fav_langs = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in fav_langs.keys():
    print(name.title())

#in the example below we call out friends names and show a special message

fav_langs = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['phil', 'sarah']
for name in fav_langs.keys():
    print(name.title())

    if name in friends:
        print("Hi " + name.title() + ", I see your favorite language is " + fav_langs[name].title() + "!")

if 'erin' not in fav_langs.keys():
    print("Erin, please take our poll.")

#you can also use the sorted function to loop through a dictionary in order
fav_langs = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in sorted(fav_langs.keys()):
    print(name.title() + ", thank you for taking the poll.")

#using the values() method you can call only the value when the key is not necessary
fav_langs = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("The following languages have been mentioned: ")
for lang in fav_langs.values():
    print(lang.title())

#changing the above to use a set we can remove duplication
fav_langs = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("The following languages have been mentioned: ")
for lang in set(fav_langs.values()):
    print(lang.title())