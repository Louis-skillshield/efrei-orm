# Efrei · Journée 4 · Du SQL à l'ORM avec SQLAlchemy

On décrit les tables de la base Vélib' comme des classes Python, puis on les interroge sans écrire de SQL.

## Installation

```bash
git clone https://github.com/Louis-skillshield/efrei-orm.git
cd efrei-orm
cp .env.example .env      # puis renseigner vos identifiants PostgreSQL
uv sync
```

La base `velib_db` de la journée 3 doit être chargée.

## Contenu

| Fichier | Rôle |
|---|---|
| `models/` | Une classe par table. `station.py` est l'exemple complet ; `velo.py`, `abonne.py` et `trajet.py` sont à écrire (`# TODO O2`, `# TODO O3`) |
| `main.py` | Les requêtes ORM des mini-pratiques, à écrire (`# TODO O2`, `O3`, `O5`) |
| `demo_orm.py` | 7 démos fournies : SELECT, relations, GROUP BY, INSERT, piège du N+1, correction, SQL brut |
| `src/database.py` | Moteur SQLAlchemy à partir du `.env` |

## Lancer

```bash
uv run python demo_orm.py 1      # les démos, de 1 à 7
uv run python main.py            # vos réponses
```

Les énoncés (O1 à O5) sont dans les mini-pratiques de la journée 4.
Cherchez `TODO` dans le projet pour trouver tous les endroits où coder.
