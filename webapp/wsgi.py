import os
import sys 
sys.path.append("/opt/cbmonitor/") 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webapp.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
