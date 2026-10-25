"""
Modèle EXEMPLE, déjà complet : s'en inspirer pour écrire velo.py, abonne.py et trajet.py.

Table SQL correspondante :
    station (id, nom, arrondissement, capacite, date_fermeture)
"""

from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base

if TYPE_CHECKING:
    # Import réservé à l'éditeur de code : à l'exécution, velo.py importe déjà station.py
    from models.velo import Velo


class Station(Base):
    __tablename__ = "station"                       # le nom de la table dans PostgreSQL

    id: Mapped[int] = mapped_column(primary_key=True)   # clé primaire
    nom: Mapped[str]                                # colonne obligatoire (NOT NULL)
    arrondissement: Mapped[int]
    capacite: Mapped[int]
    date_fermeture: Mapped[date | None]             # « | None » : la colonne accepte NULL

    # Une station -> plusieurs vélos garés (relation 1:N)
    # TODO O2 : une fois models/velo.py écrit, décommenter la ligne suivante
    # velo_list: Mapped[list["Velo"]] = relationship(back_populates="station")

    def __repr__(self):
        return f"Station({self.id}, {self.nom!r})"
