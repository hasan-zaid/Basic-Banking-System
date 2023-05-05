#HASAN_AKRAM_ABDULLAH_ZAID
#TP066635

def create_admin_staff_account():
#This is a function used by the super admin to create admin staff accounts.

    print("\nNote\ The use of WHITE SPACES is NOT allowed for the new admin's username and password"
          "\nYou can use symbols instead, underscores are preferred")

#It first asks the user to enter a username and a password that will be used later as the admin login credentials.
    admin_staff_name = input("Enter the new admin's username : ").upper()
    admin_staff_password = input("Enter the new admin's password : ").upper()

    if admin_staff_password == "" or admin_staff_name == "":
        print("Username and password can't be empty, try again")
        create_admin_staff_account()



    admins_list = []
    admins_list.append(admin_staff_password)
    admins_list.append(admin_staff_name)

#These conditions are used to detect if there are any white spaces in the username or passwrod that the super admin has given.
    if " " in admin_staff_name:
        print("White space detected in admin's username ! Please, try again\n")
        create_admin_staff_account()
    if " " in admin_staff_password:
        print("White space detected in admin's password ! Please, try again\n")
        create_admin_staff_account()
    else:
        print("New Details Accepted")

    admins_list_to_file = " ".join(admins_list)

#A try and except structure to specify which mode the admins file should be opened with; write or append.
    try:
        admins_file = open("admins.txt", "a")
        admins_file.write("\n"+admins_list_to_file)
        admins_file.close()
        print("Admin staff account has been created successfully")
    except:
        admins_file = open("admins.txt", "w")
        admins_file.write(admins_list_to_file)
        admins_file.close()
        print("Admin staff account has been created successfully")

    print("\nTo go back to super_admin_menu, press 1")
    print("To go back to the main menu, press 2")
    print("To exit the program, press any other key")

#Simple input to decide what should the program do next.
    super_admin_choice2 = input()

    if super_admin_choice2 == "1":
        super_admin_menu()
    elif super_admin_choice2 == "2":
        welcome_menu()
    else:
        exit()





def super_admin_menu():
#This function is just for displaying the available options for the super admin.

#In this while loop, the super admins is asked to type in the login username and password. There is an option to go back to the main menu
#in case another user accessed this function by accident. In other words, it is there to avoid getting stuck and needing to restart the whole program.
    while True:
        super_admin_decision = input("Type A if you wanna go back to the main menu or any other key to continue : ")
        if super_admin_decision.upper() == "A":
            welcome_menu()
        username = input("Please type in your username : ").lower()
        password = input("Please type in your password : ").lower()
        if password == "1234" and username == "super admin":
            print("\nSuccessful Authentication")

            print("\nWhat would you like to do ?")
            print("1- Create Admin Staff Account")
            print("2- Take me back to the main menu")

            print("Kindly, specify the number of the desired operation : ")

#Another while loop for deciding what to do next depending on the user input.
            while True:
                super_admin_choice = int(input())

                if super_admin_choice == 1:
                    create_admin_staff_account()
                elif super_admin_choice == 2:
                    welcome_menu()
                else:
                    print("Ivalid entry, please try again")

        else:
            print("\nIncorrect Username or Password !")


def admin_staff_login():
#As the name sugest, this function's job is to give access to admins menu where they can do various operations.
#It basiclly take the input for username and password from the user and compares them with the existing data in the admins text file created when creating the admins accounts.

    admins_list = []
    admins_file = open("admins.txt", "r")
    for line in admins_file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        admins_list.append(line_list)
    admins_file.close()

#Another escape gate in case the user forgets the data or presses by mistake.
    out = input("Enter 1 to go back to the previous menu, or any other key to continue : ")
    if out == "1":
        welcome_menu()
    admin_staff_username = input("Enter your username : ").upper()
    counter = 0
    for list in admins_list:
        counter = counter + 1
        if admin_staff_username in list:
            admin_login_info = list
            break
        elif counter == len(admins_list):
            print("Wrong username, try again")
            admin_staff_login()
            break

#A while loop for making sure the password matches that in the text file. It has another escape gate
#because forgetting your password and not being able to retreat is not particularily a convenient situation.
    while True:
        admin_staff_password = input("Enter your password or just press 1 if you have forgotten it : ").upper()
        if admin_staff_password in admin_login_info:
            print("\nWelcome", admin_login_info[1])
            admin_staff_menu()
            break
        elif admin_staff_password == "1":
            welcome_menu()
            break

        else:
            print("Wrong password, try again")

