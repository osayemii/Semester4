"""Shared references to the GUI widgets.

main.py fills these in after building the window. Every other module
does `import state` and reads/writes these attributes, which avoids
passing widgets into every function and avoids circular imports.
"""

current_agent = None  # dict for the logged-in agent, set by login.py

entries = []          # [e1, e2, ..., status_combo] in form order
listdisplay = None    # the Treeview table of properties
image_label = None    # label that shows the chosen image filename
selected_image = None  # full path of the image picked for the current row

enquiries_tree = None      # Treeview table of unhandled enquiries
summary_frame = None       # frame the summary tab draws its labels into
