# 1. Prompt the user to enter names (comma separated)
raw_input = input("Enter a list of names separated by commas: ")

# 2. Convert the string into a list and clean up whitespace
names_list = [name.strip() for name in raw_input.split(",")]

# 3. Remove duplicates by converting to a set, then back to a list
unique_names = list(set(names_list))

# 4. Sort the names alphabetically
unique_names.sort()

# 5. Display the results
print("\nFinal Sorted List:", unique_names)
print("Total number of names entered:", len(names_list))
