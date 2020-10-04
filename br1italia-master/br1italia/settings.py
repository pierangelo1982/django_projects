"""
Django settings for br1italia project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))




ADMINS = (
    ('Name surname', 'your@email.com'),

)

MANAGERS = (
    ('Name surname', 'pierangelo1982@gmail.com'),
)



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'xxxxx'
EMAIL_HOST_PASSWORD = 'xxxxxx'
DEFAULT_FROM_EMAIL = 'xxxxxxx'
CONTACT_RECIPIENTS = False

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vwa)hhh%85ml(b_!0d_!1&ys60y4+9%9a-s7^fx-^&r74to((4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['www.br1italia.it',
		'test.br1italia.it']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'easy_thumbnails',
    'image_cropping',
    'sito',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'br1italia.urls'

WSGI_APPLICATION = 'br1italia.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'xxxxxxxx',
        'USER': 'xxxxxx',
        'PASSWORD': 'xxxxx',
        'HOST': 'db',
        'PORT': '3306',
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
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATICFILES_DIRS = (
    #os.path.join(BASE_DIR, "static"),
    '/code/static/',
)

#STATICFILES_DIRS = ()

STATIC_ROOT = '/code/'

STATIC_URL = '/static/'

MEDIA_ROOT = '/code/media/'

#MEDIA_URL = "http://www.br1italia.it/media/"
MEDIA_URL = "http://127.0.0.1:8000/media/"
#MYDIR = "http://www.br1italia.it"
MYDIR = "http://127.0.0.1:8000"
#TEMPLATE_DIRS = "/var/www/vhosts/vps93689.ovh.net/br1italia.it/br1italiabox/br1italia/sito/templates"



from easy_thumbnails.conf import Settings as thumbnail_settings
THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS

###
IMAGE_CROPPING_THUMB_SIZE = (1425, 500)

IMAGE_CROPPING_SIZE_WARNING = True
