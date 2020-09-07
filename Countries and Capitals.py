import random
from itertools import chain


#CONTINENTS
continents = {
    'asia': '50',
    'africa': '54',
    'europe': '51',
    'north america': '23',
    'south america': '12',
    'australia': '14',
    'antarctica': '0'
}

#ASIA - 50 Countries
asian_countries = {
    "Afghanistan": "Kabul",
    "Armenia": "Yerevan",
    "Azerbaijan": "Baku",
    "Bahrain": "Manama",
    "Bangladesh": "Dhaka",
    "Bhutan": "Thimphu",
    "Brunei": "Bandar Seri Begawan",
    "Cambodia": "Phnom Penh",
    "China": "Beijing",
    "Cyprus": "Nicosia",
    "Georgia": "Tbilisi",
    "India": "New Delhi",
    "Indonesia": "Jakarta",
    "Iran": "Tehran",
    "Iraq": "Baghdad",
    "Israel": "Jerusalem",
    "Japan": "Tokyo",
    "Jordan": "Amman",
    "Kazakhstan": "Nur - Sultan",
    "Kuwait": "Kuwait City",
    "Kyrgyzstan": "Bishkek",
    "Laos": "Vientiane",
    "Lebanon": "Beirut",
    "Malaysia": "Kuala Lumpur",
    "Maldives": "Male",
    "Mongolia": "Ulaanbaatar",
    "Myanmar": "Naypyidaw",
    "Nepal": "Kathmandu",
    "North Korea": "Pyongyang",
    "Oman": "Muscat",
    "Pakistan": "Islamabad",
    "Palestine": "Jerusalem(East)",
    "Philippines": "Manila",
    "Qatar": "Doha",
    "Russia": "Moscow",
    "Saudi Arabia": "Riyadh",
    "Singapore": "Singapore",
    "South Korea": "Seoul",
    "Sri Lanka": "Sri Jayawardenepura Kotte",
    "Syria": "Damascus",
    "Taiwan": "Taipei",
    "Tajikistan": "Dushanbe",
    "Thailand": "Bangkok",
    "Timor - Leste": "Dili",
    "Turkey": "Ankara",
    "Turkmenistan": "Ashgabat",
    "United Arab Emirates": "Abu Dhabi",
    "Uzbekistan": "Tashkent",
    "Vietnam": "Hanoi",
    "Yemen": "Sana'a"
}

asian_capitals = ["Kabul", "Yerevan", "Baku", "Manama", "Dhaka", "Thimphu", "Bandar Seri Begawan", "Phnom Penh", "Beijing", "Nicosia", "Tbilisi", "New Delhi", "Jakarta", "Tehran", "Baghdad", "Jerusalem", "Tokyo", "Amman", "Nur - Sultan", "Kuwait City", "Bishkek", "Vientiane", "Beirut", "Kuala Lumpur", "Male", "Ulaanbaatar", "Naypyidaw", "Kathmandu", "Pyongyang", "Muscat", "Islamabad", "Jerusalem(East)", "Manila", "Doha", "Moscow", "Riyadh", "Singapore", "Seoul", "Sri Jayawardenepura Kotte", "Damascus", "Taipei", "Dushanbe", "Bangkok", "Dili", "Ankara", "Ashgabat", "Abu Dhabi", "Tashkent", "Hanoi", "Sana'a", "Ashgabat", "Abu Dhabi"]

