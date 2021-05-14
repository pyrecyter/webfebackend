"""
Django settings for Cl_beautesoft project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import calendar
from django.utils import timezone

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0hvkn)58&z=%mogc(sz!324jk5-g4pp*8q=7$g(g7lvb3b(^hf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['52.60.58.9','127.0.0.1','103.253.15.184']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'django_crontab',
    'mathfilters',
    'corsheaders',
    'cl_table',
    'cl_app',
    'custom',
]

MIDDLEWARE = [
    'Cl_beautesoft.middleware.open_access_middleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'cl_table.middleware.OneSessionPerUserMiddleware',
]

ROOT_URLCONF = 'Cl_beautesoft.urls'

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

WSGI_APPLICATION = 'Cl_beautesoft.wsgi.application'

CRONJOBS = [
    # ('1 8 * * *', 'cl_table.cron.token_create_job', '>> /home/monica/Doodle_Project/backend_beautesoft/tokcron.log')
    #('0 8 * * *', 'cl_table.cron.token_create_job')

]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

#postgres
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'beautesoft_db',
#         'USER': 'admin',
#         'PASSWORD': 'Doodle@123',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# #microsoft sql client server
# DATABASES = {
#     'default': {
#         'ENGINE': 'sql_server.pyodbc',
#         'NAME': 'BioSkin_TPN_Tampines_20200904',
#         'HOST': 'sequoiademo.ddns.net',
#         'PORT': '1435',
#         'USER': 'sa',
#         'PASSWORD': 'bigtree',
#         'OPTIONS': {
#             'driver': 'ODBC Driver 17 for SQL Server',
#         }
#     }
# }

# #microsoft sql local server
# DATABASES = {
#     'default': {
#         'ENGINE': 'sql_server.pyodbc',
#         'NAME': 'healspahq_backup9',
#         # 'HOST': 'localhost',
#         'HOST': '103.253.15.184',
#         'PORT': '1433',
#         'USER': 'sa',
#         'PASSWORD': 'Doodle@123',
#         'OPTIONS': {
#             'driver': 'ODBC Driver 17 for SQL Server',
#         }
#     }
# }

# msSQL demo db
DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'MidysonTrain',
        'HOST': '103.253.15.184',
        'PORT': '1433',
        'USER': 'sa',
        'PASSWORD': 'Doodle@123',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        }
    }
}

#mysql
# DATABASES =  {
#         'default': {
#             'ENGINE': 'django.db.backends.mysql',
#             'NAME': 'beautesoft_db',
#             'USER': 'root',
#             'PASSWORD': 'Doodle@123',
#             'HOST': '127.0.0.1',
#             'PORT': '3306',
#         }
#     }

REST_FRAMEWORK = {
   'DEFAULT_AUTHENTICATION_CLASSES': (
       'rest_framework.authentication.TokenAuthentication',
   ),
   'DEFAULT_AUTHENTICATION_CLASSES': (
        'cl_table.authentication.ExpiringTokenAuthentication',  # custom authentication class
    ),
   'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
   ),
   'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']

}
  


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
#TIME_ZONE =  'Asia/Calcutta'
TIME_ZONE = 'Asia/Singapore'

USE_I18N = True

USE_L10N = True

#USE_TZ = True
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
PDF_ROOT = MEDIA_ROOT + '/pdf/'

# CORS Settings
CORS_ALLOW_METHODS =['DELETE','GET','OPTIONS','PATCH','POST','PUT',]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8000',
    # 'http://3.6.59.208',
    
)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_PORT = 587
EMAIL_HOST_USER = 'monica.b@doodleblue.com'
EMAIL_HOST_PASSWORD = 'MonicaBhass$05'

SMS_SECRET_KEY = "JBSWY3DPEHPK3VAG"
SMS_ACCOUNT_SID = 'AC2d4568886585462a8f7dbd240e09dc7c'
SMS_AUTH_TOKEN = '55774b4bfa51688df9380670a364423a'
SMS_SENDER = "+12097193857"

# LOGIN_URL = '/api/login/'
# LOGIN_REDIRECT_URL='/api/login/'

TOKEN_EXPIRED_AFTER_HOURS = 24

path = os.getcwd()
paths = path+'/log'

today = timezone.now().date()
month = today.strftime('%B')
year = today.strftime('%Y')

directory = month+"_"+year
month_folder = paths+'/'+directory
try:
    os.mkdir(month_folder)
except OSError:
    pass
    # print("%s Folder already exists" % month_folder)
else:
    pass
    # print("%s Successfully created" % month_folder)

# month_no = (today.strftime('%m')).lstrip('0')
# count = calendar.monthrange(int(year),int(month_no))
# backupCount = count[1]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s',
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class':  'logging.handlers.TimedRotatingFileHandler',
            'filename': month_folder +'/debug.log',
            'when': 'D', #D
            'interval': 1, #1
            'backupCount': 31, #31 
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}