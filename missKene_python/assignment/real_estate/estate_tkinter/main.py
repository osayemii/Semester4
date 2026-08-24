"""Main file: builds the window, wires the buttons to the CRUD modules."""
import tkinter as tk
from tkinter import ttk, END

import db
import state
from add import Add
from read import Read
from update import Update
from delete import Delete
from show import Show
from images import browse_image


# Fill the entry fields when a row in the table is clicked
def on_row_select(event):
    selected = state.listdisplay.selection()
    if not selected:
        return
    values = state.listdisplay.item(selected[0], "values")
    for entry, value in zip(state.entries, values):
        entry.delete(0, END)
        entry.insert(0, value)


root = tk.Tk()
root.geometry('1000x700')
root.minsize(900, 620)
root.title("Osayemi's real estate marketing")

# ---------- Header (centered heading + sub-heading) ----------
header_frame = ttk.Frame(root)
header_frame.pack(fill='x', pady=(15, 5))

ttk.Label(header_frame, text="Real Estate Marketing", style='Title.TLabel').pack()
ttk.Label(header_frame, text="Welcome to Osayemi's real estate marketing Ltd.",
          style='Subtitle.TLabel').pack()

# ---------- Entry form: 4 fields on the left, 4 on the right ----------
form_frame = ttk.Frame(root)
form_frame.pack(pady=15)

left_form = ttk.Frame(form_frame)
left_form.grid(row=0, column=0, padx=30)

right_form = ttk.Frame(form_frame)
right_form.grid(row=0, column=1, padx=30)


def add_field(parent, row, label_text):
    ttk.Label(parent, text=label_text, style='Field.TLabel').grid(
        row=row, column=0, sticky='w', padx=(0, 10), pady=10)
    entry = ttk.Entry(parent, width=32, style='Wide.TEntry')
    entry.grid(row=row, column=1, pady=10)
    return entry


e1 = add_field(left_form, 0, "Property ID")
e2 = add_field(left_form, 1, "Name")
e3 = add_field(left_form, 2, "Description")
e4 = add_field(left_form, 3, "Address")

e5 = add_field(right_form, 0, "Size")
e6 = add_field(right_form, 1, "Country")
e7 = add_field(right_form, 2, "State")
e8 = add_field(right_form, 3, "Price")

# ---------- Image picker (one image per property) ----------
ttk.Button(right_form, text="Browse Image", command=browse_image,
           style='Action.TButton').grid(row=4, column=0, pady=10, sticky='w')

image_label = ttk.Label(right_form, text="No image selected", style='Field.TLabel')
image_label.grid(row=4, column=1, pady=10, sticky='w')

# ---------- Hand the widgets to the shared state module ----------
state.entries = [e1, e2, e3, e4, e5, e6, e7, e8]
state.image_label = image_label

e1.focus_set()

# ---------- Buttons ----------
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

ttk.Button(button_frame, text='Add', command=Add, style='Action.TButton',
           width=12).grid(row=0, column=0, padx=8)
ttk.Button(button_frame, text='Read', command=Read, style='Action.TButton',
           width=12).grid(row=0, column=1, padx=8)
ttk.Button(button_frame, text='Update', command=Update, style='Action.TButton',
           width=12).grid(row=0, column=2, padx=8)
ttk.Button(button_frame, text='Delete', command=Delete, style='Action.TButton',
           width=12).grid(row=0, column=3, padx=8)
ttk.Button(button_frame, text='Refresh', command=Show, style='Action.TButton',
           width=12).grid(row=0, column=4, padx=8)

# ---------- Table ----------
table_frame = ttk.Frame(root)
table_frame.pack(fill='both', expand=True, padx=15, pady=(5, 15))

cols = ("Property_id", "Name", "Description", "Address", "Size", "Country", "State", "Price")
col_widths = {"Property_id": 90, "Name": 120, "Description": 200, "Address": 140,
              "Size": 70, "Country": 90, "State": 90, "Price": 90}

listdisplay = ttk.Treeview(table_frame, columns=cols, show="headings",
                           style='Custom.Treeview')
for col in cols:
    listdisplay.heading(col, text=col)
    listdisplay.column(col, width=col_widths[col], anchor='center')

table_scrollbar = ttk.Scrollbar(table_frame, orient='vertical',
                                command=listdisplay.yview)
listdisplay.configure(yscrollcommand=table_scrollbar.set)

listdisplay.pack(side='left', fill='both', expand=True)
table_scrollbar.pack(side='right', fill='y')

listdisplay.bind("<<TreeviewSelect>>", on_row_select)

state.listdisplay = listdisplay

# ---------- Database setup + first load ----------
db.create_tables()
Show()

# ======================================================================
# STYLES
# ======================================================================
BG_COLOR = '#f4f6f8'
ACCENT_COLOR = '#b30000'
HEADING_BG = '#dfe6ea'

root.configure(bg=BG_COLOR)

style = ttk.Style(root)
if 'vista' in style.theme_names():
    style.theme_use('vista')  # Windows' native/inbuilt widget theme

style.configure('TFrame', background=BG_COLOR)
style.configure('TLabel', background=BG_COLOR, font=('Segoe UI', 10))
style.configure('Field.TLabel', background=BG_COLOR, font=('Segoe UI', 10, 'bold'))
style.configure('Title.TLabel', background=BG_COLOR, foreground=ACCENT_COLOR,
                font=('Calibri', 30, 'bold'))
style.configure('Subtitle.TLabel', background=BG_COLOR, foreground='#333333',
                font=('Segoe UI', 11))
style.configure('Wide.TEntry', padding=6)
style.configure('Action.TButton', font=('Segoe UI', 10, 'bold'), padding=8)
style.configure('Custom.Treeview', rowheight=26, font=('Segoe UI', 9))
style.configure('Custom.Treeview.Heading', font=('Segoe UI', 10, 'bold'),
                background=HEADING_BG)

root.mainloop()