def admin_staff_menu():
#This is the control board for admin staff. They can only reach this point after loging in with the username and the password.
#It provides the admins with several options like printing a bank statment for customers or changing their passwords.

    print("What would you like to do ?")

    print("1- Add a new customer account")
    print("2- Change customer's account password")
    print("3- Print a customer's bank statement")
    print("4- Go back to main menu")
    print("5- Exit program")

    while True:

        print("\nPlease Type the number of the desired option : ")
        admin_staff_choice = input()

        if admin_staff_choice == "1":
            add_new_customer_account()
            break
        elif admin_staff_choice == "2":
            change_password_for_admins()
            break
        elif admin_staff_choice == "3":
            print_bank_statement_for_admins()
            break
        elif admin_staff_choice == "4":
            welcome_menu()
            break
        elif admin_staff_choice == "5":
            exit()
        else:
            print("Invalid entery !")


def change_password_for_admins():
#This function enables admins to change customers' passwords.

    print("Enter the ID of the customer")
    id = input(">")
    print("Enter the customer's current password")
    current_password = input(">")

    customer_operations_file = open("customers.txt", "r")
    container = []
    for line in customer_operations_file:
        splitted_line = line.split()
        container.append(splitted_line)
    customer_operations_file.close()

    if len(container[0]) == 0:
        container.pop(0)

#A while loop to take the new password and replaces it with the old one.
    while True:
        for list in container:
            if current_password == list[5] and id == list[4]:
                print("Enter the new password. It must not contain any whitespaces")
                new_password = input(">")
                if new_password == "":
                    print("password can't be empty, try again")
                    change_password_for_admins()
                if " " in new_password:
                    break
                list[5] = new_password
                break
        if current_password != list[5] and new_password == list[5]:
            break
        else:
            print("Password or customer ID was not found, make sure you type them correctly")
            change_password_for_admins()


    print("Password was changed successfully")

    organizer = 0

#This is where the text file gets updated with the new password.
    for list in container:
        converter = " ".join(list)
        organizer = organizer + 1
        if organizer == 1:
            customer_operations_file = open("customers.txt", "w")
            customer_operations_file.write(converter)
            customer_operations_file.close()
        else:
            customer_operations_file = open("customers.txt", "a")
            customer_operations_file.write("\n" + converter)
            customer_operations_file.close()

    admin_staff_menu()


def add_new_customer_account():
#Here is where the admins can approve registeration requests and add them to the customers database.

    from datetime import datetime

    try:
        registeraion_handler = open("customer_registerations", "r")
    except:
        print("New registerations database not found !!")
        admin_staff_menu()
    chosen_customer = []
    for line in registeraion_handler:
        list = line.split()
        chosen_customer.append(list)
    registeraion_handler.close()
    if len(chosen_customer) == 0:
        print("No pending registeration requests !!")
        admin_staff_menu()

    print(chosen_customer, "\nAbove are the pending registeration requests")

#This is a try and except structure to determine the account number that should be assgined to the customer account.
#The for loop is for ensuring a consecutive account numbers starting from 8000
    try:
        incrementor = open("num.txt", "r")
        for number in incrementor:
            num = int(number)
            num = num + 1
            identifier = num
        change = str(identifier)
        incrementor.close()
        incrementor = open("num.txt", "w")
        incrementor.write(change)
        incrementor.close()
    except:
        incrementor = open("num.txt", "w")
        account_no = "8000"
        incrementor.write(account_no)
        incrementor.close()
        incrementor = open("num.txt", "r")
        for number in incrementor:
            num = int(number)
            num = num + 1
            identifier = num
        change = str(identifier)
        incrementor.close()
        incrementor = open("num.txt", "w")
        incrementor.write(change)
        incrementor.close()

    found = False
    while found == False:
        choose_request = input("Type in the first name of the customer you would like to add : ").upper()
        confirm_request = input("Now, enter the birth date of the chosen customer : ")
        for item in chosen_customer:
            if choose_request in item and confirm_request in item:
                found = True
                account_number = change
                item.append(account_number)
                added_customer = item
                break
        if choose_request in item and confirm_request in item:
            break
        print('\nNot found, make sure to enter the details accurately')

    done_registeration_request = chosen_customer.index(item)
    chosen_customer.pop(done_registeration_request)
    for string in chosen_customer:
        remaining_list = " ".join(string)
        registeraion_handler = open("customer_registerations", "w")
        registeraion_handler.write(remaining_list)
        registeraion_handler.close()

    x = datetime.now()
