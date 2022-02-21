
from tkinter import END, LEFT, ttk

import tkinter as tk

import sqlite3


def connect():

    connection = sqlite3.connect("C:\\Users\\gorob\\Desktop\\currenciesApp\\currencies.db")

    connection.commit()

    connection.close()

#Viev Data from DataBase
def viewData():

    connection = sqlite3.connect("C:\\Users\\gorob\\Desktop\\currenciesApp\\currencies.db")

    cursor = connection.cursor()

    cursor.execute("SELECT * from currencies")

    rows = cursor.fetchall()    

    for row in rows:
        tree.insert("", tk.END, values=row)        
    
    connection.close()
    
#Update Data from Database
def updateData():
    from currenciesDataBase import updateDataBase
    
# connect to the database

connect() 

root = tk.Tk()

tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4"), show='headings')

tree.column("#1", anchor=tk.CENTER)

tree.heading("#1", text="id")

tree.column("#2", anchor=tk.CENTER)

tree.heading("#2", text="currency")

tree.column("#3", anchor=tk.CENTER)

tree.heading("#3", text="price")

tree.column("#4", anchor=tk.CENTER)

tree.heading("#4", text="date_")

tree.pack()

button1 = tk.Button(text="Display data", command=viewData)
button2 = tk.Button(text="Update data", command=updateData)
button1.pack(side = tk.LEFT)
button2.pack(side=tk.RIGHT)
root.mainloop()