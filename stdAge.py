try:
    age = int(input("Enter your age: "))
    print("Age successfully recorded")

except ValueError:
    print("Invalid age entered")
