from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base

if TYPE_CHECKING:
    # Import réservé à l'éditeur de code : à l'exécution, velo.py importe déjà station.py
    from models.velo import Velo


class Station(Base):
    __tablename__ = "station"

    id: Mapped[int] = mapped_column(primary_key=True)
    nom: Mapped[str]
    arrondissement: Mapped[int]
    capacite: Mapped[int]
    date_fermeture: Mapped[date | None]

    # Une station -> plusieurs vélos garés (relation 1:N)
    velo_list: Mapped[list["Velo"]] = relationship(back_populates="station")

    def __repr__(self):
        return f"Station({self.id}, {self.nom!r})"
