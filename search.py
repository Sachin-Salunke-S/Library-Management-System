import sqlite3

from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as mb
import tkinter.simpledialog as sd
import os

connector = sqlite3.connect('library.db')
cursor = connector.cursor()

root = Tk()
root.title('Library Management System')
root.geometry('400x400')
root.resizable(True, True)

lf_bg = 'Grey'  # Left Frame Background Color
rtf_bg = 'Grey'  # Right Top Frame Background Color
rbf_bg = 'Grey'  # Right Bottom Frame Background Color
btn_hlb_bg = 'Grey'
Label(root, text='LIBRARY MANAGEMENT SYSTEM', font=("Noto Sans CJK TC", 15, 'bold'), bg=btn_hlb_bg, fg='White').pack(side=TOP, fill=X)

def search():
        query = entry_username.get()
        try:
            content = connector.execute('SELECT * FROM LIBRARY WHERE BK_ID=?',query)
            stmt = str(content.fetchone())[1:-1]
            stmt2 = stmt.replace(',','\n')
        except:
            stmt2 = 'Invalid BOOK ID\nPlease Enter VALID BOOK ID'
        mb.showinfo("Query Result", stmt2)

label_username = Label(root, text="ENTER BOOK ID")
label_username.pack(pady=5)
entry_username = Entry(root)
entry_username.pack(pady=5)
button_register = Button(root, text="Search", command=search)
button_register.pack(pady=5)
