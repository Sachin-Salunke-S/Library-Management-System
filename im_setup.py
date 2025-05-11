import tkinter as tk
from PIL import Image, ImageTk

#Functions for the login process
def register_user():
    username = tk.Entry_username.get()
    password = tk.Entry_password.get()

    if username == "" or password == "":
        messagebox.showwarning("Input Error", "Please fill in both fields")
        return

    try:
        c.execute("INSERT INTO user (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        messagebox.showinfo("Success", "User registered successfully")
    except sqlite3.IntegrityError:
        messagebox.showwarning("Error", "Username already exists")

def login_user():
    username = tk.Entry_username.get()
    password = tk.Entry_password.get()

    c.execute("SELECT * FROM user WHERE username = ? AND password = ?", (username, password))
    result = c.fetchone()

    if result:
        messagebox.showinfo("Success", "Login successful")
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
    label_image = tk.Label(root, image=img)
    label_image.image = img  # Keep a reference to prevent garbage collection

    # Create a username tk.Label

    # Arrange the elements: image behind the username tk.Label
    label_image.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    # Center the image behind username

  # Pack the remaining elements
    label_username = tk.Label(root, text="Username")
    label_username.pack(pady=5)
    entry_username = tk.Entry(root)
    entry_username.pack(pady=5)

    label_password = tk.Label(root, text="Password")
    label_password.pack(pady=5)
    entry_password = tk.Entry(root, show='*')
    entry_password.pack(pady=5)

    button_register = tk.Button(root, text="Register", command=register_user)
    button_register.pack(pady=5)
    button_login = tk.Button(root, text="Login", command=login_user)
    button_login.pack(pady=5)


root = tk.Tk()
# Call the function with the path to your image file
create_image_label(root, 'lib.jpg')
root.title('Library Management System')
root.geometry('1010x530')
root.resizable(0, 0)
root.mainloop()
