"""Add function -> Crud."""
from tkinter import messagebox

import db
import state
from helpers import clear_form, get_form_values
from show import Show


def Add():
    values = get_form_values()          # (property_id, name, ..., price)
    property_id = values[0]

    conn = db.get_connection()
    cursor = conn.cursor()
    try:
        sql = ("INSERT INTO estate_info"
               "(Property_id, Name, Description, Address, Size, Country, State, Price) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
        cursor.execute(sql, values)

        # save the chosen image path (if one was browsed) for this property
        if state.selected_image:
            img_sql = "INSERT INTO estate_image (Property_id, image_path) VALUES (%s, %s)"
            cursor.execute(img_sql, (property_id, state.selected_image))

        conn.commit()
        messagebox.showinfo("Information", "Data inserted successfully.")
        Show()
    except Exception as e:
        print(e)
        conn.rollback()
        messagebox.showerror("Error", str(e))
    finally:
        conn.close()
