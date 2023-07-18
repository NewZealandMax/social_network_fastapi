from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, PositiveInt


class PostUpdate(BaseModel):
    """Schema for updating post."""
    title: Optional[str]
    text: Optional[str]


class PostCreate(PostUpdate):
    """Schema for creating post."""
    title: str = Field(..., min_length=3, max_length=128)
    text: str = Field(..., min_length=1, max_length=1024)
    create_date: datetime
    author_id: int


class PostDB(PostCreate):
    """Schema for reading post."""
    id: PositiveInt
    reactions: dict[str, list[str]]

    class Config:
        from_attributes = True
