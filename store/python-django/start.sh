#!/bin/sh

# Remove old dabatabase, if found

rm -f db.sqlite3

# Provision a new database

python manage.py makemigrations store
python manage.py migrate
rm -rf store/migrations

# Load sample data

python manage.py loaddata store/fixtures/*

# Start the server

python manage.py runserver
