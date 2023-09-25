customer_name = str(input("Enter customer name: "))
customer_number = int(input("Enter customer number: "))

def Customer_details():
    product_prices = [10, 20, 30, 40, 50]
    selected_products = []
    total_bill = 0
      
    while True:
        print("Select your products and quantity:")
        print("1. Product 1")
        print("2. Product 2")
        print("3. Product 3")
        print("4. Product 4")
        print("5. Product 5")
        print("6. Finish and calculate total bill") 
        
        choose = input("Select the product: ")

        if choose == "1":
            quantity = int(input("Enter product Quantity in 1 kgs: "))
            if quantity >= 0:
                selected_products.append(("Product 1", quantity * product_prices[0]))
        elif choose == "2":
            quantity = int(input("Enter product Quantity in 1 kgs: "))
            if quantity >= 0:
                selected_products.append(("Product 2", quantity * product_prices[1]))
        elif choose == "3":
            quantity = int(input("Enter product Quantity in 1 kgs: "))
            if quantity >= 0:
                selected_products.append(("Product 3", quantity * product_prices[2]))
        elif choose == "4":
            quantity = int(input("Enter product Quantity in 1 kgs: "))
            if quantity >= 0:
                selected_products.append(("Product 4", quantity * product_prices[3]))
        elif choose == "5":
            quantity = int(input("Enter product Quantity in 1 kgs: "))
            if quantity >= 0:
                selected_products.append(("Product 5", quantity * product_prices[4]))
        elif choose == "6":
            break
        else:
            print("Invalid choice. Please try again.")
    
    total_bill = sum(item[1] for item in selected_products)
    
    bill_details = f"Customer name: {customer_name}\n" \
                   f"Customer number: {customer_number}\n"

    for product, price in selected_products:
        bill_details += f"{product}: {price}\n"

    bill_details += f"Total bill: {total_bill}\n"

    # Open a file with append and read mode (a+)
    with open("d:\\Files\\task2.txt", "w+") as file:
        file.write(bill_details)
    
    print("Bill generated successfully!")

def iterator():
    while True:
        print("Choose your option:")
        print("1. Calculate bill")
        print("2. Exit")
        
        choose = input("Enter your choice: ")

        if choose == "1":
            Customer_details()
        elif choose == "2":
            break
        else:
            print("Invalid choice. Please try again.")

# Calling the iterator function
iterator()
