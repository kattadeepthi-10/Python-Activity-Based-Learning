Order Processing, Dispatch and Inventory Reconciliation System
# Problem Statement
The Order Processing and Inventory Reconciliation System is a Python program that processes product orders, dispatch quantities, and returned items to update the available inventory.

The program calculates outstanding order quantities by comparing the ordered and dispatched amounts. It identifies inconsistent records when the dispatched quantity exceeds the ordered quantity. For valid records, it updates stock by subtracting dispatched items and adding returned items. Finally, it displays the outstanding quantities, updated stock, and record status for each product.
# Algorithm
1. Start the program.
2. Create an inventory dictionary containing product names and current stock.
3. Store order records as tuples containing item name, quantity ordered, quantity dispatched, and quantity returned.
4. Display the table headings.
5. Process each order record using a for loop.
6. Extract the item name, ordered quantity, dispatched quantity, and returned quantity.
7. Check whether the dispatched quantity is greater than the ordered quantity.
   - If yes, mark the record as inconsistent and set outstanding quantity to zero.
   - Otherwise, mark the record as valid and calculate outstanding quantity as ordered minus dispatched.
8. For valid records, update inventory by subtracting dispatched quantities and adding returned quantities.
9. Retrieve the updated stock for the item.
10. Display the item name, outstanding quantity, new stock, and record status.
11. After processing all records, display the final inventory dictionary.
12. Stop the program.
# Mermaid Flowchart
``` mermaid
  
flowchart TD
    A([Start]) --> B[Create inventory dictionary]
    B --> C[Store order records]
    C --> D[Display table headings]
    D --> E[Read next order record]
    E --> F[Extract item, ordered, dispatched and returned]
    F --> G{Dispatched > Ordered?}
    G -- Yes --> H[Mark record INCONSISTENT]
    H --> I[Set outstanding = 0]
    G -- No --> J[Mark record VALID]
    J --> K[Calculate outstanding = ordered - dispatched]
    K --> L{Item exists in inventory?}
    L -- Yes --> M[Update stock = stock - dispatched + returned]
    L -- No --> N[Skip inventory update]
    M --> O[Retrieve current stock]
    N --> O
    I --> O
    O --> P[Display order details]
    P --> Q{More records?}
    Q -- Yes --> E
    Q -- No --> R[Display final inventory]
    R --> S([Stop])
```
# Input
The program uses the following predefined inventory and order records.

Initial inventory
Product	Current stock
Laptop	50
Smartphone	120
Headphones	80
Tablet	35

Order records
Product	Ordered	Dispatched	Returned
Laptop	10	10	2
Smartphone	25	20	0
Headphones	15	18	1
Tablet	5	5	0

# Expected Output
ITEM         | OUTSTANDING | NEW STOCK  | RECORD STATUS
Laptop       | 0           | 42         | VALID
Smartphone   | 5           | 100        | VALID
Headphones   | 0           | 80         | INCONSISTENT (Dispatched > Ordered)
Tablet       | 0           | 30         | VALID

Final Updated Inventory Stockroom Count:
{'Laptop': 42, 'Smartphone': 100, 'Headphones': 80, 'Tablet': 30}



Sample calculations
- Laptop: \(50-10+2=42\) units remaining.
- Smartphone: \(25-20=5\) units outstanding; updated stock is \(120-20=100\).
- Headphones: 18 units dispatched exceeds 15 ordered, so the record is inconsistent and stock remains 80.
- Tablet: \(35-5=30\) units remaining.
