MANAGE=django-admin.py

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=test1.settings $(MANAGE) test test1

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=test1.settings $(MANAGE) runserver

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=test1.settings $(MANAGE) syncdb --noinput