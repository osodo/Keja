# Keja

## Linux
## Requirements
* Python 3.6
* virtualenv
* Django 2.0.1 and above
* Text editor :joy: :joy:
* Requirements file for additional python packages

## Installation
* virtualenv -p /usr/bin/python3.6 --no-site-packages { **folder name eg Keja** }
* cd { **folder name eg Keja** }
* source bin/activate
* git clone [GitHub Repository](https://github.com/osodo/Keja)
* cd Keja
* inside the airbnb/settings.py file remove the line **import secrets as s**
* change the following lines
	###### Email configurations
	* EMAIL_HOST = s.os.environ["EMAIL_HOST"]
	* EMAIL_HOST_USER = s.os.environ["EMAIL_HOST_USER"]
	* EMAIL_HOST_PASSWORD = s.os.environ["EMAIL_HOST_PASSWORD"]
	* EMAIL_PORT = s.os.environ["EMAIL_PORT"]
	* EMAIL_USE_TLS = True

	###### Email configurations
	* EMAIL_HOST = "smtp.gmail.com"
	* EMAIL_HOST_USER = your email address
	* EMAIL_HOST_PASSWORD = your email password
	* EMAIL_PORT = "587"
	* EMAIL_USE_TLS = True

* then generate a 50 length key
* pip install -r Requirements.txt
* python manage.py makemigrations
* python manage.py migrate
* python manage.py createsuperuser
* python manage.py collectstatic
> add a user, caretaker and house through the admin panel atleast 5
* python manage.py runserver 8080
