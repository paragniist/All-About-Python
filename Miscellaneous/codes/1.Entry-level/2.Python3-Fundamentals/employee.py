

class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def calculate_paycheck(self):
        return self.salary - self.salary/52