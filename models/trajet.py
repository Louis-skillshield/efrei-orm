from datetime import datetime
from decimal import Decimal

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.abonne import Abonne
from models.base import Base
from models.velo import Velo


class Trajet(Base):
    __tablename__ = "trajet"

    id: Mapped[int] = mapped_column(primary_key=True)
    abonne_id: Mapped[int] = mapped_column(ForeignKey("abonne.id"))
    velo_id: Mapped[int] = mapped_column(ForeignKey("velo.id"))
    station_depart_id: Mapped[int] = mapped_column(ForeignKey("station.id"))
    station_arrivee_id: Mapped[int | None] = mapped_column(ForeignKey("station.id"))
    depart_le: Mapped[datetime]
    arrivee_le: Mapped[datetime | None]
    distance_km: Mapped[Decimal | None]
    montant: Mapped[Decimal | None]

    abonne: Mapped[Abonne] = relationship(back_populates="trajet_list")
    velo: Mapped[Velo] = relationship()

    def __repr__(self):
        return f"Trajet({self.id}, abonné {self.abonne_id}, {self.montant} €)"
