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
    

@app.route('/offer', methods=['GET', 'POST'])
@login_required
def set_offer():
    form = forms.OfferForm()
    if form.validate_on_submit():
        print(request.form)
        return render_template('offer.html', form=form)
    else:
        print(form.expiration_date)
        print(form.errors)
        return render_template('offer.html', form=form)


@app.route('/users')
@login_required
def get_users():
    response = {}
    response['title'] = 'Usuários'
    response['content'] = [(u.name, u.email, u.dt_criacao, [o.price for o in u.offers]) 
            for u in models.User.query.all()]
    return render_template('response.html', response=response)

@app.route('/offers')
@login_required
def get_offers():
    response = {}
    response['title'] = 'Offers'
    response['content'] = [(o.id, o.price, [(u.name, u.email ) for u in o.users]) 
            for o in models.Offer.query.all()]
    return render_template('response.html', response=response)

    