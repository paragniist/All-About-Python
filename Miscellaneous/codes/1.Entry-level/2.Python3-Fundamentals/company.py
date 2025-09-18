from employee import employee

class Company:
    def __init__(self):
        self.employee = []
    def addEmployee(self,employee):
        self.employee.append(employee)
    def display(self):
        for emp in self.employee:
            print(emp.name)

def main():
    mycompany = Company()
    employee1 = employee('Bob Barber',20000)
    mycompany.addEmployee(employee1)
    employee2 = employee('James Bond', 50000)
    mycompany.addEmployee(employee2)
    employee3 = employee('Harry potter', 10000)
    mycompany.addEmployee(employee3)
    mycompany.display()

main()
