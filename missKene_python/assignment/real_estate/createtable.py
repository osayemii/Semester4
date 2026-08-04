import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'real_estate'
)
cursor = conn.cursor()

# sql = '''
# CREATE TABLE IF NOT EXISTS estate_info(
#     Property_id VARCHAR(20) NOT NULL,
#     Name VARCHAR(100),
#     Description VARCHAR(300),
#     Address VARCHAR(100),
#     Size DOUBLE,
#     Country VARCHAR(50),
#     State VARCHAR(50),
#     Price DOUBLE
# )
# '''

sql = '''CREATE TABLE IF NOT EXISTS estate_image(
    id INT PRIMARY KEY AUTO_INCREMENT,
    Property_id VARCHAR(20) NOT NULL,
    FOREIGN KEY (Property_id) REFERENCES estate_info(Property_id),
    image_path VARCHAR(250) NOT NULL
    )'''

cursor.execute(sql)
print('Table created successfully.')
conn.close()