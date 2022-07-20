from database import *
from login import *
from api import *
from user_input import *
import datetime
from flask import Flask, render_template, url_for, flash, redirect, request
from form import RegistrationForm, LoginForm
from flask_behind_proxy import FlaskBehindProxy
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, current_user, login_user, logout_user

#Flask
app = Flask(__name__)
proxied = FlaskBehindProxy(app)  ## add this line
app.config['SECRET_KEY'] = '288c97cf1b11a5726d571d84ccc1f5f5'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

#Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#Connect to food database
phone_number = "4256471907"
database = connect_database()

# model that define what will be included in the database
# db.model is the way that shows how our database will look like
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phonenumber = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    # this is a magic method 
    def __repr__(self):
        return f"User('{self.phonenumber}', '{self.password}')"

@app.route("/")
@app.route("/index")
@app.route("/home")
def home():
    return render_template("index.html")

#Hana Register
@app.route("/register", methods = ['GET','POST'])                          # this tells you the URL the method below is related to
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if User.query.filter_by(phonenumber=form.phonenumber.data).first():
            return redirect(url_for('register'))
        else:
            user = User(phonenumber=form.phonenumber.data, password=form.password.data)
            db.session.add(user)
            db.session.commit()
            flash(f'Account created for {form.phonenumber.data}!', 'success')
            return redirect(url_for('login')) # if so - send to home page
    return render_template('register.html', title='Register', form=form) 

@app.route("/login", methods = ['GET','POST'])
def login():
    #https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login
    form = LoginForm()
    if form.validate_on_submit():
        #Get Data
        phonenumber = form.phonenumber.data
        password = form.password.data

        #Confirm data
        check_user = User.query.filter_by(phonenumber=phonenumber).first()
        if not check_user or not check_user.password == password:
            flash('Login credentials incorrect, please try again')
            return redirect(url_for('login')) 
        else:
            login_user(check_user, remember=True)
            return redirect(url_for('dashboard'))


    return render_template("login.html", title = "Log-In", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/add")
@login_required
def add():    
    return render_template("additems.html")

@app.route("/dashboard", methods=['GET', 'POST'])
@login_required
def dashboard():
    if phone_number != "":
        data = database_to_json(database, current_user.phonenumber)#'[[4, "2020-10-05 00:00:00", "Oranges"], [8, "2022-07-19 00:00:00", "Apples"], [9, "2022-07-23 00:00:00", "Beef"]]'
        return render_template("dashboard.html", data=data)
    else:
        return redirect(url_for('login'))

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