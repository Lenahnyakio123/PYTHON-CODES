class Employee:
    # i. Parent class with name and ID
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    # ii. displayEmployee() method
    def displayEmployee(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")

class Lecturer(Employee):
    # iii. Child class inheriting from Employee
    def __init__(self, name, emp_id, subject):
        super().__init__(name, emp_id)
        # iv. Teaching subject attribute
        self.subject = subject

    # v. displayLecturer() method
    def displayLecturer(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Teaching Subject: {self.subject}")

# vi. Main section
if __name__ == "__main__":
    # Create a Lecturer object and assign details
    lecturer1 = Lecturer("Dr. John Doe", "LEC001", "Object Oriented Programming")
    
    # Display all information
    lecturer1.displayLecturer()
    
    # Alternative: You can also use the parent method
    # print("\nUsing parent method:")
    # lecturer1.displayEmployee()
