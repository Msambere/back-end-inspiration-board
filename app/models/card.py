from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db

class Card(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(nullable=False)
    likes: Mapped[int] = mapped_column(default=0)

    def to_dict(self):
        card_dict = dict(
            id=self.id,
            text=self.text,
            likes=self.likes,
        )
        return card_dict
    
    @classmethod
    def from_dict(cls, card_data):
        return cls(
            text=card_data.get("text"),
            likes=card_data.get("likes"),
        )
