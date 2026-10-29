
# Format: (Book ID, Days Allowed, Actual Days Taken)
borrowing_records = [
    ("BK101", 14, 18),  # 4 days late
    ("BK102", 7, 7),    # On time
    ("BK103", 10, 19)   # 9 days late
]

available_books = []

# Process each book record
for book in borrowing_records:
    book_id, allowed_days, actual_days = book

    days_overdue = actual_days - allowed_days

    if days_overdue <= 0:
        fine = 0.00
        days_overdue = 0
    elif days_overdue <= 5:
        fine = days_overdue * 0.50
    else:
        fine = 2.50 + ((days_overdue - 5) * 1.00)

    # Add returned book back to the library
    available_books.append(book_id)

    # Print individual results
    print(f"Book ID: {book_id}")
    print(f"Days Overdue: {days_overdue}")
    print(f"Fine Calculated: ${fine:.2f}")
    print()

# Print final availability summary
print("\nBooks Reconciled & Returned to Shelf:")
print(available_books)
