from tkinter import *

root = Tk()
root.option_add('font', 'consulor 26')
root.title("ToDoList")
root.geometry("400x400")

todo = Listbox(root, height=24, width=40)
todo.place(x=150,y=4)

mainloop()