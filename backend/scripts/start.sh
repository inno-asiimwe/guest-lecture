#! /bin/bash

printf "Waiting for postgres"

while ! nc -z database 5432; do
    sleep 0.1
done

printf "postgres started"

printf "Run Migrations"

flask db upgrade

printf "Start application on port 5000"

flask run --host=0.0.0.0 --port=5000