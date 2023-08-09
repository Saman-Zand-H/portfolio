python manage.py collectstatic --no-input
python manage.py migrate
python manage.py loaddata fixtures/cv.json
python manage.py loaddata fixtures/users.json
python manage.py loaddata fixtures/blog.json

if [ "$ENVIRONMENT" = "development" ]
then
	python manage.py runserver 0.0.0.0:8000
else
	hypercorn --config conf.asgi:application/hypercorn.config.py
fi
