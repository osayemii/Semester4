import tkinter as tk
import mysql.connector
from tkinter import messagebox
from tkinter import ttk

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Sales_record"
)

cursor = db.cursor()

root = tk.Tk()
root.title("Osayemi's sales record")
root.geometry("800x800")


# ---------------- TITLE ----------------

tk.Label(
    root,
    text="Osayemi's sales record",
    font=("Arial", 30),
    fg="red"
).place(x=450, y=30)

tk.Label(
    root,
    text="sales record V.1 for K & K",
    font=("Arial", 14),
    fg="blue"
).place(x=450, y=90)


# ---------------- ITEMS ----------------

tk.Label(
    root,
    text="Items",
    font=("Arial", 25)
).place(x=490, y=130)


# ---------------- TABLE ----------------

columns = ("Product ID", "Name", "Price", "Stock")

table = ttk.Treeview(
    root,
    columns=columns,
    show="headings",
    height=20
)

table.heading("Product ID", text="Product ID")
table.heading("Name", text="Name")
table.heading("Price", text="Price")
table.heading("Stock", text="Stock")

table.column("Product ID", width=150)
table.column("Name", width=250)
table.column("Price", width=150)
table.column("Stock", width=150)

table.place(x=455, y=200)


# ---------------- NEW ITEMS ----------------

tk.Label(
    root,
    text="New Items",
    font=("Arial", 25)
).place(x=95, y=130)


# Product ID
tk.Label(
    root,
    text="Product ID",
    font=("Arial", 14),
    fg="blue"
).place(x=45, y=200)

product_id_entry = tk.Entry(root, width=28)
product_id_entry.place(x=175, y=200)


# Name
tk.Label(
    root,
    text="Name",
    font=("Arial", 14),
    fg="blue"
).place(x=45, y=250)

name_entry = tk.Entry(root, width=28)
name_entry.place(x=175, y=250)


# Price
tk.Label(
    root,
    text="Price",
    font=("Arial", 14),
    fg="blue"
).place(x=45, y=300)

price_entry = tk.Entry(root, width=28)
price_entry.place(x=175, y=300)


# Stock
tk.Label(
    root,
    text="Stock",
    font=("Arial", 14),
    fg="blue"
).place(x=45, y=350)

stock_entry = tk.Entry(root, width=28)
stock_entry.place(x=175, y=350)


def add_product():
    product_id = product_id_entry.get()
    name = name_entry.get()
    price = price_entry.get()
    stock = stock_entry.get()

    sql = "INSERT INTO products (product_id, Name, price, stock) VALUES (%s, %s, %s, %s)"
    values = (product_id, name, price, stock)

    cursor.execute(sql, values)
    db.commit()

    messagebox.showinfo("Success", "Product added successfully")
    refresh()


def read_products():
    table.delete(*table.get_children())

    cursor.execute("SELECT product_id, Name, price, stock FROM products")

    for row in cursor.fetchall():
        table.insert("", tk.END, values=row)


def update_product():
    product_id = product_id_entry.get()
    name = name_entry.get()
    price = price_entry.get()
    stock = stock_entry.get()

    sql = """
        UPDATE products
        SET Name=%s, price=%s, stock=%s
        WHERE product_id=%s
    """

    values = (name, price, stock, product_id)

    cursor.execute(sql, values)
    db.commit()

    messagebox.showinfo("Success", "Product updated successfully")
    refresh()


def delete_product():
    product_id = product_id_entry.get()

    sql = "DELETE FROM products WHERE product_id=%s"

    cursor.execute(sql, (product_id,))
    db.commit()

    messagebox.showinfo("Success", "Product deleted successfully")
    refresh()


def refresh():
    table.delete(*table.get_children())

    cursor.execute("SELECT product_id, Name, price, stock FROM products")

    for row in cursor.fetchall():
        table.insert("", tk.END, values=row)


# ---------------- BUTTONS ----------------

tk.Button(
    root,
    text="Add",
    height=3,
    width=13,
    command=add_product
).place(x=45, y=420)

tk.Button(
    root,
    text="Read",
    height=3,
    width=13,
    command=read_products
).place(x=165, y=420)

tk.Button(
    root,
    text="Update",
    height=3,
    width=13,
    command=update_product
).place(x=45, y=500)

tk.Button(
    root,
    text="Delete",
    height=3,
    width=13,
    command=delete_product
).place(x=165, y=500)

tk.Button(
    root,
    text="Refresh",
    height=3,
    width=13,
    command=refresh
).place(x=45, y=580)


root.mainloop()
