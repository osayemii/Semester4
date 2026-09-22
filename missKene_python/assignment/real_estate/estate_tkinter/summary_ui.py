"""Summary tab: totals + enquiries per property."""
from datetime import date
from tkinter import ttk

import db
import state


def first_day_of_this_month():
    return date.today().replace(day=1)


def first_day_of_next_month():
    today = date.today()
    if today.month == 12:
        return today.replace(year=today.year + 1, month=1, day=1)
    return today.replace(month=today.month + 1, day=1)


def build_summary_tab(parent):
    ttk.Button(parent, text="Refresh", command=refresh_summary).pack(
        anchor='w', padx=5, pady=5)

    frame = ttk.Frame(parent, padding=20)
    frame.pack(fill='both', expand=True)

    state.summary_frame = frame
    refresh_summary()


def refresh_summary():
    frame = state.summary_frame
    for widget in frame.winfo_children():
        widget.destroy()

    conn = db.get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM estate_info")
    total_listings = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM estate_info WHERE Status = 'sold' "
        "AND Date_sold >= %s AND Date_sold < %s",
        (first_day_of_this_month(), first_day_of_next_month()),
    )
    sold_this_month = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM enquiries")
    total_enquiries = cursor.fetchone()[0]

    ttk.Label(frame, text=f"Total listings: {total_listings}",
              font=('Segoe UI', 12)).pack(anchor='w', pady=3)
    ttk.Label(frame, text=f"Sold this month: {sold_this_month}",
              font=('Segoe UI', 12)).pack(anchor='w', pady=3)
    ttk.Label(frame, text=f"Total enquiries: {total_enquiries}",
              font=('Segoe UI', 12)).pack(anchor='w', pady=3)

    ttk.Label(frame, text="Enquiries per property:",
              font=('Segoe UI', 12, 'bold')).pack(anchor='w', pady=(15, 5))

    cursor.execute('''
        SELECT estate_info.Name, COUNT(enquiries.enquiry_id) AS total
        FROM estate_info
        LEFT JOIN enquiries ON estate_info.Property_id = enquiries.Property_id
        GROUP BY estate_info.Property_id
        ORDER BY total DESC
    ''')
    for name, total in cursor.fetchall():
        ttk.Label(frame, text=f"  {name}: {total}").pack(anchor='w')

    conn.close()
