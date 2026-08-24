"""Image selection for a property (one image per row)."""
from tkinter import filedialog

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
