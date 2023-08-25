python manage.py collectstatic --no-input
python manage.py migrate
python manage.py loaddata fixtures/cv.json \
	fixtures/users.json fixtures/blog.json
python manage.py test

if [ "$ENVIRONMENT" = "development" ]
then
	python manage.py runserver 0.0.0.0:8000
else
	daphne -v 3 -e ssl:8000:privateKey=/certs/private.key:certKey=/certs/cert.pem conf.asgi:application
fi
