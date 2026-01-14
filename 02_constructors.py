# constructor is start with __
# whenever we write init it means constructor
# # constructor is initialize an object.

# class Employee:
#     def __init__(self,salary,name,bond):
#        self.salary=salary #create a instance attribute of name salary and assign it with salary..
#        self.name=name
#        self.bond=bond

#     def get_salary(self):
#         return self.name
    
#     def get_info(self):
#         print(f"The nem of the employee is {self.name}. salary of the employee is {self.salary}.And the of the employee with company is {self.bond}...")

# e1=Employee(34000,"yash patil",4)
# print(e1.get_salary())
# e1.get_info()

class employee:
    def __init__(self,roll,present):
        self.roll=roll
        self.present=present
    def get_ready(self):
        return self.present
    def get_info(self):
        print(f"The roll no of the student is {self.roll}.and he today {self.present}..")
e1=employee(21,"present")
print(e1.get_ready())
e1.get_info()