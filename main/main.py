import tkinter as tk
from tkinter import messagebox
from tkinter import Listbox
from tkinter import Entry
from tkinter import END
from tkinter import Button
from tkinter import Label
from tkinter import PhotoImage
from tkinter.constants import DISABLED, NORMAL
import speech_recognition as sr
import sqlite3 as sq
import threading
import time

conn = sq.connect("list.db")
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS tasks (title text)')

root = tk.Tk()
todolist = []
root.option_add('font', 'consulor 26')
root.title("ToDoList")
root.geometry("420x280")
r = sr.Recognizer()
auto = False

listname = Entry(root, width=16, font=('Tahoma', 12))
listname.place(x=20, y=50)
todo = Listbox(root, height=12, width=25, font=('Tahoma'))
todo.place(x=180, y=23)

def speech_thread():
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
    threadspeech = threading.Thread(target=speechtotext)
    threadspeech.start()

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

def listen_thread():
    global auto
    auto = False
    b1['state'] = DISABLED
    b2['state'] = NORMAL
    def autospeechtotext():
        while True:
            try:
                with sr.Microphone() as source:
                    audio_text = r.listen(source)
                    text = r.recognize_google(audio_text, language='th')
                    print(text)
                    global auto
                    if auto:
                        break
                    if "ปิด" in text:
                        break
                    if "เพิ่ม" in text:
                        print("kanungnij")
                    
            except:
                pass
        b1['state'] = NORMAL
        b2['state'] = DISABLED
    threadauto = threading.Thread(target=autospeechtotext)
    threadauto.start()

def changer():
    global auto
    auto = True

    

photo = PhotoImage(file= r"microphone.png")
photoimage = photo.subsample(6,6)
Button(root, text="Add list" ,command=addlist ,width=20).place(x=20,y=90)
Button(root, image= photoimage,command=speech_thread).place(x=20, y=212)
Button(root, text="Clear list",width=20, command=clearlist).place(x=20,y=150)
Button(root, text="Remove list",width=20, command=delete).place(x=20,y=120)
Label(root, text="List name :").place(x=20, y=30)
Button(root, text="Exit",width=20, command=exit).place(x=20,y=180)
b1 = Button(root, text='ON', width=5,command=listen_thread)
b2 = Button(root, text='OFF', width=5,command=changer,state=DISABLED)
b1.place(x=70, y=220)
b2.place(x=120, y=220)

retasks()

root.mainloop()

auto = True
conn.commit()
cur.close()