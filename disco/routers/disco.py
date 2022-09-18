from typing import List
from fastapi import APIRouter, Depends, status
from disco import schemas, database, oauth2
from sqlalchemy.orm import Session
from disco.repository import disco

router = APIRouter(
    prefix="/disco",
    tags=['Productos']
)

get_db = database.get_db


@router.get('/', response_model=schemas.ShowProductos,status_code=status.HTTP_200_OK)
def scrape_productos(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return schemas.ShowProductos(records=disco.get_all(db))

@router.get('/electronica', response_model=schemas.ShowProductos,status_code=status.HTTP_200_OK)
def mostrar_productos(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return schemas.ShowProductos(records=disco.show_all(db))

@router.get('/electronica/{marca}', response_model=schemas.ShowProductos,status_code=status.HTTP_200_OK)
def filtrar_por_marca(marca:str, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return schemas.ShowProductos(records=disco.marcas(marca, db))

