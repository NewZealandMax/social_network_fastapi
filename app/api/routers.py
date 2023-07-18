from fastapi import APIRouter

from app.api.endpoints import post_router, user_router

main_router = APIRouter()

main_router.include_router(post_router)
main_router.include_router(user_router)
