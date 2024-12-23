from flask import Blueprint, make_response, abort, request

from app import db
from app.models.board import Board
from app.routes.routes_utilities import validate_model, create_model

board_bp = Blueprint("board_bp", __name__,url_prefix="/boards")


@board_bp.post("")
def create_board():
    response_data = request.get_json()
    if not response_data.get("title"):
        abort(make_response({"details": "Invalid data"}, 400))
    new_board = create_model(Board, response_data)
    response = {
            "board": new_board
    }
    return response, 201

@board_bp.get("")
def get_all_board():
    title_param = request.args.get("title")

    query = db.select(Board)
    if title_param:
        query = query.where(Board.title.like(f"%{title_param}"))

    boards = db.session.scalars(query).all()
    return [board.to_dict() for board in boards]



@board_bp.delete("/<board_id>")
def delete_board(board_id):
    validate_model(Board, board_id)
    query = db.select(Board).where(Board.id == board_id)
    board = db.session.scalar(query)
    if not board:
        response = {"message": f"{board_id} not found"}
        abort(make_response(response, 404))

    db.session.delete(board)
    db.session.commit()

    return {
        "details": f'Task {board_id} "{board.title}" successfully deleted'
    }

