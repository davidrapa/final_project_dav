from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)

# Import models here
from models import User, Transaction, Budget

# Define routes and views
@app.route('/')
def home():
    return render_template('home.html')

# Add other routes and views here

if __name__ == '__main__':
    app.run(debug=True)
