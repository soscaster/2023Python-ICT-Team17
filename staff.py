import sys
sys.dont_write_bytecode = True
import tkinter as tk
from tkinter import messagebox, ttk, font as tkfont
import process_checker as func
import os
import platform
import zipfile
import datetime
from reportlab.pdfgen import canvas
clear = lambda: os.system('clear')
from domains import sql_session
from domains import sql_customers
from domains import sql_books
from domains import sql_store
from domains import sql_sell

if platform.system() == "Windows":
    clear = lambda: os.system('cls')
else:
    clear = lambda: os.system('clear')

# CUSTOMER SECTION

# Create a new window for creating customer info [DONE]
def add_customer():
    clear()
    # Create a new window
    customer = tk.Toplevel(window)
    customer.title("Add New Customer Info")
    customer.geometry("900x700")
    customer.resizable(False, False)

    # Create widgets
    btn_font = tkfont.Font(family="Arial", size=15)
    lbl_img = tk.Label(customer, image=imgcus)
    lbl_img.place(x=0, y=0)

    # Create labels
    lbl_customer = tk.Label(customer, text="Add New Customer Info", font=("Arial", 23, 'bold'), justify="center", bg='white', fg='#318bd2')
    lbl_customer_id = tk.Label(customer, text="Customer ID", font=("Arial", 15), bg='white', fg='#318bd2')
    lbl_customer_name = tk.Label(customer, text="Customer Name", font=("Arial", 15), bg='white', fg='#318bd2')
    lbl_customer_dob = tk.Label(customer, text="Customer DOB (dd/mm/yyyy)", font=("Arial", 15), bg='white', fg='#318bd2')
    lbl_customer_address = tk.Label(customer, text="Customer Address", font=("Arial", 15), bg='white', fg='#318bd2')
    lbl_customer_phone = tk.Label(customer, text="Customer Phone (10 digits)", font=("Arial", 15), bg='white', fg='#318bd2')
    lbl_customer_email = tk.Label(customer, text="Customer Email", font=("Arial", 15), bg='white', fg='#318bd2')

    # Create entry boxes   
    global cu_ID, cu_name, cu_dob, cu_address, cu_phone, cu_email 
    cu_ID = tk.StringVar()
    cu_name = tk.StringVar()
    cu_dob = tk.StringVar()
    cu_address = tk.StringVar()
    cu_phone = tk.StringVar()
    cu_email = tk.StringVar()

    ent_customer_id = tk.Entry(customer, width=43, textvariable=cu_ID, font=("Arial", 13), relief='flat', borderwidth=0, fg='firebrick1', highlightthickness=0, justify="left")
    ent_customer_name = tk.Entry(customer, width=43, textvariable=cu_name, font=("Arial", 13), relief='flat', borderwidth=0, fg='firebrick1', highlightthickness=0, justify="left")
    ent_customer_dob = tk.Entry(customer, width=43, textvariable=cu_dob, font=("Arial", 13), relief='flat', borderwidth=0, fg='firebrick1', highlightthickness=0, justify="left")
    ent_customer_address = tk.Entry(customer, width=43, textvariable=cu_address, font=("Arial", 13), relief='flat', borderwidth=0, fg='firebrick1', highlightthickness=0, justify="left")
    ent_customer_phone = tk.Entry(customer, width=43, textvariable=cu_phone, font=("Arial", 13), relief='flat', borderwidth=0, fg='firebrick1', highlightthickness=0, justify="left")
    ent_customer_email = tk.Entry(customer, width=43, textvariable=cu_email, font=("Arial", 13), relief='flat', borderwidth=0, fg='firebrick1', highlightthickness=0, justify="left")

    # Enter event for entry boxess
    ent_customer_id.bind("<Return>", lambda event: ent_customer_name.focus())
    ent_customer_name.bind("<Return>", lambda event: ent_customer_dob.focus())
    ent_customer_dob.bind("<Return>", lambda event: ent_customer_address.focus())
    ent_customer_address.bind("<Return>", lambda event: ent_customer_phone.focus())
    ent_customer_phone.bind("<Return>", lambda event: ent_customer_email.focus())
    ent_customer_email.bind("<Return>", lambda event: add_customer_func(cu_ID.get(), cu_name.get(), cu_dob.get(), cu_address.get(), cu_phone.get(), cu_email.get()))

    # Create lines for entry boxes
    line_customer_id = tk.Canvas(customer, width=433, height=2, bg='firebrick1', highlightthickness=0)
    line_customer_id.place(x=370, y=214)
    line_customer_name = tk.Canvas(customer, width=433, height=2, bg='firebrick1', highlightthickness=0)  
    line_customer_name.place(x=370, y=274)
    line_customer_dob = tk.Canvas(customer, width=433, height=2, bg='firebrick1', highlightthickness=0)
    line_customer_dob.place(x=370, y=334)
    line_customer_address = tk.Canvas(customer, width=433, height=2, bg='firebrick1', highlightthickness=0)
    line_customer_address.place(x=370, y=394)
    line_customer_phone = tk.Canvas(customer, width=433, height=2, bg='firebrick1', highlightthickness=0)
    line_customer_phone.place(x=370, y=454)
    line_customer_email = tk.Canvas(customer, width=433, height=2, bg='firebrick1', highlightthickness=0)
    line_customer_email.place(x=370, y=514)

    # Create buttons
    btn_save = tk.Button(customer, image = img_save, text="Save", compound = 'left', width=320, height = 25, bg='#0052cc', fg='#ffffff', bd=0, activebackground='firebrick1', highlightthickness=0, command=lambda: add_customer_func(cu_ID.get(), cu_name.get(), cu_dob.get(), cu_address.get(), cu_phone.get(), cu_email.get()))
    btn_save['font'] = btn_font
    btn_exit = tk.Button(customer, image = img_e2, text="Exit", compound = 'left', width=320, height = 25, bd=0, activebackground='firebrick1', highlightthickness=0, command=customer.destroy, bg='#0052cc', fg='#ffffff')
    btn_exit['font'] = btn_font

    # Style labels, entry boxes and buttons
    lbl_customer.place(x=410, y=90)
    lbl_customer_id.place(x=370, y=160)
    ent_customer_id.place(x=370, y=190)
    lbl_customer_name.place(x=370, y=220)
    ent_customer_name.place(x=370, y=250)
    lbl_customer_dob.place(x=370, y=280)
    ent_customer_dob.place(x=370, y=310)
    lbl_customer_address.place(x=370, y=340)
    ent_customer_address.place(x=370, y=370)
    lbl_customer_phone.place(x=370, y=400)
    ent_customer_phone.place(x=370, y=430)
    lbl_customer_email.place(x=370, y=460)
    ent_customer_email.place(x=370, y=490)
    btn_exit.place(x=100, y=580)
    btn_save.place(x=460, y=580)

    # Define a function for saving customer info
    def add_customer_func(cu_ID, cu_name, cu_dob, cu_address, cu_phone, cu_email):
        if func.check_if_empty(cu_ID) == False:
            messagebox.showerror("Error","Customer ID cannot be empty!", parent=customer)
        elif func.check_if_empty(cu_name) == False:
            messagebox.showerror("Error","Customer name cannot be empty!", parent=customer)
        elif func.check_if_empty(cu_dob) == False:
            messagebox.showerror("Error","Customer date of birth cannot be empty!", parent=customer)
        elif func.check_dob(cu_dob) == False:
            messagebox.showerror("Error", "Invalid Date of Birth format!\nPlease try again!", parent=customer)
        elif func.check_if_empty(cu_phone) == False:
            messagebox.showerror("Error","Customer phone number cannot be empty!", parent=customer)
        elif func.check_phone(cu_phone) == False:
            messagebox.showerror("Error", "Invalid phone number!\nPlease try again!", parent=customer)
        elif func.check_if_empty(cu_email) == False:
            messagebox.showerror("Error","Customer e-mail address cannot be empty!", parent=customer)
        elif func.check_email(cu_email) == False:
            messagebox.showerror("Error", "Invalid e-mail type!\nPlease try again!", parent=customer)
        elif sql_customers.Database().Validate(cu_ID, cu_phone, cu_email, 1) == True:
            messagebox.showerror("Error", "ID or Phone or Email info is already exists!\nPlease try again!", parent = customer)
        else:
            if func.add_customer(cu_ID, cu_name, cu_dob, cu_address, cu_phone, cu_email) == True:
                messagebox.showinfo("Success", "Customer info saved successfully!\nPress 'OK' to continue", parent = customer)
                # Close the window
                if sql_customers.Database().Storage() == 0:
                    btn_customer['state'] = 'disabled'
                else:
                    if sql_books.Database().Storage() == 0:
                        btn_sell_book['state'] = 'disabled'
                    else:
                        btn_sell_book['state'] = 'normal'
                    btn_customer['state'] = 'normal'
                customer.destroy()
            elif func.add_customer(cu_ID, cu_name, cu_dob, cu_address, cu_phone, cu_email) == False:
                messagebox.showerror("Error", "Customer info failed to save!\nPlease check again!", parent = customer)
        

