"""Update function -> crUd."""
from tkinter import messagebox

import db
import state
from helpers import get_form_values
from show import Show


def Update():
    values = get_form_values()          # (property_id, name, ..., price)
    property_id = values[0]

    conn = db.get_connection()
    cursor = conn.cursor()
    try:
        sql = ('UPDATE estate_info SET Name=%s, Description=%s, Address=%s, Size=%s, '
               'Country=%s, State=%s, Price=%s WHERE Property_id=%s')
        # reorder: everything after the id first, then the id for the WHERE clause
        cursor.execute(sql, values[1:] + (property_id,))

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
