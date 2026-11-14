try:
    age = input("Enter your age: ")

    age = int(age)

    print("Age successfully recorded")

except ValueError:
    print("Invalid age entered")
