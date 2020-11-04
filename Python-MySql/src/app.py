from flask import Flask, render_template
import os
from wtforms import StringField, SubmitField
import mysql.connector as db
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

mycursor = None
mydb=None


@app.before_first_request
def intial_db_setup():
    print("Initial DB Setup")
    global mydb
    global mycursor
    mydb = db.connect(host="databases", user="root", password="123456")

    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")

    mydb = db.connect(host="databases", user="root", password="123456",database="mydatabase")
    mycursor = mydb.cursor()

    mycursor.execute(
         "CREATE TABLE IF NOT EXISTS customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")



    # sql = "INSERT INTO customers1 (name, address) VALUES (%s, %s)"
    # val = [
    #     ('Peter', 'Lowstreet 4'),
    #     ('Amy', 'Apple st 652'),
    #     ('Hannah', 'Mountain 21'),
    #     ('Michael', 'Valley 345'),
    #     ('Sandy', 'Ocean blvd 2'),
    #     ('Betty', 'Green Grass 1'),
    #     ('Richard', 'Sky st 331'),
    #     ('Susan', 'One way 98'),
    #     ('Vicky', 'Yellow Garden 2'),
    #     ('Ben', 'Park Lane 38'),
    #     ('William', 'Central st 954'),
    #     ('Chuck', 'Main Road 989'),
    #     ('Viola', 'Sideway 1633')
    # ]
    #
    # mycursor.executemany(sql, val)
    #
    # mydb.commit()
    #
    # print(mycursor.rowcount, "was inserted.")



class Customer(FlaskForm):
    name = StringField("Name :",validators=[InputRequired(message="Required")])
    address = StringField("Address : ",validators=[InputRequired(message="Required")])
    submit = SubmitField("Enter")


@app.route("/", methods=['GET', 'POST'])
def root():
    form = Customer()
    if form.validate_on_submit():
        name = form.name.data
        address = form.address.data
        print(name, address)
        sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        val = (name,address)
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")
        form.name.data = ""
        form.address.data = ""
        message = "Data submitted successfully"
        return render_template("home.html", form=form, message=message)
    return render_template("home.html", form=form)


@app.route("/create")
def create():
    file_name = '/data/sample_file.txt'
    with open(file_name, 'w') as file_write:
        for i in range(1, 11):
            file_write.write(f'{i} \n')

    return "Created a file"


@app.route("/read")
def read():
    # file_name = '/data/sample_file.txt'
    lines = None
    # with os.scandir('/data/') as entries:
    #     for entry in entries:
    #         with open(entry) as file_read:
    #             lines = file_read.readlines()
    # return render_template("index.html", lines=lines)
    mycursor.execute("SELECT id, name, address FROM customers")

    myresult = mycursor.fetchall()
    return render_template("read.html",myresult=myresult)


if __name__ == '__main__':
    # app.run(host="0.0.0.0", debug=True, port="8000")
    #app.run(debug=True)
    app.run(host="0.0.0.0", debug=True, port="8000")
