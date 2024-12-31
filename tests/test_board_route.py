import pytest
from app.models.board import Board



# ---- Get Method Tests ----
def test_get_all_boards_with_no_records(client):
    # Act
    response = client.get("/boards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {"boards":[]}

def test_get_one_board(client, two_saved_boards):
    # Act
    response = client.get("/boards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body["board"] == {
        "id": 1,
        "title": "All the Fruitz",
        "owner": "Fruit Lover",
        "cards": []
    }

def test_get_one_board_does_not_exist(client, two_saved_boards):
    # Act
    response = client.get("/boards/3")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {
        "details": "Board with id 3 does not exist"
    }

def test_get_one_board_invalid_id(client, two_saved_boards):
    # Act
    response = client.get("/boards/one")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {
        "details": "Board with id one is invalid"
    }

def test_get_all_cards_for_specific_board(client, two_saved_boards, two_saved_cards):
    # Act
    response = client.get("/boards/1/cards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {"cards":[
        {"id": 1,"text": "Banana","likes": 3, "board_id": 1},
        {"id": 2,"text": "Apple","likes": 2, "board_id": 1}
        ]}

def test_get_all_cards_for_empty_board(client, two_saved_boards):
    # Act
    response = client.get("/boards/2/cards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "cards": []
    }

# ---- Post Method Tests ---- 

def test_create_one_board(client):
    # Act
    response = client.post("/boards", json={
        "title": "New Board",
        "owner": "New Owner"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {"board":{
        "id": 1,
        "title": "New Board",
        "owner": "New Owner",
        "cards": []
        }
    }
    
# @pytest.mark.skip(reason="Weird test error from flask")
def test_create_one_board_missing_title(client):
    # Act
    response = client.post("/boards", json={
        "owner": "New Owner"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {"details": "Invalid request: missing title"}

# @pytest.mark.skip(reason="Weird test error from flask")
def test_create_one_board_missing_owner(client):
    # Act
    response = client.post("/boards", json={
        "title": "New Board"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {"details": "Invalid request: missing owner"}


def test_create_card_with_board(client, two_saved_boards):
    # Act
    response = client.post("/boards/1/cards", json={
        "text": "New Card",
        "likes": "0"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {"card":{
        "id": 1,
        "text": "New Card",
        "likes": 0,
        "board_id": 1
    }}

# @pytest.mark.skip(reason="Weird test error from flask")
def test_create_card_with_board_missing_text(client, two_saved_boards):
    # Act
    response = client.post("/boards/1/cards", json={
        "likes": "0"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {"details": "Invalid request: missing text"}

# ---- Update Method Test ----
def test_update_board(client, two_saved_boards):
    # Act
    response = client.patch("/boards/1", json={
        "title": "Updated Title",
        "owner": "Updated Owner"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {"board":{
        "id": 1,
        "title": "Updated Title",
        "owner": "Updated Owner",
        "cards": []
    }}


def test_update_board_title_only(client, two_saved_boards):
    # Act
    response = client.patch("/boards/1", json={
        "title": "Updated Title"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {"board":{
        "id": 1,
        "title": "Updated Title",
        "owner": "Fruit Lover",
        "cards": []
    }}

def test_update_board_owner_only(client, two_saved_boards):
    # Act
    response = client.patch("/boards/1", json={
        "owner": "Updated Owner"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {"board":{
        "id": 1,
        "title": "All the Fruitz",
        "owner": "Updated Owner",
        "cards": []
    }}
# ---- Delete Method Test ----
def test_delete_board(client, two_saved_boards):
    # Act
    response = client.delete("/boards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "details": 'Board 1 "All the Fruitz" successfully deleted'
    }
    #Is there a way to test call validate model or query the database to check deletion?
