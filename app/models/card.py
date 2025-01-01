from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db

class Card(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(nullable=False)
    likes: Mapped[int] = mapped_column(default=0)
    board_id: Mapped[int] = mapped_column(ForeignKey("board.id"))
    board: Mapped["Board"] = relationship(back_populates="cards")

    def to_dict(self):
        card_dict = dict(
            id=self.id,
            text=self.text,
            likes=self.likes,
            board_id=self.board_id
        )
        return card_dict
    
    @classmethod
    def from_dict(cls, card_data):
        return cls(
            text=card_data.get("text"),
            likes=card_data.get("likes"),
            board_id=card_data.get("board_id")
        )
    @classmethod
    def attr_list(cls):
        return ["text"]