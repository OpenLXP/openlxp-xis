#!/usr/bin/env bash
# start-server.sh
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (cd openlxp-xis; python manage.py createsuperuser --no-input)
fi
(cd openlxp-xis; gunicorn openlxp_xis_project.wsgi --reload --user www-data --bind 0.0.0.0:8010 --workers 3) &
nginx -g "daemon off;"
