from flask import render_template, request, redirect, jsonify
from app import app
from app import forms
from app import models
from app import user_datastore
from app import db
from flask_login.utils import login_user, logout_user, login_required

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = forms.RegistrationForm()
    if form.validate_on_submit():
        # cadastra usuario
        u = models.User(username=request.form['username'],
             email=request.form['email'])
        u.set_password(request.form['password'])
        db.session.add(u)
        db.session.commit()

        return redirect('/')
    else: #Get ou post errado
        return render_template('registration.html', form=form)
    
@app.route('/users')
@login_required
def get_users():
    us = [(u.username, u.email, u.password, u.dt_criacao) for u in models.User.query.all()]
    return jsonify(us)