def customer_list():

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
    list_customer = tk.Toplevel(window)
    list_customer.title("Customer List")
    list_customer.geometry("1100x500")
    list_customer.resizable(False,False)

    lbl_img = tk.Label(list_customer, image = imglist)
    lbl_img.place(x=0, y=0)
    lbl_title = tk.Label(list_customer, text="Customer List", font=("Arial", 25, 'bold'), justify="center", bg='white', fg='#318bd2')
    lbl_title.place(x=440, y=40)

    # Create tree view frame
    frm = tk.Frame(list_customer)
    frm.place(x=70, y=90)

    # Create scrollbar
    tree_scroll = tk.Scrollbar(frm)
    tree_scroll.pack(side='right', fill='y')

    # Create tree view
    tree = ttk.Treeview(frm, yscrollcommand=tree_scroll.set)
    tree.pack()

    # Configure scrollbar
    tree_scroll.config(command=tree.yview)
    tree['show']='headings'

    # Define number of columns
    tree["columns"] = ("ID", "Name", "Date of Birth", "Address", "Phone", "Email")
    #Assign the width,minwidth and anchor to the respective columns 
    tree.column ("ID", width=100, minwidth=50,anchor=tk.CENTER) 
    tree.column ("Name", width=200, minwidth=100,anchor=tk.CENTER) 
    tree.column ("Date of Birth", width=100, minwidth=100,anchor=tk.CENTER) 
    tree.column ("Address", width=250, minwidth=150, anchor=tk .CENTER) 
    tree.column ("Phone", width=150, minwidth=150, anchor=tk .CENTER) 
    tree.column ("Email", width=150, minwidth=150, anchor=tk.CENTER)

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
        db = sql_customers.Database().Storage()
        for i in range(0,len(db)):
            if i % 2 == 0:
                tree.insert('', i, iid= None, values = (db[i][0],db[i][1],db[i][2],db[i][3],db[i][4],db[i][5],">"+db[i][0]),tags='even_row')
            else:
                tree.insert('', i, iid= None, values = (db[i][0],db[i][1],db[i][2],db[i][3],db[i][4],db[i][5],">"+db[i][0]),tags='odd_row')
                
    list_all()

    def del_cf():
        # Return STRING VALUE of the selected item
        try:
            del_ID = tree.item(tree.focus())['values'][6][1:]
        except:
            return
        cf = messagebox.askyesno("Delete", "Are you sure you want to delete this customer?", parent=list_customer)
        if cf == True:
            delete_customer_func(del_ID)

    def delete_customer_func(id):
        if func.remove_customer(id) == True:
            messagebox.showinfo("Success", "Customer deleted successfully!", parent=list_customer)
            tree.delete(tree.focus())
            if len(sql_customers.Database().Storage()) == 0:
                btn_customer['state'] = 'disabled'
            else:
                btn_customer['state'] = 'normal'
        else:
            messagebox.showerror("Error", "Customer not deleted!", parent=list_customer)

    # Add button frames

    btn_refresh = tk.Button(list_customer, text="Refresh", width=14, height=2, bg='#318bd2', fg='white', activebackground='firebrick1', highlightthickness=0, command=lambda: list_all())
    btn_refresh['font'] = ['Arial', '15', 'bold']
    btn_search = tk.Button(list_customer, text="Search", width=14, height=2, bg='#318bd2', fg='white', activebackground='firebrick1', highlightthickness=0, command=lambda: Search_interface())
    btn_search['font'] = ['Arial', '15', 'bold']
    btn_delete = tk.Button(list_customer, text="Delete", width=14, height=2, bg='#318bd2', fg='white', activebackground='firebrick1', highlightthickness=0, command=lambda: del_cf())
    btn_delete['font'] = ['Arial', '15', 'bold']
    btn_update = tk.Button(list_customer, text="Update", width=14, height=2, bg='#318bd2', fg='white', activebackground='firebrick1', highlightthickness=0, command=lambda: modify_customer())
    btn_update['font'] = ['Arial', '15', 'bold']
    btn_exit = tk.Button(list_customer, text="Exit", width=14, height=2, bg='#318bd2', fg='white', activebackground='firebrick1', highlightthickness=0, command=list_customer.destroy)
    btn_exit['font'] = ['Arial', '15', 'bold']

    btn_refresh.place(x=72, y=390)
    btn_search.place(x=267, y=390)
    btn_delete.place(x=462, y=390)
    btn_update.place(x=657, y=390)
    btn_exit.place(x=852, y=390)

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
            if func.Searchall_customer(id, name, dob, address, phone, email) == False:
                messagebox.showerror("Error", "Something went wrong\nPlease try again!", parent=list_customer)
            elif len(func.Searchall_customer(id, name, dob, address, phone, email))==0:
                messagebox.showinfo("","0 results found!", parent=list_customer)
            else:
                db = func.Searchall_customer(id, name, dob, address, phone, email)
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

        # Get customer list
        cus_ID.set(id)

        # Get customer info and set to entry boxes after selecting customer
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
            cf = messagebox.askyesno("Save", "Are you sure you want to overide this customer info?", parent=customer)
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

        # Define a function for saving customer info
        def modify_customer_func():
            if func.check_if_empty(cus_ID.get()) == False:
                messagebox.showerror("Error","Customer ID cannot be empty!", parent=customer)
            elif func.check_if_empty(cus_name.get()) == False:
                messagebox.showerror("Error","Customer name cannot be empty!", parent=customer)
            elif func.check_if_empty(cus_dob.get()) == False:
                messagebox.showerror("Error","Customer date of birth cannot be empty!", parent=customer)
            elif func.check_dob(cus_dob.get()) == False:
                messagebox.showerror("Error", "Invalid Date of Birth format!\nPlease try again!", parent=customer)
            elif func.check_if_empty(cus_phone.get()) == False:
                messagebox.showerror("Error","Customer phone number cannot be empty!", parent=customer)
            elif func.check_phone(cus_phone.get()) == False:
                messagebox.showerror("Error", "Invalid phone number!\nPlease try again!", parent=customer)
            elif func.check_if_empty(cus_email.get()) == False:
                messagebox.showerror("Error","Customer e-mail address cannot be empty!", parent=customer)
            elif func.check_email(cus_email.get()) == False:
                messagebox.showerror("Error", "Invalid e-mail type!\nPlease try again!", parent=customer)
            elif sql_customers.Database().Validate(cus_ID.get(), cus_phone.get(), cus_email.get(), 2) == True:
                messagebox.showerror("Error", "Phone or Email info is already exists!\nPlease try again!", parent=customer)
            else:
                sql_customers.Database().Update(cus_name.get(), cus_dob.get(), cus_address.get(), cus_phone.get(), cus_email.get(), cus_ID.get())
                messagebox.showinfo("Success", "Customer info saved!\nPlease refresh the page to see the changes!", parent=customer)
                customer.destroy()
            
#End customer section

