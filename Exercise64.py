#quang_thong
total_cost_pennies = 0

while True:
    price = input("Enter the price of an item (or blank to finish): ")
    if price == '':
        break
    total_cost_pennies += int(float(price) * 100)  # $ to pennies
remainder = total_cost_pennies % 5
adjusted_total = total_cost_pennies - remainder if remainder < 2.5 else total_cost_pennies + (5 - remainder)
print(f"Total cost of items: ${total_cost_pennies / 100:.2f}")
print(f"Amount due for cash payment: ${adjusted_total / 100:.2f}")
