from typing import List, Union, Dict, Any

from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm.session import Session
from app.crud.base import CRUDBase
from app.models.quiz import Quiz
from app.schemas.quiz import QuizCreate, QuizUpdate


class CRUDQuiz(CRUDBase[Quiz, QuizCreate, QuizUpdate]):
    def create_with_category(self, db: Session, *, obj_in: QuizCreate, category_id: int) -> Quiz:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = Quiz(
            **obj_in_data,
            category_id=category_id
        )  # type: ignore

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_all_with_category(
        self, db: Session, *, category_id: int
    ) -> List[Quiz]:
        return db.query(self.model).filter(Quiz.category_id == category_id).all()

quiz = CRUDQuiz(Quiz)
