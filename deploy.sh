#!/bin/bash

rsync -rvh --exclude 'deploy.sh' --exclude '.DS_Store' --exclude '.gitignore' --exclude '.git' --exclude 'uploads' --exclude 'venv' --exclude 'staticfiles' --exclude 'db.sqlite3' --exclude '*.pyc' --exclude '.idea' ./ -e ssh 'luis@205.185.120.249:/opt/django/shpesfba/shpesfba/'

ssh luis@205.185.120.249 <<'ENDSSH'
source /opt/django/shpesfba/venv/bin/activate
python /opt/django/shpesfba/shpesfba/manage.py collectstatic --no-input
python /opt/django/shpesfba/shpesfba/manage.py migrate
touch /opt/django/shpesfba/uwsgi.ini
ENDSSH
