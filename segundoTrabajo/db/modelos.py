from datetime import datetime
from sqlmodel import Field, SQLModel
from uuid import uuid4

class Clientes(SQLModel, table=True):
    id: str = Field(default=str(uuid4()), primary_key=True)
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default_factory=datetime.now)
    nombre: str
    apellido: str

class Pedidos(SQLModel, table=True):
    id: str = Field(default=str(uuid4()), primary_key=True)
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default_factory=datetime.now)
    clienteID: str = Field(foreign_key="clientes.id")
    estado: str = Field(default="Pendiente") #Pendiente, en proceso, entregado

class Productos(SQLModel, table=True):
    id: str = Field(default=str(uuid4()), primary_key=True)
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default_factory=datetime.now)
    nombre: str
    descripcion: str 

class ProductosEnPedidos(SQLModel, table=True):
    id: str = Field(default=str(uuid4()), primary_key=True)
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default_factory=datetime.now)
    pedidoID: str = Field(foreign_key="pedidos.id")
    productoID: str = Field(foreign_key="productos.id")
    cantidad: int 
