from domains import sql_admin
from domains import sql_staff
from domains import sql_books
from domains import sql_store
from domains import sql_customers

import re

pattern = '^[a-z0-9]+[\.]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
validate_phone_number_pattern = "^\\+?[0-9][0-9]{2,14}$"

def add_admin(id, name, dob, phone, email):
    try:
        sql_staff.Database().Insert(id, name, dob, phone, email)
        return True
    except:
        return False

def add_staff(id, pwd, name, dob, address, phone, email):
    try:
        sql_staff.Database().Insert(id, pwd, name, dob, address, phone, email, 0)
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
    if (re.search(pattern,email)):
        return True
    else:
        return False

def check_phone(phone):
    if (re.match(validate_phone_number_pattern,phone)):
        return True
    else:
        return False

    