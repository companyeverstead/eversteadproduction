
# """
# Django settings for eversteadinvest project.
# """

# from pathlib import Path
# import os

# from dotenv import load_dotenv
# import dj_database_url

# load_dotenv()

# # ============================================================
# # BASE DIRECTORY
# # ============================================================

# BASE_DIR = Path(__file__).resolve().parent.parent

# # ============================================================
# # SECURITY
# # ============================================================

# SECRET_KEY = os.getenv(
#     "SECRET_KEY",
#     "django-insecure-dev-key-change-this",
# )

# DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "yes")

# ALLOWED_HOSTS = [
#     "eversteadinvest.com",
#     "www.eversteadinvest.com",
#     "127.0.0.1",
#     "localhost",
# ]

# extra_hosts = os.getenv("ALLOWED_HOSTS", "")
# if extra_hosts:
#     ALLOWED_HOSTS += [
#         host.strip() for host in extra_hosts.split(",") if host.strip()
#     ]

# railway_domain = os.getenv("RAILWAY_PUBLIC_DOMAIN")
# if railway_domain:
#     ALLOWED_HOSTS.append(railway_domain)

# # ============================================================
# # CSRF
# # ============================================================

# CSRF_TRUSTED_ORIGINS = [
#     "http://127.0.0.1:8000",
#     "http://localhost:8000",
#     "https://eversteadinvest.com",
#     "https://www.eversteadinvest.com",
# ]

# extra_csrf_origins = os.getenv("CSRF_TRUSTED_ORIGINS", "")
# if extra_csrf_origins:
#     CSRF_TRUSTED_ORIGINS += [
#         origin.strip() for origin in extra_csrf_origins.split(",")
#         if origin.strip()
#     ]

# # ============================================================
# # PROXY SSL
# # ============================================================

# # Only trust Railway's forwarded HTTPS header in production.
# if not DEBUG:
#     SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
# else:
#     SECURE_PROXY_SSL_HEADER = None

# # ============================================================
# # APPLICATIONS
# # ============================================================

# INSTALLED_APPS = [
#     "django.contrib.admin",
#     "django.contrib.auth",
#     "django.contrib.contenttypes",
#     "django.contrib.sessions",
#     "django.contrib.messages",
#     "django.contrib.staticfiles",
#     "django_countries",
#     "widget_tweaks",
#     "home",
#     "userprofile",
#     "investment",
#     "connectwallet",
# ]

# # ============================================================
# # MIDDLEWARE
# # ============================================================

# MIDDLEWARE = [
#     "django.middleware.security.SecurityMiddleware",
#     "django.contrib.sessions.middleware.SessionMiddleware",
#     "django.middleware.common.CommonMiddleware",
#     "django.middleware.csrf.CsrfViewMiddleware",
#     "django.contrib.auth.middleware.AuthenticationMiddleware",
#     "django.contrib.messages.middleware.MessageMiddleware",
#     "django.middleware.clickjacking.XFrameOptionsMiddleware",
# ]

# # ============================================================
# # URL / WSGI
# # ============================================================

# ROOT_URLCONF = "eversteadinvest.urls"
# WSGI_APPLICATION = "eversteadinvest.wsgi.application"

# # ============================================================
# # TEMPLATES
# # ============================================================

# TEMPLATES = [
#     {
#         "BACKEND": "django.template.backends.django.DjangoTemplates",
#         "DIRS": [BASE_DIR / "templates"],
#         "APP_DIRS": True,
#         "OPTIONS": {
#             "context_processors": [
#                 "django.template.context_processors.request",
#                 "django.contrib.auth.context_processors.auth",
#                 "django.contrib.messages.context_processors.messages",
#             ],
#         },
#     },
# ]

# # ============================================================
# # DATABASE
# # ============================================================

# DATABASES = {
#     "default": dj_database_url.config(
#         default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
#         conn_max_age=600,
#     )
# }

# # ============================================================
# # PASSWORD VALIDATION
# # ============================================================

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
#     },
# ]

# # ============================================================
# # INTERNATIONALIZATION
# # ============================================================

# LANGUAGE_CODE = "en-us"
# TIME_ZONE = "UTC"
# USE_I18N = True
# USE_TZ = True

# # ============================================================
# # STATIC FILES
# # ============================================================

# STATIC_URL = "/static/"
# STATIC_ROOT = BASE_DIR / "staticfiles"
# STATICFILES_DIRS = [BASE_DIR / "static"]

# # ============================================================
# # MEDIA FILES
# # ============================================================

# MEDIA_URL = "/media/"
# MEDIA_ROOT = BASE_DIR / "media"