#Here the datetime module was used to get the value of milliseconds and then this value is used as the default for the customer account.
    password = x.strftime("%f")
    account_password = str(password)
    registered_users = [added_customer[4], added_customer[5], added_customer[0], added_customer[1], added_customer[2], account_password, added_customer[3]]
    print(registered_users)
    add_new_customers_to_database = " ".join(registered_users)

#A try except structure to officially add the account to the customers text file.
    try:
        database = open("customers.txt", "a")
        database.write("\n" + add_new_customers_to_database)
        database.close()
    except:
        database = open("customers.txt", "w")
        database.write(add_new_customers_to_database)
        database.close()
    print("the account for customer : (", registered_users[2], registered_users[3],
          ") has been added to the database successfully"
          "\nIt has been assigned the following account number : (", account_number,
          ") and the the following password : (", password, ")")

    print("\nWhat do you want to do now ?")

    while True:
        print("\nPress 1 to go back to the admin menu"
              "\nPress 2 to go back to the main menu"
              "\nPress 3 to exit the program")
        choice = input()
        if choice == "1":
            admin_staff_menu()
            break
        elif choice == "2":
            welcome_menu()
            break
        elif choice == "3":
            exit()
        else:
            print("Invalid entery ! try again")


def customer_menu():
#This is the customers board where they can do all of the available options such as deposit, banks report, change passwords, etc...

    print("\nWhat would you like to do ?")

    while True:
        print("\n1- Perform deposit"
              "\n2- Perform withdrawal"
              "\n3- Print a bank statement"
              "\n4- Check my balance"
              "\n5- Change my password"
              "\n6- Go back to previous menu"
              "\n7- Go to home page"
              "\n8- Exit program")

        customer_choice = input()

        if customer_choice == "1":
            deposit()
            break
        elif customer_choice == "2":
            withdraw()
            break
        elif customer_choice == "3":
            print_bank_statement()
            break
        elif customer_choice == "4":
            check_balance()
            break
        elif customer_choice == "5":
            change_password()
            break
        elif customer_choice == "6":
            customer_page()
            break
        elif customer_choice == "7":
            welcome_menu()
            break
        elif customer_choice == "8":
            exit()
        else:
            print("Invalid entery, try again")




def customer_login():
#This function is used by the customer after his account has been added and approved by the admin staff
# before that the function will return a message clerifying that the customer account is still not in the customers data file.


    customers_list = []
    try:
        customers_file = open("customers.txt", "r")
    except:
        print("Sorry, customers database was not found")
        customer_page()
    for line in customers_file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        customers_list.append(line_list)
    customers_file.close()
    if len(customers_list[0]) == 0:
        customers_list.pop(0)


#Here is an escape gate for when the customer tries to login but the account is yet to be added.
    out = input("Enter 1 to go back to the previous menu, or any other key to continue : ")
    if out == "1":
        customer_page()

#While loop for taking the account number and password and authenticate the user.
    while True:
        customer_account_number = input("Enter your account number : ")
        customer_password = input("Enter your password or just press 1 if you have forgotten it : ")
        for list in customers_list:
            if customer_password == list[5] and customer_account_number == list[1]:
                customer_login_info = list
                important_info = customer_account_number+" "+customer_login_info[0]
                customer_login.var = important_info
                print("\nWelcome", customer_login_info[2], customer_login_info[3])
                customer_menu()
                break
            elif customer_password == "1":
                customer_page()
                break
        print("Wrong ID or Password, try again")


def print_specific_bank_statement_for_admins():
#This function is accessable by admins and its job is to take a specific time period from the admin and prints all the transactions the chosen customers as made during this period.

    print("Enter the account number for the customer you would like to print his/her bank statement")
    customer_account_number = input(">")


    if customer_account_number == "":
        print("account number can't be empty, try again")
        print_specific_bank_statement_for_admins()

    selective_list = []

    customers_file = open("customers.txt", "r")
    for line in customers_file:
        splitted_line = line.split()
        selective_list.append(splitted_line)
    customers_file.close()

