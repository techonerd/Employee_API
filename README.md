# Employee API
Basic API for employee data.

Steps to set-up:
 1. Clone this repo.
 2. Create python environment by using:
    python -m venv (your_environment_name)
 3. Install dependencies using:
    pip install -r requirements.txt
 4. Make migrations using:
    python manage.py makemigrations
    python manage.py migrate
 5. Create superuser using:
    python manage.py createsuperuser
 6. Run server:
    python manage.py runserver
  
If getting operationalerror run:
    python manage.py migrate --run-syncdb

 Environment variables:



    |  VARIABLE NAME  	|  DESCRIPTION  |
    |  DEBUG_VALUE      |  Debug value depending on dev or prod env |
    |  SECRET_KEY		|  Secret Key for the Django Application |

