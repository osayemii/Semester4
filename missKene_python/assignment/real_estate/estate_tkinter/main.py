"""Main file: builds the window, wires the buttons to the CRUD modules."""
import tkinter as tk
from tkinter import ttk, END

import db
import state
import login
from add import Add
from read import Read
from update import Update
from delete import Delete
from show import Show
from images import browse_image, load_image_for_property, delete_image
from enquiries_ui import build_enquiries_tab
from summary_ui import build_summary_tab


# Fill the entry fields when a row in the table is clicked
def on_row_select(event):
    selected = state.listdisplay.selection()
    if not selected:
        return
    values = state.listdisplay.item(selected[0], "values")
    for entry, value in zip(state.entries[:-1], values[:-1]):
        entry.delete(0, END)
        entry.insert(0, value)
    state.entries[-1].set(values[-1] if values[-1] else 'available')

    property_id = values[0]
    load_image_for_property(property_id)


def build_main_window(root):
    root.geometry('1000x700')
    root.minsize(900, 620)
    root.resizable(True, True)
    root.title("Osayemi's real estate marketing")

    # ---------- Header ----------
    header_frame = ttk.Frame(root)
    header_frame.pack(fill='x', pady=(15, 5))

    ttk.Label(header_frame, text="Real Estate Marketing", style='Title.TLabel').pack()
    ttk.Label(header_frame,
              text=f"Logged in as {state.current_agent['name']}",
              style='Subtitle.TLabel').pack()

    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True, padx=10, pady=10)

    listings_tab = ttk.Frame(notebook)
    enquiries_tab = ttk.Frame(notebook)
    summary_tab = ttk.Frame(notebook)

    notebook.add(listings_tab, text="Listings")
    notebook.add(enquiries_tab, text="Enquiries")
    notebook.add(summary_tab, text="Summary")

    build_listings_tab(listings_tab)
    build_enquiries_tab(enquiries_tab)
    build_summary_tab(summary_tab)

    apply_styles(root)

    Show()


def build_listings_tab(root):
    # ---------- Entry form: 3 fields each in left, middle, right groups ----------
    form_frame = ttk.Frame(root)
    form_frame.pack(pady=15)

    left_form = ttk.Frame(form_frame)
    left_form.grid(row=0, column=0, padx=25)

    middle_form = ttk.Frame(form_frame)
    middle_form.grid(row=0, column=1, padx=25)

    right_form = ttk.Frame(form_frame)
    right_form.grid(row=0, column=2, padx=25)

    def add_field(parent, row, label_text):
        ttk.Label(parent, text=label_text, style='Field.TLabel').grid(
            row=row, column=0, sticky='w', padx=(0, 10), pady=10)
        entry = ttk.Entry(parent, width=24, style='Wide.TEntry')
        entry.grid(row=row, column=1, pady=10)
        return entry

    e1 = add_field(left_form, 0, "Property ID")
    e2 = add_field(left_form, 1, "Name")
    e3 = add_field(left_form, 2, "Description")

    e4 = add_field(middle_form, 0, "Address")
    e5 = add_field(middle_form, 1, "Size")
    e6 = add_field(middle_form, 2, "Country")

    e7 = add_field(right_form, 0, "State")
    e8 = add_field(right_form, 1, "Price")

    ttk.Label(right_form, text="Status", style='Field.TLabel').grid(
        row=2, column=0, sticky='w', padx=(0, 10), pady=10)
    status_combo = ttk.Combobox(right_form, width=21, state='readonly',
                                 values=['available', 'under offer', 'sold', 'withdrawn'])
    status_combo.set('available')
    status_combo.grid(row=2, column=1, pady=10)

    # ---------- Image picker (one image per property) ----------
    image_frame = ttk.Frame(root)
    image_frame.pack(pady=(0, 10))

    ttk.Button(image_frame, text="Browse Image", command=browse_image,
               style='Action.TButton').pack(side='left', padx=(0, 10))

    image_label = ttk.Label(image_frame, text="No image selected", style='Field.TLabel')
    image_label.pack(side='left', padx=(0, 10))

    ttk.Button(image_frame, text="Delete Image", command=delete_image,
               style='Action.TButton').pack(side='left')

    # ---------- Hand the widgets to the shared state module ----------
    state.entries = [e1, e2, e3, e4, e5, e6, e7, e8, status_combo]
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

    # ---------- Table (shows 10 rows at a time; scroll for the rest) ----------
    table_frame = ttk.Frame(root)
    table_frame.pack(fill='x', padx=15, pady=(5, 15))

    cols = ("Property_id", "Name", "Description", "Address", "Size", "Country",
            "State", "Price", "Status")
    col_widths = {"Property_id": 80, "Name": 110, "Description": 170, "Address": 120,
                  "Size": 60, "Country": 80, "State": 80, "Price": 80, "Status": 90}

    listdisplay = ttk.Treeview(table_frame, columns=cols, show="headings",
                               height=10, style='Custom.Treeview')
    for col in cols:
        listdisplay.heading(col, text=col)
        listdisplay.column(col, width=col_widths[col], anchor='center')

    table_scrollbar = ttk.Scrollbar(table_frame, orient='vertical',
                                    command=listdisplay.yview)
    listdisplay.configure(yscrollcommand=table_scrollbar.set)

    listdisplay.pack(side='left', fill='x', expand=True)
    table_scrollbar.pack(side='right', fill='y')

    listdisplay.bind("<<TreeviewSelect>>", on_row_select)

    state.listdisplay = listdisplay


def apply_styles(root):
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


if __name__ == '__main__':
    db.create_tables()

    root = tk.Tk()
    login.show_login(root, lambda: build_main_window(root))
    root.mainloop()
