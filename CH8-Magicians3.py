def show_mages(mages):
    for mage in mages:
        print(mage)

def make_great(mages):
    great_mages = []
    while mages:
        mage = mages.pop()
        great_mage = mage + ' the Great'
        great_mages.append(great_mage)
    for great_mage in great_mages:
        mages.append(great_mage)
        print(great_mage)

    return mage_list

mage_list = ['bigby', 'mordenkainen', 'tenser', 'leomund', 'otiluke']

print("\nGreat mages:")
great_mages = make_great(mage_list[:])
show_mages(great_mages)

print("\nOriginal mages:")
show_mages(mage_list)