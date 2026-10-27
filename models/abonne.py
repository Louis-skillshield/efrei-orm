from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base

if TYPE_CHECKING:
    from models.trajet import Trajet


class Abonne(Base):
    __tablename__ = "abonne"

    id: Mapped[int] = mapped_column(primary_key=True)
    nom: Mapped[str]
    prenom: Mapped[str]
    email: Mapped[str]
    date_naissance: Mapped[date]
    date_inscription: Mapped[date]

    # Un abonné -> plusieurs trajets (relation 1:N)
    trajet_list: Mapped[list["Trajet"]] = relationship(back_populates="abonne")

    def __repr__(self):
        return f"Abonne({self.id}, {self.prenom} {self.nom})"
