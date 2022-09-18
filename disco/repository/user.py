
from sqlalchemy.orm import Session
from disco import models, schemas
from fastapi import HTTPException, status
from disco.hashing import Hash


def create(request: schemas.User, db: Session):
    new_user = models.User(
        name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
