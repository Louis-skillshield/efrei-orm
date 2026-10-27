"""
Correction des mini-pratiques ORM (journée 4).

Lancer :
    uv run python corrections_orm.py
"""

from sqlalchemy import func, select, text
from sqlalchemy.orm import Session

from models import Station, Trajet, Velo
from src.database import get_engine

engine = get_engine(echo=False)     # passer à True pour voir le SQL généré


def get_velo_electrique_maintenance_list(session):
    """O2. Les vélos électriques actuellement en maintenance."""
    query = (
        select(Velo)
        .where(Velo.type == "électrique", Velo.etat == "maintenance")
        .order_by(Velo.id)
    )
    return session.scalars(query).all()


def get_trajet_count_by_arrondissement(session):
    """O3. Nombre de trajets par arrondissement de la station de départ."""
    query = (
        select(Station.arrondissement, func.count(Trajet.id).label("nombre_trajets"))
        .join(Trajet, Trajet.station_depart_id == Station.id)
        .group_by(Station.arrondissement)
        .order_by(func.count(Trajet.id).desc())
    )
    return session.execute(query).all()


def get_top_station_by_type(session):
    """O5 (bonus). Top 3 des stations de départ par type de vélo, en SQL brut avec text()."""
    query = text("""
        WITH depart_type AS (
            SELECT v.type AS type_velo, s.nom AS station, COUNT(*) AS nombre_trajets
            FROM trajet t
            JOIN velo v ON v.id = t.velo_id
            JOIN station s ON s.id = t.station_depart_id
            GROUP BY v.type, s.nom
        ),
        classement AS (
            SELECT *, ROW_NUMBER() OVER (PARTITION BY type_velo
                                         ORDER BY nombre_trajets DESC) AS rang
            FROM depart_type
        )
        SELECT type_velo, rang, station, nombre_trajets
        FROM classement
        WHERE rang <= :rang_max
        ORDER BY type_velo, rang;
    """)
    return session.execute(query, {"rang_max": 3}).all()


if __name__ == "__main__":
    with Session(engine) as session:
        velo_list = get_velo_electrique_maintenance_list(session)
        print(f"O2. {len(velo_list)} vélos électriques en maintenance :", velo_list)

        print("O3. Trajets par arrondissement de départ :")
        for arrondissement, nombre_trajets in get_trajet_count_by_arrondissement(session)[:5]:
            suffixe = "er" if arrondissement == 1 else "e"
            print(f"    {arrondissement:>2}{suffixe} : {nombre_trajets}")

        print("O5. Top 3 des stations par type de vélo :")
        for row in get_top_station_by_type(session):
            print(f"    {row.type_velo:<10} {row.rang}. {row.station} ({row.nombre_trajets})")
