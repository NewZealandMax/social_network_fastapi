from datetime import datetime
from http import HTTPStatus
from typing import Optional

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.posts.models import Post
from app.posts.schemas import PostCreate, PostUpdate
from app.users.models import User


async def get_all_posts(
    session: AsyncSession
) -> list[Post]:
    """Returns all posts."""
    posts = await session.execute(
        select(Post).order_by(Post.create_date.desc())
    )
    return posts.scalars().all()


async def get_post_by_id(
    post_id: int,
    session: AsyncSession
) -> Optional[Post]:
    """Retrieves post by id."""
    post = await session.execute(
        select(Post).where(Post.id == post_id)
    )
    post = post.scalars().first()
    if post is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Post is not exist.'
        )
    return post


async def check_post_before_edit(
    post_id: int,
    session: AsyncSession,
    user: User
) -> Post:
    """Checks user is author."""
    post = await get_post_by_id(post_id, session)
    if post.author_id != user.id:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN,
            detail='Only author can edit the post.'
        )
    return post


async def check_user_is_not_author(
    post_id: int,
    session: AsyncSession,
    user: User
) -> Post:
    """Checks user is not post author."""
    post = await get_post_by_id(post_id, session)
    if post.author_id == user.id:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN,
            detail='Author can not like or dislike post'
        )
    return post


async def create_new_post(
    data_in: PostCreate,
    session: AsyncSession,
    user: User
) -> Post:
    """Creates new post."""
    create_data = data_in.model_dump()
    post = Post()
    for field, value in create_data.items():
        setattr(post, field, value)
    setattr(post, 'author_id', user.id)
    setattr(post, 'create_date', datetime.utcnow())
    session.add(post)
    await session.commit()
    await session.refresh(post)
    return post


async def update_post_by_id(
    post_id: int,
    update_data: PostUpdate,
    session: AsyncSession,
    user: User
) -> Post:
    """Updates current user's post."""
    post = await check_post_before_edit(post_id, session, user)
    data = update_data.model_dump()
    for field, value in data.items():
        setattr(post, field, value)
    session.add(post)
    await session.commit()
    await session.refresh(post)
    return post


async def delete_post_by_id(
    post_id: int,
    session: AsyncSession,
    user: User
) -> Post:
    """Deletes post by id."""
    post = await check_post_before_edit(post_id, session, user)
    await session.delete(post)
    await session.commit()
    return post
