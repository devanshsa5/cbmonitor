build:
	virtualenv -p python3.7 env
	env/bin/pip install --cache-dir /tmp/pip -r requirements.txt

clean:
	rm -f `find . -name *.pyc`

flake8:
	env/bin/flake8 webapp

run:
	env/bin/python webapp/manage.py makemigrations
	env/bin/python webapp/manage.py migrate
	env/bin/python webapp/manage.py runserver 0.0.0.0:8000

restart:
	env/bin/python webapp/manage.py makemigrations
	env/bin/python webapp/manage.py migrate --run-syncdb
	chmod a+rw /tmp/cbmonitor.sock
	systemctl restart emperor.uwsgi.service
	nginx -s reload
