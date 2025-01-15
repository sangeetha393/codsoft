def calculator():
    print(" Calculator")
    print("Choose an operation from the above :")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication(*)")
    print("4. Division (/)")
    print("5. Exit ...")

    while True:
        choice = input("\nEnter your choice (1/2/3/4/5): ")

        if choice == '5':
            print("GOOD BYE DONE WITH THE CALCULATION LET ME KNOW FURTHER")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == '1':
                    print(f"The result is: {int(num1+num2)}")
                elif choice == '2':
                    print(f"The result is: {int(num1 - num2)}")
                elif choice == '3':
                    print(f"The result is: {int(num1*num2)}")
                elif choice == '4':
                    print(f"The result is: {num1/num2}")
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print("Invalid choice! Please select a valid option.")

# Run the calculator
calculator()