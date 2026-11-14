from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, salary):
        
        self.__name = name
        self.__salary = salary

   
    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def display_info(self):
        print(f"Employee Name: {self.__name}")

   
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

   
    def calculate_salary(self):
        return self.get_salary()


class PartTimeEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

   
    def calculate_salary(self):
        return self.get_salary() * 0.5


emp1 = FullTimeEmployee("Aurelia Wambui", 350000)
emp2 = PartTimeEmployee("Lynn Wangari", 100000)


employees = [emp1, emp2]
for emp in employees:
    emp.display_info()
    print(f"Calculated Salary: {emp.calculate_salary()}")
    print("--------------------")
