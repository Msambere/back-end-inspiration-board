from app import create_app, db
from app.models.card import Card
from app.models.board import Board

my_app = create_app()
with my_app.app_context():

    db.session.add(Card(board_id=1, text="hola", likes="0"))
    db.session.add(Card(board_id=1, text="hi", likes="0"))
    db.session.add(Card(board_id=1, text="bonjour", likes="0"))
    db.session.add(Card(board_id=1, text="annyeonghaseyo", likes="0"))
    db.session.add(Card(board_id=1, text="hallo", likes="0"))
    db.session.add(Card(board_id=1, text="namaste", likes="0"))

    db.session.add(Card(board_id=2, text="apple", likes="0"))
    db.session.add(Card(board_id=2, text="orange", likes="0"))
    db.session.add(Card(board_id=2, text="cherry", likes="0"))

    db.session.add(Card(board_id=3, text="red", likes="0"))
    db.session.add(Card(board_id=3, text="blue", likes="0"))
    db.session.add(Card(board_id=3, text="green", likes="0"))
    db.session.add(Card(board_id=3, text="yellow", likes="0"))

    db.session.add(Card.from_dict({"board_id": 4, "text": 'We got this!', "likes": 100 }))
    db.session.add(Card.from_dict({"board_id": 4, "text": 'We can do it!', "likes": 200}))
    db.session.add(Card.from_dict({"board_id": 4, "text": 'We are fullstack SWEs!', "likes": 300}))
    db.session.add(Card.from_dict({"board_id": 4, "text": 'Mood Board baddies for the W!', "likes": 500}))
  
    db.session.commit()
