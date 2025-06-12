# List and dictionary comprehensions
# List comprehension

#square = [x**2 for x in range(10)]
#print(square)



# Example four: List comprehension with condition
# numbers = [1, 2, 3, 4, 5]
# square_dict = {x: x**2 for x in numbers}
# print(square_dict)

# List comprehension with condition
# Must be even numbers
# even_square = [x**2 for x in range(10) if x % 2 == 0]
# print(even_square)

# Exercise 1: Real world example: 
# Exercise  three: Create an ATM withdrawal program - use if-else statement to check account balance before allowing withdrawal
# balance = 100000  

# withdraw = int(input("Enter amount to withdraw: "))

# if withdraw <= balance:
#     balance -= withdraw
#     print(f"Withdrawal successful! New balance: {balance}")
# else:
#     print("Insufficient balance.")

# Assignment 1: Create and inventory management - Use loops to disply or update a list of stock items
inventory = {"Sugar": 10, "Rice": 20, "Beans": 15}

for item, quantity in inventory.items():
    print(item, ":", quantity)

item = input("Enter item to update: ")
new_qty = int(input("Enter new quantity: "))

if item in inventory:
    inventory[item] = new_qty
    print(item, "updated to", new_qty)
else:
    print("Item not found.")
