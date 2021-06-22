import re


def prompt_user():
    menu='''
    Main Menu
    ---------
    Press 1 for Librarian
    Press 2 for User
    Press 3 to Quit
    
    '''
    print(menu)
    choice=input()
    #print(choice)
    return choice

def options_prompt():
    menu='''
    Sub Menu
    --------
    Press 1 to Login
    Press 2 to Register
    Press 3 to Back to Main Menu
    
    '''
    print(menu)
    choice=input()
    #print(choice)
    return choice

    
def incorrect_choice():
    print("Invalid Option Selected.")
    return

def login_prompt():
    menu='''
    Login with your user ID and password
    -------------------------------------
    '''
    print(menu)
    id=0
    id=input("Enter your ID: ")
    while (not id.isnumeric()) or (id == '0'):
        id=input("Enter your ID: ")
    id=int(id)
    pwd=input("Enter your Password: ")
    #print(flg,id,pwd)
    #user_det=check_user_cred(id,pwd,flg)
    return id,pwd

def lib_menu():
    menu='''
    Librarian Menu
    --------------
    Press 1 to Add New Librarian
    Press 2 to Update Librarian Details
    Press 3 to View Book Details
    Press 4 to Add Books
    Press 5 to Update Books
    Press 6 to Delete Book
    Press 7 to Update User Details
    Press 8 to Delete User
    Press 9 to Logout
    
'''
    print(menu)
    choice3=input("Enter a valid number: ")
    while not choice3.isnumeric() or choice3 not in('1','2','3','4','5','6','7','8','9'):
        choice3=input("Enter a valid number: ")
    #print(choice)
    return choice3

def user_menu():
    menu='''
    User Menu
    ---------
    Press 1 to Update User Details
    Press 2 to View Book Details
    Press 3 to Rent Book
    Press 4 to Return Book
    Press 5 to Logout
    
    '''
    print(menu)
    choice3=input("Enter a number: ")
    while not choice3.isnumeric() or choice3 not in('1','2','3','4','5'):
        choice3=input("Enter a number: ")
    #print(choice)
    return choice3


def get_user():
    #print("INside get user###")
    user_name = (input("Please enter your username: ")).strip()
    while not user_name:
        print("User name is mandatory")
        user_name = (input("Please enter your username: ")).strip()
    user_name = user_name.title()
    pwd_1, pwd_2 = get_pwd()
    while pwd_1 != pwd_2:
        print("Passwords did not match. Re-enter password.")
        pwd_1, pwd_2 = get_pwd()
    ph_no = (input("Please enter phone no. of the user(not more than 10 digits): ")).strip()
    if ph_no:
        ph_no=check_phno(ph_no)
    email = (input("Please enter your email address: ")).strip()
    if email:
        email=check_email(email)
    return user_name, pwd_1,ph_no,email

def get_upd_lib_user(user_id):
    print(f"Update Details for User ID {user_id}")
    print("\n")
    user_name = (input("Please enter name of the user: ")).strip()
    if user_name:
        user_name = user_name.title()
    ph_no = (input("Please enter phone no. of the user(not more than 10 digits): ")).strip()
    if ph_no:
        ph_no=check_phno(ph_no)
    email = (input("Please enter your email address: ")).strip()
    if email:
        email=check_email(email)
    return user_name, ph_no, email

def get_pwd():
    pwd_1 = input("Please enter your password(not more than 8 chars): ")
    pwd_2 = input("Please re-enter your password(not more than 8 chars): ")
    
    while len(pwd_1)<=0 or len(pwd_1)>8:
        print("Password length is incorrect")
        pwd_1 = input("Please enter your password(not more than 8 chars): ")
        pwd_2 = input("Please re-enter your password(not more than 8 chars): ")
    return pwd_1, pwd_2

def check_phno(ph_no):
    while len(ph_no)>10:
            print("Phone number length is incorrect")
            ph_no = input("Please enter phone no. of the user(not more than 10 digits): ")
            
    return ph_no
   
def check_email(email):
    email = email.upper()
    regex=r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b'
    while len(email)>0 and not(re.search(regex,email)):
        print("Enter a valid Email ID")
        email = (input("Please enter your email address: ")).strip()
    return email
    
def get_book():
    book_name = (input("Please enter name of the book: ")).strip()
    while not book_name:
        print("Book name is mandatory")
        book_name = (input("Please enter name of the book: ")).strip()
    book_name = book_name.title()
    author = (input("Please enter author of the book: ")).strip()
    while not author:
        print("Author name is mandatory")
        author = (input("Please enter author of the book: ")).strip()
    author = author.title()
    pubcomp = (input("Please enter publication company: ")).strip()
    pubcomp=pubcomp.title()
    return book_name, author, pubcomp

def book_stock():
    choice = input("Do you want to update stock of book? Enter Y/N: ")
    while choice.upper() not in('Y','N'):
        print("Incorrect choice, enter Y or N")
        book_stock()
    return choice

def get_upd_book():
    book_id='0'
    while (not book_id.isnumeric()) or (book_id == '0'):
        book_id = (input("Please enter id of the book: ")).strip()
    book_id=int(book_id)
    book_name = (input("Please enter name of the book: ")).strip()
    if book_name:
        book_name = book_name.title()
    author = (input("Please enter author of the book: ")).strip()
    if author:
        author=author.title()
    pubcomp = (input("Please enter publication company: ")).strip()
    if pubcomp:
        pubcomp=pubcomp.title()
    stock = (input("Please enter number of books: ")).strip()
    return book_id,book_name, author, pubcomp,stock


def get_book_id():
    book_id='0'
    while (not book_id.isnumeric()) or (book_id == '0'):
        book_id = (input("Please enter id of the book: ")).strip()
    book_id=int(book_id)
    return book_id

def get_user_id():
    user_id='0'
    while (not user_id.isnumeric()) or (user_id == '0'):
        user_id = (input("Please enter id of the user: ")).strip()
    user_id=int(user_id)
    return user_id