#AFRICA - 54 Countries
african_countries = {
    "Algeria": "Algiers",
    "Angola": "Luanda",
    "Benin": "Porto-Novo",
    "Botswana": "Gaborone",
    "Burkina Faso": "Ouagadougou",
    "Burundi": "Gitega",
    "Cabo Verde": "Praia",
    "Cameroon": "Yaounde",
    "Central African Republic": "Bangui",
    "Chad": "N'Djamena",
    "Comoros": "Moroni",
    "Democratic Republic of the Congo": "Kinshasa",
    "Republic of the Congo": "Brazzaville",
    "Cote d'Ivoire": "Yamoussoukro",
    "Djibouti": "Djibouti City",
    "Egypt": "Cairo",
    "Equatorial Guinea": "Malabo",
    "Eritrea": "Asmara",
    "Eswatini": "Mbabane",
    "Ethiopia": "Addis Ababa",
    "Gabon": "Libreville",
    "Gambia": "Banjul",
    "Ghana": "Accra",
    "Guinea": "Conakry",
    "Guinea-Bissau": "Bissau",
    "Kenya": "Nairobi",
    "Lesotho": "Maseru",
    "Liberia": "Monrovia",
    "Libya": "Tripoli",
    "Madagascar": "Antananarivo",
    "Malawi": "Lilongwe",
    "Mali": "Bamako",
    "Mauritania": "Nouakchott",
    "Mauritius": "Port Louis",
    "Morocco": "Rabat",
    "Mozambique": "Maputo",
    "Namibia": "Windhoek",
    "Niger": "Niamey",
    "Nigeria": "Abuja",
    "Rwanda": "Kigali",
    "Sao Tome and Principe": "São Tomé",
    "Senegal": "Dakar",
    "Seychelles": "Victoria",
    "Sierra Leone": "Freetown",
    "Somalia": "Mogadishu",
    "South Africa": "Cape Town",
    "South Sudan": "Juba",
    "Sudan": "Khartoum",
    "Tanzania": "Dodoma",
    "Togo": "Lomé",
    "Tunisia": "Tunis",
    "Uganda": "Kampala",
    "Zambia": "Lusaka",
    "Zimbabwe": "Harare"
}

african_capitals = ["Algiers", "Luanda", "Porto-Novo", "Gaborone", "Ouagadougou", "Gitega", "Praia", "Yaounde", "Bangui", "N'Djamena", "Moroni", "Kinshasa", "Brazzaville", "Yamoussoukro", "Djibouti City", "Cairo", "Malabo", "Asmara", "Mbabane", "Addis Ababa", "Libreville", "Banjul", "Accra", "Conakry", "Bissau", "Nairobi", "Maseru", "Monrovia", "Tripoli", "Antananarivo", "Lilongwe", "Bamako", "Nouakchott", "Port Louis", "Rabat", "Maputo", "Windhoek", "Niamey", "Abuja", "Kigali", "São Tomé", "Dakar", "Victoria", "Freetown", "Mogadishu", "Cape Town", "Juba", "Khartoum", "Dodoma", "Lomé", "Tunis", "Kampala", "Lusaka", "Harare", "Lomé", "Kampala"]

#EUROPE - 51 Countries
europe_countries = {
    "Albania": "Tirana",
    "Andorra": "Andorra la Vella",
    "Armenia": "Yerevan",
    "Austria": "Vienna",
    "Azerbaijan": "Baku",
    "Belarus": "Minsk",
    "Belgium": "Brussels",
    "Bosnia and Herzegovina": "Sarajevo",
    "Bulgaria": "Sofia",
    "Croatia": "Zagreb",
    "Cyprus": "Nicosia",
    "Czechia": "Prague",
    "Denmark": "Copenhagen",
    "Estonia": "Tallinn",
    "Finland": "Helsinki",
    "France": "Paris",
    "Georgia": "Tbilisi",
    "Germany": "Berlin",
    "Greece": "Athens",
    "Hungary": "Budapest",
    "Iceland": "Reykjavik",
    "Ireland": "Dublin",
    "Italy": "Rome",
    "Kazakhstan": "Nur - Sultan",
    "Kosovo": "Pristina",
    "Latvia": "Riga",
    "Liechtenstein": "Vaduz",
    "Lithuania": "Vilnius",
    "Luxembourg": "Luxembourg(city)",
    "Malta": "Valletta",
    "Moldova": "Chisinau",
    "Monaco": "Monaco",
    "Montenegro": "Podgorica",
    "Netherlands": "Amsterdam",
    "North Macedonia": "Skopje",
    "Norway": "Oslo",
    "Poland": "Warsaw",
    "Portugal": "Lisbon",
    "Romania": "Bucharest",
    "Russia": "Moscow",
    "San Marino": "San Marino",
    "Serbia": "Belgrade",
    "Slovakia": "Bratislava",
    "Slovenia": "Ljubljana",
    "Spain": "Madrid",
    "Sweden": "Stockholm",
    "Switzerland": "Bern",
    "Turkey": "Ankara",
    "Ukraine": "Kyiv",
    "United Kingdom": "London",
    "Vatican City": "Vatican City"
}

