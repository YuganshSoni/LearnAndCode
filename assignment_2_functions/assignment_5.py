"""
A. Violation of the Single Responsibility Principle (SRP)
    The class is responsible for too many unrelated tasks:
1.Holding employee data.
2.Performing database operations.
3.Generating reports in multiple formats.
4.Executing business rules such as employee termination.

This does not follow SRP as it gives many reasons to change. Because they are all combined in one class, any change in one area forces changes to the same class, which violates SRP.

B. Violation of the Open/Closed Principle (OCP)
The class must be modified whenever a new change needs to occur in any functionality.
This means the class is not closed for modification, making extensions risky and error-prone.

C. Poor Naming Practices
Some method names are:
Inconsistent in style
Overly long and hard to read
Incorrectly formatted (for example, improper capitalization)
Poor naming reduces readability and makes the code harder to understand and maintain.
improved function names : 
a. save_employee()
b. print_employee_details_xml()
c. print_employee_details_csv()
d. terminate_employee()
e. is_working()

D. Tight Coupling and Low Testability
The class directly depends on:
Database logic
Specific output formats like XML and CSV

As a result:
The class cannot be easily tested in isolation
Changes in one dependency can break unrelated functionality
"""

class Employee:
    id : int
    name : str
    department : str
    working : bool

    def save_employee():
        pass
    def export_employee_details_to_xml():
        pass
    def export_employee_details_to_csv():
        pass
    def terminate_employee():
        pass
    def is_working()->bool:
        pass