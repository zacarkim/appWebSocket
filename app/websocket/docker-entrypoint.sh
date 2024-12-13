#!/bin/bash

# echo "Flush the manage.py command it any"

# while ! python manage.py flush --no-input 2>&1; do
#   echo "Flusing django manage command"
#   sleep 3
# done

echo "Makemigrations the Database at startup of project"

# Wait for few minute and run db migraiton
while ! python manage.py makemigrations --no-input 2>&1; do
   echo "Makemigrations is in progress status"
   sleep 3
done

echo "Migrate --run-syncdb the Database at startup of project"

# Wait for few minute and run db migraiton
while ! python manage.py migrate --run-syncdb  2>&1; do
   echo "Migration --run-syncdb is in progress status"
   sleep 3
done

echo "Migrate the Database at startup of project"

# Wait for few minute and run db migraiton
while ! python manage.py migrate  2>&1; do
   echo "Migration is in progress status"
   sleep 3
done

# Wait for few minute and run collectstatic
while ! python manage.py collectstatic --no-input  2>&1; do
   echo "Collectstatic is in progress status"
   sleep 3
done

echo "Create a superuser ADMIN"
while ! python manage.py createdefaultsuperuser --user "$DJANGO_ADMIN_USER" --password "$DJANGO_ADMIN_PASSWORD" --email "$DJANGO_ADMIN_EMAIL" 2>&1; do
   echo "Create superuser is in progress status"
   sleep 3
done

echo "Django docker is fully configured successfully."

# echo "Starting server"
# python manage.py runserver 0.0.0.0:$APP_EXPOSE

# daphne -p $DJANGO_PORT_EXPOSE -b 0.0.0.0 websocket.asgi:application

exec "$@"