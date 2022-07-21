"""
file: login.py
author: Emmanuel Griffin
author: Nicole de Moura
description: Checks if a given phone number is valid
             Checks if a given password is secure
"""

import requests
import sqlite3


"""
phone number - the phone number the user wants to sign up with
check_valid_phone - returns true if the phone number given is valid and false otherwise
"""
def check_valid_phone(phone_number):
    if phone_number.isdigit():
        print("Valid Number")
        return phone_number
    else:
        print("Invalid Number, please remove any '-' or '+' symbols.")
        return False

"""
password - the password the user wants to use
secure_password - returns true if the password is secure and false otherwise 
"""
def secure_password(password):
    special_char = '[@_!#$%^&*()<>?/\|}{~:]'
    num = False
    special = False
    if len(password) < 8:
        print("Password length must exceed 7 characters")
        return False
    for char in password:
        if char.isdigit():
            num = True
        if char in special_char:
            special = True
    if num is True and special is True:
        print("Secure password")
        return password
    elif num is False and special is True:
        print("Needs number in password")
        return False
    elif num is True and special is False:
        print("Needs special character in password")
        return False
    else:
        print("Needs number and special character in password")
        return False

"""
phone number - the phone number the user wants to make an account with
password - the password the user wants to make an account with
make_account - creates an account for a user and holds that data
returns false if an account is already made and true if the account
was created 
"""
def make_account(phone_number, password):
    conn = sqlite3.connect('accounts.db')
    cursor = conn.cursor()

    sql = '''CREATE TABLE IF NOT EXISTS ACCOUNTS(
    PHONE VARCHAR(255),
    PASSWORD VARCHAR(255)
    )'''
    cursor.execute(sql)

    cursor.execute("SELECT PHONE FROM ACCOUNTS WHERE PHONE = ?", (phone_number,))
    exists = cursor.fetchone()

    if exists:
        print("An account with this phone number already exists, login instead")
        conn.close()
        return False
    else:
        cursor.execute('''INSERT INTO ACCOUNTS(
        PHONE, PASSWORD) VALUES 
        (?, ?)''', (phone_number, password))

    conn.commit()
    cursor.execute("SELECT * FROM ACCOUNTS")
    print("Welcome! You can now log in using your credentials",
          cursor.fetchall()[-1])

    conn.close()
    return phone_number

"""
simulates a login, the user inputs an phone number, if you have signed
in before with the same phone number you successfully have logged in
if the phone number doesn't exist in our database (so you haven't signed up before)
you will be prompted to try another phone number that has signed up or sign up now
returns true if you sign up and false if you login
"""
def log_in(phone_number, password):
    conn = sqlite3.connect('accounts.db')
    cursor = conn.cursor()
    print("LOGIN STARTED")
            
    try:
        cursor.execute("SELECT PHONE FROM ACCOUNTS WHERE PHONE = ?", (phone_number))
        if len(cursor.fetchall()) < 1:
            raise Exception()
            return False
        else:
            print(cursor.fetchall())
            print(type(cursor.fetchall()))
            print("Login success")
            return phone_number
    except:
        print("Please enter an existing phone number, or type 2 to sign up")
        return False

    conn.close()

"""
sigh_up contuines to prompt the user for an phone number until they give a valid phone number
after that they have to create a secure password
"""
def sign_up(phone_number):
    phone_valid = check_valid_phone(phone_number)
    while not phone_valid:
        phone = input("Phone Number: ")
        phone_valid = check_valid_phone(phone)

    print("Secure password requirements: Must be 8 characters or longer, must include one number, and one special character")
    password_valid = secure_password(input("Password: "))
    while not password_valid:
        password_valid = secure_password(input("Password: "))

    return make_account(phone_valid, password_valid)

"""
Returns all account data
"""
def get_all_login_data():
    conn = sqlite3.connect('accounts.db')
    cursor = conn.cursor()
    sql_query = """SELECT * FROM ACCOUNTS;"""
    cursor.execute(sql_query)
    return cursor.fetchall()

"""
Returns row asscoatiated with given phone number, None if there is no row under given number
phone_number - phone_number to search for
"""
def get_login_data_by_number(phone_number):
    conn = sqlite3.connect('accounts.db')
    cursor = conn.cursor()
    sql_query = f"""SELECT * FROM ACCOUNTS WHERE PHONE = {phone_number};"""
    cursor.execute(sql_query)
    return cursor.fetchall()
    