"""
Django settings for lwc project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
print BASE_DIR
# print "base dir is " + BASE_DIR +"/templates/"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j-o1w!_ioc9mcitalt0(mcjtaa7$057-$)652ng907(l4)2fzc'

    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'newsletter',
    'joins',
    'south',
 
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'lwc.middleware.ReferMiddleware',
)

ROOT_URLCONF = 'lwc.urls'

WSGI_APPLICATION = 'lwc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
    import dj_database_url
    DATABASES['default'] =  dj_database_url.config()
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# SHARE_URL="http://127.0.0.1:8000/?ref="
 
TEMPLATE_DIRS={
# BASE_DIR +"/templates/",
 '/home/shaks/Desktop/lwc/scr/templates/',

     
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
 
STATIC_URL = '/static/'

# STATIC_ROOT ="/Desktop/lwc/scr/static/static_root/"
STATIC_ROOT =os.path.join(BASE_DIR,'static','static_root')

STATICFILES_DIRS=(
    os.path.join(BASE_DIR,'static','static_dirs'),
    # '/Desktop/lwc/scr/static/static_dirs/',

) 

# MEDIA_ROOT='/Desktop/lwc/scr/static/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'static','media'),

MEDIO_URL='/media/'


    