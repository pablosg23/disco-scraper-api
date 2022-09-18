from sqlalchemy.orm import Session
from disco import models, schemas
from fastapi import HTTPException, status
from . import scraper


def get_all(db: Session):
    scraper.scraper()
    scraper.to_db()
    disco = db.query(models.disco).all()
    if not disco:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Vuelve a intentarlo")
    return disco

def show_all(db: Session):
    disco = db.query(models.disco).all()
    if not disco:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Aún hay productos listados")
    return disco

def marcas(marca: str,db: Session):
    disco = db.query(models.disco).filter(models.disco.marca==marca.upper()).all()
    if not disco:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No se ha encontrado productos de la marca {marca.upper()}")
    return disco
