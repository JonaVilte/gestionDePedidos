from sqlmodel import Session, select
from db.modelos import Pedidos
from db.conecxion import db

def consultarPedidos(clienteID: str):
    with Session(db) as sesion:
        consulta = select(Pedidos).where(Pedidos.clienteID == clienteID)
        pedidos = sesion.exec(consulta).all()
        return pedidos
