#6-4
py_terms = {
    'syntax': 'defines how the program is written.',
    'comment': 'using a hashtag you can enter a non-coded not about the program.',
    'function': 'block of organized, reusable code used to perform a single action to a related object.',
    'method': 'is called by name but is associated to an object, it is dependent upon an object.',
    'range': 'function that accepts an interger and returns a range object - a type of iterable.',
    'class': 'defined wireframes of objects',
    'dictionares': 'made up of key-value pairs where each key corresponds to a value.',
    'len': 'returns the number of top-level items contained in the object being queried.',
    'for loops': 'provides a clean iteration syntax.',
    'print': 'function to display the output of a program.',
}

for key, value in py_terms.items():
    print("\n" + key.title() + ":")
    print(value)

#6-5
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'snake': 'usa',
}

for river, country in rivers.items():
    print("\nThe river " + river.title() + " runs through the country " + country.title() + ".")

print("\nRivers mentioned: ")
for river, country in rivers.items():
    print(river.title())
print("\nCountries mentioned: ")
for river, country in rivers.items():
    print(country.title())

#6-6
fav_langs = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'anna': '',
    'casey': 'c#',
    'eddie': 'java',
    'tony': '',
}

takers = ['jen','phil', 'sarah', 'edward', 'casey', 'eddie']
for name in fav_langs.keys():
    if name in takers:
        print("\nHi " + name.title() + ", I see you have taken the poll, thanks!")
    elif name not in takers:
        print("\n" + name.title() + ", please take our poll.")