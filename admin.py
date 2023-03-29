import sys
sys.dont_write_bytecode = True
import tkinter as tk
from tkinter import messagebox, ttk, font as tkfont
import func

# Database connection using sqlite3
# Functions: Modify store details - Add staff - Modify staff - Delete staff - View staff - Search staff by ID or name
# Store detail: store_id, store_name, store_address, store_phone, store_email
# Staff detail: st_ID, st_name, st_dob, st_address, st_phone, st_email
# Customer detail: cus_ID, cus_name, cus_dob, cus_address, cus_phone, cus_email

# Create a new window for modifying store info
def modify_store():
    # Create a new window
    store = tk.Toplevel(admin)
    store.title("Modify Store Info")
    store_frame = tk.Frame(store)

    # Create widgets
    btn_font = tkfont.Font(family="Arial", size=15)

    # Create labels
    lbl_store = tk.Label(store_frame, text="Modify Store Info", font=("Arial", 20, 'bold'), justify="center")
    lbl_store_id = tk.Label(store_frame, text="Store ID", font=("Arial", 15))
    lbl_store_name = tk.Label(store_frame, text="Store Name", font=("Arial", 15))
    lbl_store_address = tk.Label(store_frame, text="Store Address", font=("Arial", 15))
    lbl_store_phone = tk.Label(store_frame, text="Store Phone", font=("Arial", 15))
    lbl_store_email = tk.Label(store_frame, text="Store Email", font=("Arial", 15))

    # Create entry boxes
    ent_store_id = tk.Entry(store_frame, width=30)
    ent_store_name = tk.Entry(store_frame, width=30)
    ent_store_address = tk.Entry(store_frame, width=30)
    ent_store_phone = tk.Entry(store_frame, width=30)
    ent_store_email = tk.Entry(store_frame, width=30)

    # Create buttons
    btn_save = tk.Button(store_frame, text="Save", width=21, bg='#0052cc', fg='#ffffff')
    btn_save['font'] = btn_font
    btn_exit = tk.Button(store_frame, text="Exit", width=21, command=store.destroy, bg='#fc0303', fg='#ffffff')
    btn_exit['font'] = btn_font

    # Style labels, entry boxes and buttons
    store_frame.grid(row=0, column=0, sticky="nsew")
    lbl_store.grid(row=0, column=0, columnspan=2, padx= 15, pady=15, sticky="nsew")
    lbl_store_id.grid(row=1, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_store_name.grid(row=2, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_store_address.grid(row=3, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_store_phone.grid(row=4, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_store_email.grid(row=5, column=0, padx= 15, pady=5, sticky="nsew")
    ent_store_id.grid(row=1, column=1, padx= 15, pady=5, sticky="nsew")
    ent_store_name.grid(row=2, column=1, padx= 15, pady=5, sticky="nsew")
    ent_store_address.grid(row=3, column=1, padx= 15, pady=5, sticky="nsew")
    ent_store_phone.grid(row=4, column=1, padx= 15, pady=5, sticky="nsew")
    ent_store_email.grid(row=5, column=1, padx= 15, pady=5, sticky="nsew")
    btn_save.grid(row=6, column=0, padx= 15, pady=5, sticky="nsew")
    btn_exit.grid(row=6, column=1, padx= 15, pady=5, sticky="nsew")

    # Prevent resizing
    store.resizable(False, False)

# Create a new window for creating staff info
def add_staff():
    # Create a new window
    staff = tk.Toplevel(admin)
    staff.title("Modify Staff Info")
    staff_frame = tk.Frame(staff)

    # Create widgets
    btn_font = tkfont.Font(family="Arial", size=15)

    # Create labels
    lbl_staff = tk.Label(staff_frame, text="Modify Staff Info", font=("Arial", 20, 'bold'), justify="center")
    lbl_staff_id = tk.Label(staff_frame, text="Staff ID", font=("Arial", 15))
    lbl_staff_name = tk.Label(staff_frame, text="Staff Name", font=("Arial", 15))
    lbl_staff_dob = tk.Label(staff_frame, text="Staff DOB", font=("Arial", 15))
    lbl_staff_address = tk.Label(staff_frame, text="Staff Address", font=("Arial", 15))
    lbl_staff_phone = tk.Label(staff_frame, text="Staff Phone", font=("Arial", 15))
    lbl_staff_email = tk.Label(staff_frame, text="Staff Email", font=("Arial", 15))

    # Create entry boxes   
    global st_ID, st_name, st_dob, st_address, st_phone, st_email 
    st_ID = tk.StringVar()
    st_name = tk.StringVar()
    st_dob = tk.StringVar()
    st_address = tk.StringVar()
    st_phone = tk.StringVar()
    st_email = tk.StringVar()

    ent_staff_id = tk.Entry(staff_frame, width=30, textvariable=st_ID)
    ent_staff_name = tk.Entry(staff_frame, width=30, textvariable=st_name)
    ent_staff_dob = tk.Entry(staff_frame, width=30, textvariable=st_dob)
    ent_staff_address = tk.Entry(staff_frame, width=30, textvariable=st_address)
    ent_staff_phone = tk.Entry(staff_frame, width=30, textvariable=st_phone)
    ent_staff_email = tk.Entry(staff_frame, width=30, textvariable=st_email)

    # Create buttons
    btn_save = tk.Button(staff_frame, text="Save", width=21, bg='#0052cc', fg='#ffffff', command=add_staff_func)
    btn_save['font'] = btn_font
    btn_exit = tk.Button(staff_frame, text="Exit", width=21, command=staff.destroy, bg='#fc0303', fg='#ffffff')
    btn_exit['font'] = btn_font

    # Style labels, entry boxes and buttons
    staff_frame.grid(row=0, column=0, sticky="nsew")
    lbl_staff.grid(row=0, column=0, columnspan=2, padx= 15, pady=15, sticky="nsew")
    lbl_staff_id.grid(row=1, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_staff_name.grid(row=2, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_staff_dob.grid(row=3, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_staff_address.grid(row=4, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_staff_phone.grid(row=5, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_staff_email.grid(row=6, column=0, padx= 15, pady=5, sticky="nsew")
    ent_staff_id.grid(row=1, column=1, padx= 15, pady=5, sticky="nsew")
    ent_staff_name.grid(row=2, column=1, padx= 15, pady=5, sticky="nsew")
    ent_staff_dob.grid(row=3, column=1, padx= 15, pady=5, sticky="nsew")
    ent_staff_address.grid(row=4, column=1, padx= 15, pady=5, sticky="nsew")
    ent_staff_phone.grid(row=5, column=1, padx= 15, pady=5, sticky="nsew")
    ent_staff_email.grid(row=6, column=1, padx= 15, pady=5, sticky="nsew")
    btn_save.grid(row=7, column=0, padx= 15, pady=5, sticky="nsew")
    btn_exit.grid(row=7, column=1, padx= 15, pady=5, sticky="nsew")

    # Prevent resizing
    staff.resizable(False, False)

# Define a function for saving staff info
def add_staff_func():
    func.add_staff(st_ID.get(), st_name.get(), st_dob.get(), st_address.get(), st_phone.get(), st_email.get())
    # Verify if the staff info is saved
    messagebox.showinfo("Success", "Staff info saved successfully!")

# Create a new window for modifying staff info
def modify_staff():
    # Create a new window
    staff = tk.Toplevel(admin)
    staff.title("Modify Staff Info")
    staff_frame = tk.Frame(staff)

    # Create widgets
    btn_font = tkfont.Font(family="Arial", size=15)

    # Create labels
    lbl_staff = tk.Label(staff_frame, text="Modify Staff Info", font=("Arial", 20, 'bold'), justify="center")
    lbl_staff_id = tk.Label(staff_frame, text="Staff ID", font=("Arial", 15))
    lbl_staff_name = tk.Label(staff_frame, text="Staff Name", font=("Arial", 15))
    lbl_staff_dob = tk.Label(staff_frame, text="Staff DOB", font=("Arial", 15))
    lbl_staff_address = tk.Label(staff_frame, text="Staff Address", font=("Arial", 15))
    lbl_staff_phone = tk.Label(staff_frame, text="Staff Phone", font=("Arial", 15))
    lbl_staff_email = tk.Label(staff_frame, text="Staff Email", font=("Arial", 15))

    # Get staff list from database and create a drop down menu
    staff_list = func.get_staff_list()
    staff_id_select = ttk.Combobox(staff_frame, values=staff_list, width=27)
    staff_id_select.current(0)

    # Create entry boxes, get the value from the drop down menu (st_ID, st_name, st_dob, st_address, st_phone, st_email)
    global st_ID, st_name, st_dob, st_address, st_phone, st_email 
    st_ID = tk.StringVar()
    st_name = tk.StringVar()
    st_dob = tk.StringVar()
    st_address = tk.StringVar()
    st_phone = tk.StringVar()
    st_email = tk.StringVar()
    
    lbl_staff_id_var = tk.Label(staff_frame, textvariable=st_ID, font=("Arial", 15))
    ent_staff_name = tk.Entry(staff_frame, width=30, textvariable=st_name)
    ent_staff_dob = tk.Entry(staff_frame, width=30, textvariable=st_dob)
    ent_staff_address = tk.Entry(staff_frame, width=30, textvariable=st_address)
    ent_staff_phone = tk.Entry(staff_frame, width=30, textvariable=st_phone)
    ent_staff_email = tk.Entry(staff_frame, width=30, textvariable=st_email)

    # Create buttons
    btn_save = tk.Button(staff_frame, text="Save", width=21, bg='#0052cc', fg='#ffffff', command=modify_staff_func)
    btn_save['font'] = btn_font
    btn_exit = tk.Button(staff_frame, text="Exit", width=21, command=staff.destroy, bg='#fc0303', fg='#ffffff')
    btn_exit['font'] = btn_font

    # Style labels, entry boxes and buttons
    lbl_staff.grid(row=0, column=0, columnspan=2, padx= 15, pady=5, sticky="nsew")
    lbl_staff_id.grid(row=1, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_staff_name.grid(row=2, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_staff_dob.grid(row=3, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_staff_address.grid(row=4, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_staff_phone.grid(row=5, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_staff_email.grid(row=6, column=0, padx= 15, pady=5, sticky="nsew")
    staff_id_select.grid(row=1, column=1, padx= 15, pady=5, sticky="nsew")
    lbl_staff_id_var.grid(row=1, column=1, padx= 15, pady=5, sticky="nsew")
    ent_staff_name.grid(row=2, column=1, padx= 15, pady=5, sticky="nsew")
    ent_staff_dob.grid(row=3, column=1, padx= 15, pady=5, sticky="nsew")
    ent_staff_address.grid(row=4, column=1, padx= 15, pady=5, sticky="nsew")
    ent_staff_phone.grid(row=5, column=1, padx= 15, pady=5, sticky="nsew")
    ent_staff_email.grid(row=6, column=1, padx= 15, pady=5, sticky="nsew")
    btn_save.grid(row=7, column=0, padx= 15, pady=5, sticky="nsew")
    btn_exit.grid(row=7, column=1, padx= 15, pady=5, sticky="nsew")
    
    # Prevent resizing
    staff.resizable(False, False)

# Define a function for saving staff info
def modify_staff_func():
    func.modify_staff(st_ID.get(), st_name.get(), st_dob.get(), st_address.get(), st_phone.get(), st_email.get())
    # Verify if the staff info is saved
    messagebox.showinfo("Success", "Staff info saved successfully!")


# Create a new window for create customer info
def add_customer():
    # Create a new window
    customer = tk.Toplevel(admin)
    customer.title("Modify Customer Info")
    customer_frame = tk.Frame(customer)

    # Create widgets
    btn_font = tkfont.Font(family="Arial", size=15)

    # Create labels
    lbl_customer = tk.Label(customer_frame, text="Modify Customer Info", font=("Arial", 20, 'bold'), justify="center")
    lbl_customer_id = tk.Label(customer_frame, text="Customer ID", font=("Arial", 15))
    lbl_customer_name = tk.Label(customer_frame, text="Customer Name", font=("Arial", 15))
    lbl_customer_address = tk.Label(customer_frame, text="Customer Address", font=("Arial", 15))
    lbl_customer_phone = tk.Label(customer_frame, text="Customer Phone", font=("Arial", 15))
    lbl_customer_email = tk.Label(customer_frame, text="Customer Email", font=("Arial", 15))

    # Create entry boxes
    ent_customer_id = tk.Entry(customer_frame, width=30)
    ent_customer_name = tk.Entry(customer_frame, width=30)
    ent_customer_address = tk.Entry(customer_frame, width=30)
    ent_customer_phone = tk.Entry(customer_frame, width=30)
    ent_customer_email = tk.Entry(customer_frame, width=30)

    # Create buttons
    btn_save = tk.Button(customer_frame, text="Save", width=21, bg='#0052cc', fg='#ffffff')
    btn_save['font'] = btn_font
    btn_exit = tk.Button(customer_frame, text="Exit", width=21, command=customer.destroy, bg='#fc0303', fg='#ffffff')
    btn_exit['font'] = btn_font

    # Style labels, entry boxes and buttons
    customer_frame.grid(row=0, column=0, sticky="nsew")
    lbl_customer.grid(row=0, column=0, columnspan=2, padx= 15, pady=15, sticky="nsew")
    lbl_customer_id.grid(row=1, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_customer_name.grid(row=2, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_customer_address.grid(row=3, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_customer_phone.grid(row=4, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_customer_email.grid(row=5, column=0, padx= 15, pady=5, sticky="nsew")
    ent_customer_id.grid(row=1, column=1, padx= 15, pady=5, sticky="nsew")
    ent_customer_name.grid(row=2, column=1, padx= 15, pady=5, sticky="nsew")
    ent_customer_address.grid(row=3, column=1, padx= 15, pady=5, sticky="nsew")
    ent_customer_phone.grid(row=4, column=1, padx= 15, pady=5, sticky="nsew")
    ent_customer_email.grid(row=5, column=1, padx= 15, pady=5, sticky="nsew")
    btn_save.grid(row=6, column=0, padx= 15, pady=5, sticky="nsew")
    btn_exit.grid(row=6, column=1, padx= 15, pady=5, sticky="nsew")

    # Prevent resizing
    customer.resizable(False, False)

# Create a new window for modifying customer info
def modify_customer():
    # Create a new window
    customer = tk.Toplevel(admin)
    customer.title("Modify Customer Info")
    customer_frame = tk.Frame(customer)

    # Create widgets
    btn_font = tkfont.Font(family="Arial", size=15)

    # Create labels
    lbl_customer = tk.Label(customer_frame, text="Modify Customer Info", font=("Arial", 20, 'bold'), justify="center")
    lbl_customer_id = tk.Label(customer_frame, text="Customer ID", font=("Arial", 15))
    lbl_customer_name = tk.Label(customer_frame, text="Customer Name", font=("Arial", 15))
    lbl_customer_address = tk.Label(customer_frame, text="Customer Address", font=("Arial", 15))
    lbl_customer_phone = tk.Label(customer_frame, text="Customer Phone", font=("Arial", 15))
    lbl_customer_email = tk.Label(customer_frame, text="Customer Email", font=("Arial", 15))

    # Create entry boxes
    ent_customer_id = tk.Entry(customer_frame, width=30)
    ent_customer_name = tk.Entry(customer_frame, width=30)
    ent_customer_address = tk.Entry(customer_frame, width=30)
    ent_customer_phone = tk.Entry(customer_frame, width=30)
    ent_customer_email = tk.Entry(customer_frame, width=30)

    # Create buttons
    btn_save = tk.Button(customer_frame, text="Save", width=21, bg='#0052cc', fg='#ffffff')
    btn_save['font'] = btn_font
    btn_exit = tk.Button(customer_frame, text="Exit", width=21, command=customer.destroy, bg='#fc0303', fg='#ffffff')
    btn_exit['font'] = btn_font

    # Style labels, entry boxes and buttons
    customer_frame.grid(row=0, column=0, sticky="nsew")
    lbl_customer.grid(row=0, column=0, columnspan=2, padx= 15, pady=15, sticky="nsew")
    lbl_customer_id.grid(row=1, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_customer_name.grid(row=2, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_customer_address.grid(row=3, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_customer_phone.grid(row=4, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_customer_email.grid(row=5, column=0, padx= 15, pady=5, sticky="nsew")
    ent_customer_id.grid(row=1, column=1, padx= 15, pady=5, sticky="nsew")
    ent_customer_name.grid(row=2, column=1, padx= 15, pady=5, sticky="nsew")
    ent_customer_address.grid(row=3, column=1, padx= 15, pady=5, sticky="nsew")
    ent_customer_phone.grid(row=4, column=1, padx= 15, pady=5, sticky="nsew")
    ent_customer_email.grid(row=5, column=1, padx= 15, pady=5, sticky="nsew")
    btn_save.grid(row=6, column=0, padx= 15, pady=5, sticky="nsew")
    btn_exit.grid(row=6, column=1, padx= 15, pady=5, sticky="nsew")

    # Prevent resizing
    customer.resizable(False, False)

# First window

func.create_connection()
admin = tk.Tk()
admin.title("Book Store Management System - Loged in as admin")
frame = tk.Frame(admin)

# Create widgets
btn_font = tkfont.Font(family="Arial", size=15)

# Create labels
lbl_welcome = tk.Label(frame, text="Welcome to\nBook Store Management System", font=("Arial", 20, 'bold'), justify="center")
lbl_hihi = tk.Label(frame, text=" ", font=("Arial", 13))

# Create buttons
btn_store = tk.Button(frame, text="Modify Store Info", width=21, bg='#0052cc', fg='#ffffff', command=modify_store)
btn_store['font'] = btn_font
btn_add_staff = tk.Button(frame, text="Add Staff", width=21, bg='#00ab1c', fg='#ffffff', command=add_staff)
btn_add_staff['font'] = btn_font
btn_staff = tk.Button(frame, text="Modify Staff Info", width=21, bg='#00ab1c', fg='#ffffff', command=modify_staff)
btn_staff['font'] = btn_font
btn_add_customer = tk.Button(frame, text="Add Customer", width=21, bg='#ab4d00', fg='#ffffff', command=add_customer)
btn_add_customer['font'] = btn_font
btn_customer = tk.Button(frame, text="Modify Customer Info", width=21, bg='#ab4d00', fg='#ffffff', command=modify_customer)
btn_customer['font'] = btn_font
btn_exit = tk.Button(frame, text="Exit", width=21, command=admin.quit, bg='#fc0303', fg='#ffffff')
btn_exit['font'] = btn_font

# Style labels, entry boxes and buttons
frame.grid(row=0, column=0, sticky="nsew")
lbl_welcome.grid(row=0, column=0, columnspan = 2, padx= 15, pady=15, sticky="nsew")
btn_store.grid(row=1, column=0, columnspan = 2, padx= 15, pady=5, sticky="nsew")
btn_add_staff.grid(row=2, column=0, padx= 15, pady=5, sticky="nsew")
btn_staff.grid(row=2, column=1, padx= 15, pady=5, sticky="nsew")
btn_add_customer.grid(row=3, column=0, padx= 15, pady=5, sticky="nsew")
btn_customer.grid(row=3, column=1, padx= 15, pady=5, sticky="nsew")
btn_exit.grid(row=4, column=0, columnspan = 2, padx= 15, pady=5, sticky="nsew")
lbl_hihi.grid(row=5, column=0, padx= 5, pady=5, sticky="nsew")

# Prevent resizing
admin.resizable(False, False)

admin.mainloop()