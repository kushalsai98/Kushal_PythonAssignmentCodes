customer_name=input("Enter Customer name : ")
product_name=input("Enter Product name : ")
qty=int(input("Enter Quantity : "))
item_price=float(input("Enter Item Price : "))

total_price=qty*item_price

if total_price>1000:
    discount=total_price*0.1
else:
    discount=0

final_price=total_price-discount

print("==============BILL==============")
print("Customer Name : ",customer_name)
print("Product Name : ",product_name)
print("Quantity : ",qty)
print("Item Price : ",item_price)
print("\n")
print("Total Price : ",total_price)
print("Discount : ",discount)
print("Final Price : ",final_price)
print("================================")