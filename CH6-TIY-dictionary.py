#you can use a dictionary to store like objects in separate lines
fav_langs = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

#you can then recall any value by using its key
print("Sarah's favorite language is " + fav_langs['sarah'].title() + ".")

#create a list of data about someone first name, last name, city they live in
person0 = {'f_name': 'anna', 'l_name': 'lightfoot', 'city': 'canby'}

print(person0['f_name'].title())
print(person0['l_name'].title())
print(person0['city'].title())
print("I love my wife " + person0['f_name'].title() + " " + person0['l_name'].title() + "."
      "\nWe live in the small city of " + person0['city'].title() + ".")