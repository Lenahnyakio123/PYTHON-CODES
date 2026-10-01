# Create a tuple containing customer information
customer = ("John Kamau", "C001", "0712345678", "john@example.com")

# Display the complete tuple
print("Customer Information:", customer)

# Access and display the customer's name and telephone number
print("Customer Name:", customer[0])
print("Telephone Number:", customer[2])

# Display the number of items in the tuple
print("Number of items:", len(customer))

# Attempt to modify the customer's telephone number
try:
    customer[2] = "0798765432"
except TypeError:
    print("Error: The telephone number cannot be modified.")

# State why the modification cannot be performed
print("Reason: Tuples are immutable and cannot be changed after creation.")
