python manage.py collectstatic --no-input
python manage.py migrate
python manage.py loaddata fixtures/cv.json
gunicorn -c /usr/src/app/backend/gunicorn.config.py conf.wsgi:application
