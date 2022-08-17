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

def button():
    b = Button(text="Вивести результат:", command=output())
    b.pack()
id()

def output():
        cursor.execute("SELECT name, surname, email FROM button")
        info = cursor.fetchall() 
        messagebox.showinfo("Information", info)

root.mainloop()

cursor.close()