# Book SECTION
#Function to add new book (New window)
def add_book():
    book = tk.Toplevel(window)
    book.title("Add New Book")
    book.geometry("900x700")
    book.resizable(False, False)
    
    #Add book cmd
    def add_book_func(book_id, book_title, book_genre, book_author, book_target, book_pub, book_price, book_quantity):
        if func.check_if_empty(book_id) == False:
            messagebox.showerror("Error","Book ID cannot be empty!", parent=book)
        elif func.check_if_empty(book_title) == False:
            messagebox.showerror("Error","Book title cannot be empty!", parent=book)
        elif func.check_if_empty(book_genre) == False:
            messagebox.showerror("Error","Gerne cannot be empty!", parent=book)
        elif func.check_if_empty(book_author) == False:
            messagebox.showerror("Error", "Author name cannot be empty!", parent=book)
        elif func.check_if_empty(book_target) == False:
            messagebox.showerror("Error","The target for this book cannot be empty!", parent=book)
        elif func.check_if_empty(book_pub) == False:
            messagebox.showerror("Error", "Publisher name cannot be empty!", parent=book)
        elif func.check_if_empty(book_price) == False:
            messagebox.showerror("Error","Book price cannot be empty!\nAre you giving them away?!", parent=book)
        elif func.check_if_empty(book_quantity) == False:
            messagebox.showerror("Error", "Quantity cannot be empty!", parent=book)
        elif (sql_books.Database().Validate(book_id, book_title, book_author, 1) == True):
            messagebox.showerror("Error", "Book already exist!", parent=book)
        elif (func.validate_price_quatity(book_price, book_quantity)==False):
            messagebox.showerror("Error", "Invalid Price or Quantity!", parent=book)
        else:
            if func.add_book(book_id, book_title, book_genre, book_author, book_target, book_pub, book_price, book_quantity)==True:
                messagebox.showinfo("OK", "Book added successfully!", parent=book)
                if sql_books.Database().Storage() == 0:
                    btn_book['state'] = 'disabled'
                else:
                    if sql_customers.Database().Storage() == 0:
                        btn_sell_book['state'] = 'disabled'
                    else:
                        btn_sell_book['state'] = 'normal'
                    btn_book['state'] = 'normal'
                book.destroy()
            elif func.add_book(book_id, book_title, book_genre, book_author, book_target, book_pub, book_price, book_quantity)==False:
                messagebox.showerror("Error", "Book info failed to save!\nPlease check again!", parent=book)

    # Widgets
    btn_font = tkfont.Font(family = "Arial", size = 15)
    lbl_img = tk.Label(master = book, image = imgbook)
    lbl_img.place(x = 0, y = 0)

    # Labels
    lbl_book = tk.Label(master = book, text = 'Add New Book Info', font = ("Arial", 23, "bold"), justify = "center", bg='white', fg='#318bd2')
    lbl_book_id = tk.Label(master = book, text = 'Book ID', font = ("Arial", 15), bg='white', fg='#318bd2')
    lbl_book_title = tk.Label(master = book, text = 'Title', font = ("Arial", 15), bg='white', fg='#318bd2')
    lbl_book_genre = tk.Label(master = book, text = 'Genre', font = ("Arial", 15), bg='white', fg='#318bd2')
    lbl_book_author = tk.Label(master = book, text = 'Author', font = ("Arial", 15), bg='white', fg='#318bd2')
    lbl_book_target = tk.Label(master = book, text = 'Target Audience', font = ("Arial", 15), bg='white', fg='#318bd2')
    lbl_book_pub = tk.Label(master = book, text = 'Publisher', font = ("Arial", 15), bg='white', fg='#318bd2')
    lbl_book_price = tk.Label(master = book, text = 'Price (VND)', font = ("Arial", 15), bg='white', fg='#318bd2')
    lbl_book_quantity = tk.Label(master = book, text = 'Stock', font = ("Arial", 15), bg='white', fg='#318bd2')
    
    #Define entry boxes var
    book_id = tk.StringVar()
    book_title = tk.StringVar()
    book_genre = tk.StringVar()
    book_author = tk.StringVar()
    book_target = tk.StringVar()
    book_pub = tk.StringVar()
    book_price = tk.StringVar()
    book_quantity = tk.StringVar()
    
    #Entry boxes
    ent_book_id = tk.Entry(master = book, width = 43, textvariable = book_id, font = ("Arial", 13), relief='flat', borderwidth=0, fg='firebrick1', highlightthickness=0, justify="left")
    ent_book_title = tk.Entry(master = book, width = 43, textvariable = book_title, font = ("Arial", 13), relief='flat', borderwidth=0, fg='firebrick1', highlightthickness=0, justify="left")
    ent_book_genre = tk.Entry(master = book, width = 43, textvariable = book_genre, font = ("Arial", 13), relief='flat', borderwidth=0, fg='firebrick1', highlightthickness=0, justify="left")
    ent_book_author = tk.Entry(master = book, width = 43, textvariable = book_author, font = ("Arial", 13), relief='flat', borderwidth=0, fg='firebrick1', highlightthickness=0, justify="left")
    ent_book_target = tk.Entry(master = book, width = 43, textvariable = book_target, font = ("Arial", 13), relief='flat', borderwidth=0, fg='firebrick1', highlightthickness=0, justify="left")
    ent_book_pub = tk.Entry(master = book, width = 43, textvariable = book_pub, font = ("Arial", 13), relief='flat', borderwidth=0, fg='firebrick1', highlightthickness=0, justify="left")
    ent_book_price = tk.Entry(master = book, width = 43, textvariable = book_price, font = ("Arial", 13), relief='flat', borderwidth=0, fg='firebrick1', highlightthickness=0, justify="left")
    ent_book_quantity = tk.Entry(master = book, width = 43, textvariable = book_quantity, font = ("Arial", 13), relief='flat', borderwidth=0, fg='firebrick1', highlightthickness=0, justify="left")
    
    # Enter event for entry boxes
    ent_book_id.bind("<Return>", lambda event: ent_book_title.focus())
    ent_book_title.bind("<Return>", lambda event: ent_book_genre.focus())
    ent_book_genre.bind("<Return>", lambda event: ent_book_author.focus())
    ent_book_author.bind("<Return>", lambda event: ent_book_target.focus())
    ent_book_target.bind("<Return>", lambda event: ent_book_pub.focus())
    ent_book_pub.bind("<Return>", lambda event: ent_book_price.focus())
    ent_book_price.bind("<Return>", lambda event: ent_book_quantity.focus())
    ent_book_quantity.bind("<Return>", lambda event: add_book_func(book_id.get(), book_title.get(), book_genre.get(), book_author.get(), book_target.get(), book_pub.get(), book_price.get(), book_quantity.get()))

    # Create lines for entry boxes
    line_book_id = tk.Canvas(book, width=433, height=2, bg='firebrick1', highlightthickness=0)
    line_book_id.place(x=360, y=164)
    line_book_title = tk.Canvas(book, width=433, height=2, bg='firebrick1', highlightthickness=0)
    line_book_title.place(x=360, y=224)
    line_book_genre = tk.Canvas(book, width=433, height=2, bg='firebrick1', highlightthickness=0)
    line_book_genre.place(x=360, y=284)
    line_book_author = tk.Canvas(book, width=433, height=2, bg='firebrick1', highlightthickness=0)
    line_book_author.place(x=360, y=344)
    line_book_target = tk.Canvas(book, width=433, height=2, bg='firebrick1', highlightthickness=0)
    line_book_target.place(x=360, y=404)
    line_book_pub = tk.Canvas(book, width=433, height=2, bg='firebrick1', highlightthickness=0)
    line_book_pub.place(x=360, y=464)
    line_book_price = tk.Canvas(book, width=433, height=2, bg='firebrick1', highlightthickness=0)
    line_book_price.place(x=360, y=524)
    line_book_quantity = tk.Canvas(book, width=433, height=2, bg='firebrick1', highlightthickness=0)
    line_book_quantity.place(x=360, y=584)

    # Add save cmd
    btn_save = tk.Button(book, image = img_save, text = "Save", compound = 'left', width=320, height = 25, bg='#0052cc', fg='#ffffff', bd=0, activebackground='firebrick1', highlightthickness=0,  command = lambda: add_book_func(book_id.get(), book_title.get(), book_genre.get(), book_author.get(), book_target.get(), book_pub.get(), book_price.get(), book_quantity.get()))
    btn_save['font'] = btn_font
    btn_exit = tk.Button(book, image = img_e2, text = "Exit", compound = 'left', width=320, height = 25, bg='#0052cc', fg='#ffffff', bd=0, activebackground='firebrick1', highlightthickness=0, command = book.destroy)
    btn_exit['font'] = btn_font

    # Style for all
    lbl_book.place(x=440, y=60)
    lbl_book_id.place(x=360, y=110)
    ent_book_id.place(x=360, y=140)
    lbl_book_title.place(x=360, y=170)
    ent_book_title.place(x=360, y=200)
    lbl_book_genre.place(x=360, y=230)
    ent_book_genre.place(x=360, y=260)
    lbl_book_author.place(x=360, y=290)
    ent_book_author.place(x=360, y=320)
    lbl_book_target.place(x=360, y=350)
    ent_book_target.place(x=360, y=380)
    lbl_book_pub.place(x=360, y=410)
    ent_book_pub.place(x=360, y=440)
    lbl_book_price.place(x=360, y=470)
    ent_book_price.place(x=360, y=500)
    lbl_book_quantity.place(x=360, y=530)
    ent_book_quantity.place(x=360, y=560)
    btn_exit.place(x=100, y=610)
    btn_save.place(x=460, y=610)
    

