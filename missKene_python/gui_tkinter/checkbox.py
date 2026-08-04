import tkinter as tk
root = tk.Tk()

tframe = tk.Frame(root)
tframe.pack()
bframe = tk.Frame(root)
bframe.pack(side=tk.BOTTOM)
lframe = tk.Frame(bframe)
lframe.pack(side=tk.LEFT)
rframe = tk.Frame(bframe)
rframe.pack()

def show_hobbies():
    if (read.get() & song.get()):
        dmessage = tk.Label(rframe, text="Reading books and Listening to songs", bg="blue", fg="white")
        dmessage.pack()
    elif (song.get()):
        dmessage = tk.Label(rframe, text="Listening to songs", bg="blue", fg="white")
        dmessage.pack()
    elif (read.get()):
        dmessage = tk.Label(rframe, text="Reading books", bg="blue", fg="white")
        dmessage.pack()
        
read = tk.IntVar()
song= tk.IntVar()

label1 = tk.Checkbutton(tframe, text="Reading books", variable=read, onvalue = 1, offvalue = 0).grid(column=0,row=0, sticky=tk.W)
label2 = tk.Checkbutton(tframe, text="Listening to songs", variable=song, onvalue = 1, offvalue = 0).grid(column=1, row=0, sticky=tk.W)
button1 = tk.Button(lframe, text="Click to display selected hobbies.", bg="red", padx=5, pady=5, command=show_hobbies)

button1.pack()
root.mainloop()