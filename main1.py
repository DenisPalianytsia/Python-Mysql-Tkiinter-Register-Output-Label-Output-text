from multiprocessing import connection
import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import messagebox

root =  Tk()
root.title("Base")
root.geometry("300x260")

con = mysql.connector.connect(host='localhost',
                                database='base',
                                user='denis',
                                password='denis',
                                auth_plugin='mysql_native_password')

cursor = con.cursor()

def Entry():
    lbl1 = Label(text="Введіть своє ім'я: ")
    ent1 = Entry()
    lbl2 = Label(text="Введіть своє прізвище: ")
    ent2 = Entry()
    lbl3 = Label(text="Введіть свій email: ")
    ent3 = Entry() 
    btn = Button(text="Зберегти", command=save())
    lbl1.pack()
    lbl2.pack()
    lbl3.pack()
    btn.pack()
    
def save(ent1, ent2, ent3):
    if ent1.get() != '' and ent2.get() != ''and ent3.get() != '':
         cursor.execute('INSERT INTO button (name, surname, email) VALUES ("{}", "{}", "{}")'.format(ent1.get(), ent2.get(), ent3.get()))
         connection.comit()

    else:
        messagebox.showerror('Information', 'The line is empty') 

root.mainloop()

cursor.close()