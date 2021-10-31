from tkinter import *
root = Tk()
def test():
    print("test")
    return NONE

Button(root, text="test" ,command=test).pack()

root.mainloop()