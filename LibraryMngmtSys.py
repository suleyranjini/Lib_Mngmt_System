import datetime
from dateutil.relativedelta import relativedelta
import ViewLibrary as vl
import ModelLibrary as ml
import logging

def app_login():
    choice=None
    while choice !='3':
        choice=vl.prompt_user()#Librarian, User, Quit
        #print('*******',choice)
        if choice=='1':
            #print(f"choice 1 -> {choice}")
            flg=1
            options(flg)
        elif choice=='2':
            #print(f"choice 2 -> {choice}")
            flg=2
            options(flg)
        elif choice=='3':
            #print(f"choice 3 -> {choice}")
            quit_app()
        else:
            logging.warning(f"Invalid choice selected -> {choice}")
            #print(f"incorrect {choice}")
            vl.incorrect_choice()
            app_login()


def options(flg):
    choice2=vl.options_prompt()#Login, Register, Back
    #curObj,connObj=initialiseDB()
    #print('choice2-->',choice2)
    if choice2=='1':
        present,user_id=login_user(flg)
        #print("@@@@@",present)
        if present:
            #print(f"Flag {flg}++++++UserID{user_id}")
            enter_app(flg,user_id)
        else:
            options(flg)
    elif choice2=='2':
        status=register_lib_user(flg)
        options(flg)    
    
    elif choice2=='3':
        return
    
    else:
        logging.warning(f"Invalid choice selected -> {choice2}")
        #print(f"Incorrect Option {choice}")
        vl.incorrect_choice()
        options(flg)
                


def enter_app(flg,user_id):
    choice3=None
    #print("Entered Library Management System")
    if flg==1:
        choice3=vl.lib_menu()
        #print(f"App choice 3 -> {choice3}..ID -> {user_id}")
        lib_switcher(choice3,user_id)
    
    else:
        choice3=vl.user_menu()
        #print(f"App choice 3 -> {choice3}")
        usr_switcher(choice3,user_id)
        
def lib_switcher(choice3,user_id):
    #print(f"Inside lib switch {choice3},{user_id}")
    lib_switch = {
        '1':add_lib_user,
        '2':upd_lib,
        '3':view_book,
        '4':add_book,
        '5':upd_book,
        '6':del_book,
        '7':upd_lib_user,
        '8':del_user,
        '9':logout}

    # Get the function from switcher dictionary
    func = lib_switch.get(choice3, lambda: "Invalid choice")
    # Execute the function
    return func(1,user_id)


def usr_switcher(choice3,user_id):
    usr_switch = {
        '1': upd_user,
        '2': view_book,
        '3': rent_book,
        '4': return_book,
        '5': logout}
    # Get the function from switcher dictionary
    func = usr_switch.get(choice3, lambda: "Invalid choice")
    
    # Execute the function
    return func(2,user_id)

def initialiseDB():
    dbObj=ml.DBConn()
    dbparam=dbObj.read_config()
    curObj,connObj=dbObj.connDB(dbparam)
    return curObj,connObj                

def quit_app():
    logging.info("Exited LMS")
    print("Exiting Library Management System")

def logout(flg,user_id):
    logging.info("Logged out of LMS")
    print("Logging out of Library Management System")


def login_user(flg):
    pres = False
    while pres == False:
        user_id,pwd=vl.login_prompt()
        curObj,connObj=initialiseDB()
        userObj=ml.User(curObj,connObj)
        pres=userObj.check_user_cred(flg,user_id,pwd)
        if pres:
            logging.info(f"User {user_id} Logged In")
            print(f"User {user_id} logged in")
            print()
        else:
            logging.warning(f"Invalid login attempt -> {user_id}")
            print("Incorrect Login ID or Password")
        #print('User present',pres)
    return pres,user_id

def register_lib_user(flg):
    status = False
    while status == False:
        user_name,pwd,ph_no,email=vl.get_user()
        curObj,connObj=initialiseDB()
        userObj=ml.User(curObj,connObj)
        #print('params---',flg,user_name,pwd,ph_no,email)
        status,id=userObj.create_user(flg,user_name,pwd,ph_no,email)
        if status:
            logging.info(f"User {id} created")
            print(f"User created with Login ID: {id}")
    return status



def add_lib_user(flg,user_id):
    status = False
    while status == False:
        user_name,pwd,ph_no,email=vl.get_user()
        curObj,connObj=initialiseDB()
        userObj=ml.User(curObj,connObj)
        #print('params---',flg,user_name,pwd,ph_no,email)
        status,user_id1=userObj.create_user(flg,user_name,pwd,ph_no,email)
        if status:
            logging.info(f"User {user_id1} created")
            print(f"User created with Login ID: {user_id1}")
    enter_app(flg,user_id)

def upd_lib(flg,lib_id):
    status = False
    #print("^^^^^^^^^^^^")
    user_name, ph_no, email = vl.get_upd_lib_user(lib_id)
    status,lib_id=upd_usr_details(flg,user_name, ph_no, email,lib_id)
    enter_app(flg,lib_id)

