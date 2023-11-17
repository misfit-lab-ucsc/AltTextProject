# AltTextProject

## Development

First, install necessary packages using `pip install -r requirements.txt`.

Running the project locally: `python manage.py runserver`

Create a superuser account for the Django MyAdmin: `python manage.py createsuperuser`

For database API local debugging: `python manage.py shell`

Update the database configuration:

`python manage.py makemigrations`

`python manage.py migrate`

Collect static files for deployment: `python manage.py collectstatic`