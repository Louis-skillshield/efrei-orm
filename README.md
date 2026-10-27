# Journée 4 · ORM SQLAlchemy · version formateur (corrigée)

Le sous-dossier `etudiant/` est le dépôt public
[efrei-orm](https://github.com/Louis-skillshield/efrei-orm) : c'est lui qu'on donne aux étudiants.
Ce dossier-ci contient les corrections : **ne pas le publier**.

## Installation

```bash
cp .env.example .env      # puis renseigner vos identifiants PostgreSQL
uv sync
```

La base `velib_db` de la journée 3 doit être chargée.

## Contenu

| Fichier | Rôle |
|---|---|
| `models/` | Les tables `station`, `velo`, `abonne`, `trajet` : une classe SQLAlchemy par fichier — correction des modèles à compléter |
| `main.py` | 7 démos : SELECT, relations, GROUP BY, INSERT, piège du N+1, correction, SQL brut |
| `corrections_orm.py` | Correction des mini-pratiques ORM (O2, O3, O5) |
| `src/database.py` | Moteur SQLAlchemy à partir du `.env` |

## Lancer

```bash
uv run python main.py 1        # de 1 à 7
uv run python corrections_orm.py
```
