# empty list
groceries = []

while True:
    item = input("Enter your item (q to quit): ")
    if item.lower() == "q":
        # quit while loop if q
        break
    else:
        # add item to list
        groceries.append(item)

for item in groceries:
    # print list of items
    print(groceries)