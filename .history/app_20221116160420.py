from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL']