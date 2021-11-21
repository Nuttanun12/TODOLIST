from tkinter import *
import speech_recognition as sr
import sqlite3 as sq

conn = sq.connect('listname.db')
cur = conn.cursor()

root = Tk()
todolist = []
root.option_add('font', 'consulor 26')
root.title("ToDoList")
root.geometry("420x280")
r = sr.Recognizer()

listname = Entry(root, width=16, font=('Tahoma', 12))
listname.place(x=20, y=50)
todo = Listbox(root, height=12, width=25, font=('Tahoma'))
todo.place(x=180, y=23)

def speechtotext():
    with sr.Microphone() as source:
        audio_text = r.listen(source)
        try:
            todo.insert(END, r.recognize_google(audio_text, language='th'))
        except:
            pass

def addlist():
    text = listname.get()
    if len(text) >= 1:
        todo.insert(END, text)
        listname.delete(0, END)
    else:
        pass
    return NONE

def clearlist():
    todo.delete(0, END)

photo = PhotoImage(file= r"D:\System\Desktop\work\todolist_app\TODOLIST\Photo\microphone.png")
photoimage = photo.subsample(6,6)
Button(root, text="Add list" ,command=addlist ,width=20).place(x=20,y=90)
Button(root, image= photoimage,command=speechtotext).place(x=20, y=212)
Button(root, text="Clear list",width=20, command=clearlist).place(x=20,y=150)
Button(root, text="Remove list",width=20).place(x=20,y=120)
Label(root, text="List name :").place(x=20, y=30)
Button(root, text="Exit",width=20).place(x=20,y=180)

root.mainloop()