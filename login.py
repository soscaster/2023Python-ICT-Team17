import sys
sys.dont_write_bytecode = True
import tkinter as tk
import subprocess
import datetime
import zipfile
import os
import platform
from tkinter import messagebox, font as tkfont
from domains import sql_session
from domains import sql_store
import sqlite3

# Login Image "People illustrations" by Storyset
def hide():
    box_pwd.config(show="*")
    btn_eye.config(image=eye2)
    btn_eye.config(command=show)

def show():
    box_pwd.config(show="")
    btn_eye.config(image=eye)
    btn_eye.config(command=hide)

def exit_verify():
        # Verify if the user wants to exit the program
        box = messagebox.askquestion("Exit", "Are you sure you want to exit?")
        if box == "yes":
            messagebox.showinfo("Exit", "Thank you for using the program!\n© 2023 - BI12 - ICT Team 17")
            login.quit()
        else:
            pass

login = tk.Tk()
login.title("BSMS Beta - Login")
login.geometry("800x600")
login.resizable(False, False)
login.protocol("WM_DELETE_WINDOW", exit_verify)

# Create widgets
btn_font = tkfont.Font(family="Arial", size=15)

# Create image
img = tk.PhotoImage(file="img/login2.png")
eye = tk.PhotoImage(file="img/eye.png")
eye2 = tk.PhotoImage(file="img/eye-closed.png")
bg = tk.Label(login, image=img)
bg.place(x=0, y=0)

# Create labels
lb_title = tk.Label(login, text="Login to\nBook Store\nManagement System", font=("Arial", 23, 'bold'), justify="center", bg='white', fg='#318bd2')
lb_usr = tk.Label(login, text="ID/Username", font=("Arial", 15), bg='white', fg='#318bd2')
lb_pwd = tk.Label(login, text="Password", font=("Arial", 15), bg='white', fg='#318bd2')
lb_cpr = tk.Label(login, text="© 2023 - BI12 - ICT Team 17\nVersion BETA", font=("Arial", 6), bg='#73a2c7', justify="right", fg='white')

# Create entry boxes
box_usr = tk.Entry(login, width=31, font=("Arial", 12), relief='flat', borderwidth=0, fg='firebrick1', highlightthickness=0)
box_pwd = tk.Entry(login, width=31, font=("Arial", 12), relief='flat', borderwidth=0, fg='firebrick1', show="*", highlightthickness=0)

# Enter to jump to next entry box
box_usr.bind("<Return>", lambda event: box_pwd.focus())
# Enter event for entry boxes
box_pwd.bind("<Return>", lambda event: runme(login))

# Create lines for entry boxes
line_usr = tk.Canvas(login, width=282, height=2, bg='firebrick1', highlightthickness=0)
line_pwd = tk.Canvas(login, width=282, height=2, bg='firebrick1', highlightthickness=0)
line_usr.place(x=415, y=280)
line_pwd.place(x=415, y=360)

# Create buttons
btn_eye = tk.Button(image=eye2, bd=0, bg='white', activebackground='white', highlightthickness=0, cursor="hand2", command=show)
btn_eye.place(x=701, y=340)
btn_login = tk.Button(text="Login", width=23, bg='#318bd2', bd=0, activebackground='firebrick1', highlightthickness=0, command=lambda: runme(login))
btn_exit = tk.Button(text="Exit", width=23, bg='#318bd2', bd=0, activebackground='firebrick1', highlightthickness=0, command=exit_verify)
btn_login["font"] = btn_font
btn_login.place(x=417, y=420)
btn_exit["font"] = btn_font
btn_exit.place(x=417, y=470)

# Style labels, entry boxes and buttons
lb_title.place(x=402, y=100)
lb_usr.place(x=420, y=230)
box_usr.place(x=415, y=260)
lb_pwd.place(x=420, y=310)
box_pwd.place(x=415, y=340)
lb_cpr.place(x=690, y=3)

def runme(t: tk.Tk, event=None):
    # Extract the database file
    if os.path.exists("bookstore.dat"):
        with open("bookstore.dat", "rb") as f:
            with zipfile.ZipFile(f, "r") as zip_ref:
                zip_ref.extractall()
        if os.path.exists("bookstore.dat"):
            os.remove("bookstore.dat")
    else:
        pass
    log = sqlite3.connect("bookstore.db")
    cur = log.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS staff (id PRIMARYKEY text, password text, name text, dob text, address text, phone text, email text)")
    cur.execute("SELECT * FROM staff WHERE id = ? AND password = ?", (box_usr.get(), box_pwd.get()))
    data = cur.fetchall()

    input_usr = box_usr.get()
    input_pwd = box_pwd.get()

    time = str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    if platform.system() == "Windows":
        run_me = "python"
    elif platform.system() == "Linux":
        run_me = "python3"
    else:
        run_me = "python3"



    if data:
        # Get the name of the staff
        cur.execute("SELECT name FROM staff WHERE id = ? AND password = ?", (box_usr.get(), box_pwd.get()))
        name = cur.fetchone()[0]
        sql_session.Session().Insert(input_usr, name)
        messagebox.showinfo(title="Success", message=f"Login successful as:\n{name}\nLogin time: {time}")
        # Confirm if the store data table exists or not
        if len(sql_store.Database().Storage()) == 0:
            messagebox.showinfo(title="Store data error!", message="Store Information not found!\nPlease contact Administrator first!")
        t.destroy()
        log.close()
        subprocess.call([run_me, "staff.py"])
    elif input_usr == "admin" and input_pwd == "admin":
        id = "admin"
        name = "admin"
        sql_session.Session().Insert(id, name)
        messagebox.showinfo(title="Success", message=f"Login successful as:\nAdministrator\nLogin time: {time}")
        t.destroy()
        log.close()
        subprocess.call([run_me, "admin.py"])
    elif input_usr == "vuminh" and input_pwd == "npc":
        id = "vuminh"
        name = "vuminh"
        sql_session.Session().Insert(id, name)
        messagebox.showerror(title="STOP", message="dm vu minh!\nWhat are you doing here?")
        exit()
    else:
        messagebox.showerror(title="Error", message="Invalid username or password\nPlease try again.")

login.mainloop()
