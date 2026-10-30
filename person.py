class Person:
    def __init__(self, person_id, name, age):
        self.person_id = person_id
        self.name = name
        self.age = age

    def display_details(self):
        print(f"Person ID: {self.person_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self, person_id, name, age, course, marks):
        super().__init__(person_id, name, age)
        self.course = course
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 70:
            return "Grade A"
        elif self.marks >= 60:
            return "Grade B"
        elif self.marks >= 50:
            return "Grade C"
        else:
            return "Grade D"

    def display_details(self):
        super().display_details()
        print(f"Course: {self.course}")
        print(f"Marks: {self.marks}")

class Lecturer(Person):
    def __init__(self, person_id, name, age, department, monthly_salary):
        super().__init__(person_id, name, age)
        self.department = department
        self.monthly_salary = monthly_salary

    def calculate_annual_salary(self):
        return self.monthly_salary * 12

    def display_details(self):
        super().display_details()
        print(f"Department: {self.department}")
        print(f"Monthly Salary: {self.monthly_salary}")

student1 = Student(101, "Alice", 20, "BBIT", 75)
lecturer1 = Lecturer(201, "Dr. Brian", 45, "Computing", 120000)

print("--- Student Details ---")
student1.display_details()
print(f"Final Grade: {student1.calculate_grade()}")

print("\n--- Lecturer Details ---")
lecturer1.display_details()
print(f"Annual Salary: KSh {lecturer1.calculate_annual_salary()}")
