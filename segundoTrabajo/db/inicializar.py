from sqlmodel import SQLModel
from db.conecxion import db

def crearBDYTablas():
    SQLModel.metadata.create_all(db)

