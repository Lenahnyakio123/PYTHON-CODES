def calculate_grade(mark):
    # iii. Check grading criteria and iv. Return grade
    if 70 <= mark <= 100:
        return "A"
    elif 60 <= mark <= 69:
        return "B"
    elif 50 <= mark <= 59:
        return "C"
    elif 40 <= mark <= 49:
        return "D"
    elif 0 <= mark < 40:
        return "F"
    else:
        return "Invalid mark! Enter 0 - 100"

# v. Ask user to enter mark
try:
    student_mark = float(input("Enter student's mark: "))

    # vi. Call function and display grade
    grade = calculate_grade(student_mark)
    print(f"Grade: {grade}")

except ValueError:
    print("Please enter a valid number.")