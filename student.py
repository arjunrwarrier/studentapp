import mysql.connector

mydb = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'studentdb')

mycursor = mydb.cursor()

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
        name = input("Enter name: ")
        rollno = input("Enter the rollnumber: ")
        admnum = input("Enter the admission number: ")
        college = input("Enter the college: ")
        sql = 'INSERT INTO `students`(`name`, `rollnumber`, `admno`, `college`) VALUES (%s,%s,%s,%s)'
        data = (name,rollno,admnum,college)
        mycursor.execute(sql,data)
        mydb.commit()
        print("Data inserted successfully.")
    elif(choice == 2):
        sql = 'SELECT * FROM `students`'
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)

    elif(choice == 3):
        print("Searching a student")
    elif (choice == 4):
        print("updating student")
    elif(choice == 5):
        print("delete a student")
    elif(choice==6):
        break