from sqlalchemy.orm import mapped_column, relationship, Mapped
from app import db

class Board(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=False)
    owner: Mapped[str] = mapped_column(nullable=False)
    cards: Mapped[list["Card"]] = relationship(back_populates="board", cascade="all, delete-orphan")

    def to_dict(self):
        cards = []
        for card in self.cards:
            cards.append(card.to_dict())
        result = {
            "id": self.id, 
            "title": self.title, 
            "cards": cards,
            "owner": self.owner
            }
        return result

    @classmethod
    def from_dict(cls, board_data):
        cards= []
        if board_data.get("cards"):
            cards = board_data.get("cards")
        return cls(
            title=board_data.get("title"),
            owner=board_data.get("owner"),
            cards=cards
        )
    @classmethod
    def attr_list(cls):
        return ["title", "owner"]
