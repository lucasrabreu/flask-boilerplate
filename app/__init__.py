from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_security import Security, SQLAlchemyUserDatastore

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'sqlite:///test.db'[::-1]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECURITY_PASSWORD_SALT'] = b'xxxxxxxxxx'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models
user_datastore = SQLAlchemyUserDatastore(db, models.User, models.Role)
security = Security(app, user_datastore)

from app import views
from app import forms

