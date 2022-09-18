from fastapi import APIRouter
from disco import database, schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from disco.repository import user

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db


@router.post('/', response_model=schemas.ShowUser)
def crear_usuario(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)

