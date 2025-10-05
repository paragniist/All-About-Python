class Employee:
    def __init__(self,name,age,position,salary):
        self.name = name
        self.age = age
        self.position =position
        self.salary = salary


    def increase_salary(self,x):
        self.salary+= self.salary*(x/100)

    def info(self):
         print(f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of ${self.salary}")


e1 = Employee("Ji-Soo", 38, "developer", 1200)
e2 = Employee("Lauren", 44, "tester", 1000)
e3 = Employee("Mateo", 45, "scientist", 2100)

e1.increase_salary(20)
e3.increase_salary(30)
employee = [e1,e2,e3]
for e in employee:
    e.info()