import sys
sys.dont_write_bytecode = True
import tkinter as tk
from tkinter import messagebox, ttk, font as tkfont
import process_checker as func
import os
clear = lambda: os.system('clear')
from domains import sql_session
from domains import sql_customers
from domains import sql_books

# CUSTOMER SECTION

# Create a new window for creating customer info [DONE]
def add_customer():
    # Create a new window
    customer = tk.Toplevel(window)
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
    #global cu_ID, cu_name, cu_dob, cu_address, cu_phone, cu_email 
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
        if func.check_dob(cu_dob) == False:
            messagebox.showerror("Error", "Invalid Date of Birth format!\nPlease try again!")
        elif func.check_phone(cu_phone) == False:
            messagebox.showerror("Error", "Invalid phone number!\nPlease try again!")
        elif func.check_email(cu_email) == False:
            messagebox.showerror("Error", "Invalid email type!\nPlease try again!")
        elif sql_customers.Database().Validate(cu_ID, cu_phone, cu_email, 1) == True:
            messagebox.showerror("Error", "ID or Phone or Email info is already exists!\nPlease try again!")
        else:
            if func.add_customer(cu_ID, cu_name, cu_dob, cu_address, cu_phone, cu_email) == True:
                messagebox.showinfo("Success", "Customer info saved successfully!\nPress 'OK' to continue")
                # Close the window
                if sql_customers.Database().Storage() == 0:
                    btn_customer['state'] = 'disabled'
                else:
                    btn_customer['state'] = 'normal'
                customer.destroy()
            elif func.add_customer(cu_ID, cu_name, cu_dob, cu_address, cu_phone, cu_email) == False:
                messagebox.showerror("Error", "Customer info failed to save!\nPlease check again!")
        

def customer_list():
    clear()
    list_customer = tk.Toplevel(window)

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
        if func.remove_customer(id) == True:
            messagebox.showinfo("Success", "Customer deleted successfully!")
            tree.delete(tree.focus())
            if len(sql_customers.Database().Storage()) == 0:
                btn_customer['state'] = 'disabled'
            else:
                btn_customer['state'] = 'normal'
        else:
            messagebox.showerror("Error", "Customer not deleted!")

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
        lbl_customer_dob = tk.Label(frm, text="Customer DOB (dd/mm/yyyy)", font=("Arial", 15))
        lbl_customer_address = tk.Label(frm, text="Customer Address", font=("Arial", 15))
        lbl_customer_phone = tk.Label(frm, text="Customer Phone (10 digits)", font=("Arial", 15))
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
                messagebox.showerror("Error", "Something went wrong\nPlease try again!")
            elif len(func.Searchall_customer(id, name, dob, address, phone, email))==0:
                messagebox.showinfo("","0 results found!")
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
        lbl_customer_dob = tk.Label(customer_frame, text="Customer DOB (dd/mm/yyyy)", font=("Arial", 15))
        lbl_customer_address = tk.Label(customer_frame, text="Customer Address", font=("Arial", 15))
        lbl_customer_phone = tk.Label(customer_frame, text="Customer Phone (10 digits)", font=("Arial", 15))
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
        if func.check_dob(cus_dob.get()) == False:
            messagebox.showerror("Error", "Invalid Date of Birth format!\nPlease try again!")
        elif func.check_phone(cus_phone.get()) == False:
            messagebox.showerror("Error", "Invalid phone number!\nPlease try again!")
        elif func.check_email(cus_email.get()) == False:
            messagebox.showerror("Error", "Invalid email type!\nPlease try again!")
        elif sql_customers.Database().Validate(cus_ID.get(), cus_phone.get(), cus_email.get(), 2) == True:
            messagebox.showerror("Error", "Phone or Email info is already exists!\nPlease try again!")
        else:
            sql_customers.Database().Update(cus_name.get(), cus_dob.get(), cus_address.get(), cus_phone.get(), cus_email.get(), cus_ID.get())
            messagebox.showinfo("Success", "Staff info saved!\nPlease refresh the page to see the changes!")
    
    btn_refresh.pack()
    btn_search.pack()
    btn_delete.pack()
    btn_update.pack()
    btn_exit.pack()
            
#End customer section

