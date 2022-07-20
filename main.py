
from database import *
from login import *
from api import *
from user_input import *
import datetime
from flask import Flask, render_template, url_for, flash, redirect, request
from flask_behind_proxy import FlaskBehindProxy
from flask_sqlalchemy import SQLAlchemy

#Flask
app = Flask(__name__)
proxied = FlaskBehindProxy(app)  ## add this line
#app.config['SECRET_KEY'] = '288c97cf1b11a5726d571d84ccc1f5f5'

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#db = SQLAlchemy(app)

phone_number = "4256471907"
database = connect_database()

@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    if phone_number != "":
        data = database_to_json(database, phone_number)#'[[4, "2020-10-05 00:00:00", "Oranges"], [8, "2022-07-19 00:00:00", "Apples"], [9, "2022-07-23 00:00:00", "Beef"]]'
        return render_template("dashboard.html", data=data)
    else:
        #REDIRECT TO LOGIN PAGE
        pass

def main():
    """
    action = None
    while action not in (1, 2):
        print("Type 1 to log in and 2 to sign up")
        action = input("> ")
        if action.isdigit() and int(action) == 1:
            phone_number = log_in(input("Phone Number: "))
            if phone_number != False:
                break
        elif action.isdigit() and int(action) == 2:
            phone_number = sign_up(input("Phone Number: "))
            if phone_number != False:
                create_table(database, phone_number)
                break
        else:
            print("Please type a valid option")

    print(get_all_login_data())
    print(database_to_json(database, phone_number))


    #Run user input
    #getInput()
    #format_sentence(text)
    #inputItem()


    '''
    print_database(database, phone_number)
    if not check_database(database):
        print("No previous database detected, creating new database...")
        num = phone_number#prompt(phone_number, style=custom_style_2).get("phone_number")
        create_table(database, num)
    else:
        print("Existed database detectesd, using existing database...")
    '''
    
    while True:
        name = input("Name: ")
        if name == "":
            break
        expiration_date = input("Expiration date(MM-DD-YYYY): ")
        expiration_date.lstrip("0")
        expiration_date = expiration_date.split("-")
        print(expiration_date)
        add_food_item(database, phone_number, name, datetime.datetime(int(expiration_date[2]), int(expiration_date[0]), int(expiration_date[1])))

    print("Current Food:")
    print_database(database, phone_number)

    while True:
        name = input("Delete Item Name: ")
        if name == "":
            break
        remove_food_item(database, phone_number, name)
    

    
    
    
    print_database(database, phone_number)
    #food = get_food_to_expire(database, phone_number)
    #sendMessage(phone_number, food)
"""
    pass
if __name__ == "__main__":
    main()
    app.run(debug=True, host="0.0.0.0")