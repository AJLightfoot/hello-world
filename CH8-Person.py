#Using a function to return a dictionary
def build_person(fname, lname, age=''): #added age parameter
    """Return a dictionary of info about a person."""
    person = {'first': fname, 'last': lname}
    if age:
        person['age'] = age
    return person

musician = build_person('thomas', 'forsberg', '38')
print(musician)