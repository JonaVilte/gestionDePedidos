from sqlmodel import Session, select
from db.modelos import Pedidos
from db.conecxion import db


def consultaEstado(pedidoID: int):
    with Session(db) as sesion:
        estadoPedido = sesion.exec(select(Pedidos).where(Pedidos.id == pedidoID)).first()

        return estadoPedido
