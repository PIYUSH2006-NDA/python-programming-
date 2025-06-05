# LIST, TUPLES IN PYTHON AND THEIR METHODS

# --- List Section ---
lst = ["piyush", "aakash", "mohan", "rohan"]

# Print each item in the list
for item in lst:
    print(item)

# Insert "kishor" at index 1
lst.insert(1, "kishor")
print(lst)

# Find index of "kishor"
k = lst.index("kishor")
print("Index of 'kishor':", k)

print("\n" * 3)  # Prints 3 newlines for separation


# --- Tuple Section ---
tup = ("piyush", "aakash", "mohan", "rohan")

# Print tuple elements
for name in tup:
    print(name)

# Convert tuple to list to make changes
litup = list(tup)

# Add a new element
litup.append("lokesh")

# Print updated list
print("Modified list:", litup)

# Get index of "aakash"
print("Index of 'aakash':", litup.index("aakash"))

# Get length of list
print("Length of list:", len(litup))
