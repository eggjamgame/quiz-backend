from typing import Optional
from fastapi import Form

from pydantic import BaseModel


# Shared properties
class QuizBase(BaseModel):
    description: Optional[str] = None
    answer: Optional[str] = None
    


# Properties to receive on Quiz creation
class QuizCreate(QuizBase):
    description: str
    answer: str


# Properties to receive on Quiz update
class QuizUpdate(QuizBase):
    pass

# Properties shared by models stored in DB
class QuizInDBBase(QuizBase):
    id: int
    description: str
    category_id: str

    class Config:
        orm_mode = True

# Properties to return to client
class Quiz(QuizInDBBase):
    pass


# Properties properties stored in DB
class QuizInDB(QuizInDBBase):
    pass
