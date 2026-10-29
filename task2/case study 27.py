
print("Hollow Diamond")

n = int(input("Enter number of rows :"))

if n <= 0:
    print("Invalid Dimension: Number of rows must be greater than 0")

elif n > 20:
    print("Invalid Dimension: Number of rows must be less than or equal to 20")
    print("The number is too larger for screen alignment.")

else:
    print("Dimensions validated! Generating pattern...")

    # Upper half of the diamond
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end=" ")

        for k in range(2 * i - 1):
            if k == 0 or k == 2 * i - 2:
                print("*", end=" ")
            else:
                print(" ", end=" ")

        print()

    # Lower half of the diamond
    for i in range(n - 1, 0, -1):
        for j in range(n - i):
            print(" ", end=" ")

        for k in range(2 * i - 1):
            if k == 0 or k == 2 * i - 2:
                print("*", end=" ")
            else:
                print(" ", end=" ")

        print()
