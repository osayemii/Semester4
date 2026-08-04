import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

global e1
global e2
global e3
global e4
global e5
global e6
global e7
global e8

db_host = 'localhost'
db_user = 'root'
db_password = ''
db_database = 'real_estate'

# Add function -> Crud
def Add():
    property_id = e1.get()
    name = e2.get()
    description = e3.get()
    address = e4.get()
    size = e5.get()
    country = e6.get()
    state = e7.get()
    price = e8.get()
    mysqldb = mysql.connector.connect(host=db_host, user=db_user, password=db_password, database=db_database)
    mycursor=mysqldb.cursor()
    try:
        sql = "INSERT INTO estate_info(Property_id,Name,Description,Address,Size,Country,State,Price) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (property_id,name,description,address,size,country,state,price)
        mycursor.execute(sql, val)
        mysqldb.commit()
        messagebox.showinfo("Information", "Data inserted successfully.")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e7.delete(0, END)
        e8.delete(0, END)
        e1.focus_set()
        Show()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


# Read function -> cRud
def Read():

    property_id = e1.get()
    mysqldb = mysql.connector.connect(host=db_host, user=db_user, password=db_password, database=db_database)
    mycursor=mysqldb.cursor()

    try:
        sql = 'SELECT Property_id,Name,Description,Address,Size,Country,State,Price FROM estate_info WHERE Property_id=%s'
        val = (property_id,)
        mycursor.execute(sql, val)
        records = mycursor.fetchone()
        e1.delete(0, END)
        e1.insert(0, records[0])
        e2.insert(0, records[1])
        e3.insert(0, records[2])
        e4.insert(0, records[3])
        e5.insert(0, records[4])
        e6.insert(0, records[5])
        e7.insert(0, records[6])
        e8.insert(0, records[7])

        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

# Update function -> crUd
def Update():
    property_id = e1.get()
    name = e2.get()
    description = e3.get()
    address = e4.get()
    size = e5.get()
    country = e6.get()
    state = e7.get()
    price = e8.get()
    mysqldb = mysql.connector.connect(host=db_host, user=db_user, password=db_password, database=db_database)
    mycursor=mysqldb.cursor()
    try:
        sql = 'UPDATE estate_info SET Name=%s, Description=%s, Address=%s, Size=%s, Country=%s, State=%s, Price=%s WHERE Property_id=%s'
        val = (name, description, address, size, country, state, price, property_id)
        mycursor.execute(sql, val)
        mysqldb.commit()
        messagebox.showinfo("Information", "Data updated successfully.")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e7.delete(0, END)
        e8.delete(0, END)
        e1.focus_set()
        Show()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


# Delete function -> cruD
def Delete():
    property_id = e1.get()
    mysqldb=mysql.connector.connect(host=db_host,user=db_user, password=db_password,database=db_database)
    mycursor=mysqldb.cursor()

    try:
        sql = 'DELETE FROM estate_info WHERE Property_id=%s'
        val = (property_id,)
        mycursor.execute(sql, val)
        mysqldb.commit()
        messagebox.showinfo("Information", f"Property with ID {property_id} deleted successfully.")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e7.delete(0, END)
        e8.delete(0, END)
        e1.focus_set()
        Show()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


# Show function - How all product
def Show():
    mysqldb=mysql.connector.connect(host=db_host,user=db_user, password=db_password,database=db_database)
    mycursor=mysqldb.cursor()
    children = listdisplay.get_children()

    for child in children:
        listdisplay.delete(child)

    mycursor.execute('SELECT Property_id,Name,Description,Address,Size,Country,State,Price FROM estate_info')
    records = mycursor.fetchall()
    
    for i, (Property_id,Name,Description,Address,Size,Country,State,Price) in enumerate(records,start=1):
        listdisplay.insert("", "end", values=(Property_id,Name,Description,Address,Size,Country,State,Price))
    mysqldb.close()
    
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    e1.focus_set()


