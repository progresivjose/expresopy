"""
Django settings for expresopy project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fxe7e!_ags7thj48h!wwck(1d(4zvh7ip%4l-fbu28b(=z+qff'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped.bootstrap3',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'news',
    'editorial',
    'cartoons',
    'blogs',
    'sorl.thumbnail',
    'taggit',
    'django_youtube',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'expresopy.urls'

WSGI_APPLICATION = 'expresopy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-ar'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates/'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
SOUTH_MIGRATION_MODULES = {
        'taggit': 'taggit.south_migrations',
    }

#YOUTUBE API
YOUTUBE_AUTH_EMAIL    = 'jmanuelgricart@gmail.com' 
YOUTUBE_AUTH_PASSWORD = 'etES20!1Castel' 
YOUTUBE_DEVELOPER_KEY = 'AI39si5wzATwFSBUd25hot_e3OkPvdBjvwr9Aq7RH37qFdcqU5O1CvPH5W-QPvsOp9DM8HdJztRa79KaYgk_AeQmUgphw1FRNA'
YOUTUBE_CLIENT_ID     = '90715320167-tb81a0a0mvn9tlcuv43qjgs9as0uukd0.apps.googleusercontent.com'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')