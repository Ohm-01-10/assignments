import time
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
    def update(self,a,value):
        if a=="salary":
            self.salary=value
            print("Updating... Salary")
            self.display()
        elif a=="name":
            self.name=value
            print("Updating... Name ")
            self.display()

    def delete(self):
        print("Deleting Employee",self.name)
        del self
        time.sleep(1)
        print("Employee Details Deleted")




# Adding all employee details
employee1=employees("Mehak",40000)
employee2=employees("Ashok",50000)
employee3=employees("Viren",60000)
# Displaying all details
employee1.display()
employee2.display()
employee3.display()

# Updating Salary
employee2.update("salary",70000)
# Deleting employee3 details
employee3.delete()