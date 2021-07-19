from select import select
from tkinter import *
import tkinter.scrolledtext as scrolledtext

from keyboard import press

Keyboard_App = Tk()
Keyboard_App.geometry('1050*250')
Keyboard_App.title("Master keyboard by Dominic")

equation = Tk.StringVar()
Dis_entry = Tk.entry(Keyboard_App, state='readonly', textvariable=equation)
Dis_entry.grid(rowspan=1, columnspan=100, padx=999, pady=20)

Keyboard_App.configure(bg='powder blue')

q = Tk.Button(Keyboard_App, text='Q', command=lambda: press('Q'))
q.grid(row=1, column=0, padx=6, pady=10)

w = Tk.Button(Keyboard_App, text='W', command=lambda: press('W'))
w.grid(row=1, column=1, padx=6, pady=10)

e = Tk.Button(Keyboard_App, text='E', command=lambda: press('E'))
e.grid(row=1, column=2, padx=6, pady=10)

r = Tk.Button(Keyboard_App, text='R', command=lambda: press('R'))
r.grid(row=1, column=3, padx=6, pady=10)

t = Tk.Button(Keyboard_App, text='T', command=lambda: press('T'))
t.grid(row=1, column=4, padx=6, pady=10)

y = Tk.Button(Keyboard_App, text='Y', command=lambda: press(Y))
y.grid(row=1, column=5, padx=6, pady=10)

i = Tk.Button(Keyboard_App, text='I', command=lambda: press('Q'))
i.grid(row=1, column=0, padx=6, pady=10)




def select(value):
    if value == "<-":
        txt = text.get(1.0, END)
        val = len(txt)
        text.delete(1.0, END)
        text.insert(1.0, txt[:val - 2])

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
    if button != 'space':
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
