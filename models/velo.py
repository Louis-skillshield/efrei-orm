"""
TODO O2 : décrire la table velo comme une classe Python.

Table SQL correspondante :
    velo (id, numero_serie, type, etat, station_id, date_mise_en_service)
    station_id est une clé étrangère vers station.id, et peut être NULL
    (un vélo en circulation ou en maintenance n'est garé nulle part).

Modèle à suivre : models/station.py
"""

# TODO O2 : les imports
#   - date, depuis datetime (pour la colonne date_mise_en_service)
#   - ForeignKey, depuis sqlalchemy
#   - Mapped, mapped_column, relationship, depuis sqlalchemy.orm
#   - Base, depuis models.base
#   - Station, depuis models.station (pour la relation vélo -> station)


# TODO O2 : la classe Velo, qui hérite de Base
#   - __tablename__ = "velo"
#   - id : entier, clé primaire
#   - numero_serie, type, etat : textes
#   - station_id : entier qui accepte NULL, clé étrangère vers "station.id"
#         indice : mapped_column(ForeignKey("station.id"))
#   - date_mise_en_service : date
#   - station : la relation vers la station où le vélo est garé (ou None)
#         indice : Mapped[Station | None] = relationship(back_populates="velo_list")
#   - __repr__ : renvoyer par exemple f"Velo({self.id}, {self.type!r}, {self.etat!r})"
#
# Ensuite : décommenter velo_list dans models/station.py et l'import dans models/__init__.py
