#!/usr/bin/env bash
set -euo pipefail

# DB migrations
python manage.py migrate --noinput

# Collect static files
#python manage.py collectstatic --noinput

# Create a superuser once
python manage.py shell <<'PY'
from django.contrib.auth import get_user_model
import os
User = get_user_model()
username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")
if username and email and password and not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
PY

# Start the app
exec gunicorn CocinaSalud.wsgi:application \
  --workers "${WEB_CONCURRENCY:-2}" \
  --bind ":${PORT:-8080}" \
  --timeout 600
