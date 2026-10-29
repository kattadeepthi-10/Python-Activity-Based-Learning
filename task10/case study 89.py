
total_room = 110
allocated_room = 70
unallocated_room = total_room - allocated_room

print(f"Total rooms are {total_room}.")
print(f"Allocated rooms are {allocated_room}.")
print(f"Unallocated rooms are {unallocated_room}.")

fee = int(input("Enter your fee (50000, 60000, 100000, 200000): "))

mess_fee = 20000

if fee == 50000:
    room_num = 33
    room_mates = 8
    room_type = "Non-AC"
    maintain_fee = 1000 // room_mates
    unallocated_room -= 1

elif fee == 60000:
    room_num = 61
    room_mates = 6
    room_type = "Non-AC"
    maintain_fee = 1000 // room_mates
    unallocated_room -= 2

elif fee == 100000:
    room_num = 78
    room_mates = 4
    room_type = "AC with attached washroom"
    maintain_fee = 2000 // room_mates
    unallocated_room -= 3

elif fee == 200000:
    room_num = 106
    room_mates = 3
    room_type = "AC with attached washroom"
    maintain_fee = 2000 // room_mates
    unallocated_room -= 4

else:
    print("Invalid fee category.")
    room_num = None

if room_num is not None:
    total_fee = fee + mess_fee + maintain_fee

    print(f"You are allocated to room number {room_num}.")
    print(f"Room type: {room_type}")
    print(f"Roommates: {room_mates}")
    print(f"Mess fee: ₹{mess_fee}")
    print(f"Maintenance fee per student: ₹{maintain_fee}")
    print(f"Your total fee is ₹{total_fee}.")
    print("Thank You!")

print(f"At present unallocated rooms are {unallocated_room}.")
