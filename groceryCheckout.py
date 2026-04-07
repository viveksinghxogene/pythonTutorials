item_with_prices = {
    "apples": 30,
    "banana": 20,
    "mango": 10,
    "orange": 60
}

i1 = input("Enter the first item name: ")
p1 = float(input(f"Enter the price of {i1}: "))

i2 = input("Enter the second item name: ")
p2 = float(input(f"Enter the price of {i2}: "))

i3 = input("Enter the third item name: ")
p3 = float(input(f"Enter the price of {i3}: "))

i4 = input("Enter the fourth item name: ")
p4 = float(input(f"Enter the price of {i4}: "))

qty = [1, 4, 5, 2, 2, 6, 10, 4]

item_with_prices[i1] = p1
item_with_prices[i2] = p2
item_with_prices[i3] = p3
item_with_prices[i4] = p4

item_names = list(item_with_prices.keys())

print('Before discount deductions:')
for item in item_names:
    print(f'The item {item} price is {item_with_prices[item]}')

qty_cntr = 0
for item in item_names:
    item_price = float(item_with_prices[item])
    quantity = qty[qty_cntr % len(qty)]

    discount = item_price * quantity * 0.1
    item_with_prices[item] = item_price - discount

    qty_cntr += 1

print('\nAfter discount deductions:')
for item in item_names:
    print(f'The item {item} price is {item_with_prices[item]}')