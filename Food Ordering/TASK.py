menu = {
    'PIZZA': 110,
    'BURGER': 80,
    'PASTA': 90,
    'SANDWICH': 50,
    'SALAD': 40,
    'SODA': 30,
    'COFFEE': 20,
}
status = True

print("Welcome to the Food Ordering System!")
print("PIZZA - 110 \nBURGER - 80 \nPASTA - 90 \nSANDWICH - 50 \nSALAD - 40 \nSODA - 30 \nCOFFEE - 20")
total_cost = 0

while status:
    item = input("Enter the first item you want to order: ").upper()
    if item in menu:
        total_cost += menu[item]
        print(f"{item} added to your order. Current total: {total_cost}")
    else: 
        print(f"ORDER SOMETHING ELSE {item} is not available. Please choose from the menu.")

    another_item = input("DO YOU WANT TO ORDER ANOTHER ITEM? (yes/no): ").lower()

    if another_item != 'yes':
        status = False  # exit loop
        break  # stop execution if no more items

    # Asking for second item inside loop
    item_2 = input("Enter the next item you want to order: ").upper()
    if item_2 in menu:
        total_cost += menu[item_2]
        print(f"{item_2} added to your order. Current total: {total_cost}")
    else:
        print(f"ORDER SOMETHING ELSE {item_2} is not available. Please choose from the menu.")

print(f"Your total order cost is: {total_cost}")
print("Thank you for your order! Have a great day!")