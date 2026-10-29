
# Product name and current stock
inventory = {
    "Laptop": 50,
    "Smartphone": 120,
    "Headphones": 80,
    "Tablet": 35
}

# Format: (Item, Ordered, Dispatched, Returned)
order_records = [
    ("Laptop", 10, 10, 2),
    ("Smartphone", 25, 20, 0),
    ("Headphones", 15, 18, 1),
    ("Tablet", 5, 5, 0)
]

print(f"{'ITEM':<12} | {'OUTSTANDING':<11} | {'NEW STOCK':<10} | {'RECORD STATUS'}")

for record in order_records:
    item, ordered, dispatched, returned = record

    if dispatched > ordered:
        status = "INCONSISTENT (Dispatched > Ordered)"
        outstanding = 0
    else:
        status = "VALID"
        outstanding = ordered - dispatched

        if item in inventory:
            inventory[item] = inventory[item] - dispatched + returned

    new_stock = inventory.get(item, "N/A")

    print(f"{item:<12} | {outstanding:<11} | {new_stock:<10} | {status}")

print("\nFinal Updated Inventory Stockroom Count:")
print(inventory)
