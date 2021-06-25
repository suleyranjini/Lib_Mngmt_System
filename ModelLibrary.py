from configparser import ConfigParser
from mysql.connector import MySQLConnection, Error

class DBConn:
    def __init__(self):
        
        self.filename="dbconfig.ini"
        self.section="py_mysql"
    
    def read_config(self):
        parser = ConfigParser()
        parser.read(self.filename)
        self.db={}
        if parser.has_section(self.section):
            items=parser.items(self.section)
            for item in items:
                self.db[item[0]]=item[1]
        else:
            raise Exception(f'{self.section} not found in the {self.filename} file')
        
        return self.db
    
    def connDB(self,dbparam):
        try:
            self.dbparam = dbparam
            #conn_param = self.dbparam
            #print(conn_param)
            self.conn = MySQLConnection(**self.dbparam)
            if self.conn.is_connected():
                print("Connection established")
                #print()
                self.cursor=self.conn.cursor()
            else:
                print("Connection Failure")
            
        except Error as e:
            print(e)
        
#         finally:
#             self.conn.close()
        
        return self.cursor,self.conn  
        

        

class User:
    def __init__(self,curObj,connObj):
        
        self.curObj=curObj
        self.connObj=connObj
    
    
    def check_user_cred(self,flg,user_id,pwd):
        present=False
        try:
            if flg==1:
                query="SELECT * FROM LIBRARIAN WHERE LIB_ID = %s"
                cols="(Lib ID, Lib Name, Password, Phone No., Email)"
            else:
                query="SELECT * FROM USERS WHERE ID = %s"
                cols="(User ID, User Name, Password, Phone No., Email, Late Fee)"
            self.curObj.execute(query,(user_id,))
            row=self.curObj.fetchone()
            if row:
                print()
                if row[2]==pwd:
                    print(cols)
                    print(row)
                    present=True

        except Error as e:
            print(e)
        #self.curObj.close()
        #self.connObj.close()
        return present
    
    
    # def check_user_exists(self,user_name,flg):
    #     present=False
    #     try:
            
    #         if flg==1:
    #             query="SELECT LIB_ID FROM LIBRARIAN WHERE NAME = %s"
    #         else:
    #             query="SELECT ID FROM USERS WHERE NAME = %s"
    
    #         self.curObj.execute(query,(user_name,))
    #         rows=self.curObj.fetchone()
    #         if rows:
    #             id=rows[0]
    #             present=True
    #             print(f"User having Login ID {id} already exists")
    #     except Error as e:
    #         print(e)
    #     self.curObj.close()
    #     self.connObj.close()
    #     return present
    
    def create_user(self,flg,user_name,pwd,ph_no,email):
        status=False
        try:
            if flg==1:
                ins_query="INSERT INTO LIBRARIAN(NAME,PASSWORD,PH_NO,EMAIL) VALUES(%s,%s,%s,%s)"
                args=(user_name,pwd,ph_no,email)
            else:
                ins_query="INSERT INTO USERS(NAME,PASSWORD,PH_NO,EMAIL) VALUES(%s,%s,%s,%s)"
                args=(user_name,pwd,ph_no,email)
            #args=(user_name,pwd,ph_no,email)
            self.curObj.execute(ins_query,args)
            id=self.curObj.lastrowid
            self.connObj.commit()
            status=True
        except Error as e:
            print(e)    
        #self.curObj.close()
        #self.connObj.close()
        return status,id


    
    def update_user_name(self,flg,user_id,user_name):
        status=False
        try:
            if flg==1:
                upd_query="UPDATE LIBRARIAN SET NAME = %s WHERE LIB_ID = %s"
            else:
                upd_query="UPDATE USERS SET NAME = %s WHERE ID = %s"
            
            args=(user_name,user_id)
            self.curObj.execute(upd_query,args)
            self.connObj.commit()
            status = True
        except Error as e:
            print(e)
        #self.curObj.close()
        #self.connObj.close()
        return status,user_id

    
    def update_ph_no(self,flg,user_id,ph_no):
        status=False
        try:
            if flg==1:
                upd_query="UPDATE LIBRARIAN SET PH_NO = %s WHERE LIB_ID = %s"
            else:
                upd_query="UPDATE USERS SET PH_NO = %s WHERE ID = %s"
            
            args=(ph_no,user_id)
            self.curObj.execute(upd_query,args)
            self.connObj.commit()
            status = True
        except Error as e:
            print(e)
        #self.curObj.close()
        #self.connObj.close()
        return status,user_id
    
    
    def update_email(self,flg,user_id,email):
        status=False
        try:
            if flg==1:
                upd_query="UPDATE LIBRARIAN SET EMAIL = %s WHERE LIB_ID = %s"
            else:
                upd_query="UPDATE USERS SET EMAIL = %s WHERE ID = %s"
            
            args=(email,user_id)
            self.curObj.execute(upd_query,args)
            self.connObj.commit()
            status = True
        except Error as e:
            print(e)
        #self.curObj.close()
        #self.connObj.close()
        return status,user_id
    
    def update_fees(self,flg,user_id,fees):
        status=False
        try:
            upd_query="UPDATE USERS SET FEES = %s WHERE ID = %s"
            args=(fees,user_id)
            self.curObj.execute(upd_query,args)
            self.connObj.commit()
            status = True
        except Error as e:
            print(e)
        #self.curObj.close()
        #self.connObj.close()
        return status,user_id
    
    def list_user(self):
        try:
            
            query="SELECT * FROM USERS"
            #args=(id,)
            self.curObj.execute(query)
            rows=self.curObj.fetchall()
            if rows:
                for row in rows:
                    print("(User ID,User Name,Password,Phone No.,Email,Late Fee)")
                    print()
                    print(row)
            else:
                print("There are no users to display")
        except Error as e:
            print(e)
        #self.curObj.close()
        #self.connObj.close()
        return
    
    def delete_user(self,user_id):
        status=False
        try:
            del_query="DELETE FROM USERS WHERE ID = %s"
            args=(user_id,)
            self.curObj.execute(del_query,args)
            self.connObj.commit()
            status = True
        except Error as e:
            print(e)
        #self.curObj.close()
        #self.connObj.close()
        return status,user_id    

