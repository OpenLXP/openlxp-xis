#!/usr/bin/env bash
# start-server.sh

python manage.py waitdb 
python manage.py migrate 
python manage.py loaddata admin_theme_data.json 
python manage.py createcachetable
cd /opt/app/ 
pwd 
./start-server.sh