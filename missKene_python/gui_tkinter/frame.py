import tkinter as tk
from tkinter import Frame
root = tk.Tk()

tframe = tk.Frame(root)
tframe.pack()

bframe = Frame(root)
bframe.pack(side="bottom")

lframe = Frame(root)
lframe.pack(side="left")

rframe = Frame(root)
rframe.pack()

tmessage = tk.Label(tframe, text="This is the first frame", fg="brown")
tmessage.pack()

bmessage = tk.Label(lframe, text="This is the second frame.", bg="red")
bmessage.pack()

dmessage = tk.Label(rframe, text="This is the third frame.", bg="blue", fg="white")
dmessage.pack()

root.mainloop()