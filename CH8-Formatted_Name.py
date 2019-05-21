#Example of a retrun value from a function call
def get_formatted_name(fname, lname):
    """Return a full name, neatly formatted."""
    full_name = fname + ' ' + lname
    return full_name.title()

musician = get_formatted_name('thomas', 'forsberg')
print(musician)

#Example of making an argument optional in a function call
def get_formatted_name(fname, lname, mname=''):
    """Return a full name, neatly formatted."""
    if mname:
        full_name = fname + ' ' + mname + ' ' + lname
    else:
        full_name = fname + ' ' + lname
    return full_name.title()

musician = get_formatted_name('thomas', 'forsberg', 'borje')
print(musician)
musician = get_formatted_name('thomas', 'forsberg')
print(musician)