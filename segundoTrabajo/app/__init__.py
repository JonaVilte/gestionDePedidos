from contextlib import asynccontextmanager
from fastapi import FastAPI
from db.inicializar import crearBDYTablas

@asynccontextmanager
async def cilcoDeLaApp(app: FastAPI):
    print("Iniciando la App")
    crearBDYTablas()
    yield
    print("Fin de la App")

app = FastAPI(lifespan=cilcoDeLaApp)