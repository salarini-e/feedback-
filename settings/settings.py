import os
from pathlib import Path
from . import envvars
from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
}


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


env_vars = envvars.load_envars(BASE_DIR)

db_name = env_vars['db_name']
db_user = env_vars['db_user']
db_host = env_vars['db_host']
db_port = env_vars['db_port']
db_passwd = env_vars['db_pw']
SECRET_KEY = env_vars['django_secret_key']
debug_mode = env_vars['debug_mode']
email_user = env_vars['email_sistema']
email_pass = env_vars['email_pw']
sqlite_mode = env_vars['sqlite_mode']

DEBUG = debug_mode

ALLOWED_HOSTS = ['*']

try:
    hCAPTCHA_PUBLIC_KEY = env_vars['hCAPTCHA_Public_Key']
    hCAPTCHA_PRIVATE_KEY = env_vars['hCAPTCHA_Secret_Key']
except:
    RECAPTCHA_PUBLIC_KEY = ''
    RECAPTCHA_PRIVATE_KEY = ''

try:
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = env_vars['GOOGLE_OAUTH2_PUBLIC_KEY']
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = env_vars['GOOGLE_OAUTH2_SECRET_KEY']

    SOCIAL_AUTH_FACEBOOK_KEY = env_vars['FACEBOOK_DEVELOPER_PUBLIC_KEY']
    SOCIAL_AUTH_FACEBOOK_SECRET = env_vars['FACEBOOK_DEVELOPER_SECRET_KEY']
except:
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''

    SOCIAL_AUTH_FACEBOOK_KEY = ''
    SOCIAL_AUTH_FACEBOOK_SECRET = ''

el_api_token = env_vars['el_api_token']
el_id_client = env_vars['el_id_client']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #CUSTOM
    'core',
    'feedbacks',
    'servicos',
    'pesquisas',

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

ROOT_URLCONF = 'settings.urls'

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

WSGI_APPLICATION = 'settings.wsgi.application'

if sqlite_mode:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(PROJECT_ROOT, 'yourdatabasename.db'),
        }    
    }
else:
    DATABASES = {
        'default': {
                'ENGINE': 'django.db.backends.mysql',

                'NAME': db_name,
                'PORT': db_port,

                'USER': db_user,
                'PASSWORD': db_passwd,
                'HOST': db_host,
            }
    }


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



LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = 'static/'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
LOGIN_URL = '/login/'  # Update to point to the custom login view
LOGIN_REDIRECT_URL = '/'  # Optional: Redirect after successful login
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Update media root

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# SESSION_COOKIE_DOMAIN = ".meusistema.com"  # Substitua pelo seu domínio real
# SESSION_COOKIE_NAME = "sessionid"
# SESSION_COOKIE_SECURE = True  # Se estiver usando HTTPS
# SESSION_COOKIE_HTTPONLY = True
# SESSION_COOKIE_SAMESITE = "None"  # Para permitir compartilhamento entre subdomínios
