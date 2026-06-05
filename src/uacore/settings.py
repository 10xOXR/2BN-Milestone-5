import os
from pathlib import Path
import dj_database_url


# Build paths inside the project like this: BASE_DIR / ...
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = BASE_DIR.parent

# If developing locally and using '.env' then import env and set DEBUG to True
if (PROJECT_DIR / '.env').exists():
    from dotenv import load_dotenv
    load_dotenv(PROJECT_DIR / '.env')
    DEBUG = True
else:
    DEBUG = False

# Django Secret Key
SECRET_KEY = os.getenv("SECRET_KEY")

ALLOWED_HOSTS = []

# Append content of 'SITE_NAME' env variable to 'ALLOWED_HOSTS'
# if it exists. Required for deployed site to run.
host = os.getenv("SITE_NAME")
if host:
    ALLOWED_HOSTS.append(host)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'tickets',
    'charts',
    'storages',
    'materializecssform',
    'django_cleanup.apps.CleanupConfig',
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

ROOT_URLCONF = 'uacore.urls'

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
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                "tickets.context_processors.get_args",
            ],
        },
    },
]

WSGI_APPLICATION = 'uacore.wsgi.application'


# Databases

if os.getenv("DATABASE_URL") and not os.getenv("USE_SQLITE"):
    DATABASES = {
        'default': dj_database_url.parse(os.getenv('DATABASE_URL'))
    }
else:
    print("Postgres URL not found, using sqlite3 database")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Password validation

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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'users.backends.EmailAuth'
]

# Internationalization settings

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}

AWS_STORAGE_BUCKET_NAME = '2bn-unicorn-attractor'
AWS_S3_REGION_NAME = 'eu-west-1'
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_ACL = None

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# Static files (CSS, JavaScript, Images)

STATICFILES_LOCATION = 'static'

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static"
]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIAFILES_LOCATION = 'media'

MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = (
    "/media/" if DEBUG else
    "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
)

STORAGES = {
    "default": {
        "BACKEND": (
            "django.core.files.storage.FileSystemStorage"
            if DEBUG else
            "custom_storages.MediaStorage"
        ),
    },
    "staticfiles": {
        "BACKEND": (
            "django.contrib.staticfiles.storage.StaticFilesStorage"
            if DEBUG else
            "custom_storages.StaticStorage"
        ),
    },
}

MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

MATERIALIZECSS_ICON_SET = "fontawesome"

STRIPE_PUBLISHABLE = os.getenv("STRIPE_PUBLISHABLE")
STRIPE_SECRET = os.getenv("STRIPE_SECRET")

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.getenv("EMAIL_ADDRESS")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_PORT = 587

# Override default persistant login

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Change default path for @login_required

LOGIN_URL = '/users/login/'

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
