import os
import sys

if __name__ == "__main__":
    sys.path.append("/opt/cbmonitor/") 
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webapp.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
