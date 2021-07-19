from tkinter import *
import math as m
import tkinter.messagebox

root = Tk()
root.title("Advanced scientific calculator")
root.configure(background="powder blue")
root.resizable(width="false", height="false")
root.geometry("480x624+20+20")

Cacl = Frame(root)
Cacl.grid()

txtDisplay = Entry(Cacl, font=('arial', 30, 'bold'), bg="powder blue", bd=30, width=28, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=3, pady=1)
txtDisplay.insert(0, "0")

# ==================Numbers======================================================================================
def added_value():
    print("")


numberpad = "789456123"
i = 0
btn = []
for j in range(2, 5):
    for k in range(3):
        btn.append(Button(Cacl, width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="gray99", text=numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"] = lambda x=numberpad[i]: added_value.numberEnter(x)
        i += 1


# =============Menu=====================================================================================


def iExit():
    iExit = tkinter.messagebox.askyesno = "Advanced scientific calculator", "Confirm if you want to exit"
    if iExit > 0:
        root.destroy()
    return


def Scientific():
    root.resizable(width="false", height="false")
    root.geometry("944x568+0+0")


def Standard():
    root.resizable(width="false", height="false")
    root.geometry("480x568+0+0")


menubar = Menu(Cacl)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Standard")
filemenu.add_command(label="Scientific")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=iExit)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Copy")
editmenu.add_command(label="Cut")
editmenu.add_separator()
editmenu.add_command(label="Exit")

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="View help")




root.configure(menu=menubar)
root.mainloop()






