from flask_script import Manager

from app import app

manager = Manager(app)
from app import db
from app.models import User, Offer

@manager.command
def commands():
    print("""Run:
    > flask db init
    > flask db migrate
    > flask db upgrade
    """)

@manager.command
def test_users():
    db.create_all()
    lucas = User(name='lucas', email='lucasribeiroabreu@live.com', active=False, password='123mudar')
    lucas2 = User(name='admin', email='lucasribeiroabreu@gmail.com', active=False, password='123mudar')
    of1 = Offer(price=10)
    of2 = Offer(price=20)
    of3 = Offer(price=30)
    of4 = Offer(price=40)

    lucas.offers = [of1, of2]
    db.session.add(lucas)
    db.session.add(of1)
    db.session.add(of2)
    db.session.commit()

    lucas2.offers = [of2, of3]
    db.session.add(lucas2)
    db.session.add(of3)
    db.session.commit()
    print('created')
    users = User.query.all()
    offers = Offer.query.all()
    for u in users:
        db.session.delete(u)
    for o in offers:
        db.session.delete(o)
    db.session.commit()
    print('deleted')

    
@manager.command
def create():
    db.create_all()
    print('created!')

@manager.command
def drop():
    db.drop_all()
    print('dropped')

# Create a user to test with
@manager.command
def create_user():
    db.create_all()
    user_datastore.create_user(name='Lucas', 
                               email='lucasribeiroabreu@gmail.com', 
                               password='123mudar')
    db.session.commit()


if __name__ == "__main__":
    manager.run()