#This condition will remove the first line in the customers file in case it was empty.
    if len(selective_list[0]) == 0:
        selective_list.pop(0)

    account_type = None
    counter = 0

#For loop for choosing a certain customer
    for list in selective_list:
        counter = counter + 1
        if customer_account_number == list[1]:
            account_type = list[0]
            break
        elif counter == len(selective_list):
            print("There is no customer with the account number !!"
                  "\nPress '1' to go back or any other key to try again")
            choice = input()
            if choice == "1":
                welcome_menu()
            else:
                print_specific_bank_statement_for_admins()

    file_name = customer_account_number + " " + account_type

#The datetime module is imported to be used in comparing the dates of transactions
    import datetime
    try:
        customer_operations_file = open(file_name + ".txt", "r")
    except:
        print("Customer has not made any transactions yet\n")
        admin_staff_menu()

    general_list = []
    for line in customer_operations_file:
        splitted_line = line.split()
        general_list.append(splitted_line)
    customer_operations_file.close()

#The first two lists in the general list will be removed because they are not needed in the report
    general_list.pop(0)
    general_list.pop(0)

#While loop to ensure that all dates entered by admin are true dates not just random numbers
    while True:
        try:
            start_year = int(input("Enter the year of start date : "))
            while True:
                start_month = int(input("Enter the month of start date : "))
                if 0 < start_month < 13:
                    break
                else:
                    print("Months must be between 0 and 13")
            while True:
                start_day = int(input("Enter the day of start date : "))
                if 0 < start_day < 32:
                    break
                else:
                    print("Day must be between 0 and 32")
            end_year = int(input("Enter the year of end date : "))
            while True:
                end_month = int(input("Enter the month of end date : "))
                if 0 < end_month < 13:
                    break
                else:
                    print("Months must be between 0 and 13")
            while True:
                end_day = int(input("Enter the day of end date : "))
                if 0 < end_day < 32:
                    break
                else:
                    print("Day must be between 0 and 32")

            break
        except:
            print("Make sure not to include any letters or white spaces while specifying the dates")

    counter = 0

#This is the most important loop as it is resposible for comparing the dates and printing the actual report
    for list in general_list:
        year_modifier = ["20", list[3][6:]]
        modified_year = "".join(year_modifier)
        operation_year = int(modified_year)
        operation_month = int(list[3][0:2])
        operation_day = int(list[3][3:5])
        operation_date = datetime.datetime(operation_year, operation_month, operation_day)
        start_date = datetime.datetime(start_year, start_month, start_day)
        start_date_comparison = operation_date > start_date
        end_date = datetime.datetime(end_year, end_month, end_day)
        end_date_comparison = operation_date > end_date
        if start_date_comparison == True and end_date_comparison == False:
            counter = counter + 1
            list_to_line = " ".join(list)
            print(list_to_line)

    if counter == 0:
        print("Customer has not made any transactions during the specified period\n")
    else:
        print(file_name)

    print("\nWhat do you want to do now ?"
          "\n1- Go to admins menu"
          "\n2- Go to main menu"
          "\n3- Close program")

    while True:
        choice = input(">")
        if choice == '1':
            admin_staff_menu()
        elif choice == '2':
            welcome_menu()
        elif choice == '3':
            exit()
        else:
            print("Invalid input. Try again")


def print_specific_bank_statement():
#Function for printing a bank report for certain period of time sepcified by the customer

#The datetime module is imported for comparing dates
    import datetime
    try:
        customer_operations_file = open(customer_login.var + ".txt", "r")
    except:
        print("You have not made any transactions yet\n")
        customer_menu()

    general_list = []
    for line in customer_operations_file:
        splitted_line = line.split()
        general_list.append(splitted_line)
    customer_operations_file.close()

#First two lists are removed from the general list due to not being need for the printing of the report
    general_list.pop(0)
    general_list.pop(0)