# Book SECTION
#Function to add new book (New window)
def add_book():
    book = tk.Toplevel(window)
    book.title("Add New Book")
    frm_book = tk.Frame(book) 
    
    #Add book cmd
    def add_book_func(book_id, book_title, book_genre, book_author, book_target, book_pub, book_price, book_quantity):
        if (sql_books.Database().Validate(book_id, book_title, book_author, 1) == True):
            messagebox.showerror("Error", "Book already exist!")
        elif (func.validate_price_quatity(book_price, book_quantity)==False):
            messagebox.showerror("Error", "Invalid Price or Quantity!")
        else:
            if func.add_book(book_id, book_title, book_genre, book_author, book_target, book_pub, book_price, book_quantity)==True:
                messagebox.showinfo("OK", "Book added successfully!")
                if sql_books.Database().Storage() == 0:
                    btn_book['state'] = 'disabled'
                else:
                    btn_book['state'] = 'normal'
                book.destroy()
            elif func.add_book(book_id, book_title, book_genre, book_author, book_target, book_pub, book_price, book_quantity)==False:
                messagebox.showerror("Error", "Book info failed to save!\nPlease check again!")

    #Labels
    lbl_book = tk.Label(master = frm_book, text = 'Add New Book Info', font = ("Arial", 25, "bold"), justify = "center")
    lbl_book_id = tk.Label(master = frm_book, text = 'Book ID', font = ("Arial", 15))
    lbl_book_title = tk.Label(master = frm_book, text = 'Title', font = ("Arial", 15))
    lbl_book_genre = tk.Label(master = frm_book, text = 'Genre', font = ("Arial", 15))
    lbl_book_author = tk.Label(master = frm_book, text = 'Author', font = ("Arial", 15))
    lbl_book_target = tk.Label(master = frm_book, text = 'Target Audience', font = ("Arial", 15))
    lbl_book_pub = tk.Label(master = frm_book, text = 'Publisher', font = ("Arial", 15))
    lbl_book_price = tk.Label(master = frm_book, text = 'Price (VND)', font = ("Arial", 15))
    lbl_book_quantity = tk.Label(master = frm_book, text = 'Stock', font = ("Arial", 15))
    
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
    ent_book_id = tk.Entry(master = frm_book, width = 30, textvariable = book_id, font = ("Arial", 15))
    ent_book_title = tk.Entry(master = frm_book, width = 30, textvariable = book_title, font = ("Arial", 15))
    ent_book_genre = tk.Entry(master = frm_book, width = 30, textvariable = book_genre, font = ("Arial", 15))
    ent_book_author = tk.Entry(master = frm_book, width = 30, textvariable = book_author, font = ("Arial", 15))
    ent_book_target = tk.Entry(master = frm_book, width = 30, textvariable = book_target, font = ("Arial", 15))
    ent_book_pub = tk.Entry(master = frm_book, width = 30, textvariable = book_pub, font = ("Arial", 15))
    ent_book_price = tk.Entry(master = frm_book, width = 30, textvariable = book_price, font = ("Arial", 15))
    ent_book_quantity = tk.Entry(master = frm_book, width = 30, textvariable = book_quantity, font = ("Arial", 15))
    
    
    #Add save cmd
    btn_save = tk.Button(master = frm_book, text = "Save", width = 21, font = ("Arial", 15),  command = lambda: add_book_func(book_id.get(), book_title.get(), book_genre.get(), book_author.get(), book_target.get(), book_pub.get(), book_price.get(), book_quantity.get()))
    btn_exit = tk.Button(master = frm_book, text = "Exit", width = 21, font = ("Arial", 15), command = book.destroy)
    
    #Grid layout
    frm_book.grid(row = 0, column = 0, sticky = "nsew")
    lbl_book.grid(row = 0, column = 0, columnspan = 2, padx = 15, pady = 5, sticky = "nsew")
    lbl_book_id.grid(row = 1, column = 0, padx = 15, pady = 5, sticky = "nsew")
    lbl_book_title.grid(row = 2, column = 0, padx = 15, pady = 5, sticky = "nsew")
    lbl_book_genre.grid(row = 3, column = 0, padx = 15, pady = 5, sticky = "nsew")
    lbl_book_author.grid(row = 4, column = 0, padx = 15, pady = 5, sticky = "nsew")
    lbl_book_target.grid(row = 5, column = 0, padx = 15, pady = 5, sticky = "nsew")
    lbl_book_pub.grid(row = 6, column = 0, padx = 15, pady = 5, sticky = "nsew")
    lbl_book_price.grid(row = 7, column = 0, padx = 15, pady = 5, sticky = "nsew")
    lbl_book_quantity.grid(row = 8, column = 0, padx = 15, pady = 5, sticky = "nsew")
    ent_book_id.grid(row = 1, column = 1, padx = 15, pady = 5, sticky = "nsew")
    ent_book_title.grid(row = 2, column = 1, padx = 15, pady = 5, sticky = "nsew")
    ent_book_genre.grid(row = 3, column = 1, padx = 15, pady = 5, sticky = "nsew")
    ent_book_author.grid(row = 4, column = 1, padx = 15, pady = 5, sticky = "nsew")
    ent_book_target.grid(row = 5, column = 1, padx = 15, pady = 5, sticky = "nsew")
    ent_book_pub.grid(row = 6, column = 1, padx = 15, pady = 5, sticky = "nsew")
    ent_book_price.grid(row = 7, column = 1, padx = 15, pady = 5, sticky = "nsew")
    ent_book_quantity.grid(row = 8, column = 1, padx = 15, pady = 5, sticky = "nsew")
    btn_save.grid(row = 9, column = 1, padx = 15, pady = 5, sticky = "nsew")
    btn_exit.grid(row = 9, column = 0, padx = 15, pady = 5, sticky = "nsew")
    book.rowconfigure(0, weight=1, minsize=50)
    book.columnconfigure(0, weight=1, minsize=75)
    for i in range(10):
        frm_book.rowconfigure(i, weight=1, minsize=50)
    for i in range(2):  
        frm_book.columnconfigure(i, weight=1, minsize=75) 
    
