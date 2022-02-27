class employees:
    company="XYZ"

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary


    def display(self):
        print("Employees of", employees.company,"company")
        print("Employee Name:",self.name)
        print("Employee Salary:",self.salary)
        print()

employee1=employees("alpha",70000)
employee2=employees("beta",60000)
employee1.display()
employee2.display()

