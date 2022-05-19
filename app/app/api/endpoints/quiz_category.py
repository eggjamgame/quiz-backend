from enum import Enum
from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException
from fastapi.params import Query
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.QuizCategory])
def read_quiz_category(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve quiz category.
    """
    quiz_category = crud.quiz_category.get_multi(
        db, skip=skip, limit=limit, 
    )
    return quiz_category


@router.post("/", response_model=schemas.QuizCategory)
def create_quiz_category(
    *,
    db: Session = Depends(deps.get_db),
    quiz_category_in: schemas.QuizCategoryCreate,
) -> Any:
    """
    Create new quiz category.
    """
    quiz_category = crud.quiz_category.create(db=db, obj_in=quiz_category_in)
    return quiz_category


@router.put("/{id}", response_model=schemas.QuizCategory)
def update_quiz_category(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    quiz_category_in: schemas.QuizCategoryUpdate,
) -> Any:
    """
    Update a quiz category.
    """
    quiz_category = crud.quiz_category.get(db=db, id=id)
    if not quiz_category:
        raise HTTPException(status_code=404, detail="Quiz Category not found")
    quiz_category = crud.quiz_category.update(db=db, db_obj=quiz_category, obj_in=quiz_category_in)
    return quiz_category


@router.get("/{id}", response_model=schemas.QuizCategory)
def read_quiz_category(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get quiz category by ID.
    """
    quiz_category = crud.quiz_category.get(db=db, id=id)
    if not quiz_category:
        raise HTTPException(status_code=404, detail="Quiz Category not found")
    return quiz_category


@router.delete("/{id}", response_model=schemas.QuizCategory)
def delete_quiz_category(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Delete a quiz category.
    """
    quiz_category = crud.quiz_category.get(db=db, id=id)
    if not quiz_category:
        raise HTTPException(status_code=404, detail="Quiz Category not found")
    quiz_category = crud.quiz_category.remove(db=db, id=id)
    return quiz_category

@router.get("/{id}/quiz", response_model=List[schemas.Quiz])
def read_quiz_category_episodes(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Retrieve episode with QuizCategory by episode order.
    """
    quiz_category = crud.quiz_category.get(db=db, id=id)
    if not quiz_category:
        raise HTTPException(status_code=404, detail="Quiz Category not found")
    episodes = crud.quiz.get_all_with_category(db=db, category_id=id)
    return episodes