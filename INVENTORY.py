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
