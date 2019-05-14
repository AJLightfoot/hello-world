movies = 'ragnarok'
print(movies == 'ragnarok')
print(movies != 'shining')

dice = ['d2', 'd4', 'd6', 'd8', 'd10', 'd12', 'd20']
die = 'd100'

if die not in dice:
    print("\nThe " + die.title() + " is not a standard dice in the set")

heroes = ['cable','deadpool', 'wolverine', 'night thrasher', 'thor', 'groot']
villians = ['magneto', 'sabertooth', 'thanos', 'traxxas', 'loki']

for hero in heroes:
    if hero == 'thor':
        print("\nYes " + hero.title() + " is a hero of the MCU.")

for villian in villians:
    if villian != 'loki':
        print("\nThese are villians." + villian.upper())

ages = [18, 21, 30]
for age in ages:
    if age == 18:
        print("\nthis is the first age in the list " + age.__str__() + ".")

ages = [18, 21, 30]
for age in ages:
    if age != 18:
        print("\nthis age is not in the list.")

ages = [18, 21, 30]
for age in ages:
    if age >= 18:
        print("\nAll ages are greater.")

ages = [18, 21, 30]
for age in ages:
    if age <= 35:
        print("\nAll ages are less than.")