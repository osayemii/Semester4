import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'sales_record'
)

cursor = conn.cursor()
sql = '''CREATE TABLE IF NOT EXISTS products (
    product_id CHAR(10) NOT NULL,
    Name CHAR(80),
    price DOUBLE,
    stock INT
    )'''
cursor.execute(sql)
print("Table created successfully!")
conn.close()