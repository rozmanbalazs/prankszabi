from tkinter import *

root = Tk()
root.geometry("300x200")
root.resizable(False, False)
root.title("HACKED")
root.attributes("-fullscreen", True)
root.iconbitmap("favicon.ico")

textout = Label(root,text="" ,font=("roboto", 75))

def timed():
    root.config(bg="red")
    textout.config(text="HACKED", fg="blue", bg="red")
    textout.place(x=960, y=540, anchor=CENTER)
    root.after(500, timed1)

def timed1():
    root.config(bg="lime")
    textout.config(text="BY", fg="red", bg="lime")
    textout.place(x=960, y=540, anchor=CENTER)
    root.after(500, timed2)

def timed2():
    root.config(bg="blue")
    textout.config(text="SZABI", fg="lime", bg="blue")
    textout.place(x=960, y=540, anchor=CENTER)
    root.after(500, timed)

if 0 == 0:
    timed()

root.mainloop()