#While loop to ensure the accuracy of the entered dates
    while True:
        try:
            start_year = int(input("Enter the year of start date : "))
            while True:
                start_month = int(input("Enter the month of start date : "))
                if 0 < start_month < 13:
                    break
                else:
                    print("Months must be between 0 and 13")
            while True:
                start_day = int(input("Enter the day of start date : "))
                if 0 < start_day < 32:
                    break
                else:
                    print("Day must be between 0 and 32")
            end_year = int(input("Enter the year of end date : "))
            while True:
                end_month = int(input("Enter the month of end date : "))
                if 0 < end_month < 13:
                    break
                else:
                    print("Months must be between 0 and 13")
            while True:
                end_day = int(input("Enter the day of end date : "))
                if 0 < end_day < 32:
                    break
                else:
                    print("Day must be between 0 and 32")

            break
        except:
            print("Make sure not to include any letters or white spaces while specifying the dates")

    counter = 0

#This is the main loop for comparing and printing the wanted transactions
    for list in general_list:
        year_modifier = ["20", list[3][6:]]
        modified_year = "".join(year_modifier)
        operation_year = int(modified_year)
        operation_month = int(list[3][0:2])
        operation_day = int(list[3][3:5])
        operation_date = datetime.datetime(operation_year, operation_month, operation_day)
        start_date = datetime.datetime(start_year, start_month, start_day)
        start_date_comparison = operation_date > start_date
        end_date = datetime.datetime(end_year, end_month, end_day)
        end_date_comparison = operation_date > end_date
        if start_date_comparison == True and end_date_comparison == False:
            counter = counter + 1
            list_to_line = " ".join(list)
            print(list_to_line)

#In this condition, if the couter is still 0 this basiclly mean that there are no operations made in that time
    if counter == 0:
        print("You do not have any transactions made during the period you have specified !\n")
    else:
        print(customer_login.var)

    print("\nWhat do you want to do now ?"
          "\n1- Go to customers menu"
          "\n2- Go to main menu"
          "\n3- Close program")

    while True:
        choice = input(">")
        if choice == '1':
            customer_menu()
        elif choice == '2':
            welcome_menu()
        elif choice == '3':
            exit()
        else:
            print("Invalid input. Try again")


def print_bank_statement():
    print("What do you want ?"
          "\n1- Print full bank statement"
          "\n2- Print specific-period bank statement")
    bank_statement = input(">")
    while True:
        if bank_statement == "1":
            break
        elif bank_statement == "2":
            print_specific_bank_statement()
        else:
            print("Invalid entery, try again")
    try:
        customer_operations_file = open(customer_login.var + ".txt", "r")
        for line in customer_operations_file:
            print(line)
        customer_operations_file.close()
    except:
        print("\nYou still have not performed deposits or withdrawals !")
        customer_menu()
    print("\nPress '1' to go to previous menu"
          "\nPress anything else to exit the program")
    choice = input(">")
    if choice == "1":
        customer_menu()
    else:
        exit()
def print_bank_statement_for_admins():
#This function is accessed by the admins tp print a complete a full bank report for a customer

    print("What do you want ?"
          "\n1- Print full bank statement"
          "\n2- Print specific-period bank statement")
    bank_statement = input(">")
    while True:
        if bank_statement == "1":
            break
        elif bank_statement == "2":
            print_specific_bank_statement_for_admins()
        else:
            print("Invalid entery, try again")

    print("Enter the account number of the customer you would like to print his/her bank statement")
    customer_account_number = input(">")


    if admin_staff_password == "" or admin_staff_name == "":
        print("account number can't be empty, try again")
        print_bank_statement_for_admins()

    selective_list = []

    customers_file = open("customers.txt", "r")
    for line in customers_file:
        splitted_line = line.split()
        selective_list.append(splitted_line)
    customers_file.close()

#In case the first list is empty, this condition will remove it to avoid possible errors
    if len(selective_list[0]) == 0:
        selective_list.pop(0)

    account_type = None
    counter = 0

#This loop is for fetching and feguring out exactly which customer is wanted by the admin
    for list in selective_list:
        counter = counter + 1
        if customer_account_number == list[1]:
            account_type = list[0]
            break
        elif counter == len(selective_list):
            print("There is no customer with the entered ID !!"
                  "\nPress '1' to go back or any other key to try again")
            choice = input()
            if choice == "1":
                welcome_menu()
            else:
                print_bank_statement_for_admins()

    file_name = customer_account_number+ " " +account_type

