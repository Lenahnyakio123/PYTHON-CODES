def calculate_bill(units_consumed, cost_per_unit):
    # iii. Calculate bill
    bill = units_consumed * cost_per_unit
    # iv. Return bill
    return bill

# v. Ask user to enter values
try:
    units = float(input("Enter units consumed: "))
    cost = float(input("Enter cost per unit: "))

    # vi. Call the function
    total_bill = calculate_bill(units, cost)

    # vii. Display the bill
    print(f"\nCalculated Electricity Bill: {total_bill}")

except ValueError:
    print("Please enter valid numbers only.")
