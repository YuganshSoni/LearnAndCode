from pydantic import BaseModel

class Customer(BaseModel):
    id: str
    name: str
    country: str
    company: str
    contact_person: str

class CustomerSearch:
    def search_by_country_name(self, country : str)->list[Customer]:
        query = "db query to search customer"
        result = "query result after execution"
        return result
    
    def search_by_company_name(self, company : str)->list[Customer]:
        query = "db query to search customer"
        result = "query result after execution"
        return result
    
    def search_by_contact_person(self, contact_person: str)->list[Customer]:
        query = "db query to search customer"
        result = "query result after execution"
        return result
    
class Export:
    def export_to_csv(customers : list[Customer]):
        pass