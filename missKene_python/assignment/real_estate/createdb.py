import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = ''
)

cursor = conn.cursor()
try:
    cursor.execute("CREATE DATABASE real_estate")
    print("Database created successfully.")
except:
    print("Database already exists")
    
conn.close()
