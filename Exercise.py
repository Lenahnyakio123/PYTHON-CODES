# 1. Create empty list
names = []

# 2. Prompt user - input()
n = int(input("How many names do you want to enter? "))

for i in range(n):
    name = input(f"Enter name {i+1}: ")
    names.append(name)  # append()

# 3. Count total names entered
print(f"Total names entered: {len(names)}")

# 4. Remove duplicates and sort
# list = set(names)
unique_names = list(set(names))
unique_names.sort()  # sort()

# 5. Display final sorted list - print()
print("Final sorted list without duplicates:")
print(unique_names)
