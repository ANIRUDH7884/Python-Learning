# 🛒 Python Project — Mobile Store Inventory
# Scenario

# You've joined a small mobile store as a trainee Python developer.
# The owner currently keeps product information manually and wants a basic Python program to manage today's inventory.
# Your task is to build the first version of the system.
# Important: No loops, functions, classes, database, input(), or concepts you haven't learned yet.
# Mobile Store Inventory System
# Task 1 — Store Information
# Create a tuple containing:

# Store Name
# Location
# Phone Number

# Print the store name and location individually using indexing.

store_name = "TechZone Mobiles"

store_details = ('TechZone Mobiles' , 'Kochi' , 62317826790)
store = store_details[0]
location = store_details[1]
print("Store Name : ", store)
print("Store Location : ", location)

# Task 2 — Product Inventory

# Create a list containing these products:

# Samsung S25
# iPhone 16
# OnePlus 13
# Vivo X200
# Oppo Find X8

# Then:

# Print the entire inventory.
# Print the first product.
# Print the last product.
# Print the number of products.

mobiles = ["Samsung s25" , "iphone 16", "oneplus 13", "Vivo x200", "Oppo find x8"]
print(mobiles)
print(mobiles[0])
print(mobiles[-1])
print(len(mobiles))

# Task 3 — New Stock Arrives

# These phones arrive:
# Google Pixel 10
# Nothing Phone 3
# Add them to your inventory.
# Then insert:
# Samsung A56
# at index 2.
# Print the updated inventory.

mobiles.append("Google Pixel 10")
mobiles.append("Nothing Phone 3")
mobiles.insert(2 , "Samsung A56")
print(mobiles)

# Task 4 — Product Sold Out
# Vivo X200 is sold out.
# Remove it from inventory and print the updated inventory.

mobiles.remove("Vivo x200")
print("Updated Inventory : " ,mobiles)

# Task 5 — Product Details

# Create a dictionary for:
# Product: OnePlus 13
# Brand: OnePlus
# Price: 69999
# Stock: 7
# Color: Black

# Then display:

# Product Name : OnePlus 13
# Price        : 69999
# Stock        : 7

# Access those values from the dictionary—don't manually print the values again.

smartPhone = {
  "Product" : "Oneplus 13",
  "Brand" : "Oneplus",
  "price" : 69999,
  "stock" : 7,
  "color" : "Black"
}

product_name = smartPhone.get("Product")
product_price = smartPhone.get("price")
product_stock = smartPhone.get("stock")

print("Product Name :" , product_name)
print("Product Price :" ,product_price)
print("Stock Remaining :" ,product_stock)

# Task 6 — Price Change

# The OnePlus 13 price changes from:
# 69999 → 64999
# Update the dictionary.
# Then add a new key:
# "offer": "10% Discount"
# Print the complete dictionary.

smartPhone["price"] = 64999
smartPhone.update({"Offer" : "10% Discount"})
print(smartPhone)

# Task 7 — Stock Update
# Two OnePlus 13 phones were sold.
# Change the stock:
# 7 → 5
# Then check:
# Is "stock" present in the dictionary?
# If yes:
# Stock information available
# Otherwise:
# Stock information unavailable

smartPhone["stock"] = 5

if "stock" in smartPhone :
    print("Stock Information Available")
else:
    print("Stock information unavailable")

# Task 8 — Available Brands
# The store currently has these brands:

# Samsung
# Apple
# OnePlus
# Vivo
# Samsung
# Apple
# Oppo
# OnePlus

# Create a set so duplicate brands are automatically removed.
# Then add:
# Google
# Nothing
# Remove:
# Vivo

# Print the final set.

Available_Brand = {"Samsung", "Apple", "Oneplus", "Vivo", "Samsung", "Apple", "Oneplus", "Oppo" "Vivo" }
Available_Brand.add("Google")
Available_Brand.add("Nothing")
Available_Brand.remove("Vivo")
print(Available_Brand)

# Task 9 — Price Analysis
# Use this list:
# prices = [74999, 79999, 64999, 45999, 54999]
# Your program should determine:
# Highest Price
# Lowest Price
# Total Value
# Number of Prices
# Use the Python functions you've learned rather than calculating them manually.

prices = [74999, 79999, 64999, 45999, 54999]
Highest = max(prices)
Lowest = min(prices)
Total = sum(prices)
Number = len(prices)

print("Highest Price" , Highest)
print("Lowest Price" , Lowest)
print("Total Price", Total)
print("Number Of Prices", Number)

# Task 10 — Featured Products
# From your final inventory list, display only the first 3 products using slicing.
# Then create a reversed version of the inventory and print it.

print(mobiles[ : 3])
mobiles.reverse()
print(mobiles)