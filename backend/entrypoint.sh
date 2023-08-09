python manage.py collectstatic --no-input
python manage.py migrate
python manage.py loaddata fixtures/cv.json
python manage.py loaddata fixtures/users.json
python manage.py loaddata fixtures/blog.json

if [ "$ENVIRONMENT" = "development" ]
then
	python manage.py runserver 0.0.0.0:8000
else
	daphne -v 3 -e ssl:8000:privateKey=/certs/private.key:certKey=/certs/cert.pem conf.asgi:application
fi
