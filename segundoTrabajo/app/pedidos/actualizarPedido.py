from fastapi import HTTPException
from sqlmodel import Session, select
from pydantic import BaseModel
from datetime import datetime
from db.modelos import Pedidos
from db.conecxion import db

# Definir el esquema de actualización del estado del pedido
class EstadoPedidoUpdate(BaseModel):
    estado: str

def nuevoEstado(pedidoID: int, estado: EstadoPedidoUpdate):
    with Session(db) as sesion:
        pedido = sesion.exec(select(Pedidos).where(Pedidos.id == pedidoID)).first()

        if not pedido:
            raise HTTPException(status_code=404, detail="Pedido no encontrado")

        # Actualizar el estado y la fecha de modificación
        pedido.estado = estado.estado
        pedido.updated_at = datetime.utcnow()
        sesion.add(pedido)
        sesion.commit()
        sesion.refresh(pedido)

        return {
            "pedidoID": pedidoID,
            "estado": pedido.estado,
            "updated_at": pedido.updated_at.isoformat()
        }
