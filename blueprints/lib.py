from flask import Blueprint,render_template,url_for
import pymysql
from config import *
import math

def get_book_by_id(db, book_id):
    sql_cmd = 'SELECT * from %s where book_id=%d' %\
        (DATABASE, book_id)
    with db.cursor() as cursor:
        cursor.execute(sql_cmd)
        book_tp = cursor.fetchall()[0][1:]
        book = Book(*book_tp)
        return book

def get_all_books_list(db, number_of_books, one_row_of_books):
    '''
    >>> get_all_books_dict(db, 15,4)
    结构如下：
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0]]
    '''
    n = number_of_books
    m = one_row_of_books
    books = []
    k = 0
    for i in range(math.ceil(n/m)):
        books.append([])
        for j in range(m):
            if i == math.ceil(n//m) and j>=n%m:
                continue
            k += 1
            books[i].append(get_book_by_id(db, k))
            # books[i].append(0)
    return books

db = pymysql.connect(host=HOSTNAME, port=int(PORT),password=PASSWORD,database=DATABASE,user=USERNAME)


bp = Blueprint("lib", __name__, url_prefix="/")

class Book:
    def __init__(self, name, author, publish_time, cover):
        self.cover = cover
        self.name = name
        self.author = author
        self.publish_time = publish_time

# book = Book()
# three_books = [book]*4
# books = [three_books]*5
books = get_all_books_list(db, 286, 4)

@bp.route('/')
def lib():
    print(get_book_by_id(db, 1))
    return render_template('lib.html', books = books)
