from tkinter import *
import speechmodule

root = Tk()
root.option_add('font', 'consulor 26')
root.title("ToDoList")
root.geometry("350x250")

Label(root, text="List name :").place(x=20, y=30)
Button(root, text="Add list",width=20).place(x=20,y=90)
Button(root, text="Remove list",width=20).place(x=20,y=120)
Button(root, text="Clear list",width=20).place(x=20,y=150)
Button(root, text="Exit",width=20).place(x=20,y=180)

listname = Entry(root, width=25)
todo = Listbox(root, height=12, width=25,selectmode='SINGLE')
todo.place(x=180, y=23)
listname.place(x=20, y=50)

mainloop()