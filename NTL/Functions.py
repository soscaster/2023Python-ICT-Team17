from domains import sql_admin
from domains import sql_staff
from domains import sql_books
from domains import sql_store
from domains import sql_customers

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
def input_books(id, title, genre, author, year, quantity):
    try:
        sql_books.Database().Insert(id, title, genre, author, year, quantity, None, 0)
        return True
    except:
        return False

#Nedd GUI
def set_target(self):
        print(f"Choose the target audience of this book:\n"
              f"1. Children (3-16) \n"
              f"2. Young adults (17-30) \n"
              f"3. Middle-aged adults (30-45) \n"
              f"4. Old adults (Above 45) \n")
        op = int(input(f"Your choice: "))
        match op:
            case 1:
                self.__target_audience = "Children"
            case 2:
                self.__target_audience = "Young adults"
            case 3:
                self.__target_audience = "Middle-aged adults"
            case 4:
                self.__target_audience = "Old adults"
            case _:
                print(f"Invalid choice!")

#Nedd GUI
def set_price(self):
    price = int(input("Enter price (VND): "))
    self.__price = price

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
