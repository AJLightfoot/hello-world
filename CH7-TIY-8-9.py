sandos = ['rueben', 'blt', 'pastrami', 'monte cristo', 'pastrami', 'ham n chees', 'turkey', 'pastrami', 'tuna']
ordered_sandos = []

while sandos:
    current_sando = sandos.pop()
    if current_sando == 'pastrami':
        print("The deli has run out of pastrami, sorry.")
    else:
        print("I made your " + current_sando.title() + " sandwich.")
        ordered_sandos.append(current_sando)

print("\nThe following sandwiches have been made:")
for ordered_sando in ordered_sandos:
    print(ordered_sando.title())