This program records and displays employee information.
It also demonstrates the use of Boolean values and
conversion of a number to a string using str().
"""

# Create and assign employee variables
employee_name = "John Kamau"
employee_age = 30
employee_salary = 45000.50
employee_active = True

# Display employee information using f-string formatting
print("--- Employee Information ---")
print(f"Employee Name: {employee_name}")
print(f"Employee Age: {employee_age}")
print(f"Employee Salary: {employee_salary:.2f}")
print(f"Employee Active: {employee_active}")

# Convert a number to a string before concatenating
age_text = str(employee_age)
message = "Employee age is " + age_text

print(message)
