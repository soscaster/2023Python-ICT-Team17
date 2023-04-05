import sys
sys.dont_write_bytecode = True
import tkinter as tk
from tkinter import messagebox, ttk, font as tkfont
import os
clear = lambda: os.system('clear')
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
    global store_id, store_name, store_address, store_phone, store_email
    store_id = tk.StringVar()
    store_name = tk.StringVar()
    store_address = tk.StringVar()
    store_phone = tk.StringVar()
    store_email = tk.StringVar()

    # Get values from database
    if len(sql_store.Database().Storage())==0:
        store_id.set("")
        store_name.set("")
        store_address.set("")
        store_phone.set("")
        store_email.set("")
    else:
        db = sql_store.Database().Storage()
        store_id.set(db[0][0])
        store_name.set(db[0][1])
        store_address.set(db[0][2])
        store_phone.set(db[0][3])
        store_email.set(db[0][4])

    ent_store_id = tk.Entry(store_frame, width=30, textvariable=store_id, font=("Arial", 15))
    ent_store_name = tk.Entry(store_frame, width=30, textvariable= store_name, font=("Arial", 15))
    ent_store_address = tk.Entry(store_frame, width=30, textvariable= store_address, font=("Arial", 15))
    ent_store_phone = tk.Entry(store_frame, width=30, textvariable= store_phone, font=("Arial", 15))
    ent_store_email = tk.Entry(store_frame, width=30, textvariable= store_email, font=("Arial", 15))

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
    if fu.check_phone(store_phone.get()) == False:
        messagebox.showerror("Error", "Invalid phone number!\nPlease try again!", parent=box)
    elif fu.check_email(store_email.get()) == False:
        messagebox.showerror("Error", "Invalid email type!\nPlease try again!", parent=box)
    elif fu.input_store_info(store_id.get(), store_name.get(), store_address.get(), store_phone.get(), store_email.get()) == False:
        messagebox.showerror("Error", "Store info is not modified!", parent=box)
    elif fu.input_store_info(store_id.get(), store_name.get(), store_address.get(), store_phone.get(), store_email.get()) == True:
    # Verify if the staff info is saved
        messagebox.showinfo("Success", "Store info modified successfully!", parent=box)


# Create a new window for creating staff info [DONE]
def add_staff():
    clear()
    # Create a new window
    staff = tk.Toplevel(admin)
    staff.title("Add New Staff Info")
    staff_frame = tk.Frame(staff)

    # Create widgets
    btn_font = tkfont.Font(family="Arial", size=15)

    # Create labels
    lbl_staff = tk.Label(staff_frame, text="Add New Staff Info", font=("Arial", 20, 'bold'), justify="center")
    lbl_staff_id = tk.Label(staff_frame, text="Staff ID", font=("Arial", 15))
    lbl_staff_pwd = tk.Label(staff_frame, text = "Staff Login Password", font=("Arial", 15))
    lbl_staff_name = tk.Label(staff_frame, text="Staff Name", font=("Arial", 15))
    lbl_staff_dob = tk.Label(staff_frame, text="Staff DOB (dd/mm/yyyy)", font=("Arial", 15))
    lbl_staff_address = tk.Label(staff_frame, text="Staff Address", font=("Arial", 15))
    lbl_staff_phone = tk.Label(staff_frame, text="Staff Phone (10 digits)", font=("Arial", 15))
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
        if fu.check_dob(st_dob) == False:
            messagebox.showerror("Error", "Invalid Date of Birth format!\nPlease try again!", parent=box)
        elif fu.check_phone(st_phone) == False:
            messagebox.showerror("Error", "Invalid phone number!\nPlease try again!", parent=box)
        elif fu.check_email(st_email) == False:
            messagebox.showerror("Error", "Invalid email type!\nPlease try again!", parent=box) 
        elif sql_staff.Database().Validate(st_ID, st_phone, st_email, 1) == True:
            messagebox.showerror("Error", "ID or Phone or Email is already exists!\nPlease try again!", parent=box)
        else:
            if fu.add_staff(st_ID, st_pwd, st_name, st_dob, st_address, st_phone, st_email) == True:
                messagebox.showinfo("Success", "Staff info saved successfully!\nPress 'OK' to continue", parent=box)
                # Close the window
                if len(sql_staff.Database().Storage()) == 0:
                    btn_staff['state'] = 'disabled'
                else:
                    btn_staff['state'] = 'normal'
                staff.destroy()
            elif fu.add_staff(st_ID, st_pwd, st_name, st_dob, st_address, st_phone, st_email) == False:
                messagebox.showerror("Error", "Staff info failed to save!\nPlease check again!", parent=box)


