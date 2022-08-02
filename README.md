# restaurant_service
API service for restaurant management with Docker and PostgresSQL.

## Installing

Install PostgresSQL db and create db
```shell
git clone https://github.com/vasylhnatiuk/restaurant_service/git

python -m venv venv

venv/scripts/activate

pip install -r requirements.txt

set DB_HOST=<your db hostname>
set DB_NAME=<your db name>
set DB_USER=<your db username>
set DB_PASSWORD=<your db user password>
set SECRET_KEY=<your secret key>

python manage.py runserver
```
## Run with docker

Docker should be installed
```shell
docker-compose build
docker-compose up
```
## Getting access

create user on /api/user/register/

get access token on /api/user/token/

## Features

* User functionality and authorization.
* Managing menus and restaurants.
* Creating menu with dishes, drinks.
* Adding restaurant with associated menus.
* Filtering movies and movie sessions.
* Add current menu from admin
* Includes tests 
