from dataclasses import dataclass
from typing import List, Iterable
from pathlib import Path
import csv
import io

@dataclass(frozen=True)
class Customer:
    customer_id: str
    company_name: str
    contact_name: str
    country: str

@dataclass(frozen=True)
class SearchCriteria:
    country: str | None = None
    company_name: str | None = None
    contact_name: str | None = None

class CustomerService:
    def __init__(self, customers: List[Customer]):
        self._customers = customers

    def search(self, criteria: SearchCriteria) -> List[Customer]:
        search_result: Iterable[Customer] = self._customers

        if criteria.country:
            value = criteria.country.lower()
            search_result = (customer for customer in search_result if value in customer.country.lower())

        if criteria.company_name:
            value = criteria.company_name.lower()
            search_result = (customer for customer in search_result if value in customer.company_name.lower())

        if criteria.contact_name:
            value = criteria.contact_name.lower()
            search_result = (customer for customer in search_result if value in customer.contact_name.lower())

        return sorted(search_result, key=lambda customer: customer.customer_id)

class CustomerCsvExporter:
    FILE_HEADERS = ["customer_id", "company_name", "contact_name", "country"]
    FILE_NAME="customer_details.csv"

    @classmethod
    def save_content_to_csv_file(cls, csv_file, file_exists : bool):
        with csv_file.open(mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(CustomerCsvExporter.FILE_HEADERS)

            for customer in customers:
                writer.writerow([
                    customer.customer_id,
                    customer.company_name,
                    customer.contact_name,
                    customer.country
                ])

    @classmethod
    def export(cls, customers: List[Customer]) -> str:
        csv_file = Path(cls.FILE_NAME)
        file_exists = csv_file.exists()
        cls.save_content_to_csv_file(csv_file, file_exists)

customers = [
    Customer("Customer_1", "ITT Pvt Limited", "Eric", "USA"),
    Customer("Customer_2", "ITT pvt", "John", "France"),
]

search_service = CustomerService(customers)
criteria = SearchCriteria(country="USA")
results = search_service.search(criteria)
csv_data = CustomerCsvExporter.export(results)
