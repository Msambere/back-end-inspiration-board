from sqlalchemy.orm import mapped_column, relationship, Mapped
from app import db

class Board(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=False)
    cards = relationship('Card', back_populates='board', cascade='all, delete-orphan')

    def to_dict(self):
        result = {"id": self.id, "title": self.title, "cards": self.cards}
        cards = []
        for card in self.cards:
            cards.append(card.to_dict())
            result["cards"] = cards
        return result

    @classmethod
    def from_dict(cls, board_data):
        cards= []
        if board_data.get("cards"):
            cards = board_data.get("cards")
        return cls(
            title=board_data.get("title"),
            cards=cards
        )
