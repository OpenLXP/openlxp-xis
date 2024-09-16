#!/usr/bin/env bash
# start-server.sh
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (cd /tmp/openlxp-xis/app; python manage.py createsuperuser --no-input)
fi
(cd /tmp/openlxp-xis/app; gunicorn openlxp_xis_project.wsgi --reload --user 1001 --bind 0.0.0.0:8080 --workers 3)