#Book List window
def book_list():
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

    list_book = tk.Toplevel(window)
    list_book.title("Book List")
    list_book.geometry("1100x500")
    list_book.resizable(False,False)

    lbl_img = tk.Label(list_book, image = imglist)
    lbl_img.place(x=0, y=0)
    lbl_title = tk.Label(list_book, text="Book List", font=("Arial", 25, 'bold'), justify="center", bg='white', fg='#318bd2')
    lbl_title.place(x=470, y=40)

    # Create frame for treeview
    tree_frame = tk.Frame(list_book)
    tree_frame.place(x=70, y=90)

    # Create scrollbar
    tree_scroll = tk.Scrollbar(tree_frame)
    tree_scroll.pack(side='right',fill="y")

    tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)
    tree.pack()

    # Configure scrollbar
    tree_scroll.config(command=tree.yview)
    tree['show']='headings'

    # Define number of columns
    tree["columns"] = ("ID", "Title", "Genre", "Author", "Target", "Publisher", "Price", "Quantity")
    #Assign the width,minwidth and anchor to the respective columns 
    tree.column ("ID", width=50, minwidth=20,anchor=tk.CENTER) 
    tree.column ("Title", width=150, minwidth=100,anchor=tk.CENTER) 
    tree.column ("Genre", width=100, minwidth=50,anchor=tk.CENTER) 
    tree.column ("Author", width=150, minwidth=100, anchor=tk .CENTER) 
    tree.column ("Target", width=100, minwidth=50, anchor=tk .CENTER) 
    tree.column ("Publisher", width=150, minwidth=100, anchor=tk.CENTER)
    tree.column ("Price", width=150, minwidth=100, anchor=tk .CENTER) 
    tree.column ("Quantity", width=100, minwidth=50, anchor=tk.CENTER)

    #Assign the heading names to the respective columns 
    tree.heading ("ID", text="ID", anchor=tk.CENTER) 
    tree.heading ("Title", text="Title", anchor=tk.CENTER) 
    tree.heading ("Genre", text="Genre", anchor=tk. CENTER)
    tree.heading ("Author", text="Author", anchor=tk.CENTER) 
    tree.heading ("Target", text="Target", anchor=tk.CENTER)
    tree.heading ("Publisher", text="Publisher", anchor=tk.CENTER) 
    tree.heading ("Price", text="Price", anchor=tk.CENTER)
    tree.heading ("Quantity", text="Quantity", anchor=tk.CENTER)

    # Color for odd and even row
    tree.tag_configure('even_row',background='white')
    tree.tag_configure('odd_row',background='lightblue')

    def list_all():
        tree.delete(*tree.get_children())
        db = sql_books.Database().Storage()
        for i in range(0,len(db)):
            if i % 2 == 0:
                tree.insert('', i, iid= None, values = (db[i][0],db[i][1],db[i][2],db[i][3],db[i][4],db[i][5],db[i][6],db[i][7],">"+db[i][0]),tags='even_row')
            else:
                tree.insert('', i, iid= None, values = (db[i][0],db[i][1],db[i][2],db[i][3],db[i][4],db[i][5],db[i][6],db[i][7],">"+db[i][0]),tags='odd_row')
    list_all()

    def del_cf():
        # Return STRING VALUE of the selected item
        try:
            del_ID = tree.item(tree.focus())['values'][8][1:]
        except:
            return
        cf = tk.messagebox.askyesno("Delete", "Are you sure you want to delete this book?", parent = list_book)
        if cf == True:
            delete_book_func(del_ID)

    def delete_book_func(id):
        if func.remove_book(id) == True:
            messagebox.showinfo("Success", "Book deleted successfully!", parent = list_book)
            tree.delete(tree.focus())
            if len(sql_books.Database().Storage()) == 0:
                btn_book['state'] = 'disabled'
            else:
                btn_book['state'] = 'normal'
        else:
            messagebox.showerror("Error", "Customer not deleted!", parent = list_book)

    btn_refresh = tk.Button(list_book, text="Refresh",  width=14, height=2, bg='#318bd2', fg='white', activebackground='firebrick1', highlightthickness=0, command=lambda: list_all())
    btn_refresh['font'] = ['Arial', '15', 'bold']
    btn_search = tk.Button(list_book, text="Search", width=14, height=2, bg='#318bd2', fg='white', activebackground='firebrick1', highlightthickness=0, command=lambda: Search_interface())
    btn_search['font'] = ['Arial', '15', 'bold']
    btn_delete = tk.Button(list_book, text="Delete", width=14, height=2, bg='#318bd2', fg='white', activebackground='firebrick1', highlightthickness=0, command=lambda: del_cf())
    btn_delete['font'] = ['Arial', '15', 'bold']
    btn_update = tk.Button(list_book, text="Update", width=14, height=2, bg='#318bd2', fg='white', activebackground='firebrick1', highlightthickness=0, command=lambda: mod_book())
    btn_update['font'] = ['Arial', '15', 'bold']
    btn_exit = tk.Button(list_book, text="Exit", width=14, height=2, bg='#318bd2', fg='white', activebackground='firebrick1', highlightthickness=0, command=list_book.destroy)
    btn_exit['font'] = ['Arial', '15', 'bold']

    btn_refresh.place(x=72, y=390)
    btn_search.place(x=267, y=390)
    btn_delete.place(x=462, y=390)
    btn_update.place(x=657, y=390)
    btn_exit.place(x=852, y=390)

    def Search_interface():
        search_inter = tk.Toplevel(list_book)
        frm = tk.Frame(search_inter)
        # Create widgets
        btn_font = tkfont.Font(family="Arial", size=15)

        # Create labels
        lbl_book = tk.Label(frm, text="Search Book", font=("Arial", 20, 'bold'), justify="center")
        lbl_book_id = tk.Label(frm, text="Book ID", font=("Arial", 15))
        lbl_book_title = tk.Label(frm, text="Book Title", font=("Arial", 15))
        lbl_book_genre = tk.Label(frm, text="Book Genre", font=("Arial", 15))
        lbl_book_author = tk.Label(frm, text="Book Author", font=("Arial", 15))
        lbl_book_target = tk.Label(frm, text="Book Target", font=("Arial", 15))
        lbl_book_publisher = tk.Label(frm, text="Book Publisher", font=("Arial", 15))
        lbl_book_price = tk.Label(frm, text="Book Price (Format: ?-?)", font=("Arial", 15))
        lbl_book_quantity = tk.Label(frm, text="Book Quantity (Format: ?-?)", font=("Arial", 15))


        # Create entry boxes   
        global id, title, genre, author, target, publisher, price, quantity
        id = tk.StringVar()
        title = tk.StringVar()
        genre = tk.StringVar()
        author = tk.StringVar()
        target = tk.StringVar()
        publisher = tk.StringVar()
        price = tk.StringVar()
        quantity = tk.StringVar()

        ent_book_id = tk.Entry(frm, width=30, textvariable=id, font=("Arial", 15))
        ent_book_title = tk.Entry(frm, width=30, textvariable=title, font=("Arial", 15))
        ent_book_genre = tk.Entry(frm, width=30, textvariable=genre, font=("Arial", 15))
        ent_book_author = tk.Entry(frm, width=30, textvariable=author, font=("Arial", 15))
        ent_book_target = tk.Entry(frm, width=30, textvariable=target, font=("Arial", 15))
        ent_book_publisher = tk.Entry(frm, width=30, textvariable=publisher, font=("Arial", 15))
        ent_book_price = tk.Entry(frm, width=30, textvariable=price, font=("Arial", 15))
        ent_book_quantity = tk.Entry(frm, width=30, textvariable=quantity, font=("Arial", 15))

        # Create buttons
        btn_search = tk.Button(frm, text="Search", width=21, bg='#0052cc', fg='#ffffff', command=lambda: Search_book(id.get(), title.get(), genre.get(), author.get(), target.get(), publisher.get(), price.get(), quantity.get()))
        btn_search['font'] = btn_font
        btn_exit = tk.Button(frm, text="Exit", width=21, command=search_inter.destroy, bg='#fc0303', fg='#ffffff')
        btn_exit['font'] = btn_font

        # Style labels, entry boxes and buttons
        frm.grid(row=0, column=0, sticky="nsew")
        lbl_book.grid(row=0, column=0, columnspan=2, padx= 15, pady=15, sticky="nsew")
        lbl_book_id.grid(row=1, column=0, padx= 15, pady=5, sticky="nsew")
        lbl_book_title.grid(row=3, column=0, padx= 15, pady=5, sticky="nsew")
        lbl_book_genre.grid(row=4, column=0, padx= 15, pady=5, sticky="nsew")
        lbl_book_author.grid(row=5, column=0, padx= 15, pady=5, sticky="nsew")
        lbl_book_target.grid(row=6, column=0, padx= 15, pady=5, sticky="nsew")
        lbl_book_publisher.grid(row=7, column=0, padx= 15, pady=5, sticky="nsew")
        lbl_book_price.grid(row=8, column=0, padx= 15, pady=5, sticky="nsew")
        lbl_book_quantity.grid(row=9, column=0, padx= 15, pady=5, sticky="nsew") 
        ent_book_id.grid(row=1, column=1, padx= 15, pady=5, sticky="nsew")
        ent_book_title.grid(row=3, column=1, padx= 15, pady=5, sticky="nsew")
        ent_book_genre.grid(row=4, column=1, padx= 15, pady=5, sticky="nsew")
        ent_book_author.grid(row=5, column=1, padx= 15, pady=5, sticky="nsew")
        ent_book_target.grid(row=6, column=1, padx= 15, pady=5, sticky="nsew")
        ent_book_publisher.grid(row=7, column=1, padx= 15, pady=5, sticky="nsew")
        ent_book_price.grid(row=8, column=1, padx= 15, pady=5, sticky="nsew")
        ent_book_quantity.grid(row=9, column=1, padx= 15, pady=5, sticky="nsew")
        btn_exit.grid(row=10, column=0, padx= 15, pady=5, sticky="nsew")
        btn_search.grid(row=10, column=1, padx= 15, pady=5, sticky="nsew")
        
        # Prevent resizing
        search_inter.resizable(False, False)

        def Search_book(id, title, genre, author, target, publisher, price, quantity):
            data = func.check_price_quantity_format(price, quantity)
            if data == False:
                messagebox.showerror("Error", "Invalid Price or Quantity format!", parent = search_inter)
            elif func.Searchall_book(id, title, genre, author, target, publisher, data[0], data[1], data[2], data[3]) == False:
                messagebox.showerror("Error", "Something went wrong\nPlease try again!", parent = search_inter)
            elif len(func.Searchall_book(id, title, genre, author, target, publisher, data[0], data[1], data[2], data[3]))==0:
                messagebox.showinfo("","0 results found!", parent = search_inter)
            else:
                db = func.Searchall_book(id, title, genre, author, target, publisher, data[0], data[1], data[2], data[3])
                tree.delete(*tree.get_children())
                for i in range(0,len(db)):
                    tree.insert('', i, iid= None, values = (db[i][0],db[i][1],db[i][2],db[i][3],db[i][4],db[i][5],db[i][6],db[i][7],">"+db[i][0]))
                search_inter.destroy()

    #Function to modify book info
    def mod_book():
        try:
            id = tree.item(tree.focus())['values'][8][1:]
        except:
            return
        book = tk.Toplevel(window)
        book.title("Modify Book Info")
        frm_book = tk.Frame(book)

        #Mode book cmd
        def mod_book_func():
            if func.check_if_empty(book_id.get()) == False:
                messagebox.showerror("Error","Book ID cannot be empty!", parent=book)
            elif func.check_if_empty(book_title.get()) == False:
                messagebox.showerror("Error","Book title cannot be empty!", parent=book)
            elif func.check_if_empty(book_genre.get()) == False:
                messagebox.showerror("Error","Gerne cannot be empty!", parent=book)
            elif func.check_if_empty(book_author.get()) == False:
                messagebox.showerror("Error", "Author name cannot be empty!", parent=book)
            elif func.check_if_empty(book_target.get()) == False:
                messagebox.showerror("Error","The target for this book cannot be empty!", parent=book)
            elif func.check_if_empty(book_pub.get()) == False:
                messagebox.showerror("Error", "Publisher name cannot be empty!", parent=book)
            elif func.check_if_empty(book_price.get()) == False:
                messagebox.showerror("Error","Customer e-mail address cannot be empty!", parent=book)
            elif func.check_if_empty(book_price.get()) == False:
                    messagebox.showerror("Error", "Book price cannot be empty!\nAre you giving them away?!", parent=book)
            elif func.check_if_empty(book_quantity.get()) == False:
                messagebox.showerror("Error", "Quantity cannot be empty!", parent=book)
            elif sql_books.Database().Validate(book_id.get(), book_title.get(), book_author.get(), 2) == True:
                messagebox.showerror("Error", "Book with modfied info is already exist!\nPlease try again!", parent = book)
            elif (func.validate_price_quatity(book_price.get(), book_quantity.get())==False):
                messagebox.showerror("Error", "Invalid Price or Quantity!", parent = book)
            else:
                sql_books.Database().Update(book_title.get(), book_genre.get(),book_author.get(),book_target.get(),book_pub.get(),book_price.get(),book_quantity.get(),book_id.get())
                messagebox.showinfo("OK", "Book Info Modded!", parent = book)
                book.destroy()

        #Labels
        lbl_book = tk.Label(master = frm_book, text = 'Modify Book Info', font = ("Arial", 25, "bold"), justify = "center")
        lbl_book_title = tk.Label(master = frm_book, text = 'Title', font = ("Arial", 15))
        lbl_book_genre = tk.Label(master = frm_book, text = 'Genre', font = ("Arial", 15))
        lbl_book_author = tk.Label(master = frm_book, text = 'Author', font = ("Arial", 15))
        lbl_book_target = tk.Label(master = frm_book, text = 'Target Audience', font = ("Arial", 15))
        lbl_book_pub = tk.Label(master = frm_book, text = 'Publisher', font = ("Arial", 15))
        lbl_book_price = tk.Label(master = frm_book, text = 'Price (VND)', font = ("Arial", 15))
        lbl_book_quantity = tk.Label(master = frm_book, text = 'Stock', font = ("Arial", 15))

        #Entry boxes var
        book_id = tk.StringVar()
        book_title = tk.StringVar()
        book_genre = tk.StringVar()
        book_author = tk.StringVar()
        book_target = tk.StringVar()
        book_pub = tk.StringVar()
        book_price = tk.StringVar()
        book_quantity = tk.StringVar()

        book_info = sql_books.Database().Search(id)[0]
        book_id.set(book_info[0])
        book_title.set(book_info[1])
        book_genre.set(book_info[2])
        book_author.set(book_info[3])
        book_target.set(book_info[4])
        book_pub.set(book_info[5])
        book_price.set(book_info[6])
        book_quantity.set(book_info[7])
        
        #Entry boxes
        ent_book_title = tk.Entry(master = frm_book, width = 30, textvariable = book_title, font = ("Arial", 15))
        ent_book_genre = tk.Entry(master = frm_book, width = 30, textvariable = book_genre, font = ("Arial", 15))
        ent_book_author = tk.Entry(master = frm_book, width = 30, textvariable = book_author, font = ("Arial", 15))
        ent_book_target = tk.Entry(master = frm_book, width = 30, textvariable = book_target, font = ("Arial", 15))
        ent_book_pub = tk.Entry(master = frm_book, width = 30, textvariable = book_pub, font = ("Arial", 15))
        ent_book_price = tk.Entry(master = frm_book, width = 30, textvariable = book_price, font = ("Arial", 15))
        ent_book_quantity = tk.Entry(master = frm_book, width = 30, textvariable = book_quantity, font = ("Arial", 15))
        
        #Save info cmd
        def save_book():
            cf = messagebox.askyesno("Save", "Update this book info?", parent = book)
            if cf == True:
                mod_book_func()
                
        #Buttons        
        btn_save = tk.Button(frm_book, text="Save", font = ("Arial", 15), width=21, command=lambda: save_book())
        btn_exit = tk.Button(frm_book, text="Exit", font = ("Arial", 15), width=21, command=book.destroy)

        #Grid layout
        frm_book.grid(row = 0, column = 0, sticky = "nsew")
        lbl_book.grid(row = 0, column = 0, columnspan = 2, padx = 15, pady = 5, sticky = "nsew")
        lbl_book_title.grid(row = 1, column = 0, padx = 15, pady = 5, sticky = "nsew")
        lbl_book_genre.grid(row = 2, column = 0, padx = 15, pady = 5, sticky = "nsew")
        lbl_book_author.grid(row = 3, column = 0, padx = 15, pady = 5, sticky = "nsew")
        lbl_book_target.grid(row = 4, column = 0, padx = 15, pady = 5, sticky = "nsew")
        lbl_book_pub.grid(row = 5, column = 0, padx = 15, pady = 5, sticky = "nsew")
        lbl_book_price.grid(row = 6, column = 0, padx = 15, pady = 5, sticky = "nsew")
        lbl_book_quantity.grid(row = 7, column = 0, padx = 15, pady = 5, sticky = "nsew")
        ent_book_title.grid(row = 1, column = 1, padx = 15, pady = 5, sticky = "nsew")
        ent_book_genre.grid(row = 2, column = 1, padx = 15, pady = 5, sticky = "nsew")
        ent_book_author.grid(row = 3, column = 1, padx = 15, pady = 5, sticky = "nsew")
        ent_book_target.grid(row = 4, column = 1, padx = 15, pady = 5, sticky = "nsew")
        ent_book_pub.grid(row = 5, column = 1, padx = 15, pady = 5, sticky = "nsew")
        ent_book_price.grid(row = 6, column = 1, padx = 15, pady = 5, sticky = "nsew")
        ent_book_quantity.grid(row = 7, column = 1, padx = 15, pady = 5, sticky = "nsew")
        btn_save.grid(row = 8, column = 1, padx = 15, pady = 5, sticky = "nsew")
        btn_exit.grid(row = 8, column = 0, padx = 15, pady = 5, sticky = "nsew")
        book.rowconfigure(0, weight=1, minsize=50)
        book.columnconfigure(0, weight=1, minsize=75)
        for i in range(10):
            frm_book.rowconfigure(i, weight=1, minsize=50)
        for i in range(2):  
            frm_book.columnconfigure(i, weight=1, minsize=75)

