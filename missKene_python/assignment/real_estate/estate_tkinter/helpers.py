"""Small helpers shared by the CRUD modules."""
from tkinter import END

import state


def clear_form():
    """Empty all entry boxes, reset status/image, focus first field."""
    for entry in state.entries[:-1]:
        entry.delete(0, END)
    status_combo = state.entries[-1]
    status_combo.set('available')
    state.entries[0].focus_set()

    state.selected_image = None
    if state.image_label is not None:
        state.image_label.config(text="No image selected")


def get_form_values():
    """Return the 9 entry values (8 fields + status) in table order."""
    return tuple(entry.get() for entry in state.entries)


def set_image_label(path):
    """Show the full file location of a selected/loaded image on the label."""
    state.image_label.config(text=path)
