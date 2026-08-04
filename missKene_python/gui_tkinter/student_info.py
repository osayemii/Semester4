import tkinter as tk 
from tkinter import ttk, messagebox 
import mysql.connector 
from tkinter import * 
 
root = tk.Tk() 
root.geometry("800x500") 
global e1 
global e2 
global e3 
global e4 
global e5 
 
tk.Label(root, text="Sales Information", fg="green", font=("Calibri", 30)).place(x=300, y=5) 
tk.Label(root, text="If you want to update or delete a record,", fg="black", font=("Calibri", 12)).place(x=300, y=60) 
tk.Label(root, text="then enter the Sales ID and click the Read button.", fg="black", font=("Calibri", 12)).place(x=300, y=80) 
tk.Label(root, text="Sales ID").place(x=10, y=10) 
tk.Label(root, text="Product Name").place(x=10, y=50) 
tk.Label(root, text="Quantity").place(x=10, y=90) 
tk.Label(root, text="City").place(x=10, y=130) 
 
e1 = tk.Entry(root) 
e1.place(x=140, y=10) 
 
e2 = tk.Entry(root) 
e2.place(x=140, y=50) 
 
e3 = tk.Entry(root) 
e3.place(x=140, y=90) 
 
e4 = tk.Entry(root) 
e4.place(x=140, y=130) 
 
tk.Button(root, text="Add",height=3, width=13).place(x=30, y=160) 
tk.Button(root, text="Read",height=3, width=13).place(x=140, y=160) 
tk.Button(root, text="Update",height=3, width=13).place(x=250, y=160) 
tk.Button(root, text="Delete",height=3, width=13).place(x=360, y=160)


root.mainloop()