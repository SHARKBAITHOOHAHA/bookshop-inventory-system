import csv

# list of data
id = []
Title = []
Author = []
Category = []
Quantity = []
UPrice = []
TotalP = []

dash = "-" * 101


# -------------------------------------------------------------------
# Welcome screen
def welcome():
    print(dash)
    print("Welcome to Rare library")
    print(dash)
    print("Created by: ")
    print("             Mahmoud Ahmed")
    print(dash)


# -------------------------------------------------------------------
# Read the data and store it in 7 global lists
def read():
    global id
    global Title
    global Author
    global Quantity
    global Category
    global UPrice
    global TotalP
    id = []
    Title = []
    Author = []
    Category = []
    Quantity = []
    UPrice = []
    TotalP = []

    # Open and read the .csv file from the user and read all the data and put it into 7 lists
    # file opening
    File = open("data.csv")

    # reading data
    csv_data = csv.reader(File)

    # "firstinstance" to make sure that the first row is deleted from the data
    firstinstance = True
    for row in csv_data:
        if firstinstance:
            firstinstance = False
            continue

        # Stores data into the lists
        id.append(row[0])
        Title.append(row[1])
        Author.append(row[2])
        Category.append(row[3])
        Quantity.append(int(row[4]))
        UPrice.append(float(row[5]))
        TotalP.append(int(row[4]) * float(row[5]))
    print("Data has been read successfully")


# -------------------------------------------------------------------
# List all the data read by the program from the .csv file in a table
def data_list():
    print(dash)
    print("{:<6}{:^}{:^30}{:^}{:^20}{:^}{:^8}{:^}{:^8}{:^}{:^10}{:^}{:^11}".format("BookID", "|", "Title", "|", "Author", "|", "Category", "|", "Quantity", "|", "Unit Price", "|", "Total Price"))
    print(dash)
    # Read each line of the csv file
    for i in range(len(id)):
        print("{:<6}{:^}{:^30}{:^}{:^20}{:^}{:^8}{:^}{:^8}{:^}{:^10}{:^}{:^11}".format(id[i], "|", Title[i], "|", Author[i], "|", Category[i], "|", Quantity[i], "|", UPrice[i], "|", TotalP[i]))


# -------------------------------------------------------------------
# Search the data by book's title
def search_title():
    Name = input("Enter Book's Title: ")
    # lower case for more accurate output
    Name = Name.lower()
    print(dash)
    print("{:<6}{:^}{:^30}{:^}{:^20}{:^}{:^8}{:^}{:^8}{:^}{:^10}{:^}{:^11}".format("BookID", "|", "Title", "|", "Author", "|", "Category", "|", "Quantity", "|", "Unit Price", "|", "Total Price"))
    print(dash)
    for i in range(len(id)):
        if Title[i].lower().find(Name) != -1:
            print("{:<6}{:^}{:^30}{:^}{:^20}{:^}{:^8}{:^}{:^8}{:^}{:^10}{:^}{:^11}".format(id[i], "|", Title[i], "|", Author[i], "|", Category[i], "|", Quantity[i], "|", UPrice[i], "|", TotalP[i]))


# -------------------------------------------------------------------
# Search the data by book's author
def search_author():
    Name = input("Enter Book's Title: ")
    # lower case for more accurate output
    Name = Name.lower()
    print(dash)
    print("{:<6}{:^}{:^30}{:^}{:^20}{:^}{:^8}{:^}{:^8}{:^}{:^10}{:^}{:^11}".format("BookID", "|", "Title", "|", "Author", "|", "Category", "|", "Quantity", "|", "Unit Price", "|", "Total Price"))
    print(dash)
    for i in range(len(id)):
        if Author[i].lower().find(Name) != -1:
            print("{:<6}{:^}{:^30}{:^}{:^20}{:^}{:^8}{:^}{:^8}{:^}{:^10}{:^}{:^11}".format(id[i], "|", Title[i], "|", Author[i], "|", Category[i], "|", Quantity[i], "|", UPrice[i], "|", TotalP[i]))


# -------------------------------------------------------------------
# Ask the user to enter the book's information and then add a new book to the data
def add_book():
    x = len(Title) + 1
    print("Please Enter Book details below")
    title = input("Enter the book's title: ")
    author = input("Enter the book's author name: ")
    cat = input("Enter category of the book: ")
    quan = int(input("Enter the quantity of the book: "))
    Uprice = float(input("Enter the price of the book: "))
    tp = Uprice * quan
    Title.append(title)
    Author.append(author)
    Category.append(cat)
    Quantity.append(quan)
    UPrice.append(Uprice)
    TotalP.append(tp)
    id.append(str(x))
    print("Book Added successfully")