# -------------------------
# SELL BOOK FUNC
def sell_book_func():
    #Sell book window
    sell = tk.Toplevel()
    sell.title("Sell Book")
    sell.geometry("800x600")
    sell.resizable(False, False)

    # Create widgets
    btn_font = tkfont.Font(family="Arial", size=15)
    lbl_img = tk.Label(sell, image = imgsell)
    lbl_img.place(x=0, y=0)

    # Create labels
    lb_title = tk.Label(sell, text="Sell Book", font=("Arial", 23, 'bold'), justify="center", bg='white', fg='#318bd2')
    lb_book = tk.Label(sell, text="Book Title", font=("Arial", 15), bg='white', fg='#318bd2')
    lb_customer = tk.Label(sell, text="Customer", font=("Arial", 15), bg='white', fg='#318bd2')
    lb_quantity = tk.Label(sell, text="Quantity", font=("Arial", 15), bg='white', fg='#318bd2')
    # Create a label to display the selected book quantity
    lb_available = tk.Label(sell, font=("Arial", 10), bg='white', fg='#318bd2', justify="right")

    # Create dropdown menu for book title
    get_data_b = sql_books.Database()
    get_book = get_data_b.GetBooks()
    book_title = tk.StringVar()
    book_title.set("Select Book")
    book_list = []
    for i in get_book:
        book_list.append(i[0] + " - " + i[1] + " - " + str(i[2]) + " - " + str(i[3]))
    def change_dropdown(*args):
        for i in get_book:
            if book_title.get() == i[0] + " - " + i[1] + " - " + str(i[2]) + " - " + str(i[3]):
                book_quantity = str(i[2])
                book_id = i[0]
                lb_available.config(text=f"ID: {book_id} - Quantity: {book_quantity}\nPlease notice!", justify="right")
    drop_book = tk.OptionMenu(sell, book_title, *book_list, command=change_dropdown)
    drop_book.config(width=40, height=2, font=("Arial", 12), bg='white', fg='firebrick1', activebackground='firebrick1', activeforeground='white', highlightthickness=0)
    drop_book["menu"].config(bg='white', fg='firebrick1', activebackground='firebrick1', activeforeground='white')

    
    # Create dropdown menu for customer
    get_data_c = sql_customers.Database()
    get_customer = get_data_c.GetCustomers()
    customer = tk.StringVar()
    customer.set("Select Customer")
    customer_list = []
    for i in get_customer:
        customer_list.append(i[0] + " - " + i[1])
    drop_customer = tk.OptionMenu(sell, customer, *customer_list)
    drop_customer.config(width=40, height=2, font=("Arial", 12), bg='white', fg='firebrick1', activebackground='firebrick1', activeforeground='white', highlightthickness=0)
    drop_customer["menu"].config(bg='white', fg='firebrick1', activebackground='firebrick1', activeforeground='white')
    
    # Create entry for quantity
    box_quantity = tk.Entry(sell, width=44, font=("Arial", 12), relief='flat', borderwidth=0, fg='firebrick1', highlightthickness=0, justify="center")

    # Enter event for entry boxes
    box_quantity.bind("<Return>", lambda event: sell_book())
    
    # Create lines for entry box
    line_quantity = tk.Canvas(sell, width=400, height=2, bg='firebrick1', highlightthickness=0)
    line_quantity.place(x=300, y=380)

    # Create buttons
    btn_sell_cf = tk.Button(sell, text="Sell the book", width=34, bg='#318bd2', bd=0, activebackground='firebrick1', highlightthickness=0, command=lambda: sell_book())
    btn_exit = tk.Button(sell, text="Exit", width=34, bg='#318bd2', bd=0, activebackground='firebrick1', highlightthickness=0, command=sell.destroy)
    btn_sell_cf["font"] = btn_font
    btn_sell_cf.place(x=417, y=420)
    btn_exit["font"] = btn_font
    btn_exit.place(x=417, y=470)

    # Style labels, entry boxes and buttons
    lb_title.place(x=420, y=90)
    lb_book.place(x=300, y=150)
    lb_available.place(x=600, y=140)
    drop_book.place(x=300, y=180)
    lb_customer.place(x=300, y=240)
    drop_customer.place(x=300, y=270)
    lb_quantity.place(x=300, y=330)
    box_quantity.place(x=300, y=360)
    btn_sell_cf.place(x=302, y=420)
    btn_exit.place(x=302, y=470)

    # Sell book function
    def exec_sell():
        if func.check_if_empty(box_quantity.get()) == False:
            messagebox.showerror("Error", "Please enter a quantity!", parent=sell)
            return
        else:
            book_quantity = book_title.get().split(" - ")[2]
            if func.check_book_quantity(int(book_quantity)) == False:
                messagebox.showerror("Error","Out of stock!", parent=sell)
            elif int(box_quantity.get()) > int(book_quantity):
                messagebox.showerror("Error", "Inputed quantity is greater than available!\nPlease try again.", parent=sell)
            else:
                try:
                    book_id = book_title.get().split(" - ")[0]
                    book_tit = book_title.get().split(" - ")[1]
                    book_price = book_title.get().split(" - ")[3]
                    customer_id = customer.get().split(" - ")[0]
                    customer_name = customer.get().split(" - ")[1]
                    session_get = sql_session.Session().Print()
                    session_id = session_get[1]
                    session_name = session_get[2]
                    quantity = int(box_quantity.get())
                    print(f"{book_id} - {book_tit} - {str(book_price)} - {str(quantity)} - {customer_id} - {customer_name} - {session_id} - {session_name}")
                    func.add_sell(book_id, book_tit, book_price, quantity, customer_id, customer_name, session_id, session_name)
                    func.update_quantity(book_id, quantity)
                    if len(sql_sell.Sell().Storage()) != 0:
                        btn_list.config(state="normal")
                    ask = messagebox.askyesno("Success", "SOLD!\nDo you want to generate the invoice?", parent = sell)
                    if ask == True:
                        invoice()
                        messagebox.showinfo("Success", "Done!\nFile saved at the 'invoice' folder.", parent = sell)
                    sell.destroy()
                except Exception as e:
                    print(e)
                    messagebox.showerror("Error", "Please check again\nMaybe select a book and a customer", parent=sell)
                    return
    # Print 
    def invoice():
        # Set the os.path to save the pdf invoice file
        time = str(datetime.datetime.now().strftime("%d-%m-%Y_%H:%M:%S"))
        try:
            os.makedirs("invoice")
        except FileExistsError:
        # directory already exists
            pass
        canvas_name = f"invoice/HOADON_{time}.pdf"
        c = canvas.Canvas(canvas_name, pagesize = (200, 250), bottomup= 0)
        db = sql_store.Database().Storage()
        
        c.setFont("Times-Bold", 10)
        c.setFillColorRGB(0, 0, 0)

        c.line(70, 22, 180, 22)
        c.line(5, 45, 195, 45)
        c.line(15, 120, 185, 120)
        c.line(35, 108, 35, 220)
        c.line(105, 108, 105, 220)
        c.line(135, 108, 135, 220)
        c.line(155, 108, 155, 220)
        c.line(15, 220, 185, 220)

        c.translate(10, 40)
        c.scale(1, -1)
        c.drawImage(usth, 0, 0, width=50, height=30)

        c.scale(1, -1)
        c.translate(-10, -40)

        c.setFont("Times-Bold", 10)
        c.drawCentredString(125, 20, db[0][1])

        c.setFont("Times-Bold", 5)
        c.drawCentredString(125, 30, db[0][2])
        c.drawCentredString(125, 36, db[0][3])
        c.setFont("Times-Bold", 6)
        c.drawCentredString(125, 42, db[0][4])

        c.setFont("Times-Bold", 8)
        c.setFillColorRGB(1, 0, 0)
        c.drawCentredString(100, 55, "HOA DON / INVOICE")

        c.setFont("Times-Bold", 5)
        c.setFillColorRGB(0, 0, 0)
        c.drawRightString(105, 70, "Ma hoa don / Invoice No. :")
        c.drawString(110, 70, "XXXXXXX")

        c.drawRightString(105, 80, "Xuat hoa don / Date & Time:")
        c.drawString(110, 80, time.split("_")[0] + " - " + time.split("_")[1])

        c.drawRightString(105, 90, "Ma khach hang / Customer ID :")
        c.drawString(110, 90, customer.get().split(" - ")[0])

        c.drawRightString(105, 100, "Ten khach hang / Customer Name :")
        c.drawString(110, 100, customer.get().split(" - ")[1])

        c.roundRect(15, 108, 170, 130, 10, stroke=1, fill=0)
        c.setFillColorRGB(1, 0, 0)
        c.drawCentredString(25, 118, "No.")
        c.drawCentredString(70, 118, "Book Title")
        c.drawCentredString(120, 118, "Price")
        c.drawCentredString(145, 118, "Qty.")
        c.drawCentredString(169, 118, "Total")

        c.drawCentredString(25, 215, "1")
        c.drawCentredString(70, 215, book_title.get().split(" - ")[1])
        c.drawCentredString(120, 215, book_title.get().split(" - ")[3])
        c.drawCentredString(145, 215, box_quantity.get())
        c.drawCentredString(169, 215, str(int(box_quantity.get()) * int(book_title.get().split(" - ")[3])))

        c.drawString(30, 230, f"Cam on quy khach da mua hang tai {db[0][1]}!")
        c.showPage()
        c.save()

    def sell_book():
        ask = messagebox.askyesno("Sell Book", "Are you sure you want to sell this book?", parent=sell)
        if ask == True:
            exec_sell()
        else:
            pass

