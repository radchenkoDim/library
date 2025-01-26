from .settings_base import *
import os
from pathlib import Path

#DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ["PGDATABASE"],
        "USER": os.environ["PGUSER"],
        "PASSWORD": os.environ["PGPASSWORD"],
        "HOST": os.environ["PGHOST"],
        "PORT": os.environ["PGPORT"],
    }
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ["EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD = os.environ["EMAIL_HOST_PASSWORD"]
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

# import certifi, os
# os.environ['SSL_CERT_FILE'] = certifi.where()

FILES_VOLUME_PATH = Path(os.environ["FILES_VOLUME_PATH"])

MEDIA_ROOT = FILES_VOLUME_PATH / "media"
STATIC_ROOT = FILES_VOLUME_PATH / 'staticfiles'