def upd_user(flg,user_id):
    status = False
    user_name, ph_no, email = vl.get_upd_lib_user(user_id)
    status,user_id=upd_usr_details(flg,user_name, ph_no, email,user_id)
    enter_app(flg,user_id)


def upd_lib_user(flg,lib_id):
    status = False
    view_user()
    print('\n')
    user_id1=vl.get_user_id()
    user_name, ph_no, email = vl.get_upd_lib_user(user_id1)
    status,user_id1=upd_usr_details(2,user_name, ph_no, email,user_id1)
    enter_app(flg,lib_id)    

def upd_usr_details(flg,user_name, ph_no, email,id):
    status=False
    #upd_lst=[user_name, ph_no, email]
    #print(upd_lst)
    #if all(upd_lst):
    if not(user_name) and not(ph_no) and not(email):
        print("There is nothing to update")
        status=True
    
    else:
        #print(f"User ID -${user_id}$,User -${user_name}$,Ph No -${ph_no}$,Email -${email}$")
        
        if user_name:
            curObj,connObj=initialiseDB()
            userObj=ml.User(curObj,connObj)
            status,id=userObj.update_user_name(flg,id,user_name)
            if status:
                logging.info(f"User {id} updated")
                print(f"Name for ID {id} updated to {user_name}")
        if ph_no:
            curObj,connObj=initialiseDB()
            userObj=ml.User(curObj,connObj)
            status,id=userObj.update_ph_no(flg,id,ph_no)
            if status:
                logging.info(f"User {id} updated")
                print(f"Phone Number for ID {id} updated to {ph_no}")
        if email:
            curObj,connObj=initialiseDB()
            userObj=ml.User(curObj,connObj)
            status,id=userObj.update_email(flg,id,email)
            if status:
                logging.info(f"User {id} updated")
                print(f"Email Address for ID {id} updated to {email}")
    return status,id

def add_book(flg,user_id):
    status = False
    while status == False:
        book_name, author, pubcomp=vl.get_book()
        curObj,connObj=initialiseDB()
        bookObj=ml.Book(curObj,connObj)
        present,stock,book_id,rent_date,rent_user_id=bookObj.check_book_exists(book_name,author)
        if present:
            stock+=1
            choice=vl.book_stock()
            if choice.upper()=='Y':
                curObj,connObj=initialiseDB()
                bookObj=ml.Book(curObj,connObj)
                #print(f"Book ID ->{book_id} stock ->{stock}")
                status,book_id=bookObj.update_stock(book_id,stock)
                if status:
                    logging.info(f"Book {book_id} updated")
                    print(f"Stock for Book ID {book_id} updated to {stock}")
            else:
                break
        else:
            #print('params---',book_name, author, pubcomp)
            curObj,connObj=initialiseDB()
            bookObj=ml.Book(curObj,connObj)
            status,book_id=bookObj.insert_book(book_name,author,pubcomp)
            if status:
                logging.info(f"Book {book_id} inserted")
                print(f"Book with name {book_name} entered into Database")
    enter_app(flg,user_id)


def upd_book(flg,user_id):
    status = False
    view_upd_book()
    print('\n')
    book_id,book_name, author, pubcomp,stock=vl.get_upd_book()
    #upd_lst=[book_name,author,pubcomp,stock]
    #print(upd_lst)
    if not (book_name) and not(author) and not(pubcomp) and not(stock):
    #if all(upd_lst):
        print("There is nothing to update")
        status=True
    
    else:
        #print(f"Book ID -${book_id}$,Book -${book_name}$,Author -${author}$,Pub -${pubcomp}$,Stock -${stock}$")
        
        if book_name:
            curObj,connObj=initialiseDB()
            bookObj=ml.Book(curObj,connObj)
            status,book_id=bookObj.update_book_name(book_id,book_name)
            if status:
                logging.info(f"Book {book_id} updated")
                print(f"Book Name for Book ID {book_id} updated to {book_name}")
        if author:
            curObj,connObj=initialiseDB()
            bookObj=ml.Book(curObj,connObj)
            status,book_id=bookObj.update_author(book_id,author)
            if status:
                logging.info(f"Book {book_id} updated")
                print(f"Author for Book ID {book_id} updated to {author}")
        if pubcomp:
            curObj,connObj=initialiseDB()
            bookObj=ml.Book(curObj,connObj)
            status,book_id=bookObj.update_pubcomp(book_id,pubcomp)
            if status:
                logging.info(f"Book {book_id} updated")
                print(f"Publication Company for Book ID {book_id} updated to {pubcomp}")
        if stock.isnumeric() and stock != '0':
            stock=int(stock)
            curObj,connObj=initialiseDB()
            bookObj=ml.Book(curObj,connObj)
            status,book_id=bookObj.update_stock(book_id,stock)
            if status:
                logging.info(f"Book {book_id} updated")
                print(f"Stock for Book ID {book_id} updated to {stock}")
    enter_app(flg,user_id)
    

