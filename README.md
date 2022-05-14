# testovoe_innowise_fixed
## Test task for innowise

First of all, you need to make next changes to .env file:

| Key | Value  |
| ------- | --- |
| DEBUG | 1(True) or 0(False) |
| SECRET_KEY | Secret key for Django |
| DJANGO_ALLOWED_HOSTS | Hosts that Django site can serve | 
| SQL_DATABASE | Name of your database |
| SQL_USER | Username of database user |
| SQL_PASSWORD | Password from database |
| SQL_HOST | Usually db |
| SQL_PORT | Usually 5432 |
| EMAIL_USE_TLS | True or False|
| EMAIL_USE_SSL | True or false |
| EMAIL_HOST | Your email host |
| EMAIL_PORT | Your email port |
| EMAIL_HOST_USER| Your email adress |
| EMAIL_HOST_PASSWORD| Password from your email account |

For first time run next commands:

```
docker-compose up -d --build
```

```
docker-compose exec web python manage.py makemigrations
```

```
docker-compose exec web pythoon manage.py migrate
```
To stop container:

```
docker-compose down
```

To run container again

```
docker-compose up 
```
