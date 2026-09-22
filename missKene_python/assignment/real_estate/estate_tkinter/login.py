"""Agent login screen, shown before the main window."""
from tkinter import ttk, messagebox

import db
import state


def show_login(root, on_success):
    """Build the login screen inside the given root window. Calls
    on_success() once a valid agent has logged in, and stores the
    agent on state.current_agent."""
    root.title("Agent Login")
    root.geometry("340x220")
    root.resizable(False, False)

    frame = ttk.Frame(root, padding=25)
    frame.pack(expand=True, fill='both')

    ttk.Label(frame, text="Real Estate Marketing", font=('Segoe UI', 14, 'bold')).grid(
        row=0, column=0, columnspan=2, pady=(0, 15))

    ttk.Label(frame, text="Username").grid(row=1, column=0, sticky='e', pady=6)
    username_entry = ttk.Entry(frame, width=22)
    username_entry.grid(row=1, column=1, pady=6)

    ttk.Label(frame, text="Password").grid(row=2, column=0, sticky='e', pady=6)
    password_entry = ttk.Entry(frame, width=22, show='*')
    password_entry.grid(row=2, column=1, pady=6)

    def attempt_login():
        agent = db.verify_agent(username_entry.get().strip(), password_entry.get())
        if agent:
            state.current_agent = agent
            frame.destroy()
            on_success()
        else:
            messagebox.showerror("Login failed", "Invalid username or password.")

    ttk.Button(frame, text="Login", command=attempt_login).grid(
        row=3, column=0, columnspan=2, pady=15)
    ttk.Label(frame, text="Default login: admin / admin123", foreground='gray').grid(
        row=4, column=0, columnspan=2)

    username_entry.focus_set()
    password_entry.bind('<Return>', lambda e: attempt_login())
