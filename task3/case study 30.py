
student_email = input("Enter student email address :").strip().lower()

if student_email.startswith(" "):
    print("Email should not be started by space.")

elif "@" not in student_email:
    print("Email should contain @ symbol.")

elif student_email.count("@") != 1:
    print("Email should contain only one @ symbol.")

elif not student_email.endswith(".edu"):
    print("Only institutional .edu emails are permitted.")

else:
    username = student_email.split("@")[0]

    print("\n----Registration Status : SUCCESS----")
    print(
        f"Welcome {username}! "
        "Your student account has been successfully created.")
  
