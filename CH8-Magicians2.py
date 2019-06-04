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

mage_list = ['bigby', 'mordenkainen', 'tenser', 'leomund', 'otiluke']

show_mages(mage_list)
make_great(mage_list)