"""Image selection for a property (one image per row)."""
from tkinter import filedialog, messagebox

import db
import state
from helpers import set_image_label


def browse_image():
    """Open a file dialog and remember the single chosen image path."""
    path = filedialog.askopenfilename(
        title="Select property image",
        filetypes=[
            ("Image files", "*.png *.jpg *.jpeg *.gif *.bmp"),
            ("All files", "*.*"),
        ],
    )
    if path:
        state.selected_image = path
        set_image_label(path)


def load_image_for_property(property_id):
    """Show the image already on file for the given property, if any.
    Called when a row in the listings table is selected."""
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT image_path FROM estate_image WHERE Property_id=%s",
                    (property_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        state.selected_image = row[0]
        set_image_label(row[0])
    else:
        state.selected_image = None
        state.image_label.config(text="No image on file")


def delete_image():
    """Remove the current property's image row from the database."""
    property_id = state.entries[0].get()
    if not property_id:
        messagebox.showinfo("No selection", "Please select a property first.")
        return

    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM estate_image WHERE Property_id=%s", (property_id,))
    conn.commit()
    deleted = cursor.rowcount
    conn.close()

    state.selected_image = None
    state.image_label.config(text="No image selected")

    if deleted:
        messagebox.showinfo("Information", "Image deleted successfully.")
    else:
        messagebox.showinfo("No image", "This property has no image on file.")
