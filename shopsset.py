# Create a set containing product categories
# Duplicate categories are automatically removed by the set
categories = {
    "Electronics",
    "Clothing",
    "Shoes",
    "Books",
    "Electronics",
    "Furniture",
    "Books"
}

# Display the original set
print("Original categories:", categories)

# Add a new product category
categories.add("Beauty")

# Remove one category
categories.remove("Furniture")

# Display the final set
print("Final categories:", categories)

# Explain how a set helps maintain unique categories
print("A set automatically removes duplicate values, so each product category")
print("appears only once. This helps the company maintain a list of unique categories.")