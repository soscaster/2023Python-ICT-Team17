import sys
sys.dont_write_bytecode = True
import tkinter as tk
from tkinter import messagebox, ttk, font as tkfont
import os
clear = lambda: os.system('cls')
from domains import sql_staff
from domains import sql_store
from domains import sql_customers
import process_checker as fu

# Create a new window for modifying store info [DONE]
def modify_store():
    clear()
    # Create a new window
    store = tk.Toplevel(admin)
    store.title("Modify Store Info")
    store_frame = tk.Frame(store,bg=dark_bg)

    # Create widgets
    btn_font = tkfont.Font(family="Arial", size=15)

    # Create labels
    lbl_store = tk.Label(store_frame, text="Modify Store Info", font=("Arial", 20, 'bold'),bg=dark_bg,fg=white_text, justify="center")
    lbl_store_id = tk.Label(store_frame, text="Store ID", font=("Arial", 15),bg=dark_bg,fg=white_text,)
    lbl_store_name = tk.Label(store_frame, text="Store Name", font=("Arial", 15),bg=dark_bg,fg=white_text,)
    lbl_store_address = tk.Label(store_frame, text="Store Address", font=("Arial", 15),bg=dark_bg,fg=white_text,)
    lbl_store_phone = tk.Label(store_frame, text="Store Phone", font=("Arial", 15),bg=dark_bg,fg=white_text,)
    lbl_store_email = tk.Label(store_frame, text="Store Email", font=("Arial", 15),bg=dark_bg,fg=white_text,)

    # Create entry boxes
    global store_id, store_name, store_address, store_phone, store_email
    store_id = tk.StringVar()
    store_name = tk.StringVar()
    store_address = tk.StringVar()
    store_phone = tk.StringVar()
    store_email = tk.StringVar()

    # Get values from database
    if len(sql_store.Database().select_all()) == 0:
        store_id.set("")
        store_name.set("")
        store_address.set("")
        store_phone.set("")
        store_email.set("")
    else:
        db = sql_store.Database().select_all()
        store_id.set(db[0][0])
        store_name.set(db[0][1])
        store_address.set(db[0][2])
        store_phone.set(db[0][3])
        store_email.set(db[0][4])

    ent_store_id = tk.Entry(store_frame, width=30, textvariable=store_id)
    ent_store_name = tk.Entry(store_frame, width=30, textvariable= store_name)
    ent_store_address = tk.Entry(store_frame, width=30, textvariable= store_address)
    ent_store_phone = tk.Entry(store_frame, width=30, textvariable= store_phone)
    ent_store_email = tk.Entry(store_frame, width=30, textvariable= store_email)

    # Create buttons
    btn_save = tk.Button(store_frame, text="Save", width=21, bg='#0052cc', fg='#ffffff', command = modify_store_func)
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
    btn_exit.grid(row=6, column=0, padx= 15, pady=5, sticky="nsew")
    btn_save.grid(row=6, column=1, padx= 15, pady=5, sticky="nsew")


    # Prevent resizing
    store.resizable(False, False)

def modify_store_func():

    # If function modify_store returns False, show error message
    if fu.check_if_empty(store_id.get()) == False:
        messagebox.showerror("Error","Store ID cannot be empty!")
    elif fu.check_if_empty(store_name.get()) == False:
        messagebox.showerror("Error","Store Name cannot be empty!")
    elif fu.check_if_empty(store_address.get()) == False:
        messagebox.showerror("Error","Store Address cannot be empty!")
    elif fu.check_if_empty(store_phone.get()) == False:
        messagebox.showerror("Error","Store phone cannot be empty!")
    elif fu.check_phone(store_phone.get()) == False:
        messagebox.showerror("Error", "Invalid phone number!\nPlease try again!")          
    elif fu.check_if_empty(store_email.get()) == False:
        messagebox.showerror("Error","Store E-mail cannot be empty!")      
    elif fu.check_email(store_email.get()) == False:
        messagebox.showerror("Error", "Invalid email type!\nPlease try again!")
    elif fu.input_store_info(store_id.get(), store_name.get(), store_address.get(), store_phone.get(), store_email.get()) == False:
        messagebox.showerror("Error", "Store info is not modified!")
    elif fu.input_store_info(store_id.get(), store_name.get(), store_address.get(), store_phone.get(), store_email.get()) == True:
    # Verify if the staff info is saved
        messagebox.showinfo("Success", "Store info modified successfully!")    