# CUSTOMER SECTION

# Create a new window for creating customer info [DONE]
def add_customer():
    clear()
    # Create a new window
    customer = tk.Toplevel(admin)
    customer.title("Add New Customer Info")
    customer_frame = tk.Frame(customer)

    # Create widgets
    btn_font = tkfont.Font(family="Arial", size=15)

    # Create labels
    lbl_customer = tk.Label(customer_frame, text="Add New Customer Info", font=("Arial", 20, 'bold'), justify="center")
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
        if fu.check_dob(cu_dob) == False:
            messagebox.showerror("Error", "Invalid Date of Birth format!\nPlease try again!", parent=box)
        elif fu.check_phone(cu_phone) == False:
            messagebox.showerror("Error", "Invalid phone number!\nPlease try again!", parent=box)
        elif fu.check_email(cu_email) == False:
            messagebox.showerror("Error", "Invalid email type!\nPlease try again!", parent=box)
        elif sql_customers.Database().Validate(cu_ID, cu_phone, cu_email, 1) == True:
            messagebox.showerror("Error", "ID or Phone or Email info is already exists!\nPlease try again!", parent=box)
        else:
            if fu.add_customer(cu_ID, cu_name, cu_dob, cu_address, cu_phone, cu_email) == True:
                messagebox.showinfo("Success", "Customer info saved successfully!\nPress 'OK' to continue", parent=box)
                # Close the window
                if len(sql_customers.Database().Storage()) == 0:
                    btn_customer['state'] = 'disabled'
                else:
                    btn_customer['state'] = 'normal'
                customer.destroy()
            elif fu.add_customer(cu_ID, cu_name, cu_dob, cu_address, cu_phone, cu_email) == False:
                messagebox.showerror("Error", "Customer info failed to save!\nPlease check again!", parent=box)

