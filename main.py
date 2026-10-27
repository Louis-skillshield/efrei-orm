"""
Du SQL à l'ORM : la base Vélib' avec SQLAlchemy.

Chaque démo affiche le SQL que SQLAlchemy envoie à PostgreSQL (echo=True).

Lancer une démo :
    uv run python main.py 1      # SELECT + WHERE
    uv run python main.py 2      # relations entre tables
    uv run python main.py 3      # GROUP BY
    uv run python main.py 4      # INSERT dans une transaction (annulée)
    uv run python main.py 5      # le piège du N+1
    uv run python main.py 6      # le N+1 corrigé
    uv run python main.py 7      # SQL brut avec text() (fonction de fenêtre)
"""

import sys
from datetime import datetime

from sqlalchemy import func, select, text
from sqlalchemy.orm import Session, selectinload

from models import Abonne, Station, Trajet, Velo
from src.database import get_engine

engine = get_engine(echo=True)


def run_demo_select():
    """Les stations du 11e arrondissement."""
    # SQL : SELECT * FROM station WHERE arrondissement = 11 ORDER BY nom;
    with Session(engine) as session:
        query = (
            select(Station).where(Station.arrondissement == 11).order_by(Station.nom)
        )
        for station in session.scalars(query):
            print(station.nom, station.capacite)


def run_demo_relation():
    """Un vélo et sa station : la jointure est faite pour nous."""
    with Session(engine) as session:
        velo = session.get(Velo, 1)  # SELECT … FROM velo WHERE id = 1
        print(velo, "garé à", velo.station)  # SELECT … FROM station WHERE id = …


def run_demo_group_by():
    """Nombre de trajets par type de vélo."""
    # SQL : SELECT v.type, COUNT(*) FROM trajet t JOIN velo v ON … GROUP BY v.type;
    with Session(engine) as session:
        query = (
            select(Velo.type, func.count(Trajet.id).label("nombre_trajets"))
            .join(Trajet.velo)
            .group_by(Velo.type)
        )
        for type_velo, nombre_trajets in session.execute(query):
            print(type_velo, nombre_trajets)


def run_demo_insert():
    """Créer un trajet en cours, dans une transaction… puis l'annuler."""
    with Session(engine) as session:  # la session ouvre une transaction (BEGIN)
        trajet = Trajet(
            abonne_id=42, velo_id=1, station_depart_id=5, depart_le=datetime.now()
        )
        session.add(trajet)
        session.flush()  # envoie l'INSERT, sans valider
        print("Trajet créé avec l'id", trajet.id)
        session.rollback()  # ROLLBACK : rien n'est enregistré
        # session.commit() aurait validé (COMMIT)


def run_demo_n_plus_1():
    """PIÈGE : 1 requête pour les abonnés, puis 1 requête PAR abonné."""
    with Session(engine) as session:
        abonne_list = session.scalars(select(Abonne).limit(10)).all()  # 1 requête
        for abonne in abonne_list:
            # chaque accès à trajet_list déclenche une NOUVELLE requête
            print(abonne, len(abonne.trajet_list), "trajets")
    # Bilan : 1 + 10 = 11 requêtes. Avec 2 000 abonnés : 2 001 requêtes !


def run_demo_n_plus_1_corrige():
    """CORRIGÉ : selectinload charge tous les trajets en UNE requête de plus."""
    with Session(engine) as session:
        query = select(Abonne).options(selectinload(Abonne.trajet_list)).limit(10)
        for abonne in session.scalars(query):
            print(abonne, len(abonne.trajet_list), "trajets")
    # Bilan : 2 requêtes, quel que soit le nombre d'abonnés.
    # (encore mieux ici : un GROUP BY qui ne compte que le nombre de trajets)


def run_demo_text():
    """Pour l'analyse (CTE, fenêtres), on garde le SQL… avec des paramètres."""
    query = text("""
        SELECT id, depart_le, montant,
        SUM(montant) OVER (ORDER BY depart_le) AS cumul
        FROM trajet
        WHERE abonne_id = :abonne_id
        ORDER BY depart_le
        LIMIT 5;
    """)
    with Session(engine) as session:
        for row in session.execute(query, {"abonne_id": 42}):
            print(row.id, row.depart_le, row.montant, row.cumul)


DEMO_LIST = {
    "1": run_demo_select,
    "2": run_demo_relation,
    "3": run_demo_group_by,
    "4": run_demo_insert,
    "5": run_demo_n_plus_1,
    "6": run_demo_n_plus_1_corrige,
    "7": run_demo_text,
}

if __name__ == "__main__":
    demo_number = sys.argv[1] if len(sys.argv) > 1 else "1"
    DEMO_LIST[demo_number]()
