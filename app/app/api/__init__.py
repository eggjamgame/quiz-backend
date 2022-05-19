from fastapi import APIRouter

from .endpoints import quizzes, quiz_category

api_router = APIRouter()
# api_router.include_router(posts.router, prefix="/posts", tags=["posts"])
api_router.include_router(quizzes.router, prefix="/quiz", tags=["quizzes"])
api_router.include_router(quiz_category.router, prefix="/quiz_category", tags=["quiz_categories"])
