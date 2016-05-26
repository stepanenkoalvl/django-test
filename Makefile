MANAGE=django-admin.py

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=django-test.src.someProject.settings $(MANAGE) test test1

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=django-test.src.someProject.settings $(MANAGE) runserver

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=django-test.src.someProject.settings $(MANAGE) syncdb --noinput