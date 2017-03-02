"""
Django settings for ecigshop project.

Generated by 'django-admin startproject' using Django 1.8.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from oscar.defaults import *
from oscar import OSCAR_MAIN_TEMPLATE_DIR
from oscar import get_core_apps
##from oscarapi.app import application as api

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!5&jsq9yq^1m(pld%q0=s*eui$*lsu99vvhig(uob0hm7cof2='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'widget_tweaks',
	'ecigshop',
	##'oscarapi'
]

INSTALLED_APPS = INSTALLED_APPS + get_core_apps([
	"""
    'ecigshop.address', 'ecigshop.analytics', 'ecigshop.basket', 'ecigshop.catalogue', 'ecigshop.catalogue.reviews', 
    'ecigshop.checkout', 'ecigshop.customer', 'ecigshop.offer', 'ecigshop.order', 'ecigshop.partner', 'ecigshop.payment', 
	'ecigshop.promotions', 'ecigshop.search', 'ecigshop.shipping', 'ecigshop.voucher', 'ecigshop.wishlists', 
	'ecigshop.dashboard', 'ecigshop.dashboard.catalogue', 'ecigshop.dashboard.communications', 'ecigshop.dashboard.orders', 
	'ecigshop.dashboard.pages', 'ecigshop.dashboard.partners', 'ecigshop.dashboard.promotions', 'ecigshop.dashboard.reports', 
	'ecigshop.dashboard.users', 'ecigshop.dashboard.offers', 'ecigshop.dashboard.ranges', 'ecigshop.dashboard.reviews', 
	'ecigshop.dashboard.shipping', 'ecigshop.dashboard.vouchers'
    """
    'oscar.apps.address', 'oscar.apps.analytics', 'oscar.apps.basket', 'oscar.apps.catalogue', 'oscar.apps.catalogue.reviews', 
    'oscar.apps.checkout', 'oscar.apps.customer', 'oscar.apps.dashboard', 'oscar.apps.dashboard.communications', 
    'oscar.apps.dashboard.orders', 'oscar.apps.dashboard.pages', 'oscar.apps.dashboard.partners', 'oscar.apps.dashboard.promotions', 
    'oscar.apps.dashboard.reports', 'oscar.apps.dashboard.users', 'oscar.apps.dashboard.catalogue', 'oscar.apps.dashboard.offers', 
    'oscar.apps.dashboard.ranges', 'oscar.apps.dashboard.reviews', 'oscar.apps.dashboard.shipping', 'oscar.apps.dashboard.vouchers', 
    'oscar.apps.offer', 'oscar.apps.order', 'oscar.apps.partner', 'oscar.apps.payment', 'oscar.apps.promotions', 'oscar.apps.search', 
    'oscar.apps.shipping', 'oscar.apps.voucher', 'oscar.apps.wishlists'
	
])

#INSTALLED_APPS = INSTALLED_APPS + get_core_apps(['oscar.apps.catalogue', 'oscar.apps.dashboard'])
#INSTALLED_APPS = INSTALLED_APPS + get_core_apps(['oscar.apps.catalogue'])

SITE_ID = 1


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',    
)

ROOT_URLCONF = 'ecigshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            OSCAR_MAIN_TEMPLATE_DIR
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.promotions.context_processors.promotions',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.customer.notifications.context_processors.notifications',                
            ],
        },
    },
]

WSGI_APPLICATION = 'ecigshop.wsgi.application'

AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.ecigshop'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'ATOMIC_REQUESTS': True,
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
