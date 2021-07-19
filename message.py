from tkinter import*
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('messagebox')

# showinfo,showwarning, showerror, askquestion, askokcancel, askyesno


def popup():
    response = messagebox.showinfo("This is my popup!", "Hello world!")
    Label(root, text=response).pack()
    # if response=='yes'
    #Label(root, text="You clicked yes!").pack()
    #else:
    #   Label(root, text="You clicked no!").pack()


Button(root, text="popup", command=popup).pack()

mainloop()



