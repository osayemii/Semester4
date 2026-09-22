"""Database configuration and connection helpers."""
import hashlib
from datetime import datetime

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


def _add_column_if_missing(cursor, table, column, definition):
    """estate_info already exists on some machines without the newer
    columns (Status, Agent_id, Date_listed), so ALTER it in rather than
    assuming a fresh CREATE TABLE will add them."""
    cursor.execute(
        "SELECT COUNT(*) FROM information_schema.columns "
        "WHERE table_schema = %s AND table_name = %s AND column_name = %s",
        (DB_DATABASE, table, column),
    )
    if cursor.fetchone()[0] == 0:
        cursor.execute(f"ALTER TABLE {table} ADD COLUMN {column} {definition}")


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

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS agents(
            agent_id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            phone VARCHAR(30),
            username VARCHAR(50) UNIQUE NOT NULL,
            password_hash VARCHAR(64) NOT NULL
        )
    ''')

    # Additive columns on the existing estate_info table.
    _add_column_if_missing(cursor, 'estate_info', 'Status',
                            "VARCHAR(20) NOT NULL DEFAULT 'available'")
    _add_column_if_missing(cursor, 'estate_info', 'Agent_id', 'INT NULL')
    _add_column_if_missing(cursor, 'estate_info', 'Date_listed', 'DATETIME NULL')
    _add_column_if_missing(cursor, 'estate_info', 'Date_sold', 'DATETIME NULL')

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

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS enquiries(
            enquiry_id INT PRIMARY KEY AUTO_INCREMENT,
            Property_id VARCHAR(20) NOT NULL,
            buyer_name VARCHAR(100) NOT NULL,
            buyer_email VARCHAR(100) NOT NULL,
            message VARCHAR(500),
            date_sent DATETIME NOT NULL,
            handled TINYINT(1) NOT NULL DEFAULT 0,
            FOREIGN KEY (Property_id) REFERENCES estate_info(Property_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS viewings(
            viewing_id INT PRIMARY KEY AUTO_INCREMENT,
            Property_id VARCHAR(20) NOT NULL,
            Agent_id INT,
            buyer_name VARCHAR(100) NOT NULL,
            scheduled_for DATETIME NOT NULL,
            notes VARCHAR(300),
            FOREIGN KEY (Property_id) REFERENCES estate_info(Property_id),
            FOREIGN KEY (Agent_id) REFERENCES agents(agent_id)
        )
    ''')

    conn.commit()

    # Seed one default agent so the login screen is usable on first run.
    cursor.execute("SELECT COUNT(*) FROM agents")
    if cursor.fetchone()[0] == 0:
        create_agent(cursor, "Default Agent", "agent@example.com",
                     "0000000000", "admin", "admin123")
        conn.commit()

    conn.close()


def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def create_agent(cursor, name, email, phone, username, password):
    cursor.execute(
        "INSERT INTO agents (name, email, phone, username, password_hash) "
        "VALUES (%s, %s, %s, %s, %s)",
        (name, email, phone, username, hash_password(password)),
    )


def verify_agent(username, password):
    """Return the agent row as a dict if the credentials match, else None."""
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM agents WHERE username = %s", (username,))
    agent = cursor.fetchone()
    conn.close()
    if agent and agent['password_hash'] == hash_password(password):
        return agent
    return None


def now():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
