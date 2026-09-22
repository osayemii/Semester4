"""Data access for the buyer-facing Flask site.

Reads the same real_estate MySQL database the Tkinter admin app writes
to (schema created by estate_tkinter/db.py). This module only reads,
except for add_enquiry which is the one write path buyers have.
"""
from datetime import datetime

import mysql.connector

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = ''
DB_DATABASE = 'real_estate'


def get_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_DATABASE,
    )


def search_properties(country=None, state=None, min_price=None, max_price=None):
    """Only ever returns 'available' listings, newest first. Includes each
    property's image_path (NULL if none) straight from estate_image, so the
    template knows whether a real image exists without guessing."""
    query = ("SELECT estate_info.Property_id, estate_info.Name, estate_info.Description, "
              "estate_info.Address, estate_info.Size, estate_info.Country, "
              "estate_info.State, estate_info.Price, estate_info.Status, "
              "estate_image.image_path "
              "FROM estate_info "
              "LEFT JOIN estate_image ON estate_info.Property_id = estate_image.Property_id "
              "WHERE estate_info.Status = 'available'")
    params = []

    if country:
        query += " AND estate_info.Country LIKE %s"
        params.append(f"%{country}%")
    if state:
        query += " AND estate_info.State LIKE %s"
        params.append(f"%{state}%")
    if min_price is not None:
        query += " AND estate_info.Price >= %s"
        params.append(min_price)
    if max_price is not None:
        query += " AND estate_info.Price <= %s"
        params.append(max_price)

    query += " ORDER BY estate_info.Date_listed DESC"

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    return rows


def get_property(property_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM estate_info WHERE Property_id = %s", (property_id,)
    )
    row = cursor.fetchone()
    conn.close()
    return row


def get_image(property_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM estate_image WHERE Property_id = %s", (property_id,)
    )
    row = cursor.fetchone()
    conn.close()
    return row


def get_agent(agent_id):
    if not agent_id:
        return None
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT name, email, phone FROM agents WHERE agent_id = %s",
                    (agent_id,))
    row = cursor.fetchone()
    conn.close()
    return row


def add_enquiry(property_id, buyer_name, buyer_email, message):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO enquiries (Property_id, buyer_name, buyer_email, message, "
        "date_sent, handled) VALUES (%s, %s, %s, %s, %s, 0)",
        (property_id, buyer_name, buyer_email, message,
         datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
    )
    conn.commit()
    conn.close()
