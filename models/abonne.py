"""
TODO O3 : décrire la table abonne comme une classe Python.

Table SQL correspondante :
    abonne (id, nom, prenom, email, date_naissance, date_inscription)
    Aucune colonne n'accepte NULL.

Modèle à suivre : models/station.py
"""

# TODO O3 : les imports
#   - date, depuis datetime
#   - TYPE_CHECKING, depuis typing
#   - Mapped, mapped_column, relationship, depuis sqlalchemy.orm
#   - Base, depuis models.base
#   - Trajet, depuis models.trajet, MAIS seulement sous « if TYPE_CHECKING: »
#         (trajet.py importe déjà abonne.py : un import normal ferait une boucle)
#         voir comment station.py importe Velo


# TODO O3 : la classe Abonne, qui hérite de Base
#   - __tablename__ = "abonne"
#   - id : entier, clé primaire
#   - nom, prenom, email : textes
#   - date_naissance, date_inscription : dates
#   - trajet_list : les trajets de l'abonné (relation 1:N)
#         indice : Mapped[list["Trajet"]] = relationship(back_populates="abonne")
#         "Trajet" est entre guillemets : la classe n'est pas encore importée à ce moment-là
#   - __repr__ : renvoyer par exemple f"Abonne({self.id}, {self.prenom} {self.nom})"