#Staff_list window
def staff_list():
    
    # Configure style for table
    style = ttk.Style()
    style.theme_use("default")
    style.configure ("Treeview",
        background="#D3D3D3",
        foreground="black",
        rowheight=25,
        fieldbackground="silver"
        )
    
    # Change color of selected record
    style.map('Treeview',background=[('selected','#347083')])

    clear()
    list_staff = tk.Toplevel(admin)

    list_staff.title("Staff")

    # Create tree view frame
    tree_frame = tk.Frame(list_staff)
    tree_frame.pack(pady=20,padx=20)

    # Create scrollbar
    tree_scroll = tk.Scrollbar(tree_frame)
    tree_scroll.pack(side='right',fill="y")

    # Create treeview
    tree = ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set)

    # Pack to screen
    tree.pack()

    # Configure scrollbar
    tree_scroll.config(command=tree.yview)

    tree['show']='headings'

    list_staff.resizable(False,False)

    # Define number of columns
    tree["columns"] = ("ID", "Name", "Date of Birth", "Address", "Phone", "Email")
    #Assign the width,minwidth and anchor to the respective columns 
    tree.column ("ID", width=100, minwidth=50,anchor=tk.CENTER) 
    tree.column ("Name", width=200, minwidth=100,anchor=tk.CENTER) 
    tree.column ("Date of Birth", width=100, minwidth=100,anchor=tk.CENTER) 
    tree.column ("Address", width=250, minwidth=150, anchor=tk .CENTER) 
    tree.column ("Phone", width=150, minwidth=150, anchor=tk .CENTER) 
    tree.column ("Email", width=150, minwidth=100, anchor=tk.CENTER)

    #Assign the heading names to the respective columns 
    tree.heading ("ID", text="ID", anchor=tk.CENTER) 
    tree.heading ("Name", text="Name", anchor=tk.CENTER) 
    tree.heading ("Date of Birth", text="Date of Birth", anchor=tk. CENTER)
    tree.heading ("Address", text="Address", anchor=tk.CENTER) 
    tree.heading ("Phone", text="Phone", anchor=tk.CENTER)
    tree.heading ("Email", text="Email", anchor=tk.CENTER) 

    # Color for odd and even row
    tree.tag_configure('even_row',background='white')
    tree.tag_configure('odd_row',background='lightblue')

    def list_all():
        tree.delete(*tree.get_children())
        db = sql_staff.Database().Storage()
        for i in range(0,len(db)):
            if i % 2 == 0:
                tree.insert('', i, iid= None, values = (db[i][0],db[i][2],db[i][3],db[i][4],db[i][5],db[i][6],">"+db[i][0]),tags='even_row')
            else:
                tree.insert('', i, iid= None, values = (db[i][0],db[i][2],db[i][3],db[i][4],db[i][5],db[i][6],">"+db[i][0]),tags='odd_row')
    list_all()

    def del_cf():
        # Return STRING VALUE of the selected item
        try:
            del_ID = tree.item(tree.focus())['values'][6][1:]
        except:
            return
        cf = tk.messagebox.askyesno("Delete", "Are you sure you want to delete this staff?")
        if cf == True:
            delete_staff_func(del_ID)

    # Add button frame
    button_frame = tk.LabelFrame(list_staff,text="Functions")
    button_frame.pack(fill="x",expand='yes',padx=20,pady=20)




    btn_refresh = tk.Button(button_frame, text="Refresh", width=21, command=lambda: list_all())
    btn_search = tk.Button(button_frame, text="Search", width=21, command=lambda: Search_interface())
    btn_delete = tk.Button(button_frame, text="Delete", width=21, command=lambda: del_cf())
    btn_update = tk.Button(button_frame, text="Update", width=21, command=lambda: modify_staff())
    btn_exit = tk.Button(button_frame, text="Exit", width=21, command=list_staff.destroy)

    btn_refresh.grid(row=0,column=0,padx=10,pady=10)
    btn_search.grid(row=0,column=1,padx=10,pady=10)
    btn_delete.grid(row=0,column=2,padx=10,pady=10)
    btn_update.grid(row=0,column=3,padx=10,pady=10)
    btn_exit.grid(row=0,column=4,padx=10,pady=10)

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
        btn_search = tk.Button(frm, text="Search", width=21, bg='#0052cc', fg='#ffffff', command=lambda: Search_staff(st_ID.get(), st_name.get(), st_dob.get(), st_address.get(), st_phone.get(), st_email.get()))
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
                messagebox.showerror("Error", "Something went wrong\nPlease try again!", parent=box)
            elif len(fu.Searchall_staff(id, name, dob, address, phone, email))==0:
                messagebox.showinfo("","0 results found!", parent=box)
            else:
                db = fu.Searchall_staff(id, name, dob, address, phone, email)
                tree.delete(*tree.get_children())
                for i in range(0,len(db)):
                    tree.insert('', i, iid= None, values = (db[i][0],db[i][2],db[i][3],db[i][4],db[i][5],db[i][6],">"+db[i][0]))
                search_inter.destroy()

    def delete_staff_func(id):
        if fu.remove_staff(id) == True:
            messagebox.showinfo("Success", "Staff deleted successfully!", parent=box)
            tree.delete(tree.focus())
            if len(sql_staff.Database().Storage()) == 0:
                btn_staff['state'] = 'disabled'
            else:
                btn_staff['state'] = 'normal'
        else:
            messagebox.showerror("Error", "Staff not deleted!", parent=box)

    def modify_staff():
        try:
            id = tree.item(tree.focus())['values'][6][1:]
        except:
            return
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
        st_ID.set(id)

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
            messagebox.showerror("Error", "Invalid Date of Birth format!\nPlease try again!", parent=box)
        elif fu.check_phone(st_phone.get()) == False:
            messagebox.showerror("Error", "Invalid phone number!\nPlease try again!", parent=box)
        elif fu.check_email(st_email.get()) == False:
            messagebox.showerror("Error", "Invalid email type!\nPlease try again!", parent=box)
        elif sql_staff.Database().Validate(st_ID.get(), st_phone.get(), st_email.get(), 2) == True:
            messagebox.showerror("Error", "Phone or Email info is already exists!\nPlease try again!", parent=box)
        else:
            sql_staff.Database().Update(st_pwd.get(), st_name.get(), st_dob.get(), st_address.get(), st_phone.get(), st_email.get(), st_ID.get())
            messagebox.showinfo("Success", "Staff info saved!\nPlease refresh the page to see the changes!", parent=box)


    # btn_refresh.pack()
    # btn_search.pack()
    # btn_delete.pack()
    # btn_update.pack()
    # btn_exit.pack()

