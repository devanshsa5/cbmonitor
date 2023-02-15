build:
	virtualenv -p python3 env
	env/bin/pip install --cache-dir /tmp/pip -r requirements.txt

clean:
	rm -f `find . -name *.pyc`

flake8:
	env/bin/flake8 webapp

run:
	env/bin/python webapp/manage.py makemigrations
	env/bin/python webapp/manage.py migrate
	env/bin/python webapp/manage.py migrate --run-syncdb
	env/bin/python webapp/manage.py runserver 0.0.0.0:8000

runfcgi:
	kill `cat /tmp/cbmonitor.pid` || true
	env/bin/python webapp/manage.py makemigrations
	env/bin/python webapp/manage.py migrate
	env/bin/python webapp/manage.py migrate --run-syncdb
	env/bin/python webapp/manage.py runfcgi \
		method=prefork \
		maxchildren=8 \
		minspare=2 \
		maxspare=4 \
		outlog=/tmp/cbmonitor.stdout.log \
		errlog=/tmp/cbmonitor.stderr.log \
		socket=/tmp/cbmonitor.sock \
		pidfile=/tmp/cbmonitor.pid
	chmod a+rw /tmp/cbmonitor.sock
	nginx -s reload
