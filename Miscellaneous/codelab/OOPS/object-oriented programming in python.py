from abc import ABC, abstractmethod


class AbstractEmployee(ABC):
    company_name = "Pluralsight"

    def __init__(self, name, employee_id, email):
        self.name = name
        self.employee_id = employee_id
        self.email = email

    def get_contact_info(self):
        return f"{self.name} ({self.company_name}) can be reached at {self.email}"

    @abstractmethod
    def get_role_description(self):
        pass


class Employee(AbstractEmployee):
    def get_role_description(self):
        return "General employee"


class FullTimeEmployee(AbstractEmployee):
    def __init__(self, name, employee_id, email, salary):
        super().__init__(name, employee_id, email)
        self.salary = salary

    def is_high_earner(self):
        return self.salary >= 100000

    def get_role_description(self):
        return "Full-time employee"


class Intern(AbstractEmployee):
    def __init__(self, name, employee_id, email, school):
        super().__init__(name, employee_id, email)
        self.school = school

    def get_contact_info(self):
        return f"{self.name} (from {self.school} at {self.company_name}) can be reached at {self.email}"

    def get_role_description(self):
        return f"Intern from {self.school}"


employees = [
    Employee("Alice", 101, "alice@example.com"),
    FullTimeEmployee("Bob", 102, "bob@example.com", 105000),
    Intern("Charlie", 103, "charlie@example.com", "State University")
]

for emp in employees:
    print(emp.get_contact_info())

for emp in employees:
    if isinstance(emp, FullTimeEmployee):
        if emp.is_high_earner():
            print(f"{emp.name} is a high earner.")
        else:
            print(f"{emp.name} is not a high earner.")
    else:
        print(f"{emp.name} does not have a salary attribute.")
