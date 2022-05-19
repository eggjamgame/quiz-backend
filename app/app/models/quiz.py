from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Quiz(Base):
    __tablename__ = "quiz"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    answer = Column(String)
    category_id = Column(Integer, ForeignKey(
        "quiz_category.id", ondelete="CASCADE"), nullable=False)
    category = relationship("QuizCategory")
