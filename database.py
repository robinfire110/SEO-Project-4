import os
import json
import sqlalchemy as db
import sqlite3
import pandas as pd

def delete_existing_database():
    myfile = "Notifood.db"
    if os.path.isfile(myfile):
        os.remove(myfile)


def connect_database():
    """Connects to the SQL database"""
    return db.create_engine('sqlite:///Notifood.db')

def check_database(engine):
    """Checks for existing data in database"""    
    if len(database.table_names()) < 2:
        return False
    return True

def create_table(engine, phone_number):
    """Creates a table for food items"""
    engine.execute( 
        f"""
            CREATE TABLE '{phone_number}'(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                expiration_date DATE,
                item_name VARCHAR(100)
            );
        """
    )


def add_food_item(engine, phone_number, name, expiration_date):
    """Adds a food item to the database"""
    #Check for already existing item
    if not check_food_name(engine, phone_number, name):
        engine.execute(
            f"""
                INSERT INTO '{phone_number}'(
                    expiration_date,
                    item_name)
                VALUES(
                    \'{expiration_date}\',
                    \'{name}\'
                );
            """
        )
    else:
        print("Item with this name already exists!")


def remove_food_item(engine, phone_number, name):
    """Removes a food item from the database"""
    try:
        engine.execute(
            f"""
                DELETE FROM '{phone_number}'
                WHERE item_name = \"{name}\"
            """
        )
    except Exception as e:
        print("Item doesn't exist!")


def print_database(engine, phone_number):
    """Prints the query table from the database"""
    query_result = engine.execute(f"SELECT * FROM '{phone_number}';").fetchall()
    print(pd.DataFrame(query_result))

def database_to_json(engine, phone_number):
    """https://medium.com/@PyGuyCharles/python-sql-to-json-and-beyond-3e3a36d32853"""
    conn = sqlite3.connect('Notifood.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM '{phone_number}'"
    res = cursor.execute(query)
    
    return json.dumps(cursor.fetchall())
    """
    items = []

    for row in res:
        for key in cursor.description:
            items.append({key[0]: value for value in row})

    return json.dumps({'items': items})
    """

def check_food_name(engine, phone_number, name):
    query_result = engine.execute(f"SELECT * FROM '{phone_number}' WHERE item_name = \"{name}\";").fetchall()
    return query_result != []

def get_food_to_expire(engine, phone_number):
    """Searches database and returns items set to expire within a week"""
    query = engine.execute(
        f"""
            SELECT 
                item_name,
                CAST(julianday(expiration_date) - julianday('now') AS INTEGER),
                expiration_date FROM '{phone_number}'
            WHERE julianday(expiration_date) - julianday('now') < 7;
        """
    )
    return pd.DataFrame(query).values
