from app import create_app, db
from app.models.board import Board

my_app = create_app()
with my_app.app_context():
    db.session.add(Board(title="Greetings", owner="World"))
    db.session.add(Board(title="Fruits", owner="Supermarket"))
    db.session.add(Board(title="Colors", owner="Rainbow"))
    db.session.add(Board(title="Motivation", owner="Mood Board Baddies"))
    
    
    db.session.commit()