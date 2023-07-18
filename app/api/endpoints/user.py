from fastapi import APIRouter, HTTPException

from app.users.core import auth_backend, fastapi_users
from app.users.schemas import UserCreate, UserRead, UserUpdate

user_router = APIRouter()

user_router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix='/auth/jwt',
    tags=['auth']
)

user_router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix='/auth',
    tags=['auth']
)

user_router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix='/users',
    tags=['users']
)


@user_router.delete(
    '/users/{id}',
    tags=['users'],
    deprecated=True
)
async def delete_user(id: str):
    """Do not delete users, deactivate them!"""
    raise HTTPException(
        status_code=405,
        detail='Users deletion is not allowed!'
    )