#Here the customer's transaction file gets fetched and printed
    try:
        customer_operations_file = open(file_name + ".txt", "r")
        for line in customer_operations_file:
            print(line)
        customer_operations_file.close()
    except:
        print("The chosen customer has not performed any operations yet")


    print("\nPress '1' to go to main menu"
          "\nPress anything else to exit the program")

    second_choice = input(">")
    if second_choice == "1":
        welcome_menu()
    else:
        exit()

def check_balance():
#This function is only available for customer to view their own account balances

#Here, the customer transaction file is opened
    try:
        customer_operations_file = open(customer_login.var+".txt", "r")
        customer_operations_file.close()
    except:
        customer_operations_file = open(customer_login.var+".txt", "w")
        customer_operations_file.write(customer_login.var)
        customer_operations_file.close()
        customer_operations_file = open(customer_login.var+".txt", "a")
        customer_operations_file.write("\nCurrent Balance :\t0")
        customer_operations_file.close()

#Then the file is splitted to get the current balance and display it for the customer
    balance_list = []
    customer_operations_file = open(customer_login.var + ".txt", "r")
    for item in customer_operations_file:
        item_list = item.split()
        balance_list.append(item_list)
    customer_operations_file.close()

    print("Your account balance is : " + balance_list[1][3])
    del (balance_list)

    print("\nPress '1' to go the menu"
          "\nPress anything else to exit the program")
    choice = input(">")
    if choice == "1":
        customer_menu()
    else:
        exit()


def change_password():
#This is the tool customers can use to change their own passwords.
#They are to provide the old pass in order to be able to create a new one for security reasons

    customer_operations_file = open("customers.txt", "r")
    container = []
    for line in customer_operations_file:
        splitted_line = line.split()
        container.append(splitted_line)
    customer_operations_file.close()

#In case the first list was empty it will be removed to avoid any errors durning the process
    if len(container[0]) == 0:
        container.pop(0)

    new_password = None

#This is where the user can give his old and new password to be added to the system
    while True:
        print("Enter your old password")
        old_password = input(">")
        for list in container:
            if old_password == list[5]:
                print("Enter your new password. It must not contain any whitespaces")
                new_password = input(">")
                if new_password == "":
                    print("Password can't be empty, try again")
                    change_password()
                if " " in new_password:
                    print("White space detected, try again")
                    change_password()
                else:
                    list[5] = new_password
                    break
        if old_password != list[5] and new_password == list[5]:
            break
        else:
            print("Password was not found, make sure you type the password correctly")


    print("Password was changed successfully")

    organizer = 0

#Here the customers file is updated with the new password
    for list in container:
        converter = " ".join(list)
        organizer = organizer + 1
        if organizer == 1:
            customer_operations_file = open("customers.txt", "w")
            customer_operations_file.write(converter)
            customer_operations_file.close()
        else:
            customer_operations_file = open("customers.txt", "a")
            customer_operations_file.write("\n" + converter)
            customer_operations_file.close()

    customer_menu()

def withdraw():
#This is the function used for when the user want to withdraw money from his account.

#The datetime module is used to emphasize the date of each transaction
    from datetime import datetime

    print("Enter the amount of money you would like to withdraw")

    try:
        withdrawal_amount = float(input(">"))
    except ValueError:
        print("The amount should be typed in numbers !")
        withdraw()
    print("This is the amount you have entered : "+str(withdrawal_amount))

#While loop for taking confirmation from the user to do the withdrawal
    while True:
        print("Press :"
              "\n'1' to perform the operation"
              "\n'R' to re-configure the amount"
              "\n'C' to cancel the operation")
        confirmation = input(">").lower()
        if confirmation == "1":
            break
        elif confirmation == "r":
            withdraw()
            break
        elif confirmation == "c":
            customer_menu()
            break
        else:
            print("Invalid entery !")

#Here is where the operations file is either created or opened
    try:
        customer_operations_file = open(customer_login.var+".txt", "r")
        customer_operations_file.close()
    except:
        customer_operations_file = open(customer_login.var+".txt", "w")
        customer_operations_file.write(customer_login.var)
        customer_operations_file.close()
        customer_operations_file = open(customer_login.var+".txt", "a")
        customer_operations_file.write("\nCurrent Balance :\t0")
        customer_operations_file.close()

