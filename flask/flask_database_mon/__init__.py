from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Creating your flaskapp instance
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')

# Configuring the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Creating a SQLAlchemy database instance
db = SQLAlchemy(app)
app.app_context().push()

from flask import routes