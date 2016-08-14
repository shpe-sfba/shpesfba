#!/bin/bash

rsync -rvh --exclude 'deploy.sh' --exclude '.gitignore' --exclude '.git' --exclude 'uploads' --exclude 'venv' --exclude 'staticfiles' --exclude 'db.sqlite3' --exclude '*.pyc' --exclude '.idea' ./ -e ssh 'luis@205.185.120.249:/opt/django/shpesfba/shpesfba/'

ssh luis@205.185.120.249 <<'ENDSSH'
touch /opt/django/shpesfba/uwsgi.ini
ENDSSH
