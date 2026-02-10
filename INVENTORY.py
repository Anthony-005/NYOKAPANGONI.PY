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

