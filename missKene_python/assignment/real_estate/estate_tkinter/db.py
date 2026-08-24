"""Database configuration and connection helpers."""
import mysql.connector

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = ''
DB_DATABASE = 'real_estate'


def get_connection():
    """Return a fresh connection to the real_estate database."""
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_DATABASE,
    )


def create_tables():
    """Create the tables if they don't exist yet (safe to run every startup)."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS estate_info(
            Property_id VARCHAR(20) NOT NULL PRIMARY KEY,
            Name VARCHAR(100),
            Description VARCHAR(300),
            Address VARCHAR(100),
            Size DOUBLE,
            Country VARCHAR(50),
            State VARCHAR(50),
            Price DOUBLE
        )
    ''')

    # One image per property: Property_id is UNIQUE so a second image
    # for the same property is impossible at the database level.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS estate_image(
            id INT PRIMARY KEY AUTO_INCREMENT,
            Property_id VARCHAR(20) NOT NULL UNIQUE,
            image_path VARCHAR(250) NOT NULL,
            FOREIGN KEY (Property_id) REFERENCES estate_info(Property_id)
        )
    ''')

    conn.commit()
    conn.close()