# # ============================================================
# # DEFAULT SETTINGS
# # ============================================================

# DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
# LOGIN_URL = "/userprofile/login/"

# # ============================================================
# # HTTPS SECURITY
# # ============================================================

# if DEBUG:
#     # LOCAL DEVELOPMENT: HTTP ONLY
#     SECURE_SSL_REDIRECT = False
#     SECURE_SSL_HOST = None

#     SESSION_COOKIE_SECURE = False
#     CSRF_COOKIE_SECURE = False

#     SECURE_HSTS_SECONDS = 0
#     SECURE_HSTS_INCLUDE_SUBDOMAINS = False
#     SECURE_HSTS_PRELOAD = False

# else:
#     # PRODUCTION: HTTPS ENFORCED
#     SECURE_SSL_REDIRECT = True

#     SESSION_COOKIE_SECURE = True
#     CSRF_COOKIE_SECURE = True

#     SECURE_HSTS_SECONDS = 31536000
#     SECURE_HSTS_INCLUDE_SUBDOMAINS = True
#     SECURE_HSTS_PRELOAD = True

# # ============================================================
# # EMAIL / ZOHO SMTP
# # ============================================================

# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.zoho.com")
# EMAIL_PORT = int(os.getenv("EMAIL_PORT", "587"))
# EMAIL_USE_TLS = True

# EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "")
# EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "")

# DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", EMAIL_HOST_USER)
# ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", EMAIL_HOST_USER)

# # ============================================================
# # LOGGING
# # ============================================================

# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "handlers": {
#         "console": {
#             "class": "logging.StreamHandler",
#         },
#     },
#     "root": {
#         "handlers": ["console"],
#         "level": "INFO",
#     },
# }



"""
Django settings for eversteadinvest project.
"""

from pathlib import Path
import os

from dotenv import load_dotenv
import dj_database_url

load_dotenv()

# ============================================================
# BASE DIRECTORY
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

# ============================================================
# SECURITY
# ============================================================

SECRET_KEY = os.getenv("SECRET_KEY")

if not SECRET_KEY:
    raise ValueError("SECRET_KEY environment variable is required.")

DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "yes")

ALLOWED_HOSTS = [
    host.strip()
    for host in os.getenv(
        "ALLOWED_HOSTS",
        "127.0.0.1,localhost"
    ).split(",")
    if host.strip()
]

CSRF_TRUSTED_ORIGINS = [
    origin.strip()
    for origin in os.getenv("CSRF_TRUSTED_ORIGINS", "").split(",")
    if origin.strip()
]

# ============================================================
# PROXY SSL
# ============================================================

if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# ============================================================
# APPLICATIONS
# ============================================================

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Cloudinary
    "cloudinary_storage",
    "cloudinary",

    "django_countries",
    "widget_tweaks",

    "home",
    "userprofile",
    "investment",
    "connectwallet",
]

# ============================================================
# MIDDLEWARE
# ============================================================

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

# ============================================================
# URL / WSGI
# ============================================================

ROOT_URLCONF = "eversteadinvest.urls"
WSGI_APPLICATION = "eversteadinvest.wsgi.application"

# ============================================================
# TEMPLATES
# ============================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
# ============================================================
# DATABASE
# ============================================================

DATABASE_URL = os.getenv("DATABASE_URL")

DATABASES = {
    "default": dj_database_url.config(
        default=DATABASE_URL or f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# ============================================================
# PASSWORD VALIDATION
# ============================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
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

# ============================================================
# INTERNATIONALIZATION
# ============================================================

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ============================================================
# STATIC FILES / WHITENOISE
# ============================================================

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# ============================================================
# MEDIA FILES / CLOUDINARY
# ============================================================

CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.getenv("CLOUDINARY_CLOUD_NAME"),
    "API_KEY": os.getenv("CLOUDINARY_API_KEY"),
    "API_SECRET": os.getenv("CLOUDINARY_API_SECRET"),
}

STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ============================================================
# DEFAULT SETTINGS
# ============================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
LOGIN_URL = "/userprofile/login/"

# ============================================================
# HTTPS SECURITY
# ============================================================

SECURE_SSL_REDIRECT = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG

if not DEBUG:
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
else:
    SECURE_HSTS_SECONDS = 0
    SECURE_HSTS_INCLUDE_SUBDOMAINS = False
    SECURE_HSTS_PRELOAD = False

# ============================================================
# EMAIL / RESEND
# ============================================================

RESEND_API_KEY = os.getenv("RESEND_API_KEY", "")

DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", "")
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "")

# ============================================================
# LOGGING
# ============================================================

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}
