import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x260")

con = mysql.connector.connect(host='localhost',
                                database='base',
                                user='denis',
                                password='denis',
                                auth_plugin='mysql_native_password')

cursor = con.cursor()

def id():
    lbl = Label(text="Введіть свій id:")
    ent = Entry()
    btn = Button(text="Вивести результат:", command=output(ent, lbl2))
    lbl2 =Label(text="")
    lbl.pack()
    ent.pack()
    btn.pack()
    lbl2.pack()

id()

def output(ent, lbl2):
    if ent.get() !='':
        id = int(ent.get())
        cursor.execute("SELECT name, surname, email FROM button where id = {}".format(id))
        info = cursor.fetchall()
        lbl2.config(text="{}".format(info)) 

root.mainloop()

cursor.close()