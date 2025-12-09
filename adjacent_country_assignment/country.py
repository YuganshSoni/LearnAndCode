from config import CountryMappings

class Country:
    def input_country_name():
        return input("Enter country code : ")

    def get_adjacent_country(country_code : str):
        country_code = country_code.upper()
        if country_code not in CountryMappings.adjacent_countries.keys():
            return None
        return CountryMappings.adjacent_countries.get(country_code)

    def print_adjacent_country(adjacent_country : list[str]):
        if len(adjacent_country)==0:
            print("No adjacent countries")
            return
          
        print("Adjacent countries are : ")
        for neighbor in adjacent_country:
            print(neighbor)