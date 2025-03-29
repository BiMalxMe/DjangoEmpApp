#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():

# Yo chai main thau hoo project file structure ma
#yesle office_emp_proj bhanne company(Maneko).settings lai redirect garxa
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'office_emp_proj.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