#Customer List window


def customer_list():
    clear()
    list_customer = tk.Toplevel(admin)

    list_customer.title("Staff")
    frm = tk.Frame(list_customer)
    tree = ttk.Treeview(list_customer)
    tree['show']='headings'

    list_customer.resizable(False,False)

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
        db = sql_customers.Database().Storage()
        for i in range(0,len(db)):
            tree.insert('', i, iid= None, values = (db[i][0],db[i][1],db[i][2],db[i][3],db[i][4],db[i][5],">"+db[i][0]))
    list_all()

    def del_cf():
        # Return STRING VALUE of the selected item
        try:
            del_ID = tree.item(tree.focus())['values'][6][1:]
        except:
            return
        cf = tk.messagebox.askyesno("Delete", "Are you sure you want to delete this customer?")
        if cf == True:
            delete_customer_func(del_ID)

    def delete_customer_func(id):
        if fu.remove_customer(id) == True:
            messagebox.showinfo("Success", "Customer deleted successfully!", parent=box)
            tree.delete(tree.focus())
            if len(sql_customers.Database().Storage()) == 0:
                btn_customer['state'] = 'disabled'
            else:
                btn_customer['state'] = 'normal'
        else:
            messagebox.showerror("Error", "Customer not deleted!", parent=box)

    tree.pack()
    btn_refresh = tk.Button(list_customer, text="Refresh", width=21, command=lambda: list_all())
    btn_search = tk.Button(list_customer, text="Search", width=21, command=lambda: Search_interface())
    btn_delete = tk.Button(list_customer, text="Delete", width=21, command=lambda: del_cf())
    btn_update = tk.Button(list_customer, text="Update", width=21, command=lambda: modify_customer())
    btn_exit = tk.Button(list_customer, text="Exit", width=21, command=list_customer.destroy)

    def Search_interface():
        search_inter = tk.Toplevel(list_customer)
        frm = tk.Frame(search_inter)
        # Create widgets
        btn_font = tkfont.Font(family="Arial", size=15)

        # Create labels
        lbl_customer = tk.Label(frm, text="Search Customer", font=("Arial", 20, 'bold'), justify="center")
        lbl_customer_id = tk.Label(frm, text="Customer ID", font=("Arial", 15))
        lbl_customer_name = tk.Label(frm, text="Customer Name", font=("Arial", 15))
        lbl_customer_dob = tk.Label(frm, text="Customer DOB", font=("Arial", 15))
        lbl_customer_address = tk.Label(frm, text="Customer Address", font=("Arial", 15))
        lbl_customer_phone = tk.Label(frm, text="Customer Phone", font=("Arial", 15))
        lbl_customer_email = tk.Label(frm, text="Customer Email", font=("Arial", 15))

        # Create entry boxes   
        global cus_ID, cus_name, cus_dob, cus_address, cus_phone, cus_email 
        cus_ID = tk.StringVar()
        cus_name = tk.StringVar()
        cus_dob = tk.StringVar()
        cus_address = tk.StringVar()
        cus_phone = tk.StringVar()
        cus_email = tk.StringVar()

        ent_customer_id = tk.Entry(frm, width=30, textvariable=cus_ID, font=("Arial", 15))
        ent_customer_name = tk.Entry(frm, width=30, textvariable=cus_name, font=("Arial", 15))
        ent_customer_dob = tk.Entry(frm, width=30, textvariable=cus_dob, font=("Arial", 15))
        ent_customer_address = tk.Entry(frm, width=30, textvariable=cus_address, font=("Arial", 15))
        ent_customer_phone = tk.Entry(frm, width=30, textvariable=cus_phone, font=("Arial", 15))
        ent_customer_email = tk.Entry(frm, width=30, textvariable=cus_email, font=("Arial", 15))

        # Create buttons
        btn_search = tk.Button(frm, text="Search", width=21, bg='#0052cc', fg='#ffffff', command=lambda: Search_customer(cus_ID.get(), cus_name.get(), cus_dob.get(), cus_address.get(), cus_phone.get(), cus_email.get()))
        btn_search['font'] = btn_font
        btn_exit = tk.Button(frm, text="Exit", width=21, command=search_inter.destroy, bg='#fc0303', fg='#ffffff')
        btn_exit['font'] = btn_font

        # Style labels, entry boxes and buttons
        frm.grid(row=0, column=0, sticky="nsew")
        lbl_customer.grid(row=0, column=0, columnspan=2, padx= 15, pady=15, sticky="nsew")
        lbl_customer_id.grid(row=1, column=0, padx= 15, pady=5, sticky="nsew")
        lbl_customer_name.grid(row=3, column=0, padx= 15, pady=5, sticky="nsew")
        lbl_customer_dob.grid(row=4, column=0, padx= 15, pady=5, sticky="nsew")
        lbl_customer_address.grid(row=5, column=0, padx= 15, pady=5, sticky="nsew")
        lbl_customer_phone.grid(row=6, column=0, padx= 15, pady=5, sticky="nsew")
        lbl_customer_email.grid(row=7, column=0, padx= 15, pady=5, sticky="nsew")
        ent_customer_id.grid(row=1, column=1, padx= 15, pady=5, sticky="nsew")
        ent_customer_name.grid(row=3, column=1, padx= 15, pady=5, sticky="nsew")
        ent_customer_dob.grid(row=4, column=1, padx= 15, pady=5, sticky="nsew")
        ent_customer_address.grid(row=5, column=1, padx= 15, pady=5, sticky="nsew")
        ent_customer_phone.grid(row=6, column=1, padx= 15, pady=5, sticky="nsew")
        ent_customer_email.grid(row=7, column=1, padx= 15, pady=5, sticky="nsew")
        btn_exit.grid(row=8, column=0, padx= 15, pady=5, sticky="nsew")
        btn_search.grid(row=8, column=1, padx= 15, pady=5, sticky="nsew")
        
        # Prevent resizing
        search_inter.resizable(False, False)

        def Search_customer(id, name, dob, address, phone, email):
            if fu.Searchall_customer(id, name, dob, address, phone, email) == False:
                messagebox.showerror("Error", "Something went wrong\nPlease try again!", parent=box)
            elif len(fu.Searchall_customer(id, name, dob, address, phone, email))==0:
                messagebox.showinfo("","0 results found!", parent=box)
            else:
                db = fu.Searchall_customer(id, name, dob, address, phone, email)
                tree.delete(*tree.get_children())
                for i in range(0,len(db)):
                    tree.insert('', i, iid= None, values = (db[i][0],db[i][1],db[i][2],db[i][3],db[i][4],db[i][5],">"+db[i][0]))
                search_inter.destroy()

    def modify_customer():
        try:
            id = tree.item(tree.focus())['values'][6][1:]
        except:
            return
        clear()
        # Create a new window
        customer = tk.Toplevel(list_customer)
        customer.title("Modify Customer Info")
        customer_frame = tk.Frame(customer)

        # Create widgets
        btn_font = tkfont.Font(family="Arial", size=15)

        # Create labels
        lbl_customer = tk.Label(customer_frame, text="Modify Customer Info", font=("Arial", 20, 'bold'), justify="center")
        lbl_customer_name = tk.Label(customer_frame, text="Customer Name", font=("Arial", 15))
        lbl_customer_dob = tk.Label(customer_frame, text="Customer DOB", font=("Arial", 15))
        lbl_customer_address = tk.Label(customer_frame, text="Customer Address", font=("Arial", 15))
        lbl_customer_phone = tk.Label(customer_frame, text="Customer Phone", font=("Arial", 15))
        lbl_customer_email = tk.Label(customer_frame, text="Customer Email", font=("Arial", 15))

        # Create entry boxes
        global cus_ID, cus_pwd, cus_name, cus_dob, cus_address, cus_phone, cus_email
        cus_ID = tk.StringVar()
        cus_name = tk.StringVar()
        cus_dob = tk.StringVar()
        cus_address = tk.StringVar()
        cus_phone = tk.StringVar()
        cus_email = tk.StringVar()

        # Get staff list
        cus_ID.set(id)

        # Get staff info and set to entry boxes after selecting staff
        db = sql_customers.Database().Search(id)
        cus_ID.set(db[0][0])
        cus_name.set(db[0][1])
        cus_dob.set(db[0][2])
        cus_address.set(db[0][3])
        cus_phone.set(db[0][4])
        cus_email.set(db[0][5])
        
        # Create entry boxes
        ent_customer_name = tk.Entry(customer_frame, textvariable=cus_name, width=20, font=("Arial", 15))
        ent_customer_dob = tk.Entry(customer_frame, textvariable=cus_dob, width=20, font=("Arial", 15))
        ent_customer_address = tk.Entry(customer_frame, textvariable=cus_address, width=20, font=("Arial", 15))
        ent_customer_phone = tk.Entry(customer_frame, textvariable=cus_phone, width=20, font=("Arial", 15))
        ent_customer_email = tk.Entry(customer_frame, textvariable=cus_email, width=20, font=("Arial", 15))

        # Create buttons
        def save_cf():
            cf = tk.messagebox.askyesno("Save", "Are you sure you want to overide this staff info?")
            if cf == True:
                modify_customer_func()
        
        btn_save = tk.Button(customer_frame, text="Save", width=21, bg='#0052cc', fg='#ffffff', command=lambda: save_cf())
        btn_save['font'] = btn_font

        btn_exit = tk.Button(customer_frame, text="Exit", width=21, bg='#fc0303', fg='#ffffff', command=customer.destroy)
        btn_exit['font'] = btn_font        

        # Create a grid layout
        customer_frame.grid(row=0, column=0, sticky="nsew")
        lbl_customer.grid(row=0, column=0, columnspan=2, padx= 15, pady=5, sticky="nsew")
        lbl_customer_name.grid(row=3, column=0, padx= 15, pady=5, sticky="nsew")
        lbl_customer_dob.grid(row=4, column=0, padx= 15, pady=5, sticky="nsew")
        lbl_customer_address.grid(row=5, column=0, padx= 15, pady=5, sticky="nsew")
        lbl_customer_phone.grid(row=6, column=0, padx= 15, pady=5, sticky="nsew")
        lbl_customer_email.grid(row=7, column=0, padx= 15, pady=5, sticky="nsew")
        ent_customer_name.grid(row=3, column=1, padx= 15, pady=5, sticky="nsew")
        ent_customer_dob.grid(row=4, column=1, padx= 15, pady=5, sticky="nsew")
        ent_customer_address.grid(row=5, column=1, padx= 15, pady=5, sticky="nsew")
        ent_customer_phone.grid(row=6, column=1, padx= 15, pady=5, sticky="nsew")
        ent_customer_email.grid(row=7, column=1, padx= 15, pady=5, sticky="nsew")
        btn_exit.grid(row=8, column=0, padx= 15, pady=5, sticky="nsew")
        btn_save.grid(row=8, column=1, padx= 15, pady=5, sticky="nsew")
        
        # Prevent the user from resizing the window
        customer.resizable(False, False)

    # Define a function for saving staff info
    def modify_customer_func():
        if fu.check_dob(cus_dob.get()) == False:
            messagebox.showerror("Error", "Invalid Date of Birth format!\nPlease try again!", parent=box)
        elif fu.check_phone(cus_phone.get()) == False:
            messagebox.showerror("Error", "Invalid phone number!\nPlease try again!", parent=box)
        elif fu.check_email(cus_email.get()) == False:
            messagebox.showerror("Error", "Invalid email type!\nPlease try again!", parent=box)
        elif sql_customers.Database().Validate(cus_ID.get(), cus_phone.get(), cus_email.get(), 2) == True:
            messagebox.showerror("Error", "Phone or Email info is already exists!\nPlease try again!", parent=box)
        else:
            sql_customers.Database().Update(cus_name.get(), cus_dob.get(), cus_address.get(), cus_phone.get(), cus_email.get(), cus_ID.get())
            messagebox.showinfo("Success", "Staff info saved!\nPlease refresh the page to see the changes!", parent=box)
    
    btn_refresh.pack()
    btn_search.pack()
    btn_delete.pack()
    btn_update.pack()
    btn_exit.pack()