# -------------------------------------------------------------------
# Ask the user to enter the book's ID and then remove the book from the data
def delete_book():
    ID = input("Enter Book's ID: ")
    for i in range(len(id)):
        if id[i].find(ID) != -1:
            Title.pop(i)
            Author.pop(i)
            Category.pop(i)
            Quantity.pop(i)
            UPrice.pop(i)
            TotalP.pop(i)
            id.pop(i)
            print("Book removed successfully")
            break


# -------------------------------------------------------------------
# Ask the user to enter the book's ID and then update the book's quantity to the data
def update_stock():
    ID = input("Enter Book's ID: ")
    quan = int(input("Enter the amount: "))
    for i in range(len(id)):
        if id[i].find(ID) != -1:
            Quantity[i] += quan
            # updates the total price of the stock
            TotalP[i] = UPrice[i] * Quantity[i]
            print("updated successfully")
            print(dash)
            print("{:<6}{:^}{:^30}{:^}{:^20}{:^}{:^8}{:^}{:^8}{:^}{:^10}{:^}{:^11}".format("BookID", "|", "Title", "|", "Author", "|", "Category", "|", "Quantity", "|", "Unit Price", "|",
                                                                                           "Total Price"))
            print(dash)
            print("{:<6}{:^}{:^30}{:^}{:^20}{:^}{:^8}{:^}{:^8}{:^}{:^10}{:^}{:^11}".format(id[i], "|", Title[i], "|", Author[i], "|", Category[i], "|", Quantity[i], "|", UPrice[i], "|", TotalP[i]))


# -------------------------------------------------------------------
# Ask the user to enter the book's ID and then remove the book's quantity from the data
def remove_stock():
    ID = input("Enter Book's ID: ")
    quan = int(input("Enter the amount: "))
    for i in range(len(id)):
        if Quantity[i] < quan:
            print("Please type a correct quantity")
            print(dash)
            continue
        if id[i].find(ID) != -1 and Quantity[i] >= quan:
            Quantity[i] -= quan
            # updates the total price of the stock
            TotalP[i] = UPrice[i] * Quantity[i]
            print("updated successfully")
            print(dash)
            print("{:<6}{:^}{:^30}{:^}{:^20}{:^}{:^8}{:^}{:^8}{:^}{:^10}{:^}{:^11}".format("BookID", "|", "Title", "|", "Author", "|", "Category", "|", "Quantity", "|", "Unit Price", "|",
                                                                                           "Total Price"))
            print(dash)
            print("{:<6}{:^}{:^30}{:^}{:^20}{:^}{:^8}{:^}{:^8}{:^}{:^10}{:^}{:^11}".format(id[i], "|", Title[i], "|", Author[i], "|", Category[i], "|", Quantity[i], "|", UPrice[i], "|", TotalP[i]))


# -------------------------------------------------------------------
# show the value of the books
def show_value():
    sum = 0
    for i in range(len(id)):
        sum += TotalP[i]
    print("The total value of the books is: ", sum)


# -------------------------------------------------------------------
# Save the current data to the database
def save():
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["BookID", "Title", "Author", "Category", "Quantity", "Unit Price", "Total Price"])
        for i in range(len(id)):
            writer.writerow([id[i], Title[i], Author[i], Category[i], str(Quantity[i]), str(UPrice[i]), str(TotalP[i])])
    print("Data has been saved successfully")


# -------------------------------------------------------------------
# Main program
welcome()


# -------------------------------------------------------------------
# Keeps the program running until the user enters 11 which will close the system
while True:
    print("\n1- Read data")
    print("2- List data")
    print("3- Search by title")
    print("4- Search by author")
    print("5- Add a new book")
    print("6- Delete a book")
    print("7- Add to the stock")
    print("8- Remove from the stock")
    print("9- Show total value of the books")
    print("10- Save data")
    print("11- Exit\n")

    option = int(input("Enter a number "))
    print(dash)
    if option == 1:
        # calls the read function when the user enters 1
        read()

    elif option == 2:
        # calls the data_list function when the user enters 2
        data_list()

    elif option == 3:
        # calls the search_title function when the user enters 3
        search_title()

    elif option == 4:
        # calls the search_author function when the user enters 4
        search_author()

    elif option == 5:
        # calls the add_book function when the user enters 5
        add_book()

    elif option == 6:
        # calls the delete_book function when the user enters 6
        delete_book()

    elif option == 7:
        # calls the update_stock function when the user enters 7
        update_stock()

    elif option == 8:
        # calls the remove_stock function when the user enters 8
        remove_stock()

    elif option == 9:
        # calls the show_value function when the user enters 9
        show_value()

    elif option == 10:
        # calls the save function when the user enters 10
        save()

    elif option == 11:
        # exit the program whenever the user enters 11
        print("Thank you")
        break

    else:
        # return a wrong message error whenever the user enters a wrong input
        print("Please choose a correct one ")
    print(dash)
