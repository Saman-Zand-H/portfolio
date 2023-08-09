if [ "$ENVIRONMENT" != "development" ]
then
    nginx -g daemon off;
else
    npm run serve
fi