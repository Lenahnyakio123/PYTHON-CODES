# i. Define function
def convert_temperature(celsius):
    # ii. Accept Celsius as parameter
    # iii. Convert using formula
    fahrenheit = (celsius * 9/5) + 32
    # iv. Return Fahrenheit
    return fahrenheit

# v. Ask user to enter temperature in Celsius
try:
    celsius_temp = float(input("Enter temperature in Celsius: "))

    # vi. Call function
    fahrenheit_temp = convert_temperature(celsius_temp)

    # Display to two decimal places
    print(f"{celsius_temp}°C is equal to {fahrenheit_temp:.2f}°F")

except ValueError:
    print("Please enter a valid number.")
