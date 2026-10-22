class Employee:
    # ii. Constructor
    def __init__(self, employee_id, name, basic_salary, overtime_hours):
        self.employee_id = employee_id
        self.name = name
        self.basic_salary = basic_salary
        self.overtime_hours = overtime_hours

    # iii. Gross Salary = Basic Salary + (Overtime Hours * 500)
    def calculate_gross_salary(self):
        return self.basic_salary + (self.overtime_hours * 500)

    # v. Tax = 10% of Gross Salary
    def calculate_tax(self):
        return self.calculate_gross_salary() * 0.10

    # iv. Net Salary = Gross Salary - Tax
    def calculate_net_salary(self):
        gross = self.calculate_gross_salary()
        tax = gross * 0.10
        return gross - tax

# vi. Create two employees
emp1 = Employee("1001", "Aurelia", 50000, 10)
emp2 = Employee("1002", "Samuel", 65000, 6)

# Display for Employee 1
print(f"--- Employee 1: {emp1.name} ({emp1.employee_id}) ---")
print(f"Gross Salary: KSh {emp1.calculate_gross_salary()}")
print(f"Tax (10%): KSh {emp1.calculate_tax()}")
print(f"Net Salary: KSh {emp1.calculate_net_salary()}\n")

# Display for Employee 2
print(f"--- Employee 2: {emp2.name} ({emp2.employee_id}) ---")
print(f"Gross Salary: KSh {emp2.calculate_gross_salary()}")
print(f"Tax (10%): KSh {emp2.calculate_tax()}")
print(f"Net Salary: KSh {emp2.calculate_net_salary()}")
