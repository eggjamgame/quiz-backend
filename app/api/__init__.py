from fastapi import APIRouter
from .endpoints import quizzes

api_router = APIRouter()
# api_router.include_router(posts.router, prefix="/posts", tags=["posts"])
api_router.include_router(quizzes.router, tags=["quizzes"])
api_router.include_router(quizzes.router, tags=["quiz_categories"])
