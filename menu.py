import tkinter
import os

def on_file_exit():
    root.quit()

root = tkinter.Tk()
root.title("Library Management System")
root.geometry("800x600")  # Set your desired initial window size
root.configure(bg="#808080")  # Grey background color

# Create a menu bar
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)

def about_us():
    os.system("about_us.txt")
# File menu
file_menu = tkinter.Menu(menu_bar, tearoff=False)
help_menu = tkinter.Menu(menu_bar, tearoff=False)
edit_menu = tkinter.Menu(menu_bar, tearoff=False)
view_menu = tkinter.Menu(menu_bar, tearoff=False)

menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label='Edit', menu=edit_menu)
menu_bar.add_cascade(label='View', menu=view_menu)
menu_bar.add_cascade(label='Help', menu=help_menu)
file_menu.add_command(label="Exit", command=on_file_exit)
help_menu.add_command(label = 'About Us', command=about_us)

# Other menu items (you can add more as needed)

# Make the window resizable
root.resizable(True, True)

root.mainloop()
