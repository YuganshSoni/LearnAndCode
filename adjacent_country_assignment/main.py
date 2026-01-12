from country import Country

def main():
    country_service  = Country()
    country_code = country_service.get_country_code()
    country_code = country_service.validate_country_code(country_code)
    if country_code is None:
        print("Invalid country code entered")
        return
    adjacent_countries = country_service.get_adjacent_country(country_code)
    if adjacent_countries is None:
        print("country code not present in database")
        return
    country_service.display_adjacent_country(adjacent_countries)

if __name__ == "__main__":
    main()