#The account type is determined in the below lines
    account_type = None
    customer_operations_file = open(customer_login.var+".txt", "r")
    for line in customer_operations_file:
        if "Current_Account" in line:
            account_type = "current"
        elif "Savings_Account" in line:
            account_type = "savings"
    customer_operations_file.close()

#The new balance is calculated below
    balance_operator = open(customer_login.var+".txt", "r")
    operations_list = []
    for item in balance_operator:
        item_list = item.split()
        operations_list.append(item_list)
    balance_operator.close()
    number = float(operations_list[1][3])
    calculator = number - withdrawal_amount

#This while loop checks the minimum balance for each type and if the withdrawal exceeds it, the while loop will prevent the operation from happening
    while account_type == "savings":
        if calculator >= 100:
            break
        else:
            print("Operation can not be performed due to exceeding the '100' minimum savings account balance : " + str(number))
            customer_menu()
            break
    while account_type == "current":
        if calculator >= 500:
            break
        else:
            print("Operation can not be performed due to exceeding the '500' minimum current account balance : " + str(number))
            customer_menu()
            break

#Then the lines below updates the transaction file with the new withdrawal and new balance details
    operations_list[1][3] = str(calculator)
    organizer = 0
    for list in operations_list:
        converter = " ".join(list)
        organizer = organizer + 1
        if organizer == 1:
            customer_operations_file = open(customer_login.var + ".txt", "w")
            customer_operations_file.write(converter)
            customer_operations_file.close()
        else:
            customer_operations_file = open(customer_login.var + ".txt", "a")
            customer_operations_file.write("\n" + converter)
            customer_operations_file.close()

    date_time = datetime.now()
    date = date_time.strftime("%x")
    time = date_time.strftime("%X")
    customer_operations_file = open(customer_login.var+".txt", "a")
    customer_operations_file.write("\nWITHDREW\t"+str(withdrawal_amount)+"\t ON\t"+date+"\tAT\t"+time)
    customer_operations_file.close()

    print("\nThe withdrawal was made successfully")
    customer_menu()

def deposit():
#A customers only function. This is among the most vital function in the program as it represents the living nerve of every banking system
#It is used for depositing money into the customers accounts

#Datetime module is imported to attach the date of each deposit next to it
    from datetime import datetime

    print("Enter the amount of money you would like to deposit")

    try:
        deposit_amount = float(input(">"))
    except ValueError:
        print("The amount should be typed in numbers !")
        deposit()
    print("This is the amount you have entered : "+str(deposit_amount))

#While loop for operation confirmation
    while True:
        print("Press :"
              "\n'1' to perform the operation"
              "\n'R' to re-configure the amount"
              "\n'C' to cancel the operation")
        confirmation = input(">").lower()
        if confirmation == "1":
            break
        elif confirmation == "r":
            deposit()
            break
        elif confirmation == "c":
            customer_menu()
            break
        else:
            print("Invalid entery !")

#TRY and except for opening or creating the transaction file
    try:
        customer_operations_file = open(customer_login.var+".txt", "r")
        customer_operations_file.close()
    except:
        customer_operations_file = open(customer_login.var+".txt", "w")
        customer_operations_file.write(customer_login.var)
        customer_operations_file.close()
        customer_operations_file = open(customer_login.var+".txt", "a")
        customer_operations_file.write("\nCurrent Balance :\t0")
        customer_operations_file.close()

#The lines below create the details of the new deposit
    date_time = datetime.now()
    date = date_time.strftime("%x")
    time = date_time.strftime("%X")
    customer_operations_file = open(customer_login.var+".txt", "a")
    customer_operations_file.write("\nDEPOSITED\t"+str(deposit_amount)+"\t ON\t"+date+"\tAT\t"+time)
    customer_operations_file.close()
    operations_list = []
    balance_operator = open(customer_login.var+".txt", "r")
    for item in balance_operator:
        item_list = item.split()
        operations_list.append(item_list)
    balance_operator.close()
    number = float(operations_list[1][3])
    calculator = number + deposit_amount
    operations_list[1][3] = str(calculator)

    organizer = 0

