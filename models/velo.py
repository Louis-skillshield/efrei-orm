from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.station import Station


class Velo(Base):
    __tablename__ = "velo"

    id: Mapped[int] = mapped_column(primary_key=True)
    numero_serie: Mapped[str]
    type: Mapped[str]
    etat: Mapped[str]
    station_id: Mapped[int | None] = mapped_column(ForeignKey("station.id"))
    date_mise_en_service: Mapped[date]

    station: Mapped[Station | None] = relationship(back_populates="velo_list")

    def __repr__(self):
        return f"Velo({self.id}, {self.type!r}, {self.etat!r})"
