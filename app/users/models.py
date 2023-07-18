from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy.orm import Mapped, relationship

from app.core.db import Base
from app.posts import models


class User(SQLAlchemyBaseUserTable[int], Base):
    """Common user model."""
    posts: Mapped[list['models.Post']] = relationship(
        back_populates='author',
        cascade='all, delete',
        passive_deletes=True
    )
