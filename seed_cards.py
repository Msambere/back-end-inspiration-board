from app import create_app, db
from app.models.card import Card

my_app = create_app()
with my_app.app_context():
    db.session.add(Card(text="hi", likes="0"))
    db.session.add(Card(text="hola", likes="0"))
    db.session.add(Card(text="bonjour", likes="0"))
    db.session.add(Card(text="annyeonghaseyo", likes="0"))
    db.session.add(Card(text="hallo", likes="0"))
    db.session.add(Card(text="namaste", likes="0"))
    
    db.session.commit()