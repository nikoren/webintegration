##Webintegration

- This is [django-rest-framework](http://www.django-rest-framework.org) application for HTTP based data
integration


### Installation

1. create python 3.4 virtualenv
2. Clone this repo
3. `pip install requirements.txt`
4. This app have to use `Postgres` db as backend storage for JSON fields, can't
 use `sqlite3`. Easy postgres installation docs are [here](https://postgresapp
 .com/documentation/install.html)
5. [Create db ](http://www.marinamele.com/taskbuster-django-tutorial/install-and-configure-posgresql-for-django#create-database)
6. [Update settings](http://www.marinamele.com/taskbuster-django-tutorial/install-and-configure-posgresql-for-django#settings)
7. Migrate

```bash
python manage.py makemigrations
python manage.py migrate

```
8.  Create superuser

```bash
python manage.py createsuperus
```


### Usage

1. python manage.py runserver
2. Navigate to  app root `http://127.0.0.1:8000/`
3. Django rest framework has built in borwsable api's , no http client required
4. Login as superuser, create chain, add steps to chain , add json data to steps