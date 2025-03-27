from pydantic import BaseModel
from sqlmodel import Session
from db.conecxion import db
from db.modelos import Pedidos, ProductosEnPedidos

class Productos(BaseModel):
    productoID: str
    cantidad: int

class PedidoARegistrar(BaseModel):
    clienteID: str
    productos: list[Productos] 

def registrar(pedidoARegistrar: PedidoARegistrar):
    with Session(db) as sesion:
        pedido = Pedidos(clienteID=pedidoARegistrar.clienteID)
        sesion.add(pedido)

        for producto in pedidoARegistrar.productos:
            sesion.add(
                ProductosEnPedidos(
                    pedidoID=pedido.id,
                    productoID=producto.productoID,
                    cantidad=producto.cantidad,
                )
            )

        sesion.commit()
        sesion.refresh(pedido)

    return pedido