# First window

admin = tk.Tk()
admin.title("BSMS Beta - Logged in as Administrator")
admin.geometry("800x600")

box = tk.Toplevel(admin)
box.withdraw()

imgbg = tk.PhotoImage(file="img/main.png")
# Fit the image to the buttons
m_st = tk.PhotoImage(file="img/icons/m_st.png")
img_mst = m_st.subsample(2, 2)
mod_s = tk.PhotoImage(file="img/icons/m_s.png")
img_m_s = mod_s.subsample(2, 2)
mod_c = tk.PhotoImage(file="img/icons/m_c.png")
img_m_c = mod_c.subsample(2, 2)
add_c = tk.PhotoImage(file="img/icons/a_c.png")
img_a_c = add_c.subsample(2, 2)
add_s = tk.PhotoImage(file="img/icons/a_s.png")
img_a_s = add_s.subsample(2, 2)
ex = tk.PhotoImage(file="img/icons/exit.png")
img_e = ex.subsample(2, 2)

lbl_hihi = tk.Label(image=imgbg)
lbl_hihi.place(x=0, y=0)

# Create widgets
btn_font = tkfont.Font(family="Arial", size=15)

# Create labels
lbl_welcome = tk.Label(text="Welcome to\nBook Store Management System", font=("Arial", 25, 'bold'), justify="center", bg='white', fg='#318bd2')
lb_cpr = tk.Label(admin, text="© 2023 - BI12 - ICT Team 17\nVersion BETA", font=("Arial", 6), bg='#73a2c7', justify="right", fg='white')

