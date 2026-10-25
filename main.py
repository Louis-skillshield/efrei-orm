"""
Mini-pratiques ORM (journée 4) : O2, O3 et O5 sont à écrire dans ce fichier.

O1 et O4 se font avec les démos : uv run python demo_orm.py 1

Lancer :
    uv run python main.py
"""

from sqlalchemy.orm import Session

from models import Station
from src.database import get_engine

# TODO O2 : importer select depuis sqlalchemy
# TODO O3 : importer aussi func depuis sqlalchemy
# TODO O5 : importer aussi text depuis sqlalchemy
# TODO O2 : importer Velo depuis models (une fois models/velo.py écrit)
# TODO O3 : importer aussi Trajet depuis models (une fois models/trajet.py écrit)

engine = get_engine(echo=False)     # passer à True pour voir le SQL généré


def get_velo_electrique_maintenance_list(session):
    """O2. Les vélos électriques actuellement en maintenance."""
    # TODO O2 :
    #   1. Construire la requête avec select(Velo), puis .where(...) et .order_by(Velo.id).
    #      Plusieurs conditions dans un même where() sont combinées avec AND :
    #      le type vaut "électrique" et l'état vaut "maintenance".
    #   2. Renvoyer la liste des vélos : session.scalars(query).all()
    raise NotImplementedError


def get_trajet_count_by_arrondissement(session):
    """O3. Nombre de trajets par arrondissement de la station de départ, du plus grand au plus petit."""
    # TODO O3 :
    #   1. Sélectionner deux colonnes : Station.arrondissement et le nombre de trajets,
    #      func.count(Trajet.id), nommé avec .label("nombre_trajets").
    #   2. Joindre les trajets à leur station de départ :
    #      .join(Trajet, Trajet.station_depart_id == Station.id)
    #   3. Regrouper par arrondissement avec .group_by(),
    #      puis trier par nombre de trajets décroissant : .order_by(func.count(Trajet.id).desc())
    #   4. Renvoyer des couples (arrondissement, nombre_trajets) : session.execute(query).all()
    raise NotImplementedError


def get_top_station_by_type(session):
    """O5 (bonus). Top 3 des stations de départ par type de vélo, en SQL brut avec text()."""
    # TODO O5 :
    #   1. Écrire la requête SQL dans text(""" ... """) : reprendre votre requête F3
    #      (CTE + ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ...)).
    #   2. Ne pas écrire 3 en dur : utiliser un paramètre nommé, WHERE rang <= :rang_max
    #   3. Nommer les colonnes renvoyées : type_velo, rang, station, nombre_trajets
    #   4. Renvoyer session.execute(query, {"rang_max": 3}).all()
    raise NotImplementedError


if __name__ == "__main__":
    with Session(engine) as session:
        try:
            velo_list = get_velo_electrique_maintenance_list(session)
            print(f"O2. {len(velo_list)} vélos électriques en maintenance :", velo_list)
        except NotImplementedError:
            print("O2. À compléter : get_velo_electrique_maintenance_list")

        try:
            print("O3. Trajets par arrondissement de départ :")
            for arrondissement, nombre_trajets in get_trajet_count_by_arrondissement(session)[:5]:
                suffixe = "er" if arrondissement == 1 else "e"
                print(f"    {arrondissement:>2}{suffixe} : {nombre_trajets}")
        except NotImplementedError:
            print("    À compléter : get_trajet_count_by_arrondissement")

        try:
            print("O5. Top 3 des stations par type de vélo :")
            for row in get_top_station_by_type(session):
                print(f"    {row.type_velo:<10} {row.rang}. {row.station} ({row.nombre_trajets})")
        except NotImplementedError:
            print("    À compléter (bonus) : get_top_station_by_type")
