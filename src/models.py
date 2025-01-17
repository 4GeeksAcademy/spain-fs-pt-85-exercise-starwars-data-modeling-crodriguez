import os
import sys
from sqlalchemy import Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class Usuarios(Base):
    __tablename__ = "usuarios"

    id = mapped_column(Integer, primary_key=True)
    nombre = mapped_column(String(50), nullable=False)
    apellido = mapped_column(String(50))
    correo = mapped_column(String(100), nullable=False)
    contrasena = mapped_column(String(20), nullable=False)
    fecha_suscripcion = mapped_column(String(20))
    favoritos = relationship("Usuarios", back_populates="favoritos")


class Personajes(Base):
    __tablename__ = "personajes"

    id = mapped_column(Integer, primary_key=True)
    nombre = mapped_column(String(50), nullable=False)
    especie = mapped_column(String(50))
    favoritos = relationship("Personajes", back_populates="favoritos")

class Planetas(Base):
    __tablename__ = "planetas"

    id = mapped_column(Integer, primary_key=True)
    nombre = mapped_column(String(50), nullable=False)
    sistema = mapped_column(String(50))
    favoritos = relationship("Planetas", back_populates="favoritos")

class Favoritos(Base):
    __tablename__ = "favoritos"

    id = mapped_column(Integer, primary_key=True)
    usuario_id = mapped_column(ForeignKey("usuarios.id"))
    personaje_id = mapped_column(ForeignKey("personajes.id"))
    planeta_id = mapped_column(ForeignKey("planetas.id"))
    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')