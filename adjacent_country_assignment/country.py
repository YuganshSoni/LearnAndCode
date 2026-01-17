from config import CountryMappings

class Country:
    def get_country_code(self):
        return input("Enter country code : ")
    
    def validate_country_code(self, country_code : str):
        valid_country_code = []
        for character in country_code:
            ascii_value = ord(character)
            if 97 <= ascii_value <= 122:
                valid_country_code.append(chr(ascii_value - 32))
            elif 65 <= ascii_value <= 90:
                valid_country_code.append(character)
            else:
                return None 
        return ''.join(valid_country_code)

    def get_adjacent_country(self, country_code : str):
        if country_code not in CountryMappings.adjacent_countries.keys():
            return None
        return CountryMappings.adjacent_countries.get(country_code)

    def display_adjacent_country(self, adjacent_country : list[str]):
        if len(adjacent_country)==0:
            print("No adjacent countries")
            return
          
        print("Adjacent countries are : ")
        for neighbor in adjacent_country:
            print(neighbor)