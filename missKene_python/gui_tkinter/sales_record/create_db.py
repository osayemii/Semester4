import mysql.connector

conn = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = ''
)

cursor = conn.cursor()
try:
    cursor.execute("CREATE DATABASE sales_record")
    print("Database created successfully!")
except mysql.connector.errors.DatabaseError:
    print("Error creatng database")
conn.close()