import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

#Database setup
conn = sqlite3.connect('SQL/mydb.db')
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS user
          (username TEXT PRIMARY KEY,
          password TEXT NOT NULL)
          ''')
conn.commit()
#Functions for the login process
def register_user():
    username = entry_username.get()
    password = entry_password.get()

    if username == "" or password == "":
        messagebox.showwarning("Input Error", "Please fill in both fields")
        return

    try:
        c.execute("INSERT INTO user (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        messagebox.showinfo("Success", "User registered successfully")
        import library
        
        
    except sqlite3.IntegrityError:
        messagebox.showwarning("Error", "Username already exists")

def login_user():
    username = entry_username.get()
    password = entry_password.get()

    c.execute("SELECT * FROM user WHERE username = ? AND password = ?", (username, password))
    result = c.fetchone()

    if result:
        messagebox.showinfo("Success", "Login successful")
        import library
        
    else:
        messagebox.showwarning("Error", "Invalid username or password")
def create_image_label(root, image_path):
    
    # Open the image file
    img = Image.open(image_path)
    # Resize the image using PIL (Python Imaging Library)
    img = img.resize((1010, 530))
    # Convert the PIL image object into a PhotoImage object
    img = ImageTk.PhotoImage(img)

    # Create a tk.Label with the image
    label_image = Label(root, image=img)
    label_image.image = img  # Keep a reference to prevent garbage collection

    # Arrange the elements: image behind the username tk.Label
    label_image.place(relx=0.5, rely=0.5, anchor=CENTER)
    # Center the image behind username#UI setup 
root = Tk()
create_image_label(root, 'lib.jpg')
root.title('Library Management System')
root.geometry('1010x530')
root.resizable(0, 0)

# Initializing the main GUI window
lf_bg = 'LightSkyBlue'  # Left Frame Background Color
rtf_bg = 'SkyBlue'  # Right Top Frame Background Color
rbf_bg = 'DodgerBlue'  # Right Bottom Frame Background Color
btn_hlb_bg = 'SteelBlue'  # Background color for Head Labels and Buttons

lbl_font = ('Georgia', 13)  # Font for all labels
entry_font = ('Times New Roman', 12)  # Font for all Entry widgets
btn_font = ('Gill Sans MT', 13)
Label(root, text='LIBRARY MANAGEMENT SYSTEM', font=("Noto Sans CJK TC", 15, 'bold'), bg=btn_hlb_bg, fg='White').pack(side=TOP, fill=X)

label_username = Label(root, text="Username")
label_username.pack(pady=5)
entry_username = Entry(root)
entry_username.pack(pady=5)

label_password = Label(root, text="Password")
label_password.pack(pady=5)
entry_password = Entry(root, show='*')
entry_password.pack(pady=5)

button_register = Button(root, text="Register", command=register_user)
button_register.pack(pady=5)
button_login = Button(root, text="Login", command=login_user)
button_login.pack(pady=5)



root.mainloop()

#Close the database connection when the GUI is closed
conn.close()
