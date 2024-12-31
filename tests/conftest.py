import pytest
from app import create_app
from app.db import db
from flask.signals import request_finished
from dotenv import load_dotenv
import os

from app.models.board import Board
from app.models.card import Card

load_dotenv()

@pytest.fixture
def app():
    test_config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    }
    app = create_app(test_config)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_saved_boards(app):
    # Arrange
    fruit_board = Board(title="All the Fruitz", owner="Fruit Lover")
    mountain_board = Board(title="Mountain Life", owner="Bigfoot")

    db.session.add_all([fruit_board, mountain_board])
    db.session.commit()
    
@pytest.fixture
def two_saved_cards(app):
    # Arrange
    db.session.add(Card(text="Banana", likes=3, board_id=1))
    db.session.add(Card(text="Apple", likes=2, board_id=1))
    db.session.commit()
