import tkinter as tk
from tkinter import messagebox, font as tkfont

# Database connection using sqlite3
# Functions: Modify store details - Add staff - Modify staff - Delete staff - View staff - Search staff by ID or name
# Store detail: store_id, store_name, store_address, store_phone, store_email
# Staff detail: st_ID, st_name, st_dob, st_address, st_phone, st_email
# Customer detail: cus_ID, cus_name, cus_dob, cus_address, cus_phone, cus_email

admin = tk.Tk()
admin.title("Book Store Management System - Loged in as admin")
frame = tk.Frame(admin)

# Create widgets
btn_font = tkfont.Font(family="Arial", size=15)

# Create labels
lbl_welcome = tk.Label(frame, text="Welcome to\nBook Store Management System", font=("Arial", 20, 'bold'), justify="center")
lbl_hihi = tk.Label(frame, text=" ", font=("Arial", 13))

# Create buttons
btn_store = tk.Button(frame, text="Modify Store Info", width=21, bg='#0052cc', fg='#ffffff')
btn_store['font'] = btn_font
btn_staff = tk.Button(frame, text="Modify Staff Info", width=21, bg='#00ab1c', fg='#ffffff')
btn_staff['font'] = btn_font
btn_customer = tk.Button(frame, text="Modify Customer Info", width=21, bg='#ab4d00', fg='#ffffff')
btn_customer['font'] = btn_font
btn_exit = tk.Button(frame, text="Exit", width=21, command=admin.quit, bg='#fc0303', fg='#ffffff')
btn_exit['font'] = btn_font

# Style labels, entry boxes and buttons
frame.grid(row=0, column=0, sticky="nsew")
lbl_welcome.grid(row=0, column=0, padx= 15, pady=15, sticky="nsew")
btn_store.grid(row=1, column=0, padx= 15, pady=5, sticky="nsew")
btn_staff.grid(row=2, column=0, padx= 15, pady=5, sticky="nsew")
btn_customer.grid(row=3, column=0, padx= 15, pady=5, sticky="nsew")
btn_exit.grid(row=4, column=0, padx= 15, pady=5, sticky="nsew")
lbl_hihi.grid(row=5, column=0, padx= 5, pady=5, sticky="nsew")

# Prevent resizing
admin.resizable(False, False)



admin.mainloop()