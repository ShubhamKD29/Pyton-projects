menu = {
    'Pizza': 120,
    'Burger': 80,
    'Noodles': 150,
    'Water': 20,
    'Garlic bread': 200
}

print("Welcome To Itallio CAFE")
print("----------------------------")
for food_item, price in menu.items():
    print(f"{food_item}: Rs.{price}")
print()

total_amount = 0

# checking whether item is present or not
while True:
    order = input("Enter item from the menu:")
    if order in menu:
        print(f"Order for {order} placed successfully")
        total_amount += menu[order]
        response = input("Want to order more items(yes/no):").lower()
        print()
        if response == 'yes':
            continue
        else:
            break
    else:
        print(f"{order} is currently unavailable !")

print(f"Your total amount is : Rs. {total_amount}")

