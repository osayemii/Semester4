"""Small helpers shared by the CRUD modules."""
from tkinter import END
import os

import state


def clear_form():
    """Empty all entry boxes, reset the image selection, focus first field."""
    for entry in state.entries:
        entry.delete(0, END)
    state.entries[0].focus_set()

    state.selected_image = None
    if state.image_label is not None:
        state.image_label.config(text="No image selected")


def get_form_values():
    """Return the 8 entry values in table order as a tuple."""
    return tuple(entry.get() for entry in state.entries)


def set_image_label(path):
    """Show just the filename of a selected/loaded image on the label."""
    state.image_label.config(text=os.path.basename(path))
