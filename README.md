# Bookshop Inventory System

## Overview

This Python program implements a simple inventory system for a bookshop. The system uses a CSV file to store books' data, including book ID, title, author, category, quantity, unit price, and total price. The system provides various functionalities such as reading data from the file, listing data, searching by title or author, adding a new book, deleting a book, updating stock, showing the total value of books, saving data, and exiting the program.

## Project Guidelines

### File Structure

- `lib.py`: The main Python script containing the bookshop inventory system.
- `data.csv`: CSV file containing the book data.

### Features

1. **Welcome Screen:**
   - Display a welcome screen with the bookshop's name and the names of all students who contributed to the project.

2. **Menu Options:**
      1. Read Data
      2. List Data
      3. Search by Title
      4. Search by Author
      5. Add a New Book
      6. Delete a Book
      7. Add to Current Stock
      8. Remove from Current Stock
      9. Show Total Value of Books
      10. Save Data
      11. Exit

3. **Read Data:**
   - Open and read the CSV file containing book data.
   - Print a success message along with the number of records (books) read.

4. **List Data:**
   - Display the content of the data file in a readable format.

5. **Search by Title:**
   - Prompt the user for a book title (or part of it).
   - Print data for all books with titles containing the given text.

6. **Search by Author:**
   - Prompt the user for a book author (or part of it).
   - Print data for all books with authors containing the given text.

7. **Add a New Book:**
   - Prompt for required data for a new book and add it to the database.

8. **Delete a Book:**
   - Prompt for Book ID and delete the corresponding book from the database.

9. **Add to Current Stock:**
   - Prompt for Book ID and quantity to add to its stock.
   - Update total price and display a success message.

10. **Remove from Current Stock:**
    - Prompt for Book ID and quantity to remove from its stock (not exceeding the current quantity).
    - Update total price and display a success message.

11. **Show Total Value of Books:**
    - Display a message with the total value of all books in the bookshop.

12. **Save Data:**
    - Update the data in the CSV file to reflect any changes.

13. **Exit:**
    - Print a goodbye message and exit the program.

### Documentation

- Ensure the code includes sufficient documentation using comments ('#') to explain the purpose of variables, functions, or any hard-to-understand parts of the code.

## Usage

1. Clone the repository to your local machine.
2. Run the `lib.py` script using Python.
3. Follow the on-screen menu to interact with the bookshop inventory system.

Feel free to customize the bookshop's name, student names, or any other details as needed.
