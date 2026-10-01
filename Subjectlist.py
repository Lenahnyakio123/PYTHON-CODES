# Create a list containing marks for five subjects
marks = [75, 68, 82, 60, 90]

# Display all marks
print("Marks:", marks)

# Calculate and display total marks
total = sum(marks)
print("Total marks:", total)

# Calculate and display average mark
average = total / len(marks)
print("Average mark:", average)

# Display the highest mark
print("Highest mark:", max(marks))

# Display the lowest mark
print("Lowest mark:", min(marks))

# Modify the mark of the third subject
marks[2] = 88

# Display the updated list
print("Updated marks:", marks)
