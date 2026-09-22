"""Enquiry inbox tab: list unhandled enquiries, mark them handled."""
from tkinter import ttk, messagebox

import db
import state


def build_enquiries_tab(parent):
    ttk.Button(parent, text="Refresh", command=refresh_enquiries).pack(
        anchor='w', padx=5, pady=5)

    columns = ("id", "property", "buyer_name", "buyer_email", "date")
    tree = ttk.Treeview(parent, columns=columns, show="headings", height=15)
    for col, label, width in [
        ("id", "ID", 40), ("property", "Property", 200),
        ("buyer_name", "Buyer", 140), ("buyer_email", "Email", 180),
        ("date", "Date", 150),
    ]:
        tree.heading(col, text=label)
        tree.column(col, width=width)
    tree.pack(fill='both', expand=True, padx=5, pady=5)
    tree.bind("<Double-1>", lambda e: view_enquiry())

    ttk.Button(parent, text="Mark Handled", command=mark_handled).pack(
        anchor='w', padx=5, pady=5)

    state.enquiries_tree = tree
    refresh_enquiries()


def refresh_enquiries():
    tree = state.enquiries_tree
    tree.delete(*tree.get_children())

    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT enquiries.enquiry_id, estate_info.Name, enquiries.buyer_name,
               enquiries.buyer_email, enquiries.date_sent
        FROM enquiries
        JOIN estate_info ON enquiries.Property_id = estate_info.Property_id
        WHERE enquiries.handled = 0
        ORDER BY enquiries.date_sent DESC
    ''')
    for row in cursor.fetchall():
        tree.insert("", "end", iid=row[0], values=row)
    conn.close()


def view_enquiry():
    selection = state.enquiries_tree.selection()
    if not selection:
        return
    values = state.enquiries_tree.item(selection[0], "values")
    messagebox.showinfo("Enquiry", f"Property: {values[1]}\nBuyer: {values[2]}\nEmail: {values[3]}")


def mark_handled():
    selection = state.enquiries_tree.selection()
    if not selection:
        messagebox.showinfo("No selection", "Please select an enquiry first.")
        return

    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE enquiries SET handled = 1 WHERE enquiry_id = %s",
                    (int(selection[0]),))
    conn.commit()
    conn.close()

    refresh_enquiries()