# Create buttons
btn_store = tk.Button(image= img_mst, text="Modify Store Info",compound = 'left', width=495, height=50, bg='#0052cc', fg='#ffffff', command=modify_store)
btn_store['font'] = btn_font
btn_add_staff = tk.Button(image=img_a_s,text="Add Staff",compound = 'left', width=231, height=50, bg='#00ab1c', fg='#ffffff', command=add_staff)
btn_add_staff['font'] = btn_font
btn_staff = tk.Button(image=img_m_s,text="Staff List", compound = 'left', width=231, height=50, bg='#00ab1c', fg='#ffffff', command=staff_list)
btn_staff['font'] = btn_font
# Confirm if the staff data table exists or not
if len(sql_staff.Database().Storage()) == 0:
    btn_staff.config(state="disabled")
btn_add_customer = tk.Button(image=img_a_c,text="Add Customer", compound = 'left', width=231, height=50, bg='#ab4d00', fg='#ffffff', command=add_customer)
btn_add_customer['font'] = btn_font
btn_customer = tk.Button(image=img_m_c,text="Customer List", compound = 'left', width=231, height=50, bg='#ab4d00', fg='#ffffff', command=customer_list)
btn_customer['font'] = btn_font
# Confirm if the customer data table exists or not
if len(sql_customers.Database().Storage()) == 0:
    btn_customer.config(state="disabled")
btn_exit = tk.Button(image=img_e, text="Exit", compound= 'left', width=495, height=50, command=admin.quit, bg='#570b0b', fg='#ffffff')
btn_exit['font'] = btn_font

# Style labels, entry boxes and buttons
lbl_welcome.place(x=143, y=95)
btn_store.place(x=143, y=195)
btn_add_staff.place(x=143, y=275)
btn_staff.place(x=407, y=275)
btn_add_customer.place(x=143, y=355)
btn_customer.place(x=407, y=355)
btn_exit.place(x=143, y=435)
lb_cpr.place(x=690, y=573)

# Prevent resizing
admin.resizable(False, False)
admin.mainloop()