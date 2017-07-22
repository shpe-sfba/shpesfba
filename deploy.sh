#!/bin/bash

rsync -rvh --exclude 'deploy.sh' --exclude '.env' --exclude '.DS_Store' --exclude '.gitignore' --exclude '.git' --exclude 'uploads' --exclude 'venv' --exclude 'staticfiles' --exclude 'db.sqlite3' --exclude '*.pyc' --exclude '.idea' --exclude 'shpesfbasite/settings.py' ./ -e ssh 'luis@205.185.120.249:/opt/django/shpesfba/shpesfba/'

ssh luis@205.185.120.249 <<'ENDSSH'
source /opt/django/shpesfba/shpesfba/.env
source /opt/django/shpesfba/venv/bin/activate
pip install -r /opt/django/shpesfba/shpesfba/requirements.txt
python /opt/django/shpesfba/shpesfba/manage.py collectstatic --no-input
python /opt/django/shpesfba/shpesfba/manage.py migrate
touch /opt/django/shpesfba/uwsgi.ini
ENDSSH
