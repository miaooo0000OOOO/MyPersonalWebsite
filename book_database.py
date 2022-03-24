import pymysql
from config import *
import time
import os


db = pymysql.connect(host=HOSTNAME, port=int(PORT),password=PASSWORD,database=DATABASE,user=USERNAME)

def upload_book(db, path):
    dirs = os.listdir(path)
    books_list = []

    for file in dirs:
        # if file.endswith("pdf"):
        if True:
            books_list.append({
            "book_name":file,
            "book_author":None
            })
    insert_batch(db, books_list)
            

def insert(db, book_name, book_author):
    sql_cmd = sql = 'INSERT INTO library( \
       BOOK_NAME, BOOK_AUTHOR) \
       VALUES ("%s",  "%s")' % \
       (book_name, book_author)
    with db.cursor() as cursor:
        cursor.execute(sql_cmd)
        db.commit()

def insert_batch(db, books_list):
    with db.cursor() as cursor:
        for book in books_list:
            book_name = book["book_name"]
            book_author = book["book_author"]

            sql_cmd = sql = 'INSERT INTO library( \
            BOOK_NAME, BOOK_AUTHOR) \
            VALUES ("%s",  "%s")' % \
            (book_name, book_author)
            
            cursor.execute(sql_cmd)
        
        db.commit()

def get_all_book(db):
    sql_cmd = 'SELECT * from %s' %\
        (DATABASE)
    with db.cursor() as cursor:
        cursor.execute(sql_cmd)
        return cursor.fetchall()

if __name__=='__main__':
    # book = {"book_name":"十万个为什么",
    # "book_author":"我"}
    # books = [book]*3
    # insert_batch(db, books)
    # print(get_all_book(db))
    upload_book(db, BOOKS_ROOT_PATH)
    # pass