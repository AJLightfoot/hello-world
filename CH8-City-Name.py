def city_country(city, country):
    full_statement = city + ', ' + country + '.'
    return full_statement.title()

while True:
    print("\nPlease Enter a city and country:")
    cityname = input("City: ")
    cntyname = input("Country: ")

    formatted_name = city_country(cityname, cntyname)
    print(formatted_name)