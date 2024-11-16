# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from pathlib import Path

from decouple import config


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ ENVIRONMENT
# └─────────────────────────────────────────────────────────────────────────────────────

# Define base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Set secret key
SECRET_KEY = config("BACKEND_SECRET_KEY", cast=str, default="") or "secret-key"

# Define environment constants
LOCAL = "local"
STAGING = "staging"
PRODUCTION = "production"

# Retrieve environment from .env
ENVIRONMENT = config("BACKEND_ENVIRONMENT", default=PRODUCTION)

# Retrieve debug from .env
DEBUG = config("BACKEND_DEBUG", cast=bool, default=False) and ENVIRONMENT != PRODUCTION

# Determine whether to enable Django Admin
ENABLE_DJANGO_ADMIN = config("BACKEND_ENABLE_DJANGO_ADMIN", cast=bool, default=True)

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ NETWORK
# └─────────────────────────────────────────────────────────────────────────────────────

# Define allowed hosts
ALLOWED_HOSTS = str(config("BACKEND_ALLOWED_HOSTS", cast=str, default="")).split(",")

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ SERVER
# └─────────────────────────────────────────────────────────────────────────────────────

# Define root URL config
ROOT_URLCONF = "config.urls"

# Configure ASGI application
ASGI_APPLICATION = "config.asgi.application"

# Configure WSGI application
WSGI_APPLICATION = "config.wsgi.application"

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ INSTALLED APPS
# └─────────────────────────────────────────────────────────────────────────────────────

# Define installed apps
INSTALLED_APPS = [
    # Django Contrib
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Channels
    "channels",
    # Project
    "pages",
]

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ MIDDLEWARE
# └─────────────────────────────────────────────────────────────────────────────────────

# Define middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEMPLATES
# └─────────────────────────────────────────────────────────────────────────────────────

# Define templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "debug": DEBUG,
        },
    },
]


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DATABASES
# └─────────────────────────────────────────────────────────────────────────────────────

# Define default auto field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Define databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.dummy",
    }
}

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ AUTHENTICATION
# └─────────────────────────────────────────────────────────────────────────────────────

# Define password validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ STATIC FILES
# └─────────────────────────────────────────────────────────────────────────────────────

# Define static URL
STATIC_URL = config("BACKEND_STATIC_URL", cast=str, default="") or "/static/"

# Define static root
STATIC_ROOT = BASE_DIR / "staticfiles"

# Define static files directories
STATICFILES_DIRS = [BASE_DIR / "static"]

# Define static files storage
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ INTERNATIONALIZATION
# └─────────────────────────────────────────────────────────────────────────────────────

# Define language code
LANGUAGE_CODE = "en-us"

# Define time zone
TIME_ZONE = "UTC"

# Define whether to use timezone aware datetimes
USE_TZ = False

# Define whether to enable translations
USE_I18N = True
