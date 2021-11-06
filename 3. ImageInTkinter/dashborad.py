from tkinter import *

root = Tk()
canvas = Canvas(root, width = 300, height = 300)
canvas.pack()
img = PhotoImage(file="Images/back.jpg")
canvas.create_image(20,20, anchor=NW, image=img)

if __name__ == '__main__':
    root.mainloop()