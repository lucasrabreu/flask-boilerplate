from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms import validators

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[validators.DataRequired()])
    email = EmailField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Senha', validators=[validators.Length(min=6), 
                                      validators.EqualTo('confirm', message='Senhas precisam ser iguais.'), 
                                      validators.DataRequired()])
    confirm = PasswordField('Confirme a senha')

    submit = SubmitField("Cadastrar")

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[validators.DataRequired()])
    password = PasswordField('Senha', validators=[validators.Length(min=6), 
                                      validators.DataRequired()])

    submit = SubmitField("Login")