european_capitals = ["Tirana", "Andorra la Vella", "Yerevan", "Vienna", "Baku", "Minsk", "Brussels", "Sarajevo", "Sofia", "Zagreb", "Nicosia", "Prague", "Copenhagen", "Tallinn", "Helsinki", "Paris", "Tbilisi", "Berlin", "Athens", "Budapest", "Reykjavik", "Dublin", "Rome", "Nur - Sultan", "Pristina", "Riga", "Vaduz", "Vilnius","Luxembourg(city)", "Valletta", "Chisinau", "Monaco", "Podgorica", "Amsterdam", "Skopje", "Oslo", "Warsaw", "Lisbon", "Bucharest", "Moscow", "San Marino", "Belgrade", "Bratislava", "Ljubljana", "Madrid", "Stockholm", "Bern", "Ankara", "Kyiv", "London", "Vatican City", "Stockholm"]

#NORTH AMERICA - 23 Countries
north_american_countries = {
    "Antigua and Barbuda": "Saint John's",
    "Bahamas": "Nassau",
    "Barbados": "Bridgetown",
    "Belize": "Belmopan",
    "Canada": "Ottawa",
    "Costa Rica": "San Jose",
    "Cuba": "Havana",
    "Dominica": "Roseau",
    "Dominican Republic": "Santo Domingo",
    "El Salvador": "San Salvador",
    "Grenada":"Saint George's",
    "Guatemala": "Guatemala City",
    "Haiti": "Port-au-Prince",
    "Honduras": "Tegucigalpa",
    "Jamaica": "Kingston",
    "Mexico": "Mexico City",
    "Nicaragua": "Managua",
    "Panama": "Panama City",
    "Saint Kitts and Nevis": "Basseterre",
    "Saint Lucia": "Castries",
    "Saint Vincent and the Grenadines": "Kingstown",
    "Trinidad and Tobago": "Port of Spain",
    "United States of America": "Washington, D.C"
}

north_american_capitals = ["Saint John's", "Nassau", "Bridgetown", "Belmopan", "Ottawa", "San Jose", "Havana", "Roseau", "Santo Domingo", "San Salvador", "Saint George's", "Guatemala City", "Port-au-Prince", "Tegucigalpa", "Kingston", "Mexico City", "Managua", "Panama City", "Basseterre", "Castries", "Kingstown", "Port of Spain", "Washington, D.C", "Basseterre"]

#SOUTH AMERICA - 12 Countries
south_american_countries = {
    'Argentina': 'buenos aires',
    'Bolivia': 'sucre',
    'Brazil': 'brasilia',
    'Chile': 'santiago',
    'Colombia': 'bogotá',
    'Ecuador': 'quito',
    'Guyana': 'georgetown',
    'Paraguay': 'asunción',
    'Peru': 'lima',
    'Suriname': 'paramaribo',
    'Uruguay': 'montevideo',
    'Venezuela': 'caracas'
}

south_american_capitals = ['buenos aires', 'sucre', 'brasilia', 'santiago', 'bogotá', 'quito', 'georgetown', 'asunción', 'lima', 'paramaribo', 'montevideo', 'caracas']

#AUSTRALIA - 14 Countries
australian_countries = {
    "Australia": "Canberra",
    "Fiji": "Suva",
    "Kiribati": "Tarawa",
    "Marshall Islands": "Majuro",
    "Micronesia": "Palikir",
    "Nauru": "Yaren District (de facto)",
    "New Zealand": "Wellington",
    "Palau": "Ngerulmud",
    "Papua New Guinea": "Port Moresby",
    "Samoa": "Apia",
    "Solomon Islands": "Honiara",
    "Tonga": "Nukuʻalofa",
    "Tuvalu": "Funafuti",
    "Vanuatu": "Port Vila"
}

australian_capitals = ["Canberra", "Suva", "Tarawa", "Majuro", "Palikir", "Yaren District (de facto)", "Wellington", "Ngerulmud", "Port Moresby", "Apia", "Honiara", "Nukuʻalofa", "Funafuti", "Port Vila", "Honiara", "Nukuʻalofa"]

chances = 3
positive = 'yes'
negative = 'no'
correct_answer = 'Correct\n'
incorrect_answer = 'Incorrect\n'
play = True
y = 1
z = 1


#GAME STARTS
print("Hi there! 🙂, I am Javis but you can call my Jay")
name = input("What about you? What's your name? \n")
question = input(f"Nice to meet you {name} 🤝, would like you to play a guessing game with me where you get to guess the capitals of different countries? \n").lower()