# Fill the entry fields when a row in the table is clicked
def on_row_select(event):
    selected = listdisplay.selection()
    if not selected:
        return
    values = listdisplay.item(selected[0], "values")
    for entry, value in zip((e1, e2, e3, e4, e5, e6, e7, e8), values):
        entry.delete(0, END)
        entry.insert(0, value)

root = tk.Tk()
root.geometry('1000x650')
root.minsize(900, 600)
root.title("Osayemi's real estate marketing")

# ---------- Header (centered heading + sub-heading) ----------
header_frame = ttk.Frame(root)
header_frame.pack(fill='x', pady=(15, 5))

ttk.Label(header_frame, text="Real Estate Marketing", style='Title.TLabel').pack()
ttk.Label(header_frame, text="Welcome to Osayemi's real estate marketing Ltd.", style='Subtitle.TLabel').pack()

# ---------- Entry form: 4 fields on the left, 4 on the right ----------
form_frame = ttk.Frame(root)
form_frame.pack(pady=15)

left_form = ttk.Frame(form_frame)
left_form.grid(row=0, column=0, padx=30)

right_form = ttk.Frame(form_frame)
right_form.grid(row=0, column=1, padx=30)


def add_field(parent, row, label_text):
    ttk.Label(parent, text=label_text, style='Field.TLabel').grid(row=row, column=0, sticky='w', padx=(0, 10), pady=10)
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

e1.focus_set()

# ---------- Buttons ----------
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

ttk.Button(button_frame, text='Add', command=Add, style='Action.TButton', width=12).grid(row=0, column=0, padx=8)
ttk.Button(button_frame, text='Read', command=Read, style='Action.TButton', width=12).grid(row=0, column=1, padx=8)
ttk.Button(button_frame, text='Update', command=Update, style='Action.TButton', width=12).grid(row=0, column=2, padx=8)
ttk.Button(button_frame, text='Delete', command=Delete, style='Action.TButton', width=12).grid(row=0, column=3, padx=8)
ttk.Button(button_frame, text='Refresh', command=Show, style='Action.TButton', width=12).grid(row=0, column=4, padx=8)

# ---------- Table ----------
table_frame = ttk.Frame(root)
table_frame.pack(fill='both', expand=True, padx=15, pady=(5, 15))

cols = ("Property_id", "Name", "Description", "Address", "Size", "Country", "State", "Price")
col_widths = {"Property_id": 90, "Name": 120, "Description": 200, "Address": 140,
              "Size": 70, "Country": 90, "State": 90, "Price": 90}

listdisplay = ttk.Treeview(table_frame, columns=cols, show="headings", style='Custom.Treeview')
for col in cols:
    listdisplay.heading(col, text=col)
    listdisplay.column(col, width=col_widths[col], anchor='center')

table_scrollbar = ttk.Scrollbar(table_frame, orient='vertical', command=listdisplay.yview)
listdisplay.configure(yscrollcommand=table_scrollbar.set)

listdisplay.pack(side='left', fill='both', expand=True)
table_scrollbar.pack(side='right', fill='y')

listdisplay.bind("<<TreeviewSelect>>", on_row_select)

Show()

# ======================================================================
# STYLES
# All visual/theme configuration lives here, applied after every widget
# above already exists. ttk widgets look up their style by name at draw
# time (nothing is painted until root.mainloop() runs below), so
# configuring styles here still styles everything created above it.
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
style.configure('Title.TLabel', background=BG_COLOR, foreground=ACCENT_COLOR, font=('Calibri', 30, 'bold'))
style.configure('Subtitle.TLabel', background=BG_COLOR, foreground='#333333', font=('Segoe UI', 11))
style.configure('Wide.TEntry', padding=6)
style.configure('Action.TButton', font=('Segoe UI', 10, 'bold'), padding=8)
style.configure('Custom.Treeview', rowheight=26, font=('Segoe UI', 9))
style.configure('Custom.Treeview.Heading', font=('Segoe UI', 10, 'bold'), background=HEADING_BG)

root.mainloop()