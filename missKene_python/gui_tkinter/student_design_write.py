import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

global e1
global e2
global e3
global e4
global e5

db_host, db_user, db_password, db_database = 'localhost', 'root', '', 'Studentdb_python'

# Add function - (C)-> CRUD
def Add():
    stuid = e1.get()
    stuname = e2.get()
    stuage = e3.get()
    city = e4.get()
    
    mysqldb = mysql.connector.connect(host = db_host, user = db_user, password = db_password, database = db_database)
    mycursor = mysqldb.cursor()
    
    try:
        sql = "INSERT INTO student_info(Stud_id,Name,Age,City) VALUES (%s,%s,%s,%s)"
        val = (stuid,stuname,stuage,city)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("INFORMATION", "Student record inserted successfully.")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()
        

# Read function - (R)->CRUD
def Read():
    stuid = e1.get()