def del_book(flg,user_id):
    status = False
    view_upd_book()
    print('\n')
    book_id=vl.get_book_id()
    curObj,connObj=initialiseDB()
    bookObj=ml.Book(curObj,connObj)
    status,book_id=bookObj.delete_book(book_id)
    if status:
        logging.info(f"Book {book_id} deleted")
        print(f"Book with ID {book_id} deleted from Database")
    enter_app(flg,user_id)


def del_user(flg,user_id):
    status = False
    view_user()
    print('\n')
    user_id1=vl.get_user_id()
    curObj,connObj=initialiseDB()
    userObj=ml.User(curObj,connObj)
    status,user_id1=userObj.delete_user(user_id1)
    if status:
        logging.info(f"User {user_id1} deleted")
        print(f"User with ID {user_id1} deleted from Database")
    enter_app(flg,user_id)


def view_upd_book():
    curObj,connObj=initialiseDB()
    bookObj=ml.Book(curObj,connObj)
    bookObj.list_book()
    print('\n')
    return

def view_user():
    curObj,connObj=initialiseDB()
    userObj=ml.User(curObj,connObj)
    userObj.list_user()
    return

def view_book(flg,user_id):
    curObj,connObj=initialiseDB()
    bookObj=ml.Book(curObj,connObj)
    bookObj.list_book()
    enter_app(flg,user_id)

def return_book(flg,user_id):
    status = False
    view_upd_book()
    print('\n')
    book_id=vl.get_book_id()
    curObj,connObj=initialiseDB()
    bookObj=ml.Book(curObj,connObj)
    present,stock,book_id,rent_date,rent_user=bookObj.check_book_exists('','',book_id)
    #print(type(user_id),type(rent_user))
    if rent_user == user_id:

        if present and rent_date:
            rdelta=relativedelta(datetime.date.today(),rent_date)
            datediff=rdelta.days
            orig_fee,cfee,daily_fee,final_fee = 20,0,0,0
        
            if datediff == 20:
                final_fee = orig_fee
            elif datediff > 20:
                rate,dur,counter = 5,5,1
                #print(f" datediff {datediff},rate {rate}, dur {dur}, counter {counter}, cfee {cfee}")
                for day in range(1,(datediff - 20)):
                    if day > dur:
                        rate += 1
                        dur += 5
                        counter = 1
                        cfee = cfee + daily_fee
                    if day <= dur:
                        daily_fee = rate * counter
                        counter += 1
                    
                final_fee = orig_fee + cfee + daily_fee
            else:
                final_fee = 0
            print(final_fee)
            stock += 1
            curObj,connObj=initialiseDB()
            bookObj=ml.Book(curObj,connObj)
            status,book_id=bookObj.update_stock(book_id,stock)
            curObj,connObj=initialiseDB()
            bookObj=ml.Book(curObj,connObj)
            status,book_id=bookObj.update_rented_user(book_id,None)
            curObj,connObj=initialiseDB()
            bookObj=ml.Book(curObj,connObj)
            status,book_id=bookObj.update_rented_date(book_id,None)
            curObj,connObj=initialiseDB()
            userObj=ml.User(curObj,connObj)
            status,user_id1=userObj.update_fees(flg,user_id,final_fee)
            if status:
                logging.info(f"User {user_id} updated")
                print(f"Late Fees for ID {user_id} updated to Rs.{final_fee}/-")
        else:
            logging.info("No such Book in database")
            print(f"There is no such Book in the database")
    else:
        print("Logged in user has not rented this book")
    enter_app(flg,user_id)

def rent_book(flg,user_id):
    status = False
    view_upd_book()
    print('\n')
    book_id=vl.get_book_id()
    curObj,connObj=initialiseDB()
    bookObj=ml.Book(curObj,connObj)
    present,stock,book_id,rent_date,rent_user=bookObj.check_book_exists('','',book_id)
    
    if present:
        if stock>0:
            stock-=1
            rent_user=user_id
            rent_date=datetime.date.today()
            curObj,connObj=initialiseDB()
            bookObj=ml.Book(curObj,connObj)
            status,book_id=bookObj.update_stock(book_id,stock)
            curObj,connObj=initialiseDB()
            bookObj=ml.Book(curObj,connObj)
            status,book_id=bookObj.update_rented_user(book_id,rent_user)
            if status:
                logging.info(f"Book {book_id} updated")
                print(f"User {rent_user} has rented Book with ID {book_id}")
            curObj,connObj=initialiseDB()
            bookObj=ml.Book(curObj,connObj)
            status,book_id=bookObj.update_rented_date(book_id,rent_date)
            if status:
                logging.info(f"Book {book_id} updated")
                print(f"Book with ID {book_id} rented on {rent_date}")
        else:
            print(f"Book with id {book_id} is out of stock")
    else:
        logging.info("No such Book in database")
        print(f"There is no such Book in the database")
    enter_app(flg,user_id)




if __name__ == "__main__":
    logging.basicConfig(filename='lib_mngmt.log', filemode='a', format='%(asctime)s>>>%(process)d---%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
    app_login()