name = input("Enter Your Name:")
# Lists of items
lists = '''
Rice        Rs 70/kg
Sugar       Rs 50/kg
Salt        Rs 20/kg
Oil         Rs 120/kg
Panner      Rs 200/kg
Milmaker    Rs 300/kg
Badam       Rs 800/kg
Grapes      Rs 500/kg
Maggi       Rs 100/each
Colgate     Rs 80/each
'''

# Declaration
price = 0
pricelist = []
totalprice = 0
finalamount = 0
ilist = []
qlist = []
plist = []

# Rates for items
items = {
    'Rice': 70, 'Sugar': 50, 'Salt': 20, 'Oil': 120,
    'Panner': 200, 'Milmaker': 300, 'Badam': 800, 'Grapes': 500, 'Maggi': 100, 'Colgate': 80
}

option = int(input("For a list of items, press 5: "))
if option == 5:
    print(lists)

while True:
    inp1 = int(input("If you want to buy, press 5, or 3 to exit: "))
    if inp1 == 3:
        break
    elif inp1 == 5:
        item = input("Enter your items: ")
        quantity = int(input("Enter quantity: "))
        if item in items:
            price = quantity * items[item]
            pricelist.append((item, quantity, items[item], price))
            totalprice += price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)

# Calculate GST and final amount
gst = (totalprice * 5) / 100
finalamount = gst + totalprice

if finalamount == 0:
    print(25 * "=", "Supermarket", 25 * "=")
    for i in range(len(pricelist)):
        print(i + 1, ilist[i], qlist[i], plist[i])

inp = input("Can I bill the items? (yes or no): ")
if inp.lower() == 'yes':
    print("----------------------------------")
    print("Total Price: Rs-", totalprice)
    print("GST (5%): Rs-", gst)
    print("Final Amount: Rs-", finalamount)
    print("----------------------------------")
    print("Billing successful!")
