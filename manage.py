#!/usr/bin/env python
import os
import sys
import pymysql

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AutomaticTextSummarizer.settings")
    try:
        pymysql.install_as_MySQLdb()
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHON PATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
