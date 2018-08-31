"""
Django settings for ToyShop project.

Generated by 'django-admin startproject' using Django 1.11.15.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd_2u_u^im&sb*6kze9u7f@+h4t##(+7i7@_2v445$a30bahki%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = []


# Application definition
#ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; you may, of course, use a different value.
#REGISTRATION_AUTO_LOGIN = True # Automatically log the user in.

INSTALLED_APPS = [
    'ToyShop',
    'LogicApp',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'registration',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Client',
]


ALLOWED_HOSTS = ['*']

SECRET_KEY = '_'

SITE_ID = 1
"""
ROOT_URLCONF = 'LogicApp.urls_default'
"""

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ToyShop.urls'

TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
TEMPLATE_LOGIC_APP_DIR = 'LogicApp/templates'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,TEMPLATE_LOGIC_APP_DIR,],
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

WSGI_APPLICATION = 'ToyShop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    os.path.join('ToyShop', "static"),
]


"""
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'testing@example.com'#'armgcppgcc@gmail.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
EMAIL_PORT = 1025
REGISTRATION_OPEN = True
SIMPLE_BACKEND_REDIRECT_URL = "home"
"""
"""
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_EMAIL_SUBJECT_PREFIX = '[Django Registration Test App]'
SEND_ACTIVATION_EMAIL = True
REGISTRATION_AUTO_LOGIN = False

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGIN_REDIRECT_URL = "home"
"""

REGISTRATION_OPEN  =  True                 # Если True, пользователи могут зарегистрировать
ACCOUNT_ACTIVATION_DAYS  =  7      # Однонедельное окно активации; вы, конечно, можете использовать другое значение.
REGISTRATION_AUTO_LOGIN  =  True   # Если True, пользователь будет автоматически войти в систему.
LOGIN_REDIRECT_URL  =  "home"   # Страница, которую вы хотите, чтобы пользователи пришли после успешного входа в систему
LOGIN_URL  =  '/accounts/login/'   # Пользователи страницы если они не вошли в систему,
                                                                # и пытаются получить доступ к страницам, требующим аутентификации
