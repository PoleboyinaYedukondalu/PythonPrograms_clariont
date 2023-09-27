product_database = {
    '100': {'Name': 'chocolates', 'Price': 10.0, 'Quantity': 20},
    '108': {'Name': 'ice-creams', 'Price': 35.0, 'Quantity': 15},
    '102': {'Name': 'biscuits', 'Price': 15.0, 'Quantity': 15},
    '105': {'Name': 'Sprite', 'Price': 20.0, 'Quantity': 15},
}

def save_product_list():
    with open('d:\\Files\\product_list.txt', 'w+') as product_list_file:
        for product_id, details in product_database.items():
            product_list_file.write(f"Product ID: {product_id}, Name: {details['Name']}, Price: ${details['Price']:.2f}, Quantity: {details['Quantity']}\n")

def save_bill(customer_name, receipt, total_cost):
    with open('d:\\Files\\bill.txt', 'a+') as bill_file:
        bill_file.write(f"Customer Name: {customer_name}\n")
        bill_file.write("Product Name\tQuantity\tPrice\tTotal\n")
        for product_id, quantity in receipt.items():
            if product_id in product_database:
                details = product_database[product_id]
                price = details['Price']
                total = price * quantity
                bill_file.write(f"{details['Name']}\t\t{quantity}\t\t${price:.2f}\t${total:.2f}\n")
            else:
                bill_file.write(f"Product ID {product_id} (Product not found)\n")
        bill_file.write(f"Total Cost: ${total_cost:.2f}\n")
        bill_file.write("\n")

def save_product_database():
    with open('d:\\Files\\product_database.txt', 'w+') as product_database_file:
        for product_id, details in product_database.items():
            product_database_file.write(f"{product_id} {details['Name']} {details['Price']} {details['Quantity']}\n")

def load_product_database():
    try:
        with open('d:\\Files\\product_database.txt', 'r+') as product_database_file:
            lines = product_database_file.readlines()
            for line in lines:
                parts = line.split()
                product_id = parts[0]
                product_name = parts[1]
                product_price = float(parts[2])
                product_quantity = int(parts[3])
                product_database[product_id] = {'Name': product_name, 'Price': product_price, 'Quantity': product_quantity}
    except FileNotFoundError:
        pass

# Load product database from the file (if available)
load_product_database()

def display_product_list():
    print("Product List:")
    for product_id, details in product_database.items():
        print(f"Product ID: {product_id}, Name: {details['Name']}, Price: ${details['Price']:.2f}, Quantity: {details['Quantity']}")

def generate_bill(receipt, customer_name):
    total_cost = 0.0
    print("\nBill:")
    print("Customer Name:", customer_name)
    print("Product Name\tQuantity\tPrice\tTotal")
    for product_id, quantity in receipt.items():
        if product_id in product_database:
            details = product_database[product_id]
            price = details['Price']
            total = price * quantity
            total_cost += total
            print(f"{details['Name']}\t\t{quantity}\t\t${price:.2f}\t${total:.2f}")
            product_database[product_id]['Quantity'] -= quantity
        else:
            print(f"Product ID {product_id} (Product not found)")
    print("Total Cost: ${:.2f}".format(total_cost))
    save_bill(customer_name, receipt, total_cost)
    save_product_database()

def add_product_to_database(product_id, product_name, price, quantity):
    if product_id in product_database:
        print("Product ID already exists. Use 'Update Product Details' to modify existing products.")
    else:
        product_database[product_id] = {'Name': product_name, 'Price': price, 'Quantity': quantity}
        print(f"Product {product_name} added successfully.")
        save_product_list()
        save_product_database()

def purchase_products():
    customer_name = input("Enter your name: ")
    receipt = {}
    
    while True:
        product_id = input("Enter product ID (or 'done' to finish): ")
        if product_id.lower() == 'done':
            break
        
        if product_id in product_database:
            details = product_database[product_id]
            price = details['Price']
            available_quantity = details['Quantity']
            
            quantity = int(input(f"Enter quantity for {details['Name']} (Available: {available_quantity}): "))
            
            if quantity <= available_quantity:
                if product_id in receipt:
                    receipt[product_id] += quantity
                else:
                    receipt[product_id] = quantity
                product_database[product_id]['Quantity'] -= quantity
            else:
                print("Not enough stock available.")
        else:
            print("Product not found.")
    
    total_cost = generate_bill(receipt, customer_name)

def update_product_details():
    product_id = input("Enter product ID to update: ")
    if product_id in product_database:
        new_quantity = int(input("Enter new quantity: "))
        new_price = float(input("Enter new price: $"))
        product_database[product_id]['Quantity'] = new_quantity
        product_database[product_id]['Price'] = new_price
        print(f"{product_database[product_id]['Name']} updated successfully.")
        save_product_list()
        save_product_database()
    else:
        print("Product not found.")

def main():
    while True:
        print("\nOptions:")
        print("1. Display Product List")
        print("2. Purchase Products")
        print("3. Update Product Details")
        print("4. Add New Product")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_product_list()
        elif choice == '2':
            purchase_products()
        elif choice == '3':
            update_product_details()
        elif choice == '4':
            product_id = input("Enter product ID: ")
            product_name = input("Enter product name: ")
            price = float(input("Enter product price: $"))
            quantity = int(input("Enter product quantity: "))
            add_product_to_database(product_id, product_name, price, quantity)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

