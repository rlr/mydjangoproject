DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASE_ENGINE = 'postgresql_psycopg2'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'db_*'             # Or path to database file if using sqlite3.
DATABASE_USER = 'pg_*'             # Not used with sqlite3.
DATABASE_PASSWORD = '*'         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

CACHE_BACKEND =    'memcached://127.0.0.1:11211'
CACHE_MIDDLEWARE_SECONDS = 60 * 60
CACHE_MIDDLEWARE_KEY_PREFIX = '*'                  
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

DEFAULT_FROM_EMAIL = ''
EMAIL_SUBJECT_PREFIX = ''

MEDIA_URL = 'http://*.com/media/*/'
ADMIN_MEDIA_PREFIX = '/media/admin/'