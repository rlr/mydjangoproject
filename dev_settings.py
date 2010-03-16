CACHE_BACKEND = 'locmem:///'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = '*@gmail.com'
EMAIL_HOST_PASSWORD = '*'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
#    'debug_toolbar.middleware.DebugToolbarMiddleware',
)


