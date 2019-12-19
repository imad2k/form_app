from flask import Flask, jsonify, request, render_template, redirect, session
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET'])
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def _save():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    phone_number = request.form['phone_number']
    password = request.form['password']
    
    add_user(first_name, last_name, email, phone_number, password)
    return redirect('/')

def add_user(first_name, last_name, email, phone_number, password):
    with sqlite3.connect('form.db') as conn:
        cursor = conn.cursor()
        SQL = """INSERT INTO form(first_name, last_name, email, phone, password) VALUES (?,?,?,?,?);"""
        values = first_name, last_name, email, phone_number, password
        cursor.execute(SQL, values)
        

if __name__ == "__main__":
    app.run(debug=True)