from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# Paths inside the project
TEMPLATE_DIR = BASE_DIR / "templates"

# Media files settings
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Static files settings
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# Security settings
SECRET_KEY = "django-insecure-w^6)@766xk=l4logm2joam=6ge@4-81dmql*fgr%wopeesnx-c"
DEBUG = True
ALLOWED_HOSTS = []

# Installed apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "account",
    "rest_framework",
    "cardapi",
    "captcha",
]
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', 
)


# ReCAPTCHA settings
RECAPTCHA_PUBLIC_KEY = "6LcjPSwqAAAAACSbbkmZTSgZhyWHQdLehvQzLFlQ"
RECAPTCHA_PRIVATE_KEY = "6LcjPSwqAAAAAAGb11FI-1OzNgZvjjr-c7_WUUx0"
CAPTCHA_TEST_MODE = False
# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    # 'django.middleware.csrf.CsrfViewMiddleware',
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# URL configuration
ROOT_URLCONF = "IPO.urls"

# Templates configuration
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATE_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
AUTH_USER_MODEL = 'account.CustomUser'

WSGI_APPLICATION = "IPO.wsgi.application"

# Database configuration
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bluestock',
        'USER': 'daiyanalam',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        'PORT': '5432',  
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization settings
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Custom user model
AUTH_USER_MODEL = "account.CustomUser"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
