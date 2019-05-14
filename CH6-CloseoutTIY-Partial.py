people = {
    'person_0': {
        'fname': 'anna',
        'lname': 'lightfoot',
        'city': 'canby',
    },
    'person_1': {
        'fname': 'casey',
        'lname': 'prunella',
        'city': 'oregon city',
    },
    'person_2': {
        'fname': 'tony',
        'lname': 'mijo',
        'city': 'oregon city',
    },
}

for person, info in people.items():
    print("\nPerson number: " + person)
    full_name = info['fname'] + " " + info['lname']
    location = info['city']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

pandora = {'type': 'am-staff', 'owner': 'aj',}
egor = {'type': 'great dane', 'owner': 'danni',}
chewie = {'type': 'cat', 'owner': 'casey',}

pets = [pandora, egor, chewie]

for pet in pets:
    print("Pet Type: " + pet['type'].title() + ", Pet owner: " + pet['owner'].title() + ".")

fav_places = {'bob': 'germany', 'keith': 'brazil', 'george': 'norway'}

for name, place in fav_places.items():
    print("\n" + name.title() + " loves to visit " + place.title() + ".")

fav_nums = {
    'jen': ['13', '99'],
    'sarah': ['45'],
    'edward': ['69', '420'],
    'phil': ['6', '42'],
}

for name, numbers in fav_nums.items():
    if len(numbers) == 1:
        print("\n" + name.title() + "'s favorite number is:")
        for number in numbers:
            print("\t" + number)
    else:
        print("\n" + name.title() + "'s favorite numbers are:")
        for number in numbers:
            print("\t" + number)
            