#Sale List window
def sale_list():
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

    list_sale = tk.Toplevel(window)
    list_sale.title("Sale List")
    list_sale.geometry("1100x500")
    list_sale.resizable(False,False)

    lbl_img = tk.Label(list_sale, image = imglist)
    lbl_img.place(x=0, y=0)
    lbl_title = tk.Label(list_sale, text="Sale List", font=("Arial", 25, 'bold'), justify="center", bg='white', fg='#318bd2')
    lbl_title.place(x=470, y=40)

    # Create frame for treeview
    tree_frame = tk.Frame(list_sale)
    tree_frame.place(x=70, y=90)

    # Create scrollbar
    tree_scroll = tk.Scrollbar(tree_frame)
    tree_scroll.pack(side='right',fill="y")

    tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)
    tree.pack()

    # Configure scrollbar
    tree_scroll.config(command=tree.yview)
    tree['show']='headings'

    # Define number of columns
    tree["columns"] = ("No.", "Book ID", "Book Title", "Quantity", "Customer ID", "Customer Name", "Staff ID", "Staff Name", "Date & Time")
    #Assign the width,minwidth and anchor to the respective columns 
    tree.column ("No.", width=50, minwidth=20,anchor=tk.CENTER)
    tree.column ("Book ID", width=80, minwidth=50,anchor=tk.CENTER)
    tree.column ("Book Title", width=155, minwidth=100,anchor=tk.CENTER)
    tree.column ("Quantity", width=65, minwidth=20,anchor=tk.CENTER)
    tree.column ("Customer ID", width=80, minwidth=50,anchor=tk.CENTER)
    tree.column ("Customer Name", width=155, minwidth=100,anchor=tk.CENTER)
    tree.column ("Staff ID", width=80, minwidth=50,anchor=tk.CENTER)
    tree.column ("Staff Name", width=155, minwidth=100,anchor=tk.CENTER)
    tree.column ("Date & Time", width=130, minwidth=100,anchor=tk.CENTER)

    #Assign the heading names to the respective columns 
    tree.heading ("No.", text="No.", anchor=tk.CENTER)
    tree.heading ("Book ID", text="Book ID", anchor=tk.CENTER)
    tree.heading ("Book Title", text="Book Title", anchor=tk.CENTER)
    tree.heading ("Quantity", text="Quantity", anchor=tk.CENTER)
    tree.heading ("Customer ID", text="Customer ID", anchor=tk.CENTER)
    tree.heading ("Customer Name", text="Customer Name", anchor=tk.CENTER)
    tree.heading ("Staff ID", text="Staff ID", anchor=tk.CENTER)
    tree.heading ("Staff Name", text="Staff Name", anchor=tk.CENTER)
    tree.heading ("Date & Time", text="Date & Time", anchor=tk.CENTER)

    # Color for odd and even row
    tree.tag_configure('even_row',background='white')
    tree.tag_configure('odd_row',background='lightblue')

    def list_all():
        tree.delete(*tree.get_children())
        db = sql_sell.Sell().Storage()
        for i in range(0,len(db)):
            if i % 2 == 0:
                tree.insert('', i, iid= None, values = (db[i][0],db[i][1],db[i][3],db[i][4],db[i][5],db[i][6],db[i][7],db[i][8],db[i][9]),tags='even_row')
            else:
                tree.insert('', i, iid= None, values = (db[i][0],db[i][1],db[i][3],db[i][4],db[i][5],db[i][6],db[i][7],db[i][8],db[i][9]),tags='odd_row')
    list_all()

    btn_refresh = tk.Button(list_sale, text="Refresh",  width=14, height=2, bg='#318bd2', fg='white', activebackground='firebrick1', highlightthickness=0, command=lambda: list_all())
    btn_refresh['font'] = ['Arial', '15', 'bold']
    btn_search1 = tk.Button(list_sale, text="Search", width=14, height=2, bg='#318bd2', fg='white', activebackground='firebrick1', highlightthickness=0, command=lambda: Search_interface())
    btn_search1['font'] = ['Arial', '15', 'bold']
    btn_exit = tk.Button(list_sale, text="Exit", width=14, height=2, bg='#318bd2', fg='white', activebackground='firebrick1', highlightthickness=0, command=list_sale.destroy)
    btn_exit['font'] = ['Arial', '15', 'bold']

    btn_refresh.place(x=72, y=390)
    btn_search1.place(x=267, y=390)
    btn_exit.place(x=852, y=390)

    def Search_interface():
        search_inter = tk.Toplevel(list_sale)
        frm = tk.Frame(search_inter)
        # Create widgets
        btn_font = tkfont.Font(family="Arial", size=15)

        # Create labels
        lbl_book = tk.Label(frm, text="Search Book", font=("Arial", 20, 'bold'), justify="center")
        lbl_book_id = tk.Label(frm, text="Book ID", font=("Arial", 15))
        lbl_book_title = tk.Label(frm, text="Book Title", font=("Arial", 15))
        lbl_book_genre = tk.Label(frm, text="Book Genre", font=("Arial", 15))
        lbl_book_author = tk.Label(frm, text="Book Author", font=("Arial", 15))
        lbl_book_target = tk.Label(frm, text="Book Target", font=("Arial", 15))
        lbl_book_publisher = tk.Label(frm, text="Book Publisher", font=("Arial", 15))
        lbl_book_price = tk.Label(frm, text="Book Price (Format: ?-?)", font=("Arial", 15))
        lbl_book_quantity = tk.Label(frm, text="Book Quantity (Format: ?-?)", font=("Arial", 15))


        # Create entry boxes   
        global id, title, genre, author, target, publisher, price, quantity
        id = tk.StringVar()
        title = tk.StringVar()
        genre = tk.StringVar()
        author = tk.StringVar()
        target = tk.StringVar()
        publisher = tk.StringVar()
        price = tk.StringVar()
        quantity = tk.StringVar()

        ent_book_id = tk.Entry(frm, width=30, textvariable=id, font=("Arial", 15))
        ent_book_title = tk.Entry(frm, width=30, textvariable=title, font=("Arial", 15))
        ent_book_genre = tk.Entry(frm, width=30, textvariable=genre, font=("Arial", 15))
        ent_book_author = tk.Entry(frm, width=30, textvariable=author, font=("Arial", 15))
        ent_book_target = tk.Entry(frm, width=30, textvariable=target, font=("Arial", 15))
        ent_book_publisher = tk.Entry(frm, width=30, textvariable=publisher, font=("Arial", 15))
        ent_book_price = tk.Entry(frm, width=30, textvariable=price, font=("Arial", 15))
        ent_book_quantity = tk.Entry(frm, width=30, textvariable=quantity, font=("Arial", 15))

        # # Create buttons
        # btn_search = tk.Button(frm, text="Search", width=21, bg='#0052cc', fg='#ffffff', command=lambda: Search_book(id.get(), title.get(), genre.get(), author.get(), target.get(), publisher.get(), price.get(), quantity.get()))
        # btn_search['font'] = btn_font
        btn_exit = tk.Button(frm, text="Exit", width=21, command=search_inter.destroy, bg='#fc0303', fg='#ffffff')
        btn_exit['font'] = btn_font

        # Style labels, entry boxes and buttons
        frm.grid(row=0, column=0, sticky="nsew")
        lbl_book.grid(row=0, column=0, columnspan=2, padx= 15, pady=15, sticky="nsew")
        lbl_book_id.grid(row=1, column=0, padx= 15, pady=5, sticky="nsew")
        lbl_book_title.grid(row=3, column=0, padx= 15, pady=5, sticky="nsew")
        lbl_book_genre.grid(row=4, column=0, padx= 15, pady=5, sticky="nsew")
        lbl_book_author.grid(row=5, column=0, padx= 15, pady=5, sticky="nsew")
        lbl_book_target.grid(row=6, column=0, padx= 15, pady=5, sticky="nsew")
        lbl_book_publisher.grid(row=7, column=0, padx= 15, pady=5, sticky="nsew")
        lbl_book_price.grid(row=8, column=0, padx= 15, pady=5, sticky="nsew")
        lbl_book_quantity.grid(row=9, column=0, padx= 15, pady=5, sticky="nsew") 
        ent_book_id.grid(row=1, column=1, padx= 15, pady=5, sticky="nsew")
        ent_book_title.grid(row=3, column=1, padx= 15, pady=5, sticky="nsew")
        ent_book_genre.grid(row=4, column=1, padx= 15, pady=5, sticky="nsew")
        ent_book_author.grid(row=5, column=1, padx= 15, pady=5, sticky="nsew")
        ent_book_target.grid(row=6, column=1, padx= 15, pady=5, sticky="nsew")
        ent_book_publisher.grid(row=7, column=1, padx= 15, pady=5, sticky="nsew")
        ent_book_price.grid(row=8, column=1, padx= 15, pady=5, sticky="nsew")
        ent_book_quantity.grid(row=9, column=1, padx= 15, pady=5, sticky="nsew")
        btn_exit.grid(row=10, column=0, padx= 15, pady=5, sticky="nsew")
        # btn_search.grid(row=10, column=1, padx= 15, pady=5, sticky="nsew")
        
        # Prevent resizing
        search_inter.resizable(False, False)

