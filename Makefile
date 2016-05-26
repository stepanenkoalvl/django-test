MANAGE=django-admin.py

test:
	PYTHONPATH=`pwd` $(MANAGE) test test1

run:
	PYTHONPATH=`pwd` $(MANAGE) runserver

syncdb:
	PYTHONPATH=`pwd` $(MANAGE) syncdb --noinput