#This loop updates the transaction file with the new details
    for list in operations_list:
        converter = " ".join(list)
        organizer = organizer + 1
        if organizer == 1:
            customer_operations_file = open(customer_login.var+".txt", "w")
            customer_operations_file.write(converter)
            customer_operations_file.close()
        else:
            customer_operations_file = open(customer_login.var + ".txt", "a")
            customer_operations_file.write("\n"+converter)
            customer_operations_file.close()

    print("\nThe deposit was made successfully")
    customer_menu()

def customer_page():
#This function contains the options for customers weather they are new or current customers
#Customers can either login or fill the registeration form by navigating this function

    print("What do you want to do ?")

    print("\n1- Log into my account")
    print("2- Register a new account")
    print("3- Go back to the previous menu")
    print("Type the operation number here :")

    while True:
        user_login_choice = int(input())
        if user_login_choice == 1:
            customer_login()
        elif user_login_choice == 2:
            print("Hi there,"
                  "\nyou will be asked to provide some information in order for our admin staff to register you into the database\n")
            customer_registeration_form()
        elif user_login_choice == 3:
            welcome_menu()
        else:
            print("Sorry, invalid entery")


def customer_registeration_form():
#This is the function that is used by new customer to fill in their data and save it for later until an admin checks it and approve the account opening request

    customer_name = input("First, type in your first and last name : ").upper()

    print("Now, create an ID for yourself that you can use then to login to your account"
          "\nThe ID should NOT contain any white spaces")

#While loop to make sure the user ID doesnt contain any white spaces
    while True:
        customer_ID = input().lower()
        if customer_ID == "":
            print("Customer ID can't be empty, try again")
            customer_registeration_form()
        if " " in customer_ID:
            print("White spaces detected"
                  "\nplease enter the ID again and make sure it does NOT contain any white spaces...")
        else:
            break

    print("Enter the year in which you were born : ")
    while True:
        customer_birth_year = int(input())
        if customer_birth_year > 2003:
            print("Sorry, your are underage and therefore not allowed to create a bank account"
                  "\nDon't forget to come back when you are old enough ;)")
            exit()
        else:
            break
    customer_birth_year = str(customer_birth_year)

    print("Lastly, specify the type of your account")

#While loop for choosing between current or savings account
    while True:
        account_type = input("press 1 if you want a savings account, or 2 if you want a current account : ")
        if account_type == "1":
            account_type = "Savings_Account"
            break
        elif account_type == "2":
            account_type = "Current_Account"
            break
        else:
            print(account_type, "is not a valid choice")

    registeraion_list = [customer_name, customer_ID, customer_birth_year, account_type]

    print(registeraion_list,
          "\nAbove are the details you have provided"
          "\nDouple check and type 'confirm' to proceed or type 'edit' to re-enter the details if there is something incorrect")

#Above is print function to print all the data the user has entered so he/she can make everything is correct
#Then this while loop takes the user's response and reacts accordingly
    while True:
        confirmation = input().lower()
        if confirmation == "confirm":
            break
        elif confirmation == "edit":
            customer_registeration_form()
            break
        else:
            print("Invalid entery, make sure you spell the word correctly")


    registeraion_file = " ".join(registeraion_list)

#After the new user approves the details they get stored in a text file by the try and except structure below
    try:
        registeraion_handler = open("customer_registerations", "a")
        registeraion_handler.write("\n" + registeraion_file)
        registeraion_handler.close()
    except:
        registeraion_handler = open("customer_registerations", "w")
        registeraion_handler.write(registeraion_file)
        registeraion_handler.close()

    print("Thank you for choosing ALPHA Bank"
          "\nOur admin staff will create your account as soon as possible"
          "\nHave a nice day :)")
    welcome_menu()


def welcome_menu():
#This is the first function to be used in the program and is considered as the head of the program
#It takes each user to their proper menu

    print("Welcome to ALPHA BANK")
    print("Please specify to which category you belong")

    print("\n1- Super Admin")
    print("2- Admin Staff")
    print("3- Customer")
    print("4- Exit")

    print('Enter the number of the category here : ')

#While loop to take input from the user and determine where to take him
    while True:
        user_choice = input()
        if user_choice == "1":
            super_admin_menu()
            break
        elif user_choice == "2":
            admin_staff_login()
            break
        elif user_choice == "3":
            customer_page()
            break
        elif user_choice == "4":
            exit()
        else:
            print("Invalid option, try again")


welcome_menu()