from typing import List, Union, Dict, Any

from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm.session import Session
from app.crud.base import CRUDBase
from app.models.quiz_category import QuizCategory
from app.schemas.quiz_category import QuizCategoryCreate, QuizCategoryUpdate


class QuizCategory(CRUDBase[QuizCategory, QuizCategoryCreate, QuizCategoryUpdate]):
    pass

quiz_category = QuizCategory(QuizCategory)
