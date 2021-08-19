from tkinter import *

root = Tk()
root.option_add('font', 'consulor 26')
root.title("ToDoList")
root.geometry("400x250")

Button(root, text="list add",padx=60,).place(x=8,y=80)

todo = Listbox(root, height=13, selectmode='SINGLE')
todo.place(x=250,y=4)


mainloop()