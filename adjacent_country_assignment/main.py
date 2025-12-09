from country import Country

def main():
    country_code = Country.input_country_name()
    adjacent_countries = Country.get_adjacent_country(country_code)
    if adjacent_countries is None:
        print("Invalid country code")
        return
    Country.print_adjacent_country(adjacent_countries)

if __name__ == "__main__":
    main()