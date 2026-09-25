# Supermarket Purchase Program

# Ask the customer to enter information
customer_name = input("Enter customer name: ")
product_name = input("Enter product name: ")
quantity = int(input("Enter quantity purchased: "))
price = float(input("Enter price per item: "))

# Calculate the total cost
total_cost = quantity * price

# Display the purchase information using an f-string
print("\n--- Purchase Information ---")
print(f"Customer Name: {customer_name}")
print(f"Product Name: {product_name}")
print(f"Quantity: {quantity}")
print(f"Price per Item: {price:.3f}")
print(f"Total Cost: {total_cost:.3f}")
