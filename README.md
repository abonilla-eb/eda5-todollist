# To Do List for EDA 5

## Docker image

To pull the image use
```
docker pull abonillaeb/eda5-todolist
```

### Environment variables

Django general environment variables

* DJANGO_SECRET_KEY: Django secret, used for csrf and others

  `DJANGO_SECRET_KEY=xxxxxxxxxxxxxxxxxxxxxxxxx`

* DJANGO_DEBUG: Set to anything to enable debug mode

  `DJANGO_DEBUG=1`

* DJANGO_ALLOWED_HOSTS: List of allowed hosts in Python format (is `eval`'ed in settings.py)

  `DJANGO_ALLOWED_HOSTS=['127.0.0.1', '129.168.1.30']`

Database environment variables (only PostgreSQL)

* DJANGO_DATABASE_HOST: Database host ip or name

  `DJANGO_DATABASE_HOST=127.0.0.1`

* DJANGO_DATABASE_NAME: Database name

  `DJANGO_DATABASE_NAME=eda5-todolist`

* DJANGO_DATABASE_USERNAME: Database login username

  `DJANGO_DATABASE_HOST=postgres`

* DJANGO_DATABASE_PASSWORD: Database password

  `DJANGO_DATABASE_HOST=password`
