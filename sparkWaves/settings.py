"""
Django settings for sparkWaves project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import socket
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

if socket.gethostname().startswith('Rick'):
    LIVEHOST = False
else:
    LIVEHOST = True

if LIVEHOST == False:
    from sparkWaves.private_settings import SECRET_KEY, SENDGRID_PASSWORD, SUPER_USER_EMAIL, SUPER_USER_NAME, SUPER_USER_PASSWORD, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
    os.environ['SECRET_KEY'] = str(SECRET_KEY)
    os.environ['SENDGRID_PASSWORD'] = str(SENDGRID_PASSWORD)
    os.environ['SUPER_USER_EMAIL'] = str(SUPER_USER_EMAIL)
    os.environ['SUPER_USER_NAME'] = str(SUPER_USER_NAME)
    os.environ['SUPER_USER_PASSWORD'] = str(SUPER_USER_PASSWORD)
    os.environ['AWS_ACCESS_KEY_ID'] = str(AWS_ACCESS_KEY_ID)
    os.environ['AWS_SECRET_ACCESS_KEY'] = str(AWS_SECRET_ACCESS_KEY)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']


# SECURITY WARNING: don't run with debug turned on in production!
if LIVEHOST == False:
    DEBUG = True
    TEMPLATE_DEBUG = True
else:
    DEBUG = True
    TEMPLATE_DEBUG = True


ALLOWED_HOSTS = ['sparkWaves-env-apg22ebmpm.elasticbeanstalk.com']

SITE_ID = 1

# Application definition


DEFAULT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sites',
)

THIRD_PARTY_APPS = (
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth.registration',
    'allauth',
    'allauth.account',
    'corsheaders',
)

LOCAL_APPS = (
    'profiles',
)


INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'sparkWaves.urls'

WSGI_APPLICATION = 'sparkWaves.wsgi.application'


# CORS settings
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = (
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken',
    'If-Modified-Since',
)

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
if LIVEHOST:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'static')
STATIC_URL = '/static/'

FIXTURE_DIRS = (os.path.join(BASE_DIR, 'fixtures'),)


# Rest framework settings

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'PAGINATE_BY': 10,
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}

#Auth settings:
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=2),
    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=3),
}
