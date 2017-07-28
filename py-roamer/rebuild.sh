#!/bin/bash
# Clear and rebuild Cloud SQL database

python manage.py flush      # Clear old database (does this need to be done manually?)
python manage.py makemigrations encyclopedia   # Prepare empty database with model
python manage.py makemigrations sieve           # Shouldn't do anything, since sieve uses model from encyclopedia
python manage.py migrate

echo "Building database from csv file..."
python build_database.py     # Build new database from csv file
