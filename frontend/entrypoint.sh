if [ "$ENVIRONMENT" = "development" ]
then
    npm run serve
else
    nginx -g daemon off;
fi