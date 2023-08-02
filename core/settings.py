"""
Django 4.0.3
"""

from pathlib import Path


SITE_ID = 1
DEBUG = True
ALLOWED_HOSTS = ['*']
DEFAULT_PAGINATION_NUMBER = 10
SECRET_KEY = 'django-insecure-_#vlwynmvk@wa-=jhvic-+$hz*dm(9afgyt+*+27$7sz6+=@)e'
BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'lavu2809@gmail.com'
EMAIL_HOST_PASSWORD = 'jlemtpvlfplmywcx'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
URL_PASSWORD_RESET = '/accounts/password/reset/'
RESTRICTED_SETTING_KEYS = [
    'SECRET_KEY', 'EMAIL_HOST_PASSWORD',
    'MARTOR_IMGUR_CLIENT_ID', 'MARTOR_IMGUR_API_KEY',
    'RECAPTCHA_PUBLIC_KEY', 'RECAPTCHA_PRIVATE_KEY',
]


# Martor Configuration
MARTOR_THEME = 'bootstrap'  
MARTOR_IMGUR_CLIENT_ID = 'd2a49e1427aef40'
MARTOR_IMGUR_API_KEY = '2b619c0393aa86f1b301a82aef3ba8cf6b42cbf2'
MARTOR_ENABLE_CONFIGS = {
    'emoji': 'true',       
    'imgur': 'true',        
    'mention': 'false',     
    'jquery': 'true',       
    'living': 'false',     
    'spellcheck': 'false',  
    'hljs': 'true',
    'heading' : 'true'
}



# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',

    # 3d party apps
    'captcha',
    'martor',
    'updown',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'allauth',
    'allauth.account',
    'rest_auth',
    'rest_auth.registration',
    'django_filters',

    # major apps
    'apps.accounts',
    'apps.blog',
]


MIDDLEWARE = [
    # custom middleware
    'corsheaders.middleware.CorsMiddleware',

    # default middleware
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',

    
    
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
            BASE_DIR / 'templates/allauth',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # Enable {{ STATIC_URL }} and {{ MEDIA_URL }}
                'django.template.context_processors.media',
                'django.template.context_processors.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pydb',
        'USER': 'leanhvu',
        'PASSWORD': 'levu1832002',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Cache
# https://docs.djangoproject.com/en/4.0/topics/cache/
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}


# Custom Auth User Model
AUTH_USER_MODEL = 'accounts.User'
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

    # custom auth backend
    'core.utils.backends.CustomAuthBackend'
]


# Auth and allauth settings
ACCOUNT_FORMS = {
    'signup': 'apps.accounts.forms.auth.SignUpForm',
    'login': 'apps.accounts.forms.auth.LoginForm',
    'reset_password': 'apps.accounts.forms.auth.ResetPasswordForm'
}


EMAIL_REQUIRED = True  # allauth
LOGIN_REDIRECT_URL = '/'
SOCIALACCOUNT_QUERY_EMAIL = True
ACCOUNT_EMAIL_REQUIRED = True



# Django Rest Framework Configuration
# https://www.django-rest-framework.org
REST_AUTH_EXPIRATION_DAYS = 365  # 1 year
REST_FRAMEWORK = {
    # 'DEFAULT_THROTTLE_RATES': {
    #     'anon': '10000/day',
    #     'user': '10000/day'
    # },
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        # 'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'rest_framework.filters.SearchFilter',
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
    'EXCEPTION_HANDLER': 'core.utils.handler.custom_exception_handler',
    'DEFAULT_PAGINATION_CLASS': 'core.utils.paginator.RestPagination',
    'PAGE_SIZE': 20 if DEBUG else 50
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/
LANGUAGES = (
    ('en', 'English'),
    ('fr', 'France')
)
DEFAULT_LANGUAGE = 1
LOCALE_PATHS = (
    BASE_DIR / 'locale',
    BASE_DIR / 'locale/rest_auth',
)
LANGUAGE_CODE = 'en'
USE_I18N = True
USE_L10N = True


# handle in computer machine, not in this django app
# sudo timedatectl set-timezone Asia/Jakarta
TIME_ZONE = 'Asia/Jakarta'
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
# If you want to run `./manage.py collectstatic`, please following this:
# 1. un-comment `STATIC_ROOT` and comment `STATICFILE_DIRS`
# 2. If you already done, then:
# 3. un-comment `STATICFILE_DIRS` and comment again `STATIC_ROOT`
STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = [BASE_DIR / 'static', ]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Google re-captcha (from apps.configs)
# https://developers.google.com/recaptcha/
RECAPTCHA_PUBLIC_KEY = ''
RECAPTCHA_PRIVATE_KEY = ''


# Django Cors Header
# Only enable CORS for specified domains
if DEBUG:
    CORS_ORIGIN_ALLOW_ALL = True
else:
    CORS_ORIGIN_WHITELIST = (
        'http://PySeeker.com',
        'https://PySeeker.com',
    )

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'accept-language',
    'authorization',
    'authorization-uploader',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with'
)
