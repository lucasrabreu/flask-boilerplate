from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.fields.html5 import EmailField, DateField, URLField
from wtforms import validators
from flask_security.forms import RegisterForm,\
    email_required, email_validator
from app import models, db

class ExtendedRegisterForm(RegisterForm):
    email = EmailField('E-mail', [email_required, email_validator])
    name = StringField('Nome', validators=[validators.DataRequired()])   

    def validate(self):
        # check for username
        if db.session.query(models.User).filter(models.User.email == self.email.data.strip()).first():
            #append the error message
            self.email.errors = ["Email already taken"]
            return False
        # now check for Flask-Security validate functions
        if not super(ExtendedRegisterForm, self).validate():
            return False
        return True    

class OfferForm(FlaskForm):
    name = StringField('Tipo', validators=[validators.DataRequired()])
    number = StringField('Número', validators=[validators.DataRequired()])
    valor = StringField('Valor', validators=[validators.Regexp('^[1-9][\.\d]*(,\d+)?$')])
    link = URLField('Link')
    expiration_date = DateField('expiration_date')

    submit = SubmitField("Cadastrar")
