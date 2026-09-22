"""Read function -> cRud."""
from tkinter import END, messagebox

import db as db
import state
from helpers import set_image_label


def Read():
    property_id = state.entries[0].get()

    conn = db.get_connection()
    cursor = conn.cursor()
    try:
        sql = ('SELECT Property_id, Name, Description, Address, Size, Country, State, '
               'Price, Status FROM estate_info WHERE Property_id=%s')
        cursor.execute(sql, (property_id,))
        record = cursor.fetchone()

        if record is None:
            messagebox.showwarning("Not found", f"No property with ID {property_id}.")
            return

        for entry, value in zip(state.entries[:-1], record[:-1]):
            entry.delete(0, END)
            entry.insert(0, value)
        state.entries[-1].set(record[-1] or 'available')
        state.entries[0].focus_set()

        # fetch this property's image path (if any)
        cursor.execute("SELECT image_path FROM estate_image WHERE Property_id=%s",
                       (property_id,))
        img_row = cursor.fetchone()
        if img_row:
            state.selected_image = img_row[0]
            set_image_label(img_row[0])
        else:
            state.selected_image = None
            state.image_label.config(text="No image on file")
    except Exception as e:
        print(e)
    finally:
        conn.close()
