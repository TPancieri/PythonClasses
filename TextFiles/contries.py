input_filename = 'country_info.txt'

countries = {}
with open(input_filename) as country_file:
    # the country_file object is iterable, each time you use the readline method to read a line,
    # the iterator automatically moves on to the next item. we do this to skip printing the labels
    country_file.readline()
    for row in country_file:
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency,
        }
        # print(country_dict)
        countries[country.casefold()] = country_dict
        countries[code.casefold()] = country_dict

print(countries)


while True:
    choice = input("Please choose a country \n >").casefold()
    if choice in countries:
        country_data = countries[choice]
        print(f"the capital of {choice} is {country_data['capital']}")
    elif choice == 'quit':
        break
