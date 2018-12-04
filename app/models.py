from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, \
     check_password_hash
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required


offers = db.Table('offers',
    db.Column('offer_id', db.Integer, db.ForeignKey('offer.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True)
)

class User(db.Model, UserMixin, object):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    # username = db.Column(db.String(80), unique=False, nullable=False)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    dt_criacao = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    dt_update = db.Column(db.DateTime, onupdate=datetime.utcnow, default=datetime.utcnow, nullable=False)
    offers = db.relationship('Offer', secondary=offers, lazy='subquery',
        backref=db.backref('users', lazy=True))

    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary='roles_users', back_populates='users')
    roles_users = db.relationship('RoleUser', back_populates='user')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)


class Role(db.Model, RoleMixin, object):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow, default=datetime.utcnow, nullable=False)

    users = db.relationship('User', secondary='roles_users', back_populates='roles')
    roles_users = db.relationship('RoleUser', back_populates='role')

    def __repr__(self):
        return '<Role {}>'.format(self.name)


class RoleUser(db.Model):
    __tablename__ = 'roles_users'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    user = db.relationship('User', back_populates='roles_users')
    role = db.relationship('Role', back_populates='roles_users')

    def __repr__(self):
        return '<RoleUser {}/{}>'.format(self.user_id, self.role_id)



class Offer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float)

    def __repr__(self):
        return '<Offer {} <> {}>'.format(self.id, self.price)