from flask import Blueprint, make_response, abort, request
from app import db
from app.models.board import Board
from app.models.card import Card
from app.routes.routes_utilities import validate_model, create_model, send_model_creation_slack

bp = Blueprint("board_bp", __name__,url_prefix="/boards")


@bp.post("")
def create_board():
    response_data = request.get_json()
    new_board = create_model(Board, response_data)
    response = {
            "board": new_board
    }
    send_model_creation_slack(Board, new_board["title"])
    return response, 201

@bp.post("/<board_id>/cards")
def create_card_with_board(board_id):
    board = validate_model(Board,board_id)
    request_body = request.get_json()
    request_body["board_id"] = board.id
    new_card = create_model(Card, request_body)
    send_model_creation_slack(Card, new_card["text"])
    return {"card": new_card}, 201

@bp.get("")
def get_all_boards():
    title_param = request.args.get("title")

    query = db.select(Board)
    if title_param:
        query = query.where(Board.title.like(f"%{title_param}"))

    boards = db.session.scalars(query)
    return {"boards": [board.to_dict() for board in boards]}

@bp.get("/<board_id>")
def get_one_board(board_id):
    board = validate_model(Board, board_id)
    return {"board": board.to_dict()}

@bp.get("/<board_id>/cards")
def get_all_cards_for_specific_board(board_id):
    board = validate_model(Board, board_id)
    
    cards =[]
    for card in board.cards:
        cards.append(card.to_dict())

    return {"cards": cards}


@bp.patch("/<board_id>")
def update_board(board_id):
    board = validate_model(Board, board_id)
 
    request_body = request.get_json()
    if "title" in request_body:
        board.title = request_body["title"]
    if "owner" in request_body:
        board.owner = request_body["owner"]
    db.session.commit()
    return {
        "board": board.to_dict()
    }

@bp.delete("/<board_id>")
def delete_board(board_id):
    board = validate_model(Board, board_id)

    db.session.delete(board)
    db.session.commit()

    return {
        "details": f'Board {board_id} "{board.title}" successfully deleted'
    }



