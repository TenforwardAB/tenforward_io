from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&7tywb0-=fkn$ot-&xr3d04f(41@s(r@44a(6mij5xy_x%_p&a'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['127.0.0.1', '*']
INTERNAL_IPS = [
    '127.0.0.1'
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CSRF_USE_SESSIONS = True
CSRF_COOKIE_HTTPONLY = True

try:
    from .local import *
except ImportError:
    pass
