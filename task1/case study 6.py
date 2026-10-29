
distance = float(input("Enter distance: "))
age = int(input("Enter age: "))
travel_class = input("Enter travel class (SL/3A/2A/1A): ").upper()

if travel_class == "SL":
    amt = distance * 0.50
elif travel_class == "3A":
    amt = distance * 1.30
elif travel_class == "2A":
    amt = distance * 1.85
elif travel_class == "1A":
    amt = distance * 3.10
else:
    print("Invalid class entered.")
    amt = 0

c = 0
if age < 5:
    c = 0
elif 5 <= age <= 59:
    c = 50
elif age >= 60:
    c = 40

fare = amt * (c / 100)
print(f"Total fare: {fare:.2f}")

print("Want to cancel the ticket.")
cancel_ticket = input("Enter Yes or No: ").upper()

if cancel_ticket == "YES":
    time = int(input("Enter hours remaining until train departure: "))

    if time >= 48:
        penalty = 60.0
    elif 12 <= time < 48:
        penalty = 0.25 * fare
    elif 4 < time < 12:
        penalty = 0.50 * fare
    else:
        penalty = fare

    refund = fare - penalty
    print(f"Refund amount: {refund:.2f}")
else:
    print("Enjoy your journey!")

