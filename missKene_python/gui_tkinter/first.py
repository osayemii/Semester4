import tkinter as tk

root = tk.Tk()

message = tk.Label(root, text="Hello World")
message.pack(ipadx=50, ipady=50, expand=True)

message.mainloop()