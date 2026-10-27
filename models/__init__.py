"""
Les tables Vélib' décrites comme des classes Python (SQLAlchemy 2.0).

Une classe = une table, un attribut = une colonne. Un fichier par table.
On ne décrit que les tables utiles à la démo : station, velo, abonne, trajet.

Importer les modèles depuis ce paquet : from models import Station, Velo
"""

from models.base import Base
from models.station import Station
from models.velo import Velo
from models.abonne import Abonne
from models.trajet import Trajet
