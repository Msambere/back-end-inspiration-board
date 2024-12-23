from flask import Blueprint, abort, make_response, request
from ..models.card import Card
from ..db import db
from .routes_utilities import create_model, validate_model

bp = Blueprint("bp", __name__, url_prefix="/cards")

@bp.post("")
def create_card():
    response_data = request.get_json()

    if not response_data.get("text"):
        abort(make_response({"details": "Invalid data"}, 400))
    
    return {
        "card": create_model(Card, response_data)
    }, 201

@bp.get("")
def get_all_cards():
    query = db.select(Card)
    cards = db.session.scalars(query)
    cards_response = [card.to_dict() for card in cards]
    return cards_response

@bp.put("/<card_id>")
def update_one_card(card_id):
    card = validate_model(Card, card_id)
    response_body = request.get_json()

    card.text = response_body.get("text")
    db.session.commit()

    card_response = {
        "card": card.to_dict()
    }

    return card_response, 200

@bp.patch("/<card_id>/likes")
def card_likes(card_id):
    try:
        card = validate_model(Card, card_id)
    except ValueError:
        abort(make_response({"message": f"Card with {card_id} is invalid"}, 400))

    card.likes += 1

    db.session.add(card)
    db.session.commit()

    card_response = {
        "card": card.to_dict()
    }
    
    return card_response, 200