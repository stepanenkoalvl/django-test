MANAGE=django-admin

test:
	PYTHONPATH=`pwd`/src DJANGO_SETTINGS_MODULE=someProject.settings $(MANAGE) makemigrations
	PYTHONPATH=`pwd`/src DJANGO_SETTINGS_MODULE=someProject.settings $(MANAGE) migrate
	PYTHONPATH=`pwd`/src DJANGO_SETTINGS_MODULE=someProject.settings $(MANAGE) test

run:
	PYTHONPATH=`pwd`/src DJANGO_SETTINGS_MODULE=someProject.settings $(MANAGE) runserver

