import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *
global e1
global e2
global e3
global e4
# global e5

db_host = "localhost"
db_user = "root"
db_password = ""
db_database = "studentdb_python"


#add function - (C)-CRUD
def Add():
	stuid = e1.get()
	stuname = e2.get()
	stuage = e3.get()
	city = e4.get()

	mysqldb=mysql.connector.connect(host=db_host,user=db_user, password=db_password,database=db_database)
	mycursor=mysqldb.cursor()
	try:
		sql = "INSERT INTO student_info (Stud_id,Name,Age,City) VALUES (%s, %s, %s, %s)"
		val = (stuid,stuname,stuage,city)
		mycursor.execute(sql, val)
		mysqldb.commit()
		lastid = mycursor.lastrowid
		messagebox.showinfo("information", "Student Record inserted successfully.")
		e1.delete(0, END)
		e2.delete(0, END)
		e3.delete(0, END)
		e4.delete(0, END)
		e1.focus_set()
	except Exception as e:
		print(e)
		mysqldb.rollback()
		mysqldb.close()


#read function - (R)-CRUD
def Read():
	stuid = e1.get()
	mysqldb=mysql.connector.connect(host=db_host,user=db_user, password=db_password,database=db_database)
	mycursor=mysqldb.cursor()
	try:
		sql = "SELECT Stud_id,Name,Age,City FROM student_info WHERE Stud_id= %s"
		val = stuid
		mycursor.execute(sql, val)
		records = mycursor.fetchone()
		e1.delete(0, END)
		e1.insert(0,records[0])
		e2.insert(0,records[1])
		e3.insert(0,records[2])
		e4.insert(0,records[3])

		e1.focus_set()

	except Exception as e:

		print(e)
		mysqldb.rollback()
		mysqldb.close()

#update function - (U)-CRUD
def Update():
	stuid = e1.get()
	stuname = e2.get()
	stuage = e3.get()
	city = e4.get()

	mysqldb=mysql.connector.connect(host=db_host,user=db_user, password=db_password,database=db_database)
	mycursor=mysqldb.cursor()
	try:
		sql = "UPDATE student_info SET Name= %s, Age= %s, City= %s WHERE Stud_id= %s"
		val = (stuname,stuage,city,stuid)
		mycursor.execute(sql, val)
		mysqldb.commit()
		lastid = mycursor.lastrowid
		messagebox.showinfo("information", "Student Record Updated successfully.")

		e1.delete(0, END)
		e2.delete(0, END)
		e3.delete(0, END)
		e4.delete(0, END)
		e1.focus_set()

	except Exception as e:
		print(e)
		mysqldb.rollback()
		mysqldb.close()

#delete function - (D)-CRUD
def Delete():
	stuid = e1.get()

	mysqldb=mysql.connector.connect(host=db_host,user=db_user, password=db_password,database=db_database)
	mycursor=mysqldb.cursor()

	try:
		sql = "DELETE FROM student_info WHERE Stud_id = %s"
		val = stuid
		mycursor.execute(sql, val)
		mysqldb.commit()
		lastid = mycursor.lastrowid
		messagebox.showinfo("information", "Student Record Deleted successfully.")

		e1.delete(0, END)
		e2.delete(0, END)
		e3.delete(0, END)
		e4.delete(0, END)
		e1.focus_set()

	except Exception as e:

		print(e)
		mysqldb.rollback()
		mysqldb.close()

#show function - sHOW ALL
def show():
	mysqldb=mysql.connector.connect(host=db_host,user=db_user, password=db_password,database=db_database)
	mycursor=mysqldb.cursor()
	children = listdisplay.get_children()
	for child in children:
		listdisplay.delete(child)
	mycursor.execute("SELECT Stud_id,Name,Age,City FROM student_info")
	records = mycursor.fetchall()

	for i, (Stud_id,Name,Age,City) in enumerate(records,start=1):
		listdisplay.insert("", "end", values=(Stud_id,Name,Age,City))
	mysqldb.close()



root = tk.Tk()
root.geometry("800x500")

tk.Label(root, text="Student Information", fg="green", font=("Calibri", 30)).place(x=300, y=5)
tk.Label(root, text="If you want to update or delete a record,", fg="black", font=("Calibri", 12)).place(x=300, y=60)
tk.Label(root, text="then enter the Student ID and click the Read button.", fg="black", font=("Calibri", 12)).place(x=300, y=80)
tk.Label(root, text="Student ID").place(x=10, y=10)
tk.Label(root, text="Name").place(x=10, y=50)
tk.Label(root, text="Age").place(x=10, y=90)
tk.Label(root, text="City").place(x=10, y=130)

e1 = tk.Entry(root)
e1.place(x=140, y=10)
e1.focus_set()

e2 = tk.Entry(root)
e2.place(x=140, y=50)

e3 = tk.Entry(root)
e3.place(x=140, y=90)

e4 = tk.Entry(root)
e4.place(x=140, y=130)

tk.Button(root, text="Add",command = Add,height=3, width=13).place(x=30, y=160)
tk.Button(root, text="Read",command = Read,height=3, width=13).place(x=140, y=160)
tk.Button(root, text="Update",command = Update,height=3, width=13).place(x=250, y=160)
tk.Button(root, text="Delete",command = Delete,height=3, width=13).place(x=360, y=160)
tk.Button(root, text="Refresh",command = show,height=3, width=13).place(x=470, y=160)

cols = ('Student_id', 'Name', 'Age','City')
listdisplay = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
	listdisplay.grid(row=1, column=0, columnspan=1)
	listdisplay.place(x=10, y=250)
show()
root.mainloop()
