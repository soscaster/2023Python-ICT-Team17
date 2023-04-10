from domains import sql_admin
from domains import sql_staff
from domains import sql_books
from domains import sql_store
from domains import sql_customers
from domains import sql_sell

import re

def add_admin(id, name, dob, phone, email):
    try:
        sql_staff.Database().Insert(id, name, dob, phone, email)
        return True
    except:
        return False

def add_staff(id, pwd, name, dob, address, phone, email):
    try:
        sql_staff.Database().Insert(id, pwd, name, dob, address, phone, email)
        return True
    except:
        return False

#Need GUI
def set_staff_salary(staff_list):
    for i in range(len(staff_list)):
        salary = int(input(f"\nSalary for staff {staff_list[i].get_name()} (VND/month): "))
        staff_list[i].set_salary(salary)
        sql_staff.Database().Update_salary(salary,staff_list[i].get_id())

#For staffs:
def add_book(id, title, genre, author, target, publisher, price, quantity):
    try:
        sql_books.Database().Insert(id, title, genre, author, target, publisher, price, quantity)
        return True
    except:
        return False

#For admin:
def input_store_info(id,name,address,phone,email):
    try:
        if len(sql_store.Database().Storage())==0:
            sql_store.Database().Insert(id, name, address, phone, email)
            return True
        else:
            sql_store.Database().Update(name, address, phone, email,id)
            return True
    except:
        return False
    

def add_customer(id, name, dob, address, phone, email):
    try:
        sql_customers.Database().Insert(id, name, dob, address, phone, email)
        return True
    except:
        return False
    
def add_sell(book_id, book_title, quantity, cus_id, cus_name, staff_id, staff_name):
    try:
        sql_sell.Sell().Insert(book_id, book_title, quantity, cus_id, cus_name, staff_id, staff_name)
        return True
    except:
        return False
    
def update_quantity(book_id, quantity):
    try:
        sql_books.Database().Sell(book_id, quantity)
        return True
    except:
        return False

def Search_staff(id):
    try:
        return sql_staff.Database().Search(id)[0]
    except:
        print("Error")

def Search_customer(id):
    try: 
        return sql_customers.Database().Search(id)[0]
    except:
        print("Error")

def Search_book(id):
    try:
        return sql_books.Database().Search(id)[0]
    except:
        print("Error")

def Search_admin(id):
    try:
        return sql_admin.Database().Search(id)[0]
    except:
        print("Error")

def Searchall_staff(id, name, dob, address, phone, email):
    try:
        return sql_staff.Database().Searchall(id, name, dob, address, phone, email)
    except:
        return False

def Searchall_customer(id, name, dob, address, phone, email):
    try:
        return sql_customers.Database().Searchall(id, name, dob, address, phone, email)
    except:
        return False
    
def Searchall_book(id, title, genre, author, target, publisher, price1, price2, quantity1, quantity2):
    try:
        return sql_books.Database().Searchall(id, title, genre, author, target, publisher, price1, price2, quantity1, quantity2)
    except:
        return False

def remove_staff(id):
    try:
        sql_staff.Database().Delete(id)
        return True
    except:
        return False

def remove_customer(id):
    try:
        sql_customers.Database().Delete(id)
        return True
    except:
        return False

def remove_book(id):
    try:
        sql_books.Database().Delete(id)
        return True
    except:
        return False

def remove_admin(id):
    try:
        sql_admin.Database().Delete(id)
        return True
    except:
        return False

def check_email(email):
    # Longest TLD is 63 characters
    pattern = '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,63}$'
    if (re.search(pattern,email)):
        return True
    else:
        return False

def check_phone(phone):
    validate_phone_number_pattern = "^(0|84)(2(0[3-9]|1[0-6|8|9]|2[0-2|5-9]|3[2-9]|4[0-9]|5[1|2|4-9]|6[0-3|9]|7[0-7]|8[0-9]|9[0-4|6|7|9])|3[2-9]|5[5|6|8|9]|7[0|6-9]|8[0-6|8|9]|9[0-4|6-9])([0-9]{7})$"
    if (re.match(validate_phone_number_pattern,phone)):
        return True
    else:
        return False

def check_dob(dob):
    pattern = '^[0-9]{2}/[0-9]{2}/[0-9]{4}$'
    if re.search(pattern, dob):
        return True
    else:
        return False
    
def validate_price_quatity(price, quantity):
    try:
        if (int(price)<0) or (int(quantity)<0):
            return False
    except:
        return False
    return True

def check_price_quantity_format(price, quantity):
    data = []
    pattern = '^[0-9]{1,}\\-[0-9]{1,}$'
    if (re.match(pattern, price)) and (re.match(pattern, quantity)):
        data.append(price[0:price.index('-')])
        data.append(price[price.index('-')+1:])
        data.append(quantity[0:quantity.index('-')])
        data.append(quantity[quantity.index('-')+1:])
        return data
    elif  (len(price)==0) and (len(quantity)==0):
        return ['0','2147483647','0','2147483647']
    elif (len(price)==0) and (re.match(pattern, quantity)):
        data.append('0')
        data.append('2147483647')
        data.append(quantity[0:quantity.index('-')])
        data.append(quantity[quantity.index('-')+1:])
        return data
    elif (len(quantity)==0) and (re.match(pattern, price)):
        data.append(price[0:price.index('-')])
        data.append(price[price.index('-')+1:])
        data.append('0')
        data.append('2147483647')
        return data
    else:
        return False


# Check if information is empty or contain spaces
def check_if_empty(data):
    pattern = '^(.|\s)*\S(.|\s)*$'
    if re.search(pattern,data):
        return True
    else:
        return False