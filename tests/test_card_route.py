import pytest
from app.models.card import Card


# ---- Get Method Tests ----
def test_get_all_cards_with_no_records(client):
    # Act
    response = client.get("/cards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


    
# ---- Post Method Tests ----
# ---- Upgrade Method Tests ----
def test_patch_likes(client, two_saved_boards, two_saved_cards):
    # Act
    response = client.patch("/cards/1/likes")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {"card": {
        "id": 1, 
        "text": "Banana", 
        "likes": 4, 
        "board_id": 1
        }}

def test_patch_likes_card_does_not_exist(client, two_saved_boards, two_saved_cards):
    # Act
    response = client.patch("/cards/3/likes")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"details": "Card with id 3 does not exist"}

# ---- Delete Method Tests ----
def test_delete_one_card(client, two_saved_boards, two_saved_cards):
    # Act
    response = client.delete("/cards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {"details": 'Card 1 with text "Banana" successfully deleted'}

def test_delete_one_card_does_not_exist(client, two_saved_boards, two_saved_cards):
    # Act
    response = client.delete("/cards/3")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"details": "Card with id 3 does not exist"}
