<<<<<<< HEAD
inventory={
    "steel sheets":"40 pieces",
    "steel wire":"100 metres",
    "wood":"400 pieces",
    "paint":"10 litres",
    "Trucks":"20 trucks"
    }
print(inventory)
print(inventory.values())
inventory.update({ "paint":"20 litres","wood":"450 pieces"})
print(inventory)
item = input("Enter item name: ")

if item in inventory:
    print(inventory[item])
else:
    print("Item not found")
total = 0

for value in inventory.values():
    number = value.split()[0]   # takes "40" from "40 pieces"
    total += int(number)

print("Total items:", total)

=======
inventory = {}

def add_item():
    name = input("Enter item name: ").lower()
    quantity = int(input(f"Enter quantity for {name}: "))
    
    # If item exists, update quantity; else , create it
    if name in inventory:
        inventory[name] += quantity
    else:
        inventory[name] = quantity
    print(f"Updated {name}. Current stock: {inventory[name]}")

def get_item():
    name = input("Enter the item name to search: ").lower()
    # Retrieve information using the name as a key
    if name in inventory:
        print(f"Item: {name} | Quantity: {inventory[name]}")
    else:
        print("Item not found in inventory.")

def show_total():
    # Calculate total quantity of all items
    total = sum(inventory.values())
    print(f"Total quantity of all items in inventory: {total}")

# Quick test of the logic
add_item()
add_item()
get_item()
show_total()
>>>>>>> 0ba877a7ad2061c7355147583688355604213dba
