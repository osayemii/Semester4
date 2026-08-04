import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Studentdb_python"
)
cursor= conn.cursor()
sql = '''CREATE TABLE IF NOT EXISTS student_info(
    Stud_id CHAR(10) NOT NULL,
    Name CHAR(20),
    Age INT,
    City CHAR(80))
    '''
cursor.execute(sql)
print("Table created successfully")
conn.close()
