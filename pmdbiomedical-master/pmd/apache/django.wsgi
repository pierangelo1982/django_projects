import os
import sys
import site


paths = [ '/var/www/pmdbox/pmd/',
          '/var/www/pmdbox/pmd/',
          '/var/www/pmdbox/lib/python2.7/site-packages/',
]

for path in paths:
    if path not in sys.path:
        sys.path.append(path)


# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/var/www/peabox/lib/python2.7/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/var/www/pmdbox')
sys.path.append('/var/www/pmdbox/pmd')

os.environ['DJANGO_SETTINGS_MODULE'] = 'pmd.settings'

# Activate your virtual env
activate_env=os.path.expanduser("/var/www/pmdbox/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()