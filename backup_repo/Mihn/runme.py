import sys
sys.dont_write_bytecode = True
import tkinter as tk
import subprocess
from tkinter import messagebox, font as tkfont

login = tk.Tk()
login.title("Book Store Management System")
# login.geometry = ('340x440')
background_main_color ='#333333'
text_color = '#FFFFFF'
login.configure(bg=background_main_color)
# login.resizable(False,False)  


# Create button widgets
btn_font = tkfont.Font(family="Arial", size=15,weight="bold")

# Create labels widgets
lb_title = tk.Label(login, text="Login to\nBook Store Management System", font=("Arial", 20, 'bold'), justify="center",bg=background_main_color,fg=text_color)
username_label = tk.Label(login, text="Username", font=("Arial", 15),bg=background_main_color,fg=text_color)
password_label = tk.Label(login, text="Password", font=("Arial", 15),bg=background_main_color,fg=text_color)

# Create entry boxes widgets
username_entry = tk.Entry(login, width=30, font=("Arial", 15, 'bold'), justify="center")
password_entry = tk.Entry(login, width=30, font=("Arial", 15, 'bold'), justify="center", show="*")


# Create button Frame
button_frame = tk.Frame(login, bg=background_main_color)

# Pack button frames
button_frame.pack(side=tk.BOTTOM, pady=10)

btn_login = tk.Button(button_frame, text="Login", width=21,bg='#FF3399',fg=text_color, command=lambda: runme(login))
btn_exit = tk.Button(button_frame, text="Exit",width = 21,bg='#FF0000',fg=text_color,command=login.quit)

btn_login["font"] = btn_font
btn_login.pack(side=tk.TOP)#, padx=10, expand=tk.YES)
btn_exit["font"] = btn_font
btn_exit.pack(side=tk.BOTTOM)#, padx=10, expand=tk.YES)

# Style labels, entry boxes and buttons

# def enter():
#     print("Enter pressed")
# password_entry.bind("<Return>",enter())

# Place widget on screen
lb_title.pack(side=tk.TOP, pady=15)
username_label.pack(side=tk.TOP, pady=5)
username_entry.pack(side=tk.TOP, pady=5)
password_label.pack(side=tk.TOP, pady=5)
password_entry.pack(side=tk.TOP, pady=5)



# Grid widgets
# lb_title.grid(row=0,column=0,columnspan=2,sticky='news')
# username_label.grid(row=1,column=0,sticky='news')
# username_entry.grid(row=1,column=1,sticky='news')
# password_label.grid(row=2,column=0,sticky='news')
# password_entry.grid(row=2,column=1,sticky='news')

def runme(t: tk.Tk):
    input_usr = username_entry.get()
    input_pwd = password_entry.get()

    if input_usr == "admin" and input_pwd == "admin":
        messagebox.showinfo(title="Success", message="Login successful as admin")
        t.destroy()
        subprocess.call(["python", "admin.py"])
    elif input_usr == "staff" and input_pwd == "staff":
        messagebox.showinfo(title="Success", message="Login successful as staff")
        t.destroy()
        subprocess.call(["python", "staff.py"])
    elif input_usr == "vuminh" and input_pwd == "npc":
        messagebox.showerror(title="STOP", message="dm vu minh! What are you doing here?")
        exit()
    else:
        messagebox.showerror(title="Error", message="Invalid username or password\nPlease try again.")

# enter_key = tk.Entry(login)
# username_entry.bind("<Return>", runme(login))

login.mainloop()