class Book:
    
    def __init__(self,curObj,connObj):
        
        self.curObj=curObj
        self.connObj=connObj
    
    
    def check_book_exists(self,book_name='', author='',book_id=0):
        present=False
        stock=0

        try:
            
            if book_id==0:
                #print("IN here *********")
                query="SELECT * FROM BOOKS WHERE BOOK_NAME = %s AND AUTHOR = %s"
                self.curObj.execute(query,(book_name,author,))
            else:
                #print("IN here $$$$$$$$$$")
                query="SELECT * FROM BOOKS WHERE BOOK_ID = %s"
                self.curObj.execute(query,(book_id,))
            rows=self.curObj.fetchone()
            if rows:
                book_id=rows[0]
                stock=rows[4]
                present=True 
        except Error as e:
            print(e)
        
        #self.curObj.close()
        #self.connObj.close()
        #print(f"Book id {book_id}, rent date {rent_date}, rent user {rent_user_id}, stock {stock}")
        return present,stock,book_id
    
    
    def insert_book(self,book_name, author, pubcomp):
        status=False
        try:
            ins_query="INSERT INTO BOOKS(BOOK_NAME,AUTHOR,PUBLICATION_COMPANY,STOCK) VALUES(%s,%s,%s,%s)"
            args=(book_name, author, pubcomp,1)
            self.curObj.execute(ins_query,args)
            book_id=self.curObj.lastrowid
            self.connObj.commit()
            status = True
        except Error as e:
            print(e)
        #self.curObj.close()
        #self.connObj.close()
        return status,book_id
    
    def update_stock(self,book_id,stock):
        status=False
        try:
            upd_query="UPDATE BOOKS SET STOCK = %s WHERE BOOK_ID = %s"
            args=(stock,book_id)
            self.curObj.execute(upd_query,args)
            self.connObj.commit()
            status = True
        except Error as e:
            print(e)
        #self.curObj.close()
        #self.connObj.close()
        return status,book_id
    
    def list_book(self):
        try:
            
            query="SELECT * FROM BOOKS"
            self.curObj.execute(query)
            rows=self.curObj.fetchall()
            if rows:
                for row in rows:
                    print("(Book ID,Book Name,Author,Publication Co,Stock)")
                    print()
                    print(row)
            else:
                print('There are no books to display')
        
        except Error as e:
            print(e)
        #self.curObj.close()
        #self.connObj.close()
        return
    
    def list_book_user(self,user_id):
 
        try:
            
            query="SELECT BU.BOOK_ID, BOOK_NAME, BU.RENTED_USER_ID, NAME, BU.RENTED_DATE FROM BOOK_USER BU \
                    INNER JOIN BOOKS B ON BU.BOOK_ID=B.BOOK_ID \
                    INNER JOIN USERS U ON BU.RENTED_USER_ID=U.ID \
                    WHERE BU.STATUS=0 AND BU.RENTED_USER_ID= %s"
            args=(user_id,)
            self.curObj.execute(query,args)
            rows=self.curObj.fetchall()
            if rows:
                print("[Book ID,Book Name,Rented User ID,Rented User,Rented Date]")
                print()
                for row in rows:
                    print(row)
                    
            
        except Error as e:
            print(e)
        return

    def return_book_user(self,user_id,book_id):
        status=False
        rent_date=None
        
        try:
            
            query="SELECT BU.BOOK_ID, BOOK_NAME, BU.RENTED_USER_ID, NAME, BU.RENTED_DATE FROM BOOK_USER BU \
                    INNER JOIN BOOKS B ON BU.BOOK_ID=B.BOOK_ID \
                    INNER JOIN USERS U ON BU.RENTED_USER_ID=U.ID \
                    WHERE BU.STATUS=0 AND BU.RENTED_USER_ID= %s AND BU.BOOK_ID = %s"
            args=(user_id,book_id)
            self.curObj.execute(query,args)
            rows=self.curObj.fetchone()
            if rows:
                rent_date=rows[4]
                status=True
            
        except Error as e:
            print(e)
        return status,rent_date

    def update_book_name(self,book_id,book_name):
        status=False
        try:
            upd_query="UPDATE BOOKS SET BOOK_NAME = %s WHERE BOOK_ID = %s"
            args=(book_name,book_id)
            self.curObj.execute(upd_query,args)
            self.connObj.commit()
            status = True
        except Error as e:
            print(e)
        #self.curObj.close()
        #self.connObj.close()
        return status,book_id
    
    def update_author(self,book_id,author):
        status=False
        try:
            upd_query="UPDATE BOOKS SET AUTHOR = %s WHERE BOOK_ID = %s"
            args=(author,book_id)
            self.curObj.execute(upd_query,args)
            self.connObj.commit()
            status = True
        except Error as e:
            print(e)
        #self.curObj.close()
        #self.connObj.close()
        return status,book_id

    def update_pubcomp(self,book_id,pubcomp):
        status=False
        try:
            upd_query="UPDATE BOOKS SET PUBLICATION_COMPANY = %s WHERE BOOK_ID = %s"
            args=(pubcomp,book_id)
            self.curObj.execute(upd_query,args)
            self.connObj.commit()
            status = True
        except Error as e:
            print(e)
        #self.curObj.close()
        #self.connObj.close()
        return status,book_id
    
    def delete_book(self,book_id):
        status=False
        try:
            del_query="DELETE FROM BOOKS WHERE BOOK_ID = %s"
            #print(f"${book_id}$")
            args=(book_id,)
            self.curObj.execute(del_query,args)
            self.connObj.commit()
            status = True
        except Error as e:
            print(e)
        #self.curObj.close()
        #self.connObj.close()
        return status,book_id
    
    def insert_rented_user(self,book_id,rent_user,rent_date):
        status=False
        try:
            
            ins_query="INSERT INTO BOOK_USER(BOOK_ID,RENTED_USER_ID,RENTED_DATE) VALUES (%s,%s,%s)"
            args=(book_id,rent_user,rent_date)
            self.curObj.execute(ins_query,args)
            self.connObj.commit()
            status = True
        except Error as e:
            print(e)
        #self.curObj.close()
        #self.connObj.close()
        return status,book_id
     
    def update_return_date(self,book_id,user_id,return_date,final_fee):

        status=False
        try:
            upd_query="UPDATE BOOK_USER SET RETURN_DATE = %s, STATUS = 1, FEES = %s WHERE BOOK_ID = %s AND RENTED_USER_ID = %s AND STATUS = 0"
            args=(return_date,final_fee,book_id,user_id)
            self.curObj.execute(upd_query,args)
            self.connObj.commit()
            status = True
        except Error as e:
            print(e)

        return status,book_id
    
