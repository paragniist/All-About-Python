class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

# __str__ = Defines how the object is displayed when you print it:
    def __str__(self):
        return f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of ${self.salary}"

# __repr__ = This is the developer-friendly string representation (used in debugging or REPLs):
    def __repr__(self):
        return (
            f"Employee("
            f"{repr(self.name)}, {repr(self.age)}, "
            f"{repr(self.position)}, {repr(self.salary)})"
        )

# __add__ = This overloads the + operator to define how two employees combine.
    def __add__(self, other_employee):
        # E.g. combines their age and returns a new Employee
        return Employee("Mateo", self.age + other_employee.age, "Web developer", 2000)


employee1 = Employee("Ji-Soo", 38, "developer", 1200)
employee2 = Employee("Lauren", 44, "tester", 1000)
# employee1.__class__
# employee1.__dict__

employee3 = employee1.__add__(employee2)
employee3 = employee1 + employee2
print(str(employee3))
print(repr(employee3))