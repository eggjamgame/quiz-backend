from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class QuizCategory(Base):
    __tablename__ = "quiz_category"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)