from flask import Flask, render_template,request,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import os
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from datetime import timedelta
from flask_mail import Mail , Message
from sqlalchemy.exc import IntegrityError
import socket
# from datetime import datetime



con = sqlite3.connect('./tmp/database.db')
app = Flask(__name__)
app.config['PERMANENT_SESSION_LIFETIME'] =timedelta(hours=1)
REMEMBER_COOKIE_DURATION = timedelta(20)
app.config.from_pyfile('config.cfg')

db = SQLAlchemy(app)

migrate =Migrate(app,db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
mail = Mail(app)
from views import *


if __name__ =='__main__':
     # manager.run()
    app.run(debug=True)