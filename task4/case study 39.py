
info_1 = (2601, 65, 15, 35, "yes")  # Lab
info_2 = (2602, 70, 20, 26, "yes")  # Internal
info_3 = (2603, 62, 20, 30, "no")   # Fee
info_4 = (2604, 60, 20, 30, "yes") # All clear
info_5 = (2605, 50, 20, 38, "yes") # Attendance

all_students = [info_1, info_2, info_3, info_4, info_5]

print("Student eligibility for final examination:")

for info in all_students:
    student_id, attendance, laboratory, internal, fee_clear = info

    print()
    print("Student ID:", student_id)
    print("Attendance (in percentage):", attendance)
    print("Laboratory (out of 20):", laboratory)
    print("Internal marks (out of 40):", internal)
    print("Fee clear:", fee_clear)

    unmet = []

    if attendance < 60:
        unmet.append("Your attendance is low.")

    if laboratory != 20:
        unmet.append("You have not completed your Laboratory yet.")

    if internal != 30:
        unmet.append("Your internal marks are low.")

    if fee_clear.lower() != "yes":
        unmet.append("Your fee is not cleared.")

    if len(unmet) == 0:
        print("You are eligible for final examination.")
    else:
        for requirement in unmet:
            print(requirement)

        print("Sorry, you are not eligible for final examination.")

print()
