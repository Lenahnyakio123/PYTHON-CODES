try:
    file = open("employees.txt", "r")
    content = file.read()
    print(content)
    file.close()

except FileNotFoundError:
    print("The employee file was not found.")

finally:
    print("File processing completed.")
