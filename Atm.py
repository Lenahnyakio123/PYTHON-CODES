try:
    amount = input("Enter the withdrawal amount: ")

    amount = int(amount)

    print("Withdrawal amount:", amount)

except ValueError:
    print("Invalid amount. Please enter a number.")
