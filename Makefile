MANAGE=django-admin.py

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=src.someProject.settings $(MANAGE) test 

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=src.someProject.settings $(MANAGE) runserver

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=src.someProject.settings $(MANAGE) syncdb --noinput