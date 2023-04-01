import tkinter as tk
from tkinter import messagebox, ttk, font as tkfont
import process_checker as func
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
    lbl_customer_dob = tk.Label(customer_frame, text="Customer DOB", font=("Arial", 15))
    lbl_customer_address = tk.Label(customer_frame, text="Customer Address", font=("Arial", 15))
    lbl_customer_phone = tk.Label(customer_frame, text="Customer Phone", font=("Arial", 15))
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
        if func.check_phone(cu_phone) == False:
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
                    btn_mod_customer['state'] = 'disabled'
                else:
                    btn_mod_customer['state'] = 'normal'
                customer.destroy()
            elif func.add_customer(cu_ID, cu_name, cu_dob, cu_address, cu_phone, cu_email) == False:
                messagebox.showerror("Error", "Customer info failed to save!\nPlease check again!")
        

# Create a new window for modifying customer info [DONE]
def modify_customer():
    # Create a new window
    customer = tk.Toplevel(window)
    customer.title("Modify Customer Info")
    customer_frame = tk.Frame(customer)

    # Create widgets
    btn_font = tkfont.Font(family="Arial", size=15)

    # Create labels
    lbl_customer = tk.Label(customer_frame, text="Modify Customer Info", font=("Arial", 20, 'bold'), justify="center")
    lbl_customer_id = tk.Label(customer_frame, text="Customer ID", font=("Arial", 15))
    lbl_customer_name = tk.Label(customer_frame, text="Customer Name", font=("Arial", 15))
    lbl_customer_dob = tk.Label(customer_frame, text="Customer DOB", font=("Arial", 15))
    lbl_customer_address = tk.Label(customer_frame, text="Customer Address", font=("Arial", 15))
    lbl_customer_phone = tk.Label(customer_frame, text="Customer Phone", font=("Arial", 15))
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
    customer_list = sql_customers.Database().Storage()
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
        if func.check_phone(cu_phone.get()) == False:
            messagebox.showerror("Error", "Invalid phone number!\nPlease try again!")
        elif func.check_email(cu_email.get()) == False:
            messagebox.showerror("Error", "Invalid email type!\nPlease try again!")
        elif sql_customers.Database().Validate(cu_ID.get(), cu_phone.get(), cu_email.get(), 2) == True:
            messagebox.showerror("Error", "Phone or Email info is already exists!\nPlease try again!")
        else:
            sql_customers.Database().Update(cu_name.get(), cu_dob.get(), cu_address.get(), cu_phone.get(), cu_email.get(), cu_ID.get())
            messagebox.showinfo("Success", "Customer info saved!\nPlease refresh the page to see the changes!")


    def delete_customer_func():
        if func.remove_customer(cu_ID.get()) == True:
            # Verify if the customer info is saved
            messagebox.showinfo("Success", "Customer deleted successfully!")
            if len(sql_customers.Database().Storage()) == 0:
                btn_mod_customer['state'] = 'disabled'
            else:
                btn_mod_customer['state'] = 'normal'
        elif func.remove_customer(cu_ID.get()) == False:
            messagebox.showerror("Error", "Customer not deleted!")
            
#End customer section

# Book SECTION
#Function to add new book (New window)
def add_book():
    book = tk.Toplevel(window)
    book.title("Add New Book")
    frm_book = tk.Frame(book) 
    
    #Add book cmd
    def add_book_func(book_id, book_title, book_genre, book_author, book_target, book_pub, book_price, book_quantity):
        if sql_books.Database().Validate(book_id, book_title, 1) == True:
            messagebox.showerror("Error", "Book already exist!")
            book.destroy()
        else:
            if func.add_book(book_id, book_title, book_genre, book_author, book_target, book_pub, book_price, book_quantity)==True:
                messagebox.showinfo("OK", "Book added successfully!")     
                # Close the window
                if sql_books.Database().Storage() == 0:
                    btn_mod_customer['state'] = 'disabled'
                else:
                    btn_mod_customer['state'] = 'normal'
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
    

