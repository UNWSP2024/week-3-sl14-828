# There are two kinds of hot dogs sold:
# Hot Dog ($3.50), Chili Dog ($4.50).
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).
# Also tax is 7%.
# Write a program the inputs the type of hot dog wanted and optional toppings.
# The program then displays the hot dog cost, tax and total cost.

# Hot dog prices
hot_dog_price = 3.50
chili_dog_price = 4.50
cheese_price = 0.50
peppers_price = 0.75
onions_price = 1.00

# Tax rate
tax_rate = 0.07

# prompt
hot_dog_type = input("Enter the type of hot dog (Hot Dog/Chili Dog): ")

# cost calculation without addons
if hot_dog_type == "Hot Dog":
    hot_dog_cost = hot_dog_price
elif hot_dog_type == "Chili Dog":
    hot_dog_cost = chili_dog_price
else:
    print("Invalid hot dog type selected.")
    hot_dog_cost = 0.0

# additionals to total
cheese = input("Do you want cheese? (yes/no): ")
peppers = input("Do you want peppers? (yes/no): ")
onions = input("Do you want grilled onions? (yes/no): ")

# Topping cost calculation
topping_cost = 0.0

if cheese == "yes":
    topping_cost += cheese_price
if peppers == "yes":
    topping_cost += peppers_price
if onions == "yes":
    topping_cost += onions_price

# Total cost calculation
subtotal = hot_dog_cost + topping_cost
tax = subtotal * tax_rate
total_cost = subtotal + tax

# Display the costs
print("\nReceipt:")
print("\nHotdog cost:", hot_dog_cost)
print("\nToppings cost:", topping_cost)
print("\nSubtotal:", subtotal)
print("\nTax:", tax)
print("\nTotal:", total_cost)
