from typing import Any, List

import os
import shutil
from unicodedata import category

from fastapi import APIRouter, Body, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings

router = APIRouter()


@router.get("/", response_model=List[schemas.Quiz])
def read_quizzes(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 5,
) -> Any:
    """
    Retrieve quizzes.
    """
    quizs = crud.quiz.get_multi(db, skip=skip, limit=limit)
    return quizs


@router.post("/", response_model=schemas.Quiz)
def create_quiz(
    *,
    db: Session = Depends(deps.get_db),
    quiz_in: schemas.QuizCreate,
    category_id: int = Body(...),
) -> Any:
    """
    Create new quiz.
    """
    if not crud.quiz_category.get(db=db, id=category_id):
        raise HTTPException(
            status_code=400, detail="Category not found. Maybe You've tried to insert wrong number")
    quiz = crud.quiz.create_with_category(
        db=db, obj_in=quiz_in, category_id=category_id)
    return quiz


@router.put("/{id}", response_model=schemas.Quiz)
def update_quiz(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    quiz_in: schemas.QuizUpdate,
) -> Any:
    """
    Update an quiz.
    """
    quiz = crud.quiz.get(db=db, id=id)
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    quiz = crud.quiz.update(db=db, obj_in=quiz_in)
    return quiz


@router.get("/{id}", response_model=schemas.Quiz)
def read_quiz(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get quiz by ID.
    """
    quiz = crud.quiz.get(db=db, id=id)
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    return quiz


@router.delete("/{id}", response_model=schemas.Quiz)
def delete_quiz(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Delete an quiz.
    """
    quiz = crud.quiz.get(db=db, id=id)
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    quiz = crud.quiz.remove(db=db, id=id)
    return quiz