#Function to modify book info
def mod_book():
    book = tk.Toplevel(window)
    book.title("Modify Book Info")
    frm_book = tk.Frame(book)

    #Mode book cmd
    def mod_book_func():
        if sql_books.Database().Validate(book_id.get(), book_title.get(), 2) == True:
            messagebox.showerror("Error", "The inputted title is already exists!\nPlease try again!")
        else:
            sql_books.Database().Update(book_title.get(), book_genre.get(),book_author.get(),book_target.get(),book_pub.get(),book_price.get(),book_quantity.get(),book_id.get())
            messagebox.showinfo("OK", "Book Info Modded!")

    #Labels
    lbl_book = tk.Label(master = frm_book, text = 'Modify Book Info', font = ("Arial", 25, "bold"), justify = "center")
    lbl_book_id = tk.Label(master = frm_book, text = 'Book ID', font = ("Arial", 15))
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

    def get_book_info():
        book_info = sql_books.Database().Search(book_id.get())[0]
        book_id.set(book_info[0])
        book_title.set(book_info[1])
        book_genre.set(book_info[2])
        book_author.set(book_info[3])
        book_target.set(book_info[4])
        book_pub.set(book_info[5])
        book_price.set(book_info[6])
        book_quantity.set(book_info[7])

    #Option menu list
    book_list = sql_books.Database().Storage()
    book_list = [i[0] for i in book_list]
    book_id.set(book_list[0])
    book_menu = tk.OptionMenu(frm_book, book_id, *book_list)
    book_id.trace('w', lambda *args: get_book_info())
    book_menu.config(font = ("Arial", 15))
    
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
            book.destroy()
            
    #Buttons        
    btn_save = tk.Button(frm_book, text="Save", font = ("Arial", 15), width=21, command=lambda: save_book())
    btn_exit = tk.Button(frm_book, text="Exit", font = ("Arial", 15), width=21, command=book.destroy)

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
    book_menu.grid(row = 1, column = 1, padx = 15, pady = 5, sticky = "nsew")
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
    
    
    
window = tk.Tk()

window.title("Staff")
frm = tk.Frame(window)

btn_font = tkfont.Font(family="Arial", size=15)

lbl_welcome = tk.Label(master=frm, text='Bookstore management \n(Staff edition)\n', font=("Arial", 25, "bold"), justify="center")

btn_add_book = tk.Button(master = frm, text = 'Add book', font = ("Arial", 15), width = 21, command = add_book)
btn_add_book['font'] = btn_font
btn_mod_book = tk.Button(master = frm, text='Modify book info', font = ("Arial", 15), width = 21, command = mod_book)
btn_mod_book['font'] = btn_font
btn_add_customer = tk.Button(master = frm, text = 'Add customer', font = ("Arial", 15), width = 21, command = add_customer)
btn_add_customer['font'] = btn_font
btn_mod_customer = tk.Button(master = frm, text = 'Modify customer info', font = ("Arial", 15), width = 21, command = modify_customer)
btn_mod_customer['font'] = btn_font
btn_cut = tk.Button(master = frm, text = 'Exit', font = ("Arial", 15), width = 21, command = window.quit)
btn_cut['font'] = btn_font
if len(sql_books.Database().Storage()) == 0:
    btn_mod_book.config(state="disabled")
if len(sql_customers.Database().Storage()) == 0:
    btn_mod_customer.config(state="disabled")

frm.grid(row = 0, column = 0, sticky = "nsew")
lbl_welcome.grid(row = 0, column = 0, columnspan = 2, sticky = "nsew")
btn_add_book.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = "nsew")
btn_mod_book.grid(row = 1, column = 1, padx = 10, pady = 5, sticky = "nsew")
btn_add_customer.grid(row = 2, column = 0, padx = 10, pady = 5, sticky = "nsew")
btn_mod_customer.grid(row = 2, column = 1, padx = 10, pady = 5, sticky = "nsew")
btn_cut.grid(row = 3, column = 0, columnspan = 2, padx = 10, pady = 5, sticky = "nsew")

frm.rowconfigure(0, weight=1, minsize=50)
frm.rowconfigure(1, weight=1, minsize=50)
frm.rowconfigure(2, weight=1, minsize=50)
frm.rowconfigure(3, weight=1, minsize=50)
frm.columnconfigure(0, weight=1, minsize=75)
frm.columnconfigure(1, weight=1, minsize=75)
window.columnconfigure(0, weight=1, minsize=75)
window.rowconfigure(0, weight=1, minsize=50)

window.mainloop()

#need verify before saving to db