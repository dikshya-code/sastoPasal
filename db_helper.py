import sqlite3

def connect():
    return sqlite3.connect('sasto-pasal.db')


def execute_query(query):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

def fetch_data(query):
     connection = connect()
     cursor = connection.cursor()
     cursor.execute(query)
     records = cursor.fetchall()
     cursor.close()
     return records

def initiaize_db():
    create_product_table()
    delete_old_data()

def create_product_table():
    query = "CREATE TABLE IF NOT EXISTS products (id INTEGER, title TEXT,price REAL,description TEXT, category TEXT, image TEXT)"
    execute_query(query=query)

def delete_old_data():
    query = "DELETE FROM products"
    execute_query(query=query)

def insert_product_to_db(product_list):
    connection = connect()
    cursor = connection.cursor()
    for product in product_list:
        query = "INSERT INTO products(id, title, price, description, category, image) VALUES(?, ?, ?, ?, ?, ?)"
        cursor.execute(query, (product.id, product.title, product.price, product.description,product.category, product.image))
        connection.commit()