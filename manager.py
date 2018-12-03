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
    lucas = User(username='lucass', email='lucas@gmail.com', active=True, password='0123456')
    lucas2 = User(username='lucass2', email='lucas2@gmail.com', active=True, password='0123456')
    of1 = Offer(price=10)
    of2 = Offer(price=20)
    of3 = Offer(price=30)
    of4 = Offer(price=40)

    # lucas.offers = [of1, of2]
    db.session.add(lucas)
    # db.session.add(of1)
    # db.session.add(of2)
    db.session.commit()

    # lucas2.offers = [of2, of3]
    db.session.add(lucas2)
    # db.session.add(of3)
    db.session.commit()

@manager.command
def clean_db():
    users = User.query.all()
    offers = Offer.query.all()

    for u in users:
        db.session.delete(u)
    
    for o in offers:
        db.session.delete(o)

    db.session.commit()

if __name__ == "__main__":
    manager.run()