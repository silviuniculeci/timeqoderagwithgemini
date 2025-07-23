#!/bin/sh
source .venv/bin/activate

# For local development, you can still use Flask's dev server:
# export FLASK_APP=main
# export FLASK_DEBUG=1
# python -u -m flask run -p ${PORT:-8080}

# For production (e.g., Cloud Run), use Gunicorn
exec gunicorn --bind :${PORT:-8080} --workers 1 --threads 8 --timeout 0 main:app
