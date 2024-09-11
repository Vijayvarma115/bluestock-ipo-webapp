Follow these command to run this project:

git clone https://github.com/Vijayvarma115/bluestock-ipo-webapp.git

cd bluestock-ipo-webapp

pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver



How to connect a Django application to your PostgreSQL database

## Setting Up PostgreSQL Database

1. **Install PostgreSQL:**

   Make sure PostgreSQL is installed on your system. You can download it from the official [PostgreSQL website](https://www.postgresql.org/download/).

2. **Create a PostgreSQL Database and User:**

   Once PostgreSQL is installed, create a new database and a user for your Django application. You can do this using the PostgreSQL command-line interface (`psql`) or a graphical tool like pgAdmin.

   Open your terminal and run the following commands:


CREATE DATABASE bluestock;
CREATE USER daiyanalam WITH PASSWORD '12345';
ALTER ROLE daiyanalam SET client_encoding TO 'utf8';
ALTER ROLE daiyanalam SET default_transaction_isolation TO 'read committed';
ALTER ROLE daiyanalam SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE bluestock TO daiyanalam;



Install PostgreSQL Adapter for Python

pip install psycopg2-binary



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bluestock',
        'USER': 'daiyanalam',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

Apply Migrations:
-->python3 manage.py makemigrations

-->python3 manage.py migrate

-->python3 manage.py runserver

**Follow these video link how to connect with postgresql:**

https://drive.google.com/file/d/1jUYqTqp_CTMRYu6FKNIT5327IPQh0fYk/view?usp=sharing

