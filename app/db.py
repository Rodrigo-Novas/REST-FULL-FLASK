"""
instanciamos la DB dentro de este archivo para no tener referencias circulares.
Además, se crea la clase BaseModelMixin con métodos de utilidad para los modelos.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BaseModelMixin:
    def save(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        """
        Obtiene todos los registros
        """
        return cls.query.all()
    
    @classmethod
    def get_by_id(cls,id):
        """
        Obtiene los registros con el id especificado
        """
        return cls.query.get(id)

    @classmethod
    def simple_filter(cls, **kwargs):
        """
        Filtro por clave valor (**kwargs)
        """
        return cls.query.filter_by(**kwargs).all()