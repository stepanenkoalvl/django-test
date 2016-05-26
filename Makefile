MANAGE=django-admin

syncdb:
	PYTHONPATH=`pwd`/src DJANGO_SETTINGS_MODULE=someProject.settings $(MANAGE) syncdb --noinput

test:
	PYTHONPATH=`pwd`/src DJANGO_SETTINGS_MODULE=someProject.settings $(MANAGE) test

run:
	PYTHONPATH=`pwd`/src DJANGO_SETTINGS_MODULE=someProject.settings $(MANAGE) runserver

