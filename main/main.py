from tkinter import *
from tkinter import messagebox
import speech_recognition as sr
import sqlite3 as sq

conn = sq.connect("list.db")
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS tasks (title text)')

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
            text = r.recognize_google(audio_text, language='th')
            todo.insert(END, text)
            cur.execute('insert into tasks values (?)',(text,))
            todolist.append(text)
            conn.commit()
        except:
            pass

def addlist():
    word = listname.get()
    if len(word) >= 1:
        todo.insert(END, word)
        listname.delete(0, END)
        todolist.append(word)
        cur.execute('INSERT INTO tasks VALUES (?)',(word,))
        conn.commit()
    else:
        pass
    return NONE

def updatelist():
    todo.delete(0,END)
    for i in todolist:
        todo.insert(END, i)

def delete():
    try:
        selete = todo.get(todo.curselection())
        if selete in todolist:
            todolist.remove(selete)
            updatelist()
            cur.execute('delete from tasks where title = ?',(selete))
            print(selete)
            conn.commit()
    except:
        pass


def clearlist():
    warn = messagebox.askyesno("DeleteALL", "Are you sure?")
    if warn:
        todo.delete(0, END)
        cur.execute('delete from tasks')
        todolist.clear()
        conn.commit()
    else:
        pass
    
def exit():
    root.destroy()

def retasks():
    for row in conn.execute("select title from tasks"):
        todo.insert(END, row)
        todolist.append(row)

photo = PhotoImage(file= r"microphone.png")
photoimage = photo.subsample(6,6)
Button(root, text="Add list" ,command=addlist ,width=20).place(x=20,y=90)
Button(root, image= photoimage,command=speechtotext).place(x=20, y=212)
Button(root, text="Clear list",width=20, command=clearlist).place(x=20,y=150)
Button(root, text="Remove list",width=20, command=delete).place(x=20,y=120)
Label(root, text="List name :").place(x=20, y=30)
Button(root, text="Exit",width=20, command=exit).place(x=20,y=180)

retasks()

root.mainloop()

conn.commit()
cur.close()