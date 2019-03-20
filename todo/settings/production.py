from todo.settings.base import *
import dj_database_url


APP_URL = os.environ.get('APP_URL', '')

DEBUG = os.environ.get('DEBUG', False)

ALLOWED_HOSTS = [APP_URL]

DATABASES['default'] = dj_database_url.config()