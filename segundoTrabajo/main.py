from fastapi import HTTPException
from app.pedidos.actualizarPedido import nuevoEstado, EstadoPedidoUpdate
from app.clientes.consultarPedidosDelCliente import consultarPedidos
from app.clientes.consultarEstadoDelPedido import consultaEstado
from db.modelos import Clientes, Productos
from app.clientes.registrar import registrar as registrarNuevoCliente
from app.productos.registrar import registrar as registrarNuevoProducto
from app.pedidos.registrar import PedidoARegistrar, registrar as registrarNuevoPedido
from app import app 

@app.get("/api/v1/ok")
def read_root():
    return {"status": "Ok"}

@app.post("/api/v1/clientes")
def post_clientes(cliente: Clientes):
    return registrarNuevoCliente(cliente)

@app.post("/api/v1/productos")
def post_productos(porducto: Productos):
    return registrarNuevoProducto(porducto)

@app.post("/api/v1/pedidos")
def post_pedidos(pedido: PedidoARegistrar):
    return registrarNuevoPedido(pedido)

@app.get("/api/v1/clientes/{clienteID}/pedidos")
def get_pedidos_del_cliente(clienteID: str):
    pedidos = consultarPedidos(clienteID)
    return {"pedido": pedidos}

@app.get("/api/v1/pedidos/{pedidoID}/estado")
def get_estado_del_pedido(pedidoID: str):
    estadoPedido = consultaEstado(pedidoID)
    if not estadoPedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return {"pedidoID": pedidoID, "estado": estadoPedido.estado}

@app.put("/api/v1/pedidos/{pedidoID}/estado")
def put_nuevo_estado_de_pedido(pedidoID: str, estado: EstadoPedidoUpdate):
    return nuevoEstado(pedidoID, estado)
