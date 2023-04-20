item = []
qty = []
price = []

def addItem():
        item.append(input("Item name: "))
        qty.append(int(input("Quantity: ")))
        price.append(float(input("Price: ")))
        print('Item has been added to the inventory')
        print()
        
def delItem():
    itemName = input('Name of item to be removed: ')
    for x in range(len(item)):
        if item[x] == itemName:
            item.remove(itemName)
            print('Item has been deleted')
            print()

def viewInventory():
    if len(item) == 0:
        print ("Inventory is empty!")
        print()
    else:
        for n in range(0, len(item)):
            print("Item name: ", ''.join(item[n]))
            print("Quantity: ", qty[n])
            print("Price: ", price[n])
            print()
        
def updateInventory():
    itemName = input('Name of item to be updated: ')
    for x in range(len(item)):
        if item[x] == itemName:
            print('Name: ', item[x])
        print("Quantity: ", qty[x])
        print("Price: ", price[x])
        print()
        
        qty[x] = int(input("Updated quantity: "))
        price[x] = int(input("Updated price: "))
        
        print("Updated successfully!")
        print()
            
while True:

    print('1 - Add item')
    print ('2 - Remove item')
    print('3 - View inventory')
    print('4 - Update inventory')
    print('5 - Exit')

    option = ""
    try: option = int(input('\nEnter your choice (1-5): '))
    except ValueError:
        print('Incorrect Entry!')

    if option == 5:
        break

    elif option == 1:
        addItem()

    elif option == 2:
        delItem()

    elif option == 3:
        viewInventory()

    elif option == 4:
        updateInventory()

    else:
        print('Incorrect entry!, Try again?')
