"""Delete function -> cruD."""
from tkinter import messagebox

import db as db
import state as state
from show import Show


def Delete():
    property_id = state.entries[0].get()

    conn = db.get_connection()
    cursor = conn.cursor()
    try:
        # child rows first, otherwise the foreign keys block the delete
        cursor.execute("DELETE FROM estate_image WHERE Property_id=%s", (property_id,))
        cursor.execute("DELETE FROM enquiries WHERE Property_id=%s", (property_id,))
        cursor.execute("DELETE FROM viewings WHERE Property_id=%s", (property_id,))
        cursor.execute("DELETE FROM estate_info WHERE Property_id=%s", (property_id,))
        conn.commit()
        messagebox.showinfo("Information",
                            f"Property with ID {property_id} deleted successfully.")
        Show()
    except Exception as e:
        print(e)
        conn.rollback()
        messagebox.showerror("Error", str(e))
    finally:
        conn.close()
