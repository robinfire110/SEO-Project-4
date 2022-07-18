
from database import *
from login import *
from api import *
from user_input import *


def main():

    phone_number = ""
    database = connect_database()
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
        expiration_date = input("Expiration date(Year-month-date): ")
        add_food_item(database, phone_number, name, expiration_date)

    print("Current Food:")
    print_database(database, phone_number)

    while True:
        name = input("Delete Item Name: ")
        if name == "":
            break
        remove_food_item(database, phone_number, name)

    
    
    """
    while(True):
        next_job = prompt(program_options, style=custom_style_2).get("program")

        if next_job == "Add item":
            new_item = prompt(add_options, style=custom_style_2)
            add_food_item(
                database,
                new_item.get("item_name"),
                new_item.get("expiration_date")
            )
        elif next_job == "Remove item":
            remove_item = prompt(remove_options, style=custom_style_2)
            remove_food_item(database, remove_item.get("item_name"))
        elif next_job == "List items":
            print_database(database)
        else:
            break
    """
    
    print_database(database, phone_number)
    #food = get_food_to_expire(database, phone_number)
    #sendMessage(phone_number, food)

if __name__ == "__main__":
    main()