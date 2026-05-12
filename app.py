from flask import Flask,render_template,url_for,redirect,request
import mysql.connector as c
app=Flask(__name__)

def get_db():
    con=c.connect(
        host="localhost",
        user="root",
        password="",
        database="inventory_management"
    )
    return con


@app.route('/')
def home():
    return render_template("login.html")

@app.route('/login/<name>')
def string(name):
    return name

@app.route('/dashboard')
def dashboard():
    db=get_db()
    cursor=db.cursor()
    return render_template("dashboard.html")

if __name__=="__main__":
    app.run(debug=True,port=8000)