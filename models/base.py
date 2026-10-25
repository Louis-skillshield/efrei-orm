from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Classe mère de tous les modèles : elle garde la liste des tables connues."""
    pass
