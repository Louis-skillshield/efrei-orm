"""
Les tables Vélib' décrites comme des classes Python (SQLAlchemy 2.0).

Une classe = une table, un attribut = une colonne. Un fichier par table.
On ne décrit que les tables utiles aux exercices : station, velo, abonne, trajet.

Importer les modèles depuis ce paquet : from models import Station, Velo
"""

from models.base import Base
from models.station import Station

# TODO O2 : une fois models/velo.py écrit, décommenter la ligne suivante
# from models.velo import Velo

# TODO O3 : une fois models/abonne.py et models/trajet.py écrits, décommenter les deux lignes suivantes
# from models.abonne import Abonne
# from models.trajet import Trajet
