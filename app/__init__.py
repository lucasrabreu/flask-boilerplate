from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_security import Security, SQLAlchemyUserDatastore

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'sqlite:///test.db'[::-1]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECURITY_PASSWORD_SALT'] = b'xxxxxxxxxx'
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_POST_LOGIN_VIEW'] = '/'
app.config['SECURITY_POST_REGISTER_VIEW'] = '/login'
app.config['SECURITY_SEND_REGISTER_EMAIL'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models
user_datastore = SQLAlchemyUserDatastore(db, models.User, models.Role)

from app import forms
security = Security(app, user_datastore,
         register_form=forms.ExtendedRegisterForm)

from app import views
