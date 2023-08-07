python manage.py collectstatic --no-input
python manage.py migrate
python manage.py loaddata fixtures/cv.json
if [-z ${ENVIRONMENT+x} && "$ENVIRONMENT" == "production"]
then
	gunicorn -c /usr/src/app/backend/gunicorn.config.py conf.wsgi:application
else
	python manage.py runserver 0.0.0.0:8000
fi
