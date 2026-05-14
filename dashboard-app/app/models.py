from datetime import datetime, UTC
from sqlalchemy import ForeignKey
from markupsafe import Markup
from flask_appbuilder import Model
from sqlalchemy import Column, Integer, Numeric, String, Text, Boolean, DateTime
from sqlalchemy.orm import relationship


class Categoria(Model):
    __tablename__ = 'categoria'

    id = Column(Integer, primary_key=True)

    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=True)
    imagen = Column(String(255), nullable=True)

    estado = Column(Boolean, default=True, nullable=False)

    creado_en = Column(
        DateTime,
        default=lambda: datetime.now(UTC),
        nullable=False
    )

    actualizado_en = Column(
        DateTime,
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
        nullable=False
    )


    productos = relationship(
        'Producto',
        back_populates='categorias'
    )
    def imagen_preview(self):
    
        if self.imagen:

            return Markup(
                f'<img src="/static/{self.imagen}" width="100">'
            )

        return "Sin imagen"

    def __repr__(self):
        return self.nombre
    
class Producto(Model):
    __tablename__ = 'producto'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=True)
    precio = Column(Numeric(10, 2), nullable=False)
    categoria_id = Column(Integer, ForeignKey('categoria.id'), nullable=False)
    imagen = Column(String(255), nullable=True)
    estado = Column(Boolean, default=True, nullable=False)

    creado_en = Column(
        DateTime,
        default=lambda: datetime.now(UTC),
        nullable=False
    )

    actualizado_en = Column(
        DateTime,
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
        nullable=False
    )
    categorias = relationship(
        'Categoria',
        back_populates='productos'
    )
    def imagen_preview(self):
    
        if self.imagen:

            return Markup(
                f'<img src="/static/{self.imagen}" width="100">'
            )

        return "Sin imagen" 
    def __repr__(self):
        return self.nombre