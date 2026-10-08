# i. Create a dictionary named student
student = {
    "registration_number": "BIT/001/2026",
    "student_name": "Lenah Kangangi",
    "course": "Bachelor of Science in Information Technology",
    "year_of_study": 3
}

# ii. Display the student's name and course
print("Student Name:", student["student_name"])
print("Course:", student["course"])

# iii. Change the student's year of study
student["year_of_study"] = 3

# iv. Add an email address
student["email"] = "lenah@gmail.com"

# v. Display the complete updated dictionary
print("\nUpdated Student Dictionary:")
print(student)
