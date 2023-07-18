from datetime import datetime

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.api import reactions as r
from app.core.db import Base
from app.users import models


class Post(Base):
    """Post model."""
    title: Mapped[str] = mapped_column(String(128))
    text: Mapped[str] = mapped_column(String(1024))
    create_date: Mapped[datetime] = mapped_column(nullable=True)
    author_id: Mapped[int] = mapped_column(
        ForeignKey('user.id', ondelete='CASCADE'),
        primary_key=True
    )
    author: Mapped['models.User'] = relationship(back_populates='posts')

    def to_response_dict(self) -> dict:
        """Forms response object for post model with extra fields."""
        likes = dislikes = []
        reactions = r.reactions_cache.reactions.get(self.id)
        if reactions is not None:
            likes = reactions['likes']
            dislikes = reactions['dislikes']
        return {
            'id': self.id,
            'title': self.title,
            'text': self.text,
            'create_date': self.create_date,
            'author_id': self.author_id,
            'reactions': {
                'likes': likes,
                'dislikes': dislikes,
            }
        }
