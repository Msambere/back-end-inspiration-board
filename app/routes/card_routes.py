from flask import Blueprint, abort, make_response, request
from ..models.card import Card
from ..db import db
from .routes_utilities import create_model, validate_model

bp = Blueprint("bp", __name__, url_prefix="/cards")

@bp.get("")
def get_all_cards():
    query = db.select(Card)
    cards = db.session.scalars(query)
    cards_response = [card.to_dict() for card in cards]
    return cards_response

@bp.patch("/<card_id>")
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
    card = validate_model(Card, card_id)
    card.likes += 1
    db.session.commit()

    card_response = {
        "card": card.to_dict()
    }
    
    return card_response, 200

@bp.delete("/<card_id>")
def delete_one_card(card_id):
    card = validate_model(Card, card_id)

    db.session.delete(card)
    db.session.commit()

    return {
        "details": f'Card {card_id} with text "{card.text}" successfully deleted'
    }