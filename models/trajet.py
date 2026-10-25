"""
TODO O3 : décrire la table trajet comme une classe Python.

Table SQL correspondante :
    trajet (id, abonne_id, velo_id, station_depart_id, station_arrivee_id,
            depart_le, arrivee_le, distance_km, montant)
    Un trajet en cours n'a pas encore de station d'arrivée, d'heure d'arrivée,
    de distance ni de montant : ces quatre colonnes acceptent NULL.

Modèle à suivre : models/station.py (et models/velo.py pour les clés étrangères)
"""

# TODO O3 : les imports
#   - datetime, depuis datetime (pour depart_le et arrivee_le)
#   - Decimal, depuis decimal (pour distance_km et montant : des NUMERIC en SQL)
#   - ForeignKey, depuis sqlalchemy
#   - Mapped, mapped_column, relationship, depuis sqlalchemy.orm
#   - Base, depuis models.base
#   - Abonne et Velo, depuis models.abonne et models.velo


# TODO O3 : la classe Trajet, qui hérite de Base
#   - __tablename__ = "trajet"
#   - id : entier, clé primaire
#   - abonne_id, velo_id, station_depart_id : entiers, clés étrangères
#         vers "abonne.id", "velo.id" et "station.id"
#   - station_arrivee_id : entier qui accepte NULL, clé étrangère vers "station.id"
#   - depart_le : datetime ; arrivee_le : datetime qui accepte NULL
#   - distance_km, montant : Decimal qui acceptent NULL
#   - abonne : la relation vers l'abonné
#         indice : Mapped[Abonne] = relationship(back_populates="trajet_list")
#   - velo : la relation vers le vélo utilisé
#         indice : Mapped[Velo] = relationship()
#   - __repr__ : renvoyer par exemple f"Trajet({self.id}, abonné {self.abonne_id}, {self.montant} €)"
#
# Ensuite : décommenter les imports d'Abonne et de Trajet dans models/__init__.py
