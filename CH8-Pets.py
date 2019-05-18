#positional arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry') #order matters in a function call the arguments must match the parameters
describe_pet('dog', 'pandora3')

#rewriting code to use keyword arguments
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster') #order does not matter when using keyword arguments

#using default values in a function call
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='pandora')
describe_pet('pandora') # this function call works the same as above because the first argument is the name
describe_pet('harry', 'hamster') #you can still override the second parameter with a different arguments
describe_pet(pet_name='harry', animal_type='hamster') #this works the same but uses keyword to specify the parameters