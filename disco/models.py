from sqlalchemy import Column, Integer, String, ForeignKey
from disco.database import Base


class disco(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String)
    descripcion = Column(String)
    precio = Column(String)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