def exit_verify():
        # Verify if the user wants to exit the program
        box = messagebox.askquestion("Exit", "Are you sure you want to exit?")
        if box == "yes":
            # Find the bookstore.db file and then zip it
            with open("bookstore.dat", "wb") as outfile:
                with zipfile.ZipFile(outfile, "w") as zipf:
                    for file in os.listdir():
                        if file.endswith(".db"):
                            zipf.write(file)
            if os.path.exists("bookstore.db"):
                os.remove("bookstore.db")
            print("Compress files successfully!")
            messagebox.showinfo("Exit", "Thank you for using the program!\n© 2023 - BI12 - ICT Team 17")
            window.quit()
        else:
            pass

if os.path.exists("bookstore.db"):
    window = tk.Tk()
    window.geometry("800x600")
    window.protocol("WM_DELETE_WINDOW", exit_verify)
    

    imgbg = tk.PhotoImage(file="img/main.png")
    imgbook = tk.PhotoImage(file="img/book.png")
    imgsell = tk.PhotoImage(file="img/sell.png")
    imgcus= tk.PhotoImage(file="img/cus.png")
    imglist = tk.PhotoImage(file="img/list.png")
    # Fit the image to the buttons
    mod_c = tk.PhotoImage(file="img/icons/m_c.png")
    img_m_c = mod_c.subsample(2, 2)
    add_c = tk.PhotoImage(file="img/icons/a_c.png")
    img_a_c = add_c.subsample(2, 2)
    mod_b = tk.PhotoImage(file="img/icons/m_b.png")
    img_m_b = mod_b.subsample(2, 2)
    add_b = tk.PhotoImage(file="img/icons/a_b.png")
    img_a_b = add_b.subsample(2, 2)
    sell = tk.PhotoImage(file="img/icons/s_b.png")
    sell_b = sell.subsample(2, 2)
    book_sale = tk.PhotoImage(file="img/icons/b_s.png")
    img_b_s = book_sale.subsample(2, 2)
    ex = tk.PhotoImage(file="img/icons/exit.png")
    img_e = ex.subsample(2, 2)
    img_e2 = ex.subsample(3, 3)
    save = tk.PhotoImage(file="img/icons/save.png")
    img_save = save.subsample(3, 3)
    usth = os.path.abspath("img/USTH_Logo.png")

    lbl_hihi = tk.Label(image=imgbg)
    lbl_hihi.place(x=0, y=0)

    btn_font = tkfont.Font(family="Arial", size=15)

    if len(sql_session.Session().Storage()) == 0:
        session_id = "Guest"
        session_name = "Guest"
    else:
        session_get = sql_session.Session().Print()
        session_id = session_get[1]
        session_name = session_get[2]

    window.title(f"BSMS Beta - Logged in as staff: {session_id} - {session_name}")
    window.resizable(False, False)
    lbl_session = tk.Label(master=window, text='Welcome, ' + session_id +' - '+ session_name, font=("Arial", 13, "bold"), bg='#73a2c7', justify="left", fg='white')
    lbl_welcome = tk.Label(master=window, text="Book Store Management System\n(Staff Edition)", font=("Arial", 25, 'bold'), justify="center", bg='white', fg='#318bd2')
    lb_cpr = tk.Label(window, text="© 2023 - BI12 - ICT Team 17\nVersion BETA", font=("Arial", 6), bg='#73a2c7', justify="right", fg='white')

    btn_add_book = tk.Button(image=img_a_b,text="Add Book",compound = 'left', width=231, height=50, bg='#00ab1c', fg='#ffffff', command=add_book)
    btn_add_book['font'] = btn_font
    btn_book = tk.Button(image=img_a_b,text="Manage Book List",compound = 'left', width=231, height=50, bg='#00ab1c', fg='#ffffff', command = book_list)
    btn_book['font'] = btn_font
    btn_add_customer = tk.Button(image=img_a_c,text="Add Customer", compound = 'left', width=231, height=50, bg='#ab4d00', fg='#ffffff', command = add_customer)
    btn_add_customer['font'] = btn_font
    btn_customer = tk.Button(image=img_m_c,text="Customer List", compound = 'left', width=231, height=50, bg='#ab4d00', fg='#ffffff', command = customer_list)
    btn_customer['font'] = btn_font
    btn_sell_book = tk.Button(image= sell_b, text="Sell Book",compound = 'left', width=231, height=50, bg='#0052cc', fg='#ffffff', command = sell_book_func)
    btn_sell_book['font'] = btn_font
    btn_list = tk.Button(image=img_b_s, text="Sale List",compound = 'left', width=231, height=50, bg='#0052cc', fg='#ffffff', command = sale_list)
    btn_list['font'] = btn_font
    if len(sql_sell.Sell().Storage()) == 0:
        btn_list.config(state="disabled")
    if len(sql_books.Database().Storage()) == 0:
        btn_book.config(state="disabled")
    if len(sql_customers.Database().Storage()) == 0:
        btn_customer.config(state="disabled")
    btn_cut = tk.Button(image=img_e, text="Exit", compound= 'left', width=495, height=50, bg='#570b0b', fg='#ffffff', command = exit_verify)
    btn_cut['font'] = btn_font
    if len(sql_store.Database().Storage()) == 0:
        btn_add_book.config(state="disabled")
        btn_add_customer.config(state="disabled")
        btn_sell_book.config(state="disabled")
    if len(sql_books.Database().Storage()) == 0 or len(sql_customers.Database().Storage()) == 0:
        btn_sell_book.config(state="disabled")

    lbl_welcome.place(x=143, y=95)
    btn_add_book.place(x=143, y=195)
    btn_book.place(x=407, y=195)
    btn_add_customer.place(x=143, y=275)
    btn_customer.place(x=407, y=275)
    btn_sell_book.place(x=143, y=355)
    btn_list.place(x=407, y=355)
    btn_cut.place(x=143, y=435)
    lbl_session.place(x=5, y=5)
    lb_cpr.place(x=690, y=573)

    window.mainloop()
else:
    # Messagebox to inform the user that the program is not installed
    admin = tk.Tk()
    admin.withdraw()
    messagebox.showerror("Error", "The program is not running properly!\n\nPlease run from the program 'LOGIN.PY' first!", parent=admin)
    admin.quit()