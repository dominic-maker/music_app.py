from select import select
from tkinter import *
import tkinter.scrolledtext as scrolledtext

Keyboard_App = Tk()
Keyboard_App.title("Master keyboard")
Keyboard_App.resizable(0, 0)


def select(value):
    if value == "<-":
        txt = text.get(1.0, END)
        val = len(txt)
        text.delete(1.0, END)
        text.insert(1.0, txt[:val-2])

    elif value == "space":
        text.insert(END, "")
    elif value == "Tab":
        text.insert(END, "")
    else:
        text.insert(END, value)


text = scrolledtext.ScrolledText(Keyboard_App, width=120, wrap=WORD, padx=10, pady=10, relief=RIDGE)
text.grid(row=1, columnspan=16)

buttons = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '< ', '7', '8', '9', '-',
           'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', '[', ']', '4', '5', '6', '+',
           'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', 'tab', '0', '1', '2', '3', '/',
           'caps', 'bskp', ';', '"', '-', '=', 'j', 'k', 'l', '[', ']', '4', '5', '6', '+', ]

varRow = 2
varCol = 0
for button in buttons:
    command = lambda x=button: select(x)
    if varRow != 8:
        Button(Keyboard_App, text=button, width=5, bg='black', fg='white', activebackground='black',
               relief=RIDGE, padx=8, pady=4, bd=4, command=command, ).grid(row=varRow, column=varCol)
    if button == 'space':
        Button(Keyboard_App, text=button, width=5, bg='black', fg='white', activebackground='black',
               relief=RIDGE, padx=180, pady=4, bd=6, command=command, ).grid(row=6, columnspan=16)

    varCol += 1
    if varCol > 14 and varRow == 2:
        varCol = 0
        varRow += 0
    if varCol > 14 and varRow == 3:
        varCol = 0
        varRow = 1

Keyboard_App.mainloop()


def press():
    return None