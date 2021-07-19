from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("images")
root.iconbitmap("C:/Users/DOMINIC/PycharmProject/GUI project/images")

my_img1 = ImageTk.PhotoImage(Image.open("images/aspen.png"))
my_img2 = ImageTk.PhotoImage(Image.open("images/me1.png"))
my_img3 = ImageTk.PhotoImage(Image.open("images/me2.png"))
my_img4 = ImageTk.PhotoImage(Image.open("images/me3.png"))
my_img5 = ImageTk.PhotoImage(Image.open("images/me4.png"))
my_img6 = ImageTk.PhotoImage(Image.open("images/me4.png"))
my_img7 = ImageTk.PhotoImage(Image.open("images/me5.png"))
my_img8 = ImageTk.PhotoImage(Image.open("images/me6.png"))
my_img9 = ImageTk.PhotoImage(Image.open("images/me7.png"))
my_img10 = ImageTk.PhotoImage(Image.open("images/me8.png"))
my_img11 = ImageTk.PhotoImage(Image.open("images/me9.png"))
my_img12 = ImageTk.PhotoImage(Image.open("images/me10.png"))

image_list = [my_img1,  my_img2, my_img3, my_img4, my_img5, my_img6, my_img7, my_img8, my_img9, my_img10, my_img11, my_img12]

my_Label = Label(image=my_img2)
my_Label.grid(row=0, column=0, columnspan=3)


button_quit = Button(root, text="Exit program", command=root.quit)
button_quit.pack()

root.mainloop()

