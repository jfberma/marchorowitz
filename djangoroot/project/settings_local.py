"""
This is an AUTOMATICALLY GENERATED file.
!!! DO NOT EDIT MANUALLY !!!
"""

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'marchorowitz',                    # Or path to database file if using sqlite3.
        'USER': 'jeremyberman',                    # Not used with sqlite3.
        'PASSWORD': '',                # Not used with sqlite3.
        'HOST': 'localhost',                    # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                    # Set to empty string for default. Not used with sqlite3.
    }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'sd-2a9s2df242as-df-#a-42y-z+hhi+71ge9bq=9@bz(!=d)expfk7w&t9#59i0!6e&'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/Users/jeremyberman/git/MarcHorowitz/var/static/'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/Users/jeremyberman/git/MarcHorowitz/var/uploads/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/Users/jeremyberman/git/MarcHorowitz/src/project/assets',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/Users/jeremyberman/git/MarcHorowitz/src/project/templates',
)

AUTH_USER_MODEL = 'core.User'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'gunicorn',
    'south',
    'django_extensions',
    'project',
    'project.core',
)
