import tkinter as tk
from tkinter import messagebox, font as tkfont

login = tk.Tk()
login.title("Book Store Management System")

# Create widgets
btn_font = tkfont.Font(family="Arial", size=10)

# Create labels
lb_title = tk.Label(login, text="Login to\nBook Store Management System", font=("Arial", 20, 'bold'), justify="center")
lb_usr = tk.Label(login, text="Username", font=("Arial", 13))
lb_pwd = tk.Label(login, text="Password", font=("Arial", 13))

# Create entry boxes
box_usr = tk.Entry(login, width=40, font=("Arial", 12), justify="center")
box_pwd = tk.Entry(login, width=40, font=("Arial", 12), justify="center", show="*")

# Create buttons
button_frame = tk.Frame(login)
button_frame.pack(side=tk.BOTTOM, pady=10)
btn_login = tk.Button(button_frame, text="Login", width=21, command=lambda: runme(login))
btn_exit = tk.Button(button_frame, text="Exit", width=21, command=login.quit)
btn_exit["font"] = btn_font
btn_exit.pack(side=tk.LEFT, padx=10)
btn_login["font"] = btn_font
btn_login.pack(side=tk.LEFT, padx=10)

# Style labels, entry boxes and buttons
lb_title.pack(side=tk.TOP, pady=15)
lb_usr.pack(side=tk.TOP, pady=5)
box_usr.pack(side=tk.TOP, pady=5)
lb_pwd.pack(side=tk.TOP, pady=5)
box_pwd.pack(side=tk.TOP, pady=5)

def runme(t: tk.Tk):
    input_usr = box_usr.get()
    input_pwd = box_pwd.get()

    if input_usr == "admin" and input_pwd == "admin":
        messagebox.showinfo(title="Success", message="Login successful as admin")
        t.destroy()
        # subprocess.call(["python", "admin.py"])
    elif input_usr == "staff" and input_pwd == "staff":
        messagebox.showinfo(title="Success", message="Login successful as staff")
        t.destroy()
        # subprocess.call(["python", "staff.py"])
    elif input_usr == "vuminh" and input_pwd == "npc":
        messagebox.showerror(title="STOP", message="dm vu minh")
        t.destroy()
        # subprocess.call(["python", "vuminh.py"])
    else:
        messagebox.showerror(title="Error", message="Invalid username or password\nPlease try again.")

login.mainloop()
