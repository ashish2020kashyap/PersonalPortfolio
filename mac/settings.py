

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'et5o-+7y*y-&1!%lmo^!wii)qk$@qm2o@a!*87p^-$-9t_ddbl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['kumarashish.herokuapp.com',
                 '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio',
    'storages',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mac.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'mac.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pktqrdkz',
        'USER': 'pktqrdkz',
        'PASSWORD': '0N1YyJGaOy1FacuA_RSNnB_U_DtpIU4W',
        'HOST': 'suleiman.db.elephantsql.com',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST ='smtp.sendgrid.net'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
#EMAIL_HOST_USER ='ashish160kumar@gmail.com'
EMAIL_HOST_USER ='apikey'
EMAIL_HOST_PASSWORD ='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'
#EMAIL_HOST_PASSWORD ='ashishkashyap1@'

#'smtp.gmail.com'
#smtp.sendgrid.net



USING_S3 = True

if USING_S3:
    # AWS SETTINGS
    AWS_ACCESS_KEY_ID = 'AKIATKNI4ILQ67KU4562'
    AWS_SECRET_ACCESS_KEY = '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'
    AWS_STORAGE_BUCKET_NAME = 'portfolio2021'
    AWS_DEFAULT_ACL = 'public-read'
    AWS_S3_USE_SSL =False

    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

    # AWS S3 static settings
    STATIC_FOLDER = 'static'
    STATIC_ROOT = 'media'
    STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, STATIC_FOLDER)
    STATICFILES_STORAGE = 'mac.default_storages.StaticStorage'

    # AWS S3 public media settings
    MEDIA_FOLDER = 'media'
    MEDIA_ROOT = 'media/'
    MEDIA_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, MEDIA_FOLDER)
    DEFAULT_FILE_STORAGE = 'mac.default_storages.MediaStorage'
else:
    # IF WE ARE WORKING LOCALLY WITHOUT AWS
    STATIC_URL = 'static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    MEDIA_URL = 'media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_URL)




# ANY EXTRA STATIC FOLDERS THAT DJANGO SHOULD BE AWARE OF
STATICFILES_DIRS = []