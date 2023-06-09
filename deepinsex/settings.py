"""
Django settings for deepinsex project.

Generated by 'django-admin startproject' using Django 3.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-55z-+g@1@wex_=mm1j_-4f+62*j(b8r2g!x9ah_(t5z&twp)mt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
    "18.233.140.125",
    "www.deepinsex.com",
    "deepinsex.com", 
    "localhost",
]


# Application definition

INSTALLED_APPS = [
    # 'django.contrib.admin',
    'deepinsex.custom_admin.CustomAdminConfig',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "paypal.standard.ipn",
    "paypal.standard.pdt",
    'core',
    'users',
    'videos',
    "payments",
    "subscriptions"
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

ROOT_URLCONF = 'deepinsex.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'deepinsex.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres', 
        'USER': 'postgres', 
        'PASSWORD': 'postgres',
        'HOST': 'deepinsex-db.cab1qtgx65v0.us-east-1.rds.amazonaws.com', 
        'PORT': '5432',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# AWS S3 CONFIGURATION
AWS_ACCESS_KEY_ID = 'AKIA3P5BQUSEOSL5YKUL'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'deepinsex'
AWS_DEFAULT_ACL = None

AWS_S3_REGION = 'us-west-1'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3-{AWS_S3_REGION}.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=31536000'}

# s3 static settings
AWS_LOCATION = 'static'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
STATICFILES_STORAGE = 'deepinsex.s3_storage.StaticStorage'
# STATIC_ROOT = 'static'
# STATIC_URL = '/static/'

# s3 public media settings
PUBLIC_MEDIA_LOCATION = 'media'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
DEFAULT_FILE_STORAGE = 'deepinsex.s3_storage.PublicMediaStorage'

# s3 private media settings
PRIVATE_MEDIA_LOCATION = 'private'
PRIVATE_FILE_STORAGE = 'deepinsex.s3_storage.PrivateMediaStorage'


# AWS ELASTIC TRANSCODER - CONFIGURATION
PIPELINE_ID = '1655709459722-ysecju'
OUTPUT_FILE_PREFIX = 'media/transcoded-videos/'

# CSRF
# CSRF_TRUSTED_ORIGINS = ['']


# PAYPAL - CONFIGURATION
PAYPAL_TEST = False

PAYPAL_RECEIVER_EMAIL = 'jaynovakhb@gmail.com'



PAYPAL_IDENTITY_TOKEN = "k2mxVvZFrt4Awzq6nmOYl8k_-WaZiPcOjdeB8RuSyxXSYLR6mjTSfjcY9UO"
