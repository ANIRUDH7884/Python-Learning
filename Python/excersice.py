# 🏪 Project 2 — Electronics Store Sales System
# (Product Name, Price, Quantity Sold)

products = [
    ("Laptop", 55000, 2),
    ("Mobile", 20000, 3),
    ("Headphones", 2000, 5),
    ("Keyboard", 1500, 4),
    ("Monitor", 12000, 2),
    ("Mouse", 700, 6)
]

# ✅ 1. Print Bill Items and total revenew
print("====================== BILL ================================")

total_revenew = 0
for name,price,quantity in products :
     total_price = price * quantity
     total_revenew = total_revenew + total_price
     print(name, price , 'x', quantity, '=  '  "₹",total_price)
     
#find highest and lowest seling product

highest_name = ""
highest_value = 0

lowest_name = ""
lowest_value = 99999 

for name,price,quantity in products :
     total_value = price * quantity
     if total_value > highest_value :
          highest_value = total_value
          highest_name = name

     if total_value < lowest_value :
        lowest_value = total_value
        lowest_name = name

# Count Products
premium = 0
normal = 0

for name, price, quantity in products :
      total = price * quantity
      if total >= 20000 :
           premium = premium + 1
      elif total < 20000 :
           normal = normal + 1

# 💸 Discount + GST
total_revenue = 0

for name,price,quantity in products :
     total_revenew = total_revenew + (price*quantity)

     if total_revenew >= 200000 :
          discount = total_revenew * 0.25
     elif total_revenew >= 100000 :
          discount = total_revenew * 0.15
     else:
          discount = 0

after_discount = total_revenew - discount

gst = after_discount * 0.18

final_bill = after_discount + gst

print("============================================================")
print("Total Revenew : ", total_revenew)
print("Discount : ", discount )
print("GST : ",gst)
print("Total Bill : ",final_bill)

print("Highest selling product : ", highest_name,highest_value)
print("Lowest selling profuct : ", lowest_name,lowest_value)

print("premium Products : ", premium)
print("Normal Products : ", normal)

print("============================================================")