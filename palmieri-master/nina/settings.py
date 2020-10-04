"""
Django settings for nina project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#seti ID site
SITE_ID = 1 


ADMINS = (
    ('Orizio Pierangelo', 'pierangelo1982@gmail.com'),
)

MANAGERS = (
    'Orizio Pierangelo', 'pierangelo1982@gmail.com'),



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!%t1f_@3km+k_7)_8o$^yxf(7va_o5_^0_eex$2gj+jf53^)kn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


#TEMPLATE CONTEXT

'''
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request',

    )

'''

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'contact_form',
    'filer',
    #'django_social_share',
    'easy_thumbnails',
    'image_cropping',
    'taggit',
    'sito',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'nina.urls'

WSGI_APPLICATION = 'nina.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME': 'palmieriweb',
        'USER': 'root',
        'PASSWORD': 'xxxxxxxxx',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'it-IT'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

STATIC_URL = '/static/'

MEDIA_ROOT = '/home/pierangelo/Scrivania/palmieri/nina/media/'

MEDIA_URL = "http://127.0.0.1:8000/media/"

CKEDITOR_UPLOAD_PATH = "/home/pierangelo/Scrivania/palmieri/nina/media/ckedditor/uploads"

#Adjust the thumbnail processors for easy-thumbnails
from easy_thumbnails.conf import Settings as thumbnail_settings
THUMBNAIL_PROCESSORS = (
    #'easy_thumbnails.processors.colorspace',
    #'easy_thumbnails.processors.autocrop',
    ##'easy_thumbnails.processors.scale_and_crop',
    #'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    #'easy_thumbnails.processors.filters',
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS

###
IMAGE_CROPPING_THUMB_SIZE = (1425, 500)
#cropping = ImageRatioField('image', '1425x500', size_warning=True)
IMAGE_CROPPING_SIZE_WARNING = True



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'pierangelo1982@gmail.com'
EMAIL_HOST_PASSWORD = 'xxxxxxxxxxx'
DEFAULT_FROM_EMAIL = 'pierangelo1982@gmail.com'

#ckeditors
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full',
        'height': 400,
        'width': 800,
    },
}
