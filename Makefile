MANAGE=django-admin

test:
syncdb:
	PYTHONPATH=`pwd`/src DJANGO_SETTINGS_MODULE=someProject.settings $(MANAGE) syncdb --noinput
	PYTHONPATH=`pwd`/src DJANGO_SETTINGS_MODULE=someProject.settings $(MANAGE) test

run:
	PYTHONPATH=`pwd`/src DJANGO_SETTINGS_MODULE=someProject.settings $(MANAGE) runserver

