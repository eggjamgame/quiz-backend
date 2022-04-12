from typing import Optional
from fastapi import Form

from pydantic import BaseModel



# Shared properties
class QuizCategoryBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Properties to receive on category creation
class QuizCategoryCreate(QuizCategoryBase):
    title: str
    description: str


# Properties to receive on category update
class QuizCategoryUpdate(QuizCategoryBase):
    pass

# Properties shared by models stored in DB
class QuizCategoryInDBBase(QuizCategoryBase):
    id: int
    title: str
    description: str

    class Config:
        orm_mode = True


# Properties to return to client
class QuizCategory(QuizCategoryInDBBase):
    pass


# Properties properties stored in DB
class QuizCategoryInDB(QuizCategoryInDBBase):
    pass
