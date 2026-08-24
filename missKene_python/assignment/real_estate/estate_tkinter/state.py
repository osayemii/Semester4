"""Shared references to the GUI widgets.

main.py fills these in after building the window. Every other module
does `import state` and reads/writes these attributes, which avoids
passing eight entry widgets into every function and avoids circular
imports.
"""

entries = []          # [e1, e2, e3, e4, e5, e6, e7, e8] in form order
listdisplay = None    # the Treeview table
image_label = None    # label that shows the chosen image filename
selected_image = None  # full path of the image picked for the current row
