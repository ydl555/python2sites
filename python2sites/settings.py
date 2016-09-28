# -*- coding: utf-8 -*-
"""
Django settings for python2sites project.

Generated by 'django-admin startproject' using Django 1.8.14.
"""

from __future__ import unicode_literals
import os
try:
    from python2sites.settings_secret import *
except ImportError:
    pass

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ADMINS = (
    (u'Sahin Mersin', 'electrocoder@gmail.com'),
)

TO = [ email for name, email in ADMINS ]

SECRET_KEY = 'ju(83j8+3ol(dtn9^q05p1=fe)%x&pno2ci9#l^v*&n86ys(^g'

DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '188.166.48.117',
    '.python2sites.com',
    '.python2sites.com.',
]

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sorl.thumbnail',
    'chartit',

    'profiles',
    'sites',
    'tags',
)

THUMBNAIL_DEBUG = True
THUMBNAIL_QUALITY = 85

THUMBNAIL_FORCE_OVERWRITE = True

ACCOUNT_ACTIVATION_DAYS = 7

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'python2sites.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'python2sites.wsgi.application'


WEBSITE_NAME = "Python2Sites"
WEBSITE_URL =  "http://" + WEBSITE_NAME + ".com"
WEBSITE_DESCRIPTION = "Python 2 sites. Django, Flask,"
TWITTER_PROFILE = ""
FACEBOOK_PROFILE = ""
GOOG_PLUS_PROFILE = ""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'python2sites.sqlite3'),
    }
}

MEDIA_ROOT = os.path.join(BASE_DIR, '../python2sites_media/')
STATIC_ROOT = os.path.join(BASE_DIR, "../python2sites_static/")

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

SESSION_COOKIE_AGE = 100*60

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

STATICFILES_DIRS = (
                    BASE_DIR + '/static/',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

LOGIN_URL          = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL    = '/'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

emailmsg = (u"\nSend by %s") % WEBSITE_NAME
emailmsg += (u"\nThis summary is sent from %s when we haven't seen you in a while. ") % WEBSITE_NAME
emailmsg += (u"\n© 2016 %s") % WEBSITE_NAME
emailmsg += (u"\nHelp center · Privacy policy")
emailmsg += (u"\nUnsubscribe | info@%s") % WEBSITE_URL
