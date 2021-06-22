# Lib_Mngmt_System
This application uses MVC architecture, MySQL Database and OOPs concepts to create a Library Management System.
There are three tables in the database - Librarian, User and Books. There is a foreign key relation between User and Books.
There are two actors - Librarian and Users. Librarian acts like an admin user and the users are the members of the library.
Depending on who logs into the system, a different menu is displayed to the logged in user.
A new librarian and user can register from the main menu.
A librarian has the following functionalities -
  can Add another Librarian
  can Update one's details such as name, phone and email
  can View Book details
  can Add Books
  can Update Book Details such as Name, Author, Publication Company
  can Update User Details such as name, phone and email
  can Delete Users
A member user has the following functionalities -
  can Update User Details such as name, phone and email
  can View Book details
  can Rent a Book
  can Return a rented Book

There are multiple validations on various user inputs. When a user rents a book, the Current Date and User gets updated in the Books table.
When user returns the book after 20 days, the Late Fee is calculated as Rs.20. Post that the daily rate gets incremented by 5 after every 5 days.
Late Fee after 30 days = 20+25+30
 
  
