class Employee:
    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary

    def display_info(self):
        print(f"The employee name is {self.__name}")
    
    def calculate_salary(self):
        return self.__salary


class FullTimeEmployee(Employee):
    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary
        
    def display_info(self):
        print(f"The employee name is {self.__name}")
    
    def calculate_salary(self):
        return self.__salary

class PartTimeEmployee(Employee):
    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary

    def display_info(self):
        print(f"The employee name is {self.__name}")
        
    def calculate_salary(self):
        return self.__salary * 0.5

# Create objects
ft_emp = FullTimeEmployee("FEL", 100000)
pt_emp = PartTimeEmployee("Justin", 190000)

#  Store them in a list
employees = [ft_emp, pt_emp]

#  Loop through and call methods
for emp in employees:
    emp.display_info()
    print("Calculated salary:", emp.calculate_salary())
    print("-----")

myEMP=Employee("Anthony",200000)
myEMP.display_info()
print(myEMP.calculate_salary())

ft_emp=FullTimeEmployee("FEL",100000)
ft_emp.display_info()
print(ft_emp.calculate_salary())

pt_emp= PartTimeEmployee("Justin",190000)
pt_emp.display_info()
print(pt_emp.calculate_salary())


    
