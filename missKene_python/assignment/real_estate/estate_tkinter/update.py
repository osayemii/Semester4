"""Update function -> crUd."""
from tkinter import messagebox

import db
import state
from helpers import get_form_values
from show import Show


def Update():
    values = get_form_values()          # (property_id, name, ..., price, status)
    property_id = values[0]
    status = values[8]

    conn = db.get_connection()
    cursor = conn.cursor()
    try:
        # Work out the sold date in plain Python (not SQL), so it's easy
        # to follow: stamp it the moment status becomes 'sold', clear it
        # if status moves off 'sold'. This is what lets the summary tab
        # report "sold this month" correctly.
        cursor.execute("SELECT Date_sold FROM estate_info WHERE Property_id=%s",
                        (property_id,))
        row = cursor.fetchone()
        old_date_sold = row[0] if row else None

        if status == 'sold':
            date_sold = old_date_sold if old_date_sold else db.now()
        else:
            date_sold = None

        sql = ('UPDATE estate_info SET Name=%s, Description=%s, Address=%s, Size=%s, '
               'Country=%s, State=%s, Price=%s, Status=%s, Date_sold=%s '
               'WHERE Property_id=%s')
        # reorder: everything after the id first, then the id for the WHERE clause
        cursor.execute(sql, values[1:8] + (status, date_sold, property_id))

        # insert the image row if it doesn't exist, replace the path if it does
        if state.selected_image:
            img_sql = ("INSERT INTO estate_image (Property_id, image_path) "
                       "VALUES (%s, %s) "
                       "ON DUPLICATE KEY UPDATE image_path = VALUES(image_path)")
            cursor.execute(img_sql, (property_id, state.selected_image))

        conn.commit()
        messagebox.showinfo("Information", "Data updated successfully.")
        Show()
    except Exception as e:
        print(e)
        conn.rollback()
        messagebox.showerror("Error", str(e))
    finally:
        conn.close()
