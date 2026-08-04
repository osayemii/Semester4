import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
cursor = conn.cursor()
cursor.execute("CREATE DATABASE Studentdb_python")
print("Database created successfully")
conn.close()
