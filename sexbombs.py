# Programs import
from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
import bcrypt

# Instantiate the application
app = Flask(__name__)

# Application Config. To be separated later
app.config['DEBUG'] = True
app.config['HOST'] = '127.0.0.1'
app.config['MONGO_USERNAME'] = "sexbomb"
app.config['MONGO_PASSWORD'] = "nopasswd"        # Need to figure out a more s$
app.config['MONGO_DBNAME'] = 'sexbombs'

# instantiate mongodb
mongo = PyMongo(app)

@app.route('/')
def index():
    return 'Sexbombs'

if __name__ == '__main__':
    app.run()