while play:
    if question == positive:
        print('\nGo ahead and select a continent:')
        print("\n".join(str(x) for x in continents))
        chosen_continent = input("")
        print('Okay, Here we go!\n\n')
        # ASIA
        if chosen_continent == list(continents.keys())[0]:
            print("ASIAN COUNTRIES\n")
            # ASIA PARAMETERS
            countries = list(asian_countries.keys())
            capitals = list(asian_countries.values())
            noc = 50  # number of countries/total number of iterations
            c = 50
            d = 47
            continent_capitals = asian_capitals

        # AFRICA
        elif chosen_continent == list(continents.keys())[1]:
            print("AFRICAN COUNTRIES\n")
            # AFRICA PARAMETERS
            countries = list(african_countries.keys())  # Conversion of country.keys(country name) to list
            capitals = list(african_countries.values())  # Conversion of country.values(capital name) to list
            noc = 54  # number of countries/total number of iterations
            c = 54
            d = 51
            continent_capitals = african_capitals

        # EUROPE
        elif chosen_continent == list(continents.keys())[2]:
            print("EUROPE COUNTRIES\n")
            # EUROPE PARAMETERS
            countries = list(europe_countries.keys())
            capitals = list(europe_countries.values())
            noc = 51  # number of countries/total number of iterations
            c = 51
            d = 48
            continent_capitals = european_capitals

        # NORTH AMERICA
        elif chosen_continent == list(continents.keys())[3]:
            print("NORTH AMERICAN COUNTRIES\n")
            # NORTH AMERICA PARAMETERS
            countries = list(north_american_countries.keys())
            capitals = list(north_american_countries.values())
            noc = 23  # number of countries/total number of iterations
            c = 23
            d = 20
            continent_capitals = north_american_capitals

        # SOUTH AMERICA
        elif chosen_continent == list(continents.keys())[4]:
            print("SOUTH AMERICAN COUNTRIES\n")
            # SOUTH AMERICA PARAMETERS
            countries = list(south_american_countries.keys())
            capitals = list(south_american_countries.values())
            noc = 12  # number of countries/total number of iterations
            c = 12
            d = 9
            continent_capitals = south_american_capitals

        # AUSTRALIA
        elif chosen_continent == list(continents.keys())[5]:
            print("AUSTRALIAN COUNTRIES\n")
            # AUSTRALIA PARAMETERS
            countries = list(australian_countries.keys())
            capitals = list(australian_countries.values())
            noc = 14  # number of countries/total number of iterations
            c = 14
            d = 11
            continent_capitals = australian_capitals

        # ANTARCTICA
        elif chosen_continent == list(continents.keys())[6]:
            print("Antarctica doesn't have any countries!")
            break

        # GAME CODE
        # Iteration through the total number of countries
        p = 0
        a = 1
        b = 1
        for number_of_iterations in range(noc):
            if a == d:
                continent_capitals.extend(continent_capitals[2:7])
                c = c + 6
            country = countries[p]
            answer = capitals[p]
            print(f'{b}. What is the capital of {country}?')
            random_selection_of_capitals = random.sample(continent_capitals[a:c], 3)
            list(chain(*(x.split(',') for x in random_selection_of_capitals)))  # seperation of list items
            random_selection_of_capitals.append(continent_capitals[p])  # adds answer to the list
            random.shuffle(random_selection_of_capitals)  # shuffle answer_list
            print("\n".join(str(x) for x in random_selection_of_capitals))
            country_question = input('Select an option: ')
            result = \
f"""Nicely done {name}!
You got the capital of {y} countries right.
You got the capital of {z} countries wrong\n"""
            if country_question == answer:
                print(correct_answer)
                y += 1
            else:
                print(incorrect_answer)
                z += 1
            a += 1
            p += 1
            b += 1
            if y == 1:
                y = 0
            elif z == 1:
                z = 0
        print(result)
        another_continent = input("\nDo you want to try out another continent? \n")
        if another_continent == positive:
            y = 0
            z = 0
            play = True
        elif another_continent == negative:
            play = False
            print(f"Okay {name}!, thanks for playing, have a great day.")
            break
        else:
            question = input("You have to select either 'yes' or 'no' \n")
            if question != positive or negative:
                print("Try again")
                chances = chances - 1
                if chances == 0:
                    print("You are out of chances! Game Over")
                    break

    elif question == negative:
        print('Okay, have a nice day')
        break
    else:
        question = input("You have to select either 'yes' or 'no' \n")
        if question != positive or negative:
            print("Try again")
            chances = chances - 1
            if chances == 0:
                print("You are out of chances! Game Over")
                break