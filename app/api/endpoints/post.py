from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.reactions import reactions_cache
from app.core.db import get_async_session
from app.posts.crud import (
    check_user_is_not_author, create_new_post, delete_post_by_id,
    get_all_posts, get_post_by_id, update_post_by_id
)
from app.posts.schemas import PostDB, PostCreate, PostUpdate
from app.users.core import current_user
from app.users.models import User

post_router = APIRouter(tags=['posts'])


@post_router.get(
    '/posts',
    response_model=list[PostDB]
)
async def get_posts(
    session: AsyncSession = Depends(get_async_session)
):
    """Returns all posts."""
    posts = await get_all_posts(session)
    return [post.to_response_dict() for post in posts]


@post_router.post(
    '/posts',
    response_model=PostDB
)
async def create_post(
    post: PostCreate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    """Creates new post."""
    post = await create_new_post(post, session, user)
    return post.to_response_dict()


@post_router.get(
    '/posts/{post_id}',
    response_model=PostDB
)
async def retrieve_post(
    post_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    """Gets post by id."""
    post = await get_post_by_id(post_id, session)
    return post.to_response_dict()


@post_router.patch(
    '/posts/{post_id}',
    response_model=PostDB
)
async def update_post(
    post_id: int,
    update_data: PostUpdate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    """Updates current post."""
    post = await update_post_by_id(post_id, update_data, session, user)
    return post.to_response_dict()


@post_router.delete(
    '/posts/{post_id}',
    response_model=PostDB
)
async def delete_post(
    post_id: int,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    """Deletes current post."""
    post = await delete_post_by_id(post_id, session, user)
    return post.to_response_dict()


@post_router.post(
    '/posts/{post_id}/like',
    response_model=PostDB
)
async def like_post(
    post_id: int,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    """Likes post by user."""
    post = await check_user_is_not_author(post_id, session, user)
    reactions_cache.add_like(post_id, user)
    return post.to_response_dict()


@post_router.post(
    '/posts/{post_id}/dislike',
    response_model=PostDB
)
async def dislike_post(
    post_id: int,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    """Dislikes post by user."""
    post = await check_user_is_not_author(post_id, session, user)
    reactions_cache.add_dislike(post_id, user)
    return post.to_response_dict()