#Book List window
def book_list():
    clear()
    list_book = tk.Toplevel(window)

    list_book.title("Staff")
    frm = tk.Frame(list_book)
    tree = ttk.Treeview(list_book)
    tree['show']='headings'

    list_book.resizable(False,False)

    # Define number of columns
    tree["columns"] = ("ID", "Title", "Genre", "Author", "Target", "Publisher", "Price", "Quantity")
    #Assign the width,minwidth and anchor to the respective columns 
    tree.column ("ID", width=100, minwidth=50,anchor=tk.CENTER) 
    tree.column ("Title", width=200, minwidth=100,anchor=tk.CENTER) 
    tree.column ("Genre", width=250, minwidth=150,anchor=tk.CENTER) 
    tree.column ("Author", width=200, minwidth=100, anchor=tk .CENTER) 
    tree.column ("Target", width=250, minwidth=150, anchor=tk .CENTER) 
    tree.column ("Publisher", width=250, minwidth=150, anchor=tk.CENTER)
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

    def list_all():
        tree.delete(*tree.get_children())
        db = sql_books.Database().Storage()
        for i in range(0,len(db)):
            tree.insert('', i, iid= None, values = (db[i][0],db[i][1],db[i][2],db[i][3],db[i][4],db[i][5],db[i][6],db[i][7],">"+db[i][0]))
    list_all()

    def del_cf():
        # Return STRING VALUE of the selected item
        try:
            del_ID = tree.item(tree.focus())['values'][8][1:]
        except:
            return
        cf = tk.messagebox.askyesno("Delete", "Are you sure you want to delete this book?")
        if cf == True:
            delete_book_func(del_ID)

    def delete_book_func(id):
        if func.remove_book(id) == True:
            messagebox.showinfo("Success", "Book deleted successfully!")
            tree.delete(tree.focus())
            if len(sql_books.Database().Storage()) == 0:
                btn_book['state'] = 'disabled'
            else:
                btn_book['state'] = 'normal'
        else:
            messagebox.showerror("Error", "Customer not deleted!")

    tree.pack()
    btn_refresh = tk.Button(list_book, text="Refresh", width=21, command=lambda: list_all())
    btn_search = tk.Button(list_book, text="Search", width=21, command=lambda: Search_interface())
    btn_delete = tk.Button(list_book, text="Delete", width=21, command=lambda: del_cf())
    btn_update = tk.Button(list_book, text="Update", width=21, command=lambda: mod_book())
    btn_exit = tk.Button(list_book, text="Exit", width=21, command=list_book.destroy)

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
                messagebox.showerror("Error", "Invalid Price or Quantity format!")
            elif func.Searchall_book(id, title, genre, author, target, publisher, data[0], data[1], data[2], data[3]) == False:
                messagebox.showerror("Error", "Something went wrong\nPlease try again!")
            elif len(func.Searchall_book(id, title, genre, author, target, publisher, data[0], data[1], data[2], data[3]))==0:
                messagebox.showinfo("","0 results found!")
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
            if sql_books.Database().Validate(book_id.get(), book_title.get(), book_author.get(), 2) == True:
                messagebox.showerror("Error", "Book with modfied info is already exist!\nPlease try again!")
            elif (func.validate_price_quatity(book_price.get(), book_quantity.get())==False):
                messagebox.showerror("Error", "Invalid Price or Quantity!")
            else:
                sql_books.Database().Update(book_title.get(), book_genre.get(),book_author.get(),book_target.get(),book_pub.get(),book_price.get(),book_quantity.get(),book_id.get())
                messagebox.showinfo("OK", "Book Info Modded!")

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
            cf = tk.messagebox.askyesno("Save", "Update this book info?")
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


    btn_refresh.pack()
    btn_search.pack()
    btn_delete.pack()
    btn_update.pack()
    btn_exit.pack()