# Create a new window for creating staff info [DONE]
def add_staff():
    clear()
    # Create a new window
    staff = tk.Toplevel(admin)
    staff.title("Add New Staff Info")
    staff_frame = tk.Frame(staff,bg=dark_bg)

    # Create widgets
    btn_font = tkfont.Font(family="Arial", size=15)

    # Create labels
    lbl_staff = tk.Label(staff_frame, text="Add New Staff Info", font=("Arial", 20, 'bold'),bg=dark_bg,fg=white_text, justify="center")
    lbl_staff_id = tk.Label(staff_frame, text="Staff ID", font=("Arial", 15),bg=dark_bg,fg=white_text,)
    lbl_staff_pwd = tk.Label(staff_frame, text = "Staff Login Password", font=("Arial", 15),bg=dark_bg,fg=white_text,)
    lbl_staff_name = tk.Label(staff_frame, text="Staff Name", font=("Arial", 15),bg=dark_bg,fg=white_text,)
    lbl_staff_dob = tk.Label(staff_frame, text="Staff DOB (dd/mm/yyyy)", font=("Arial", 15),bg=dark_bg,fg=white_text,)
    lbl_staff_address = tk.Label(staff_frame, text="Staff Address", font=("Arial", 15),bg=dark_bg,fg=white_text,)
    lbl_staff_phone = tk.Label(staff_frame, text="Staff Phone (10 digits)", font=("Arial", 15),bg=dark_bg,fg=white_text,)
    lbl_staff_email = tk.Label(staff_frame, text="Staff Email", font=("Arial", 15),bg=dark_bg,fg=white_text,)

    # Create entry boxes   
    global st_ID, st_pwd, st_name, st_dob, st_address, st_phone, st_email 
    st_ID = tk.StringVar()
    st_pwd = tk.StringVar()
    st_name = tk.StringVar()
    st_dob = tk.StringVar()
    st_address = tk.StringVar()
    st_phone = tk.StringVar()
    st_email = tk.StringVar()

    ent_staff_id = tk.Entry(staff_frame, width=30, textvariable=st_ID, font=("Arial", 15))
    ent_staff_pwd = tk.Entry(staff_frame, width=30, textvariable=st_pwd, font=("Arial", 15), show="*")
    ent_staff_name = tk.Entry(staff_frame, width=30, textvariable=st_name, font=("Arial", 15))
    ent_staff_dob = tk.Entry(staff_frame, width=30, textvariable=st_dob, font=("Arial", 15))
    ent_staff_address = tk.Entry(staff_frame, width=30, textvariable=st_address, font=("Arial", 15))
    ent_staff_phone = tk.Entry(staff_frame, width=30, textvariable=st_phone, font=("Arial", 15))
    ent_staff_email = tk.Entry(staff_frame, width=30, textvariable=st_email, font=("Arial", 15))

    # Create buttons
    btn_save = tk.Button(staff_frame, text="Save", width=21, bg='#0052cc', fg='#ffffff', command=lambda: add_staff_func(st_ID.get(), st_pwd.get(), st_name.get(), st_dob.get(), st_address.get(), st_phone.get(), st_email.get()))
    btn_save['font'] = btn_font
    btn_exit = tk.Button(staff_frame, text="Exit", width=21, command=staff.destroy, bg='#fc0303', fg='#ffffff')
    btn_exit['font'] = btn_font

    # Style labels, entry boxes and buttons
    staff_frame.grid(row=0, column=0, sticky="nsew")
    lbl_staff.grid(row=0, column=0, columnspan=2, padx= 15, pady=15, sticky="nsew")
    lbl_staff_id.grid(row=1, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_staff_pwd.grid(row=2, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_staff_name.grid(row=3, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_staff_dob.grid(row=4, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_staff_address.grid(row=5, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_staff_phone.grid(row=6, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_staff_email.grid(row=7, column=0, padx= 15, pady=5, sticky="nsew")
    ent_staff_id.grid(row=1, column=1, padx= 15, pady=5, sticky="nsew")
    ent_staff_pwd.grid(row=2, column=1, padx= 15, pady=5, sticky="nsew")
    ent_staff_name.grid(row=3, column=1, padx= 15, pady=5, sticky="nsew")
    ent_staff_dob.grid(row=4, column=1, padx= 15, pady=5, sticky="nsew")
    ent_staff_address.grid(row=5, column=1, padx= 15, pady=5, sticky="nsew")
    ent_staff_phone.grid(row=6, column=1, padx= 15, pady=5, sticky="nsew")
    ent_staff_email.grid(row=7, column=1, padx= 15, pady=5, sticky="nsew")
    btn_exit.grid(row=8, column=0, padx= 15, pady=5, sticky="nsew")
    btn_save.grid(row=8, column=1, padx= 15, pady=5, sticky="nsew")
    
    # Prevent resizing
    staff.resizable(False, False)

    # Define a function for saving staff info
    def add_staff_func(st_ID, st_pwd, st_name, st_dob, st_address, st_phone, st_email):
        if fu.check_if_empty(st_ID) == False:
            messagebox.showerror("Error","Staff ID cannot be empty!")
        elif fu.check_if_empty(st_name) == False:
            messagebox.showerror("Error","Staff name cannot be empty!")
        elif fu.check_if_empty(st_dob) == False:
            messagebox.showerror("Error","Date of birth cannot be empty!")
        elif fu.check_dob(st_dob) == False:
            messagebox.showerror("Error", "Invalid Date of Birth format!\nPlease try again!")  
        elif fu.check_if_empty(st_address) == False:
            messagebox.showerror("Error","Staff address cannot be empty!")
        elif fu.check_if_empty(st_phone) == False:
            messagebox.showerror("Error","Staff Phone cannot be empty")
        elif fu.check_phone(st_phone) == False:
            messagebox.showerror("Error", "Invalid phone number!\nPlease try again!")
        elif fu.check_if_empty(st_email) == False:
            messagebox.showerror("Error","Staff E-mail cannot be empty!")
        elif fu.check_email(st_email) == False:
            messagebox.showerror("Error", "Invalid email type!\nPlease try again!")
        elif sql_staff.Database().Validate(st_ID, st_phone, st_email, 1) == True:
            messagebox.showerror("Error", "ID or Phone or Email is already exists!\nPlease try again!")
        else:
            if fu.add_staff(st_ID, st_pwd, st_name, st_dob, st_address, st_phone, st_email) == True:
                messagebox.showinfo("Success", "Staff info saved successfully!\nPress 'OK' to continue")
                # Close the window
                if len(sql_staff.Database().select_all()) == 0:
                    btn_staff['state'] = 'disabled'
                else:
                    btn_staff['state'] = 'normal'
                staff.destroy()
            elif fu.add_staff(st_ID, st_pwd, st_name, st_dob, st_address, st_phone, st_email) == False:
                messagebox.showerror("Error", "Staff info failed to save!\nPlease check again!")
        

# # Create a new window for modifying staff info [DONE]

#     def delete_staff_func():
#         if fu.remove_staff(st_ID.get()) == True:
#             # Verify if the staff info is saved
#             messagebox.showinfo("Success", "Staff deleted successfully!")
#             if len(sql_staff.Database().select_all()) == 0:
#                 btn_staff['state'] = 'disabled'
#             else:
#                 btn_staff['state'] = 'normal'
#         elif fu.remove_staff(st_ID.get()) == False:
#             messagebox.showerror("Error", "Staff not deleted!")


# CUSTOMER SECTION

# Create a new window for creating customer info [DONE]
def add_customer():
    clear()
    # Create a new window
    customer = tk.Toplevel(admin)
    customer.title("Add New Customer Info")
    customer_frame = tk.Frame(customer,bg=dark_bg)

    # Create widgets
    btn_font = tkfont.Font(family="Arial", size=15)

    # Create labels
    lbl_customer = tk.Label(customer_frame, text="Add New Customer Info", font=("Arial", 20, 'bold'),bg=dark_bg,fg=white_text, justify="center")
    lbl_customer_id = tk.Label(customer_frame, text="Customer ID", font=("Arial", 15),bg=dark_bg,fg=white_text,)
    lbl_customer_name = tk.Label(customer_frame, text="Customer Name", font=("Arial", 15),bg=dark_bg,fg=white_text,)
    lbl_customer_dob = tk.Label(customer_frame, text="Customer DOB (dd/mm/yyyy)", font=("Arial", 15),bg=dark_bg,fg=white_text,)
    lbl_customer_address = tk.Label(customer_frame, text="Customer Address", font=("Arial", 15),bg=dark_bg,fg=white_text,)
    lbl_customer_phone = tk.Label(customer_frame, text="Customer Phone (10 digits)", font=("Arial", 15),bg=dark_bg,fg=white_text,)
    lbl_customer_email = tk.Label(customer_frame, text="Customer Email", font=("Arial", 15),bg=dark_bg,fg=white_text,)

    # Create entry boxes   
    global cu_ID, cu_name, cu_dob, cu_address, cu_phone, cu_email 
    cu_ID = tk.StringVar()
    cu_name = tk.StringVar()
    cu_dob = tk.StringVar()
    cu_address = tk.StringVar()
    cu_phone = tk.StringVar()
    cu_email = tk.StringVar()

    ent_customer_id = tk.Entry(customer_frame, width=30, textvariable=cu_ID, font=("Arial", 15))
    ent_customer_name = tk.Entry(customer_frame, width=30, textvariable=cu_name, font=("Arial", 15))
    ent_customer_dob = tk.Entry(customer_frame, width=30, textvariable=cu_dob, font=("Arial", 15))
    ent_customer_address = tk.Entry(customer_frame, width=30, textvariable=cu_address, font=("Arial", 15))
    ent_customer_phone = tk.Entry(customer_frame, width=30, textvariable=cu_phone, font=("Arial", 15))
    ent_customer_email = tk.Entry(customer_frame, width=30, textvariable=cu_email, font=("Arial", 15))

    # Create buttons
    btn_save = tk.Button(customer_frame, text="Save", width=21, bg='#0052cc', fg='#ffffff', command=lambda: add_customer_func(cu_ID.get(), cu_name.get(), cu_dob.get(), cu_address.get(), cu_phone.get(), cu_email.get()))
    btn_save['font'] = btn_font
    btn_exit = tk.Button(customer_frame, text="Exit", width=21, command=customer.destroy, bg='#fc0303', fg='#ffffff')
    btn_exit['font'] = btn_font

    # Style labels, entry boxes and buttons
    customer_frame.grid(row=0, column=0, sticky="nsew")
    lbl_customer.grid(row=0, column=0, columnspan=2, padx= 15, pady=15, sticky="nsew")
    lbl_customer_id.grid(row=1, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_customer_name.grid(row=2, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_customer_dob.grid(row=3, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_customer_address.grid(row=4, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_customer_phone.grid(row=5, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_customer_email.grid(row=6, column=0, padx= 15, pady=5, sticky="nsew")
    ent_customer_id.grid(row=1, column=1, padx= 15, pady=5, sticky="nsew")
    ent_customer_name.grid(row=2, column=1, padx= 15, pady=5, sticky="nsew")
    ent_customer_dob.grid(row=3, column=1, padx= 15, pady=5, sticky="nsew")
    ent_customer_address.grid(row=4, column=1, padx= 15, pady=5, sticky="nsew")
    ent_customer_phone.grid(row=5, column=1, padx= 15, pady=5, sticky="nsew")
    ent_customer_email.grid(row=6, column=1, padx= 15, pady=5, sticky="nsew")
    btn_exit.grid(row=7, column=0, padx= 15, pady=5, sticky="nsew")
    btn_save.grid(row=7, column=1, padx= 15, pady=5, sticky="nsew")
    
    # Prevent resizing
    customer.resizable(False, False)

    # Define a function for saving customer info
    def add_customer_func(cu_ID, cu_name, cu_dob, cu_address, cu_phone, cu_email):
        if fu.check_if_empty(cu_ID) == False:
            messagebox.showerror("Error","Customer ID cannot be empty!")
        elif fu.check_if_empty(cu_name) == False:
            messagebox.showerror("Error","Customer Name cannot be empty!")
        elif fu.check_if_empty(cu_dob) == False:
            messagebox.showerror("Error","Customer Date of Birth cannot be empty!")
        elif fu.check_dob(cu_dob) == False:
            messagebox.showerror("Error", "Invalid Date of Birth format!\nPlease try again!")
        elif fu.check_if_empty(cu_phone) == False:
            messagebox.showerror("Error","Customer phone number cannot be empty!")
        elif fu.check_phone(cu_phone) == False:
            messagebox.showerror("Error", "Invalid phone number!\nPlease try again!")
        elif fu.check_if_empty(cu_email) == False:
            messagebox.showerror("Error","Customer e-mail cannot be empty!")
        elif fu.check_email(cu_email) == False:
            messagebox.showerror("Error", "Invalid email type!\nPlease try again!")
        elif sql_customers.Database().Validate(cu_ID, cu_phone, cu_email, 1) == True:   
            messagebox.showerror("Error", "ID or Phone or Email info is already exists!\nPlease try again!")
        else:
            if fu.add_customer(cu_ID, cu_name, cu_dob, cu_address, cu_phone, cu_email) == True:
                messagebox.showinfo("Success", "Customer info saved successfully!\nPress 'OK' to continue")
                # Close the window
                if len(sql_customers.Database().select_all()) == 0:
                    btn_customer['state'] = 'disabled'
                else:
                    btn_customer['state'] = 'normal'
                customer.destroy()
            elif fu.add_customer(cu_ID, cu_name, cu_dob, cu_address, cu_phone, cu_email) == False:
                messagebox.showerror("Error", "Customer info failed to save!\nPlease check again!")
        

# Create a new window for modifying customer info [DONE]
def modify_customer():
    clear()
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
    lbl_customer_dob = tk.Label(customer_frame, text="Customer DOB (dd/mm/yyyy)", font=("Arial", 15))
    lbl_customer_address = tk.Label(customer_frame, text="Customer Address", font=("Arial", 15))
    lbl_customer_phone = tk.Label(customer_frame, text="Customer Phone (10 digits)", font=("Arial", 15))
    lbl_customer_email = tk.Label(customer_frame, text="Customer Email", font=("Arial", 15))

    # Create entry boxes
    global cu_ID, cu_name, cu_dob, cu_address, cu_phone, cu_email
    cu_ID = tk.StringVar()
    cu_name = tk.StringVar()
    cu_dob = tk.StringVar()
    cu_address = tk.StringVar()
    cu_phone = tk.StringVar()
    cu_email = tk.StringVar()

    # Get customer list
    customer_list = sql_customers.Database().select_all()
    customer_list = [i[0] for i in customer_list]
    cu_ID.set(customer_list[0])
    customer_menu = tk.OptionMenu(customer_frame, cu_ID, *customer_list)
    # After selecting customer, get customer info and set to entry boxes
    cu_ID.trace("w", lambda *args: get_customer_info())
    customer_menu.config(font=("Arial", 12))

    # Get customer info and set to entry boxes after selecting customer
    def get_customer_info():
        db = sql_customers.Database().Search(cu_ID.get())
        cu_ID.set(db[0][0])
        cu_name.set(db[0][1])
        cu_dob.set(db[0][2])
        cu_address.set(db[0][3])
        cu_phone.set(db[0][4])
        cu_email.set(db[0][5])
    
    # Create entry boxes
    ent_customer_name = tk.Entry(customer_frame, textvariable=cu_name, width=20, font=("Arial", 15))
    ent_customer_dob = tk.Entry(customer_frame, textvariable=cu_dob, width=20, font=("Arial", 15))
    ent_customer_address = tk.Entry(customer_frame, textvariable=cu_address, width=20, font=("Arial", 15))
    ent_customer_phone = tk.Entry(customer_frame, textvariable=cu_phone, width=20, font=("Arial", 15))
    ent_customer_email = tk.Entry(customer_frame, textvariable=cu_email, width=20, font=("Arial", 15))

    # Create buttons
    def save_cf():
        cf = tk.messagebox.askyesno("Save", "Are you sure you want to overide this customer info?")
        if cf == True:
            modify_customer_func()
    btn_save = tk.Button(customer_frame, text="Save", width=21, bg='#0052cc', fg='#ffffff', command=lambda: save_cf())
    btn_save['font'] = btn_font

    btn_exit = tk.Button(customer_frame, text="Exit", width=21, bg='#fc0303', fg='#ffffff', command=customer.destroy)
    btn_exit['font'] = btn_font
    def del_cf():
        cf = tk.messagebox.askyesno("Delete", "Are you sure you want to delete this customer?")
        if cf == True:
            delete_customer_func()
    btn_delete = tk.Button(customer_frame, text="Delete", width=21, bg='#fc7303', fg='#ffffff', command=lambda: del_cf())
    btn_delete['font'] = btn_font
    

    # Create a grid layout
    customer_frame.grid(row=0, column=0, sticky="nsew")
    lbl_customer.grid(row=0, column=0, columnspan=2, padx= 15, pady=5, sticky="nsew")
    lbl_customer_id.grid(row=1, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_customer_name.grid(row=2, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_customer_dob.grid(row=3, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_customer_address.grid(row=4, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_customer_phone.grid(row=5, column=0, padx= 15, pady=5, sticky="nsew")
    lbl_customer_email.grid(row=6, column=0, padx= 15, pady=5, sticky="nsew")
    customer_menu.grid(row=1, column=1, padx= 15, pady=5, sticky="nsew")
    ent_customer_name.grid(row=2, column=1, padx= 15, pady=5, sticky="nsew")
    ent_customer_dob.grid(row=3, column=1, padx= 15, pady=5, sticky="nsew")
    ent_customer_address.grid(row=4, column=1, padx= 15, pady=5, sticky="nsew")
    ent_customer_phone.grid(row=5, column=1, padx= 15, pady=5, sticky="nsew")
    ent_customer_email.grid(row=6, column=1, padx= 15, pady=5, sticky="nsew")
    btn_exit.grid(row=7, column=0, padx= 15, pady=5, sticky="nsew")
    btn_save.grid(row=7, column=1, padx= 15, pady=5, sticky="nsew")
    btn_delete.grid(row=8, column=0, columnspan=2, padx= 15, pady=5, sticky="nsew")
    
    # Prevent the user from resizing the window
    customer.resizable(False, False)

    # Define a function for saving customer info
    def modify_customer_func():
        if fu.check_if_empty(cu_ID) == False:
            messagebox.showerror("Error","Customer ID cannot be empty!")
        elif fu.check_if_empty(cu_name) == False:
            messagebox.showerror("Error","Customer Name cannot be empty!")
        elif fu.check_if_empty(cu_dob) == False:
            messagebox.showerror("Error","Customer Date of Birth cannot be empty!")
        elif fu.check_dob(cu_dob) == False:
            messagebox.showerror("Error", "Invalid Date of Birth format!\nPlease try again!")
        elif fu.check_if_empty(cu_phone) == False:
            messagebox.showerror("Error","Customer phone number cannot be empty!")
        elif fu.check_phone(cu_phone) == False:
            messagebox.showerror("Error", "Invalid phone number!\nPlease try again!")
        elif fu.check_if_empty(cu_email) == False:
            messagebox.showerror("Error","Customer e-mail cannot be empty!")
        elif fu.check_email(cu_email) == False:
            messagebox.showerror("Error", "Invalid email type!\nPlease try again!")
        elif sql_customers.Database().Validate(cu_ID.get(), cu_phone.get(), cu_email.get(), 2) == True:
            messagebox.showerror("Error", "Phone or Email info is already exists!\nPlease try again!")
        else:
            sql_customers.Database().Update(cu_name.get(), cu_dob.get(), cu_address.get(), cu_phone.get(), cu_email.get(), cu_ID.get())
            messagebox.showinfo("Success", "Customer info saved!\nPlease refresh the page to see the changes!")

    def delete_customer_func():
        if fu.remove_customer(cu_ID.get()) == True:
            # Verify if the customer info is saved
            messagebox.showinfo("Success", "Customer deleted successfully!")
            if len(sql_customers.Database().select_all()) == 0:
                btn_customer['state'] = 'disabled'
            else:
                btn_customer['state'] = 'normal'
        elif fu.remove_customer(cu_ID.get()) == False:
            messagebox.showerror("Error", "Customer not deleted!")

#Staff_list window
def staff_list():
    clear()
    list_staff = tk.Toplevel(admin)

    list_staff.title("Staff")
    frm = tk.Frame(list_staff)
    tree = ttk.Treeview(list_staff)
    tree['show'] = 'headings'

    list_staff.resizable(False,False)

    # Define number of columns
    tree["columns"] = ("ID", "Name", "Date of Birth", "Address", "Phone", "Email")
    #Assign the width,minwidth and anchor to the respective columns 
    tree.column ("ID", width=100, minwidth=50,anchor=tk.CENTER) 
    tree.column ("Name", width=200, minwidth=100,anchor=tk.CENTER) 
    tree.column ("Date of Birth", width=100, minwidth=100,anchor=tk.CENTER) 
    tree.column ("Address", width=250, minwidth=150, anchor=tk .CENTER) 
    tree.column ("Phone", width=150, minwidth=150, anchor=tk .CENTER) 
    tree.column ("Email", width=250, minwidth=150, anchor=tk.CENTER)

    #Assign the heading names to the respective columns 
    tree.heading ("ID", text="ID", anchor=tk.CENTER) 
    tree.heading ("Name", text="Name", anchor=tk.CENTER) 
    tree.heading ("Date of Birth", text="Date of Birth", anchor=tk. CENTER)
    tree.heading ("Address", text="Address", anchor=tk.CENTER) 
    tree.heading ("Phone", text="Phone", anchor=tk.CENTER)
    tree.heading ("Email", text="Email", anchor=tk.CENTER) 

    def list_all():
        tree.delete(*tree.get_children())
        db = sql_staff.Database().select_all()
        for i in range(0,len(db)):
            tree.insert('', i, iid= None, values = ('> '+ db[i][0],db[i][2],db[i][3],db[i][4],db[i][5],db[i][6]))
    list_all()

    def del_cf():
        # Return STRING VALUE of the selected item
        del_ID = str(tree.item(tree.focus())['values'][0][2:])
        cf = tk.messagebox.askyesno("Delete", "Are you sure you want to delete this staff?")
        if cf == True:
            delete_staff_func(del_ID)

    tree.pack()
    btn_refresh = tk.Button(list_staff, text="Refresh", width=21, command=lambda: list_all())
    btn_search = tk.Button(list_staff, text="Search", width=21, command=lambda: Search_interface())
    btn_delete = tk.Button(list_staff, text="Delete", width=21, command=lambda: del_cf())
    btn_update = tk.Button(list_staff, text="Update", width=21, command=lambda: modify_staff(str(tree.item(tree.focus())['values'][0])))
    btn_exit = tk.Button(list_staff, text="Exit", width=21, command=list_staff.destroy)

    def Search_interface():
        search_inter = tk.Toplevel(list_staff)
        frm = tk.Frame(search_inter)
        # Create widgets
        btn_font = tkfont.Font(family="Arial", size=15)

        # Create labels
        lbl_staff = tk.Label(frm, text="Search Staff", font=("Arial", 20, 'bold'), justify="center")
        lbl_staff_id = tk.Label(frm, text="Staff ID", font=("Arial", 15))
        lbl_staff_name = tk.Label(frm, text="Staff Name", font=("Arial", 15))
        lbl_staff_dob = tk.Label(frm, text="Staff DOB", font=("Arial", 15))
        lbl_staff_address = tk.Label(frm, text="Staff Address", font=("Arial", 15))
        lbl_staff_phone = tk.Label(frm, text="Staff Phone", font=("Arial", 15))
        lbl_staff_email = tk.Label(frm, text="Staff Email", font=("Arial", 15))

        # Create entry boxes   
        global st_ID, st_pwd, st_name, st_dob, st_address, st_phone, st_email 
        st_ID = tk.StringVar()
        st_name = tk.StringVar()
        st_dob = tk.StringVar()
        st_address = tk.StringVar()
        st_phone = tk.StringVar()
        st_email = tk.StringVar()

        ent_staff_id = tk.Entry(frm, width=30, textvariable=st_ID, font=("Arial", 15))
        ent_staff_name = tk.Entry(frm, width=30, textvariable=st_name, font=("Arial", 15))
        ent_staff_dob = tk.Entry(frm, width=30, textvariable=st_dob, font=("Arial", 15))
        ent_staff_address = tk.Entry(frm, width=30, textvariable=st_address, font=("Arial", 15))
        ent_staff_phone = tk.Entry(frm, width=30, textvariable=st_phone, font=("Arial", 15))
        ent_staff_email = tk.Entry(frm, width=30, textvariable=st_email, font=("Arial", 15))

        # Create buttons
        btn_search = tk.Button(frm, text="Search", width=21, bg='#0052cc', fg='#ffffff', command=lambda: [Search_staff(st_ID.get(), st_name.get(), st_dob.get(), st_address.get(), st_phone.get(), st_email.get()), search_inter.destroy()])
        btn_search['font'] = btn_font
        btn_exit = tk.Button(frm, text="Exit", width=21, command=search_inter.destroy, bg='#fc0303', fg='#ffffff')
        btn_exit['font'] = btn_font

        # Style labels, entry boxes and buttons
        frm.grid(row=0, column=0, sticky="nsew")
        lbl_staff.grid(row=0, column=0, columnspan=2, padx= 15, pady=15, sticky="nsew")
        lbl_staff_id.grid(row=1, column=0, padx= 15, pady=5, sticky="nsew")
        lbl_staff_name.grid(row=3, column=0, padx= 15, pady=5, sticky="nsew")
        lbl_staff_dob.grid(row=4, column=0, padx= 15, pady=5, sticky="nsew")
        lbl_staff_address.grid(row=5, column=0, padx= 15, pady=5, sticky="nsew")
        lbl_staff_phone.grid(row=6, column=0, padx= 15, pady=5, sticky="nsew")
        lbl_staff_email.grid(row=7, column=0, padx= 15, pady=5, sticky="nsew")
        ent_staff_id.grid(row=1, column=1, padx= 15, pady=5, sticky="nsew")
        ent_staff_name.grid(row=3, column=1, padx= 15, pady=5, sticky="nsew")
        ent_staff_dob.grid(row=4, column=1, padx= 15, pady=5, sticky="nsew")
        ent_staff_address.grid(row=5, column=1, padx= 15, pady=5, sticky="nsew")
        ent_staff_phone.grid(row=6, column=1, padx= 15, pady=5, sticky="nsew")
        ent_staff_email.grid(row=7, column=1, padx= 15, pady=5, sticky="nsew")
        btn_exit.grid(row=8, column=0, padx= 15, pady=5, sticky="nsew")
        btn_search.grid(row=8, column=1, padx= 15, pady=5, sticky="nsew")
        
        # Prevent resizing
        search_inter.resizable(False, False)



    def Search_staff(id, name, dob, address, phone, email):
        if fu.Searchall_staff(id, name, dob, address, phone, email) == False:
            messagebox.showerror("Error", "Something went wrong\nPlease try again!")
        elif len(fu.Searchall_staff(id, name, dob, address, phone, email))==0:
            messagebox.showinfo("","0 results found!")
        else:
            db = fu.Searchall_staff(id, name, dob, address, phone, email)
            tree.delete(*tree.get_children())
            for i in range(0,len(db)):
                tree.insert('', i, iid= None, values = (db[i][0],db[i][2],db[i][3],db[i][4],db[i][5],db[i][6]))

    def delete_staff_func(i):
        if fu.remove_staff(i) == True:
            # Verify if the staff info is saved
            print(i)
            messagebox.showinfo("Success", "Staff deleted successfully!")
            tree.delete(tree.focus())
        else:
            messagebox.showerror("Error", "Staff not deleted!")

    def modify_staff(id):
        clear()
        # Create a new window
        staff = tk.Toplevel(list_staff)
        staff.title("Modify Staff Info")
        staff_frame = tk.Frame(staff)

        # Create widgets
        btn_font = tkfont.Font(family="Arial", size=15)

        # Create labels
        lbl_staff = tk.Label(staff_frame, text="Modify Staff Info", font=("Arial", 20, 'bold'), justify="center")
        lbl_staff_pwd = tk.Label(staff_frame, text="Staff Login Password", font=("Arial", 15))
        lbl_staff_name = tk.Label(staff_frame, text="Staff Name", font=("Arial", 15))
        lbl_staff_dob = tk.Label(staff_frame, text="Staff DOB", font=("Arial", 15))
        lbl_staff_address = tk.Label(staff_frame, text="Staff Address", font=("Arial", 15))
        lbl_staff_phone = tk.Label(staff_frame, text="Staff Phone", font=("Arial", 15))
        lbl_staff_email = tk.Label(staff_frame, text="Staff Email", font=("Arial", 15))

        # Create entry boxes
        global st_ID, st_pwd, st_name, st_dob, st_address, st_phone, st_email
        st_ID = tk.StringVar()
        st_pwd = tk.StringVar()
        st_name = tk.StringVar()
        st_dob = tk.StringVar()
        st_address = tk.StringVar()
        st_phone = tk.StringVar()
        st_email = tk.StringVar()

        # Get staff list
        st_ID.set(str(id))

        # Get staff info and set to entry boxes after selecting staff
        db = sql_staff.Database().Search(id)
        st_ID.set(db[0][0])
        st_pwd.set(db[0][1])
        st_name.set(db[0][2])
        st_dob.set(db[0][3])
        st_address.set(db[0][4])
        st_phone.set(db[0][5])
        st_email.set(db[0][6])
        
        # Create entry boxes
        ent_staff_pwd = tk.Entry(staff_frame, textvariable=st_pwd, width=20, font=("Arial", 15), show="*")
        ent_staff_name = tk.Entry(staff_frame, textvariable=st_name, width=20, font=("Arial", 15))
        ent_staff_dob = tk.Entry(staff_frame, textvariable=st_dob, width=20, font=("Arial", 15))
        ent_staff_address = tk.Entry(staff_frame, textvariable=st_address, width=20, font=("Arial", 15))
        ent_staff_phone = tk.Entry(staff_frame, textvariable=st_phone, width=20, font=("Arial", 15))
        ent_staff_email = tk.Entry(staff_frame, textvariable=st_email, width=20, font=("Arial", 15))

        # Create buttons
        def save_cf():
            cf = tk.messagebox.askyesno("Save", "Are you sure you want to overide this staff info?")
            if cf == True:
                modify_staff_func()
        btn_save = tk.Button(staff_frame, text="Save", width=21, bg='#0052cc', fg='#ffffff', command=lambda: save_cf())
        btn_save['font'] = btn_font

        btn_exit = tk.Button(staff_frame, text="Exit", width=21, bg='#fc0303', fg='#ffffff', command=staff.destroy)
        btn_exit['font'] = btn_font

        # Create a grid layout
        staff_frame.grid(row=0, column=0, sticky="nsew")
        lbl_staff.grid(row=0, column=0, columnspan=2, padx= 15, pady=5, sticky="nsew")
        lbl_staff_pwd.grid(row=2, column=0, padx= 15, pady=5, sticky="nsew")
        lbl_staff_name.grid(row=3, column=0, padx= 15, pady=5, sticky="nsew")
        lbl_staff_dob.grid(row=4, column=0, padx= 15, pady=5, sticky="nsew")
        lbl_staff_address.grid(row=5, column=0, padx= 15, pady=5, sticky="nsew")
        lbl_staff_phone.grid(row=6, column=0, padx= 15, pady=5, sticky="nsew")
        lbl_staff_email.grid(row=7, column=0, padx= 15, pady=5, sticky="nsew")
        ent_staff_pwd.grid(row=2, column=1, padx= 15, pady=5, sticky="nsew")
        ent_staff_name.grid(row=3, column=1, padx= 15, pady=5, sticky="nsew")
        ent_staff_dob.grid(row=4, column=1, padx= 15, pady=5, sticky="nsew")
        ent_staff_address.grid(row=5, column=1, padx= 15, pady=5, sticky="nsew")
        ent_staff_phone.grid(row=6, column=1, padx= 15, pady=5, sticky="nsew")
        ent_staff_email.grid(row=7, column=1, padx= 15, pady=5, sticky="nsew")
        btn_exit.grid(row=8, column=0, padx= 15, pady=5, sticky="nsew")
        btn_save.grid(row=8, column=1, padx= 15, pady=5, sticky="nsew")
        
        # Prevent the user from resizing the window
        staff.resizable(False, False)

    # Define a function for saving staff info
    def modify_staff_func():
        if fu.check_dob(st_dob.get()) == False:
            messagebox.showerror("Error", "Invalid Date of Birth format!\nPlease try again!")
        elif fu.check_phone(st_phone.get()) == False:
            messagebox.showerror("Error", "Invalid phone number!\nPlease try again!")
        elif fu.check_email(st_email.get()) == False:
            messagebox.showerror("Error", "Invalid email type!\nPlease try again!")
        elif sql_staff.Database().Validate(st_ID.get(), st_phone.get(), st_email.get(), 2) == True:
            messagebox.showerror("Error", "Phone or Email info is already exists!\nPlease try again!")
        else:
            sql_staff.Database().Update(st_pwd.get(), st_name.get(), st_dob.get(), st_address.get(), st_phone.get(), st_email.get(), 0, st_ID.get())
            messagebox.showinfo("Success", "Staff info saved!\nPlease refresh the page to see the changes!")


    btn_refresh.pack()
    btn_search.pack()
    btn_delete.pack()
    btn_update.pack()
    btn_exit.pack()

    list_staff.mainloop()

# First window

dark_bg = "#333333"
white_text = "#FFFFFF"
admin = tk.Tk()
admin.title("Book Store Management System - Loged in as admin")
frame = tk.Frame(admin,bg=dark_bg)

# Create widgets
btn_font = tkfont.Font(family="Arial", size=15)

# Create labels
lbl_welcome = tk.Label(frame, text="Welcome to\nBook Store Management System", font=("Arial", 25, 'bold'),bg=dark_bg,fg='#FFFFFF', justify="center")
lbl_hihi = tk.Label(frame, text=" ", font=("Arial", 13),bg= dark_bg)

# Create buttons
btn_store = tk.Button(frame, text="Modify Store Info", width=21, bg='#0052cc', fg='#ffffff', command=modify_store)
btn_store['font'] = btn_font
btn_add_staff = tk.Button(frame, text="Add Staff", width=21, bg='#00ab1c', fg='#ffffff', command=add_staff)
btn_add_staff['font'] = btn_font
btn_staff = tk.Button(frame, text="Staff List", width=21, bg='#00ab1c', fg='#ffffff', command=staff_list)
btn_staff['font'] = btn_font
# Confirm if the staff data table exists or not
if len(sql_staff.Database().select_all()) == 0:
    btn_staff.config(state="disabled")
btn_add_customer = tk.Button(frame, text="Add Customer", width=21, bg='#ab4d00', fg='#ffffff', command=add_customer)
btn_add_customer['font'] = btn_font
btn_customer = tk.Button(frame, text="Customer List", width=21, bg='#ab4d00', fg='#ffffff', command=print(""))
btn_customer['font'] = btn_font
# Confirm if the customer data table exists or not
if len(sql_customers.Database().select_all()) == 0:
    btn_customer.config(state="disabled")
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