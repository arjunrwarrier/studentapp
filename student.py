while True:
    print("Select an option from the menu ")
    print("1. Add student")
    print("2. View all student")
    print("3. Search a student")
    print("4. Update a student")
    print("5. Delete a student")
    print("6.exit")

    choice = int(input("Enter an option: "))
    if(choice == 1):
        print("Student enter selected")
    elif(choice == 2):
        print("View Student")
    elif(choice == 3):
        print("Searching a student")
    elif (choice == 4):
        print("updating student")
    elif(choice == 5):
        print("delete a student")
    else:
        break