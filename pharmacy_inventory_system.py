total_revenue = 0
restock_count = 0

num_medicines = int(input("How many different medicines need to be processed? "))

for i in range(num_medicines):
    print("\nMedicine", i + 1)
    
    name = input("Enter medicine name: ")
    stock = int(input("Enter available stock: "))
    price = float(input("Enter price per unit: "))
    qty_sold = int(input("Enter quantity sold: "))
    

    if qty_sold <= stock:
        sale_amount = qty_sold * price
        total_revenue = total_revenue + sale_amount
        
        remaining_stock = stock - qty_sold
        print("Sale successful. Amount: Rs.", sale_amount)
        print("Remaining stock:", remaining_stock)
    
        if remaining_stock < 10:
            print("Warning: Low stock for", name)
            restock_count = restock_count + 1
            
    else:
        print("Error: Not enough stock available.")
        
        if stock < 10:
            print("Warning: Low stock for", name)
            restock_count = restock_count + 1

print("\nFinal Report:")
print("Total medicines processed:", num_medicines)
print("Total revenue: Rs.", total_revenue)
print("Medicines requiring restocking:", restock_count)