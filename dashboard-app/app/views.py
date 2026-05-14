import os
from flask import current_app, request
from werkzeug.utils import secure_filename
from wtforms import FileField
from .extensions import appbuilder, db
from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import Categoria, Producto
class CategoriaModelView(ModelView):
    datamodel = SQLAInterface(Categoria)
    add_form_extra_fields = {
    "imagen_file": FileField("imagen")
    }
    label_columns = {'nombre': 'Nombre', 'descripcion': 'Descripción', 'estado': 'Estado', 'creado_en': 'Creado En', 'actualizado_en': 'Actualizado En','imagen_preview':'Imagen'}
    list_columns = ['nombre', 'descripcion', 'estado', 'creado_en','imagen_preview']
    add_columns = ['nombre', 'descripcion','imagen_file', 'estado']
    edit_columns = ['nombre', 'descripcion', 'imagen', 'estado']
    show_columns = ['nombre', 'descripcion', 'imagen', 'estado', 'creado_en', 'actualizado_en']
    def pre_add(self, item):
        file = request.files.get("imagen_file")
        if file:
            filename = secure_filename(file.filename)
            upload_path = os.path.join(
                current_app.root_path,
                'static',
                'uploads'
            )
            os.makedirs(upload_path, exist_ok=True)
            file_path = os.path.join(upload_path, filename)
            file.save(file_path)
            item.imagen = f'uploads/{filename}'
class ProductoModelView(ModelView):
    add_form_extra_fields = {
        "imagen_file": FileField("imagen")
    }
    datamodel = SQLAInterface(Producto)
    label_columns = {'nombre': 'Nombre', 'descripcion': 'Descripción', 'precio': 'Precio', 'categorias': 'Categoría', 'estado': 'Estado', 'creado_en': 'Creado En', 'actualizado_en': 'Actualizado En','imagen_preview':'Imagen'}
    list_columns = ['nombre', 'precio', 'categorias', 'estado','imagen_preview']
    add_columns = ['nombre', 'descripcion','precio','categorias','estado','imagen_file']
    edit_columns = ['nombre', 'descripcion','precio','categorias','estado']
    show_columns = ['nombre', 'descripcion','precio', 'imagen','estado','creado_en','actualizado_en']
    def pre_add(self, item):
        file = request.files.get("imagen_file")
        if file:
            filename = secure_filename(file.filename)
            upload_path = os.path.join(
                current_app.root_path,
                'static',
                'uploads'
            )
            os.makedirs(upload_path, exist_ok=True)
            file_path = os.path.join(upload_path, filename)
            file.save(file_path)
            item.imagen = f'uploads/{filename}'
appbuilder.add_view(CategoriaModelView, "Categorías", icon="fa-folder-open-o", category="Configuraciones", category_icon="fa-cogs")

appbuilder.add_view(ProductoModelView, "Productos", icon="fa-cube", category="Configuraciones", category_icon="fa-cogs")