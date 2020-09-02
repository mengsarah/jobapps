# Job Application Tracker
My head is spinning with how much I need to keep track of, so I decided to make something specifically for tracking where I am in my various job applications.

## About
This is a local single-page web app for keeping track of job applications.

I'm trying to build this with the basics of accessibility and good UX practices that I know in mind. I'm still learning more.

Full functionality currently requires JavaScript. I haven't built fallbacks for the JS features yet, but I plan to. The JS features are:
1. The AJAX requests for company contacts and info
2. Showing and hiding forms, supplemental information, etc.

## How to use
1. Install Python.
2. Install [Django](https://docs.djangoproject.com/en/3.1/intro/install/).
3. Clone this repo.
4. Open your terminal/command line and `cd` into the repo.
5. You may need to make migrations. I use Windows Command Line, so my commands are `python manage.py makemigrations` and `python manage.py migrate`. Run your equivalents.
6. Start the web app with your equivalent of `python manage.py runserver`.
7. Visit http://127.0.0.1:8000/tracker/.
8. [Create a superuser account](https://docs.djangoproject.com/en/3.0/intro/tutorial02/#introducing-the-django-admin) if item details need to be changed that can't be changed otherwise.

The database used for this repo is SQLite, which should come with your Python installation.

## To do
* fallbacks for no JS
* add easier way to modify existing information without having to go into the Django admin panel