window = tk.Tk()
window.geometry("800x600")

imgbg = tk.PhotoImage(file="img/main.png")
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
ex = tk.PhotoImage(file="img/icons/exit.png")
img_e = ex.subsample(2, 2)

lbl_hihi = tk.Label(image=imgbg)
lbl_hihi.place(x=0, y=0)

btn_font = tkfont.Font(family="Arial", size=15)

session_get = sql_session.Session().Print()
session_id = session_get[1]
session_name = session_get[2]
window.title(f"BSMS Beta - Logged in as staff: {session_id} - {session_name}")
lbl_session = tk.Label(master=window, text='Welcome, ' + session_id +' - '+ session_name, font=("Arial", 13, "bold"), bg='#73a2c7', justify="left", fg='white')
lbl_welcome = tk.Label(master=window, text="Book Store Management System\n(Staff Edition)", font=("Arial", 25, 'bold'), justify="center", bg='white', fg='#318bd2')
lb_cpr = tk.Label(window, text="© 2023 Team 17 - ICT\nVersion BETA", font=("Arial", 6), bg='#73a2c7', justify="right", fg='white')

btn_add_book = tk.Button(image=img_a_b,text="Add Book",compound = 'left', width=231, height=50, bg='#00ab1c', fg='#ffffff', command=add_book)
btn_add_book['font'] = btn_font
btn_book = tk.Button(image=img_a_b,text="Manage Book List",compound = 'left', width=231, height=50, bg='#00ab1c', fg='#ffffff', command = book_list)
btn_book['font'] = btn_font
btn_add_customer = tk.Button(image=img_a_c,text="Add Customer", compound = 'left', width=231, height=50, bg='#ab4d00', fg='#ffffff', command = add_customer)
btn_add_customer['font'] = btn_font
btn_customer = tk.Button(image=img_m_c,text="Customer List", compound = 'left', width=231, height=50, bg='#ab4d00', fg='#ffffff', command = customer_list)
btn_customer['font'] = btn_font
btn_cut = tk.Button(image=img_e, text="Exit", compound= 'left', width=495, height=50, bg='#570b0b', fg='#ffffff', command = window.quit)
btn_cut['font'] = btn_font
btn_sell_book = tk.Button(image= sell_b, text="Sell Book",compound = 'left', width=495, height=50, bg='#0052cc', fg='#ffffff', command = add_book)
btn_sell_book['font'] = btn_font
if len(sql_books.Database().Storage()) == 0:
    btn_book.config(state="disabled")
if len(sql_customers.Database().Storage()) == 0:
    btn_customer.config(state="disabled")

lbl_welcome.place(x=143, y=95)
btn_add_book.place(x=143, y=195)
btn_book.place(x=407, y=195)
btn_add_customer.place(x=143, y=275)
btn_customer.place(x=407, y=275)
btn_sell_book.place(x=143, y=355)
btn_cut.place(x=143, y=435)
lbl_session.place(x=5, y=5)
lb_cpr.place(x=715, y=573)

window.mainloop()

#need verify before saving to db