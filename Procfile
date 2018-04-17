release: python src/manage.py db init
release: python src/manage.py db migrate
release: python src/manage.py db upgrade
web